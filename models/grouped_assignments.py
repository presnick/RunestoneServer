def pct2pts(x):
    return "%.2f" % (100*x)

class Grade(object):
    """Grade of one user for either a collection of assignments, or for the whole course"""
    def __init__(self):
        self.weight = 1
        self.scores = []
        self.assignment_scores = []
    
    def points(self):
        self.scores.sort()
        if len(self.scores) > self.assignments_count - self.assignments_dropped:
            # too many grades; drop lowest
            return sum(self.scores[self.assignments_dropped:])
        else:
            return sum(self.scores)
    
    def assignment_points(self):
        self.assignment_scores.sort()
        if len(self.scores) > self.assignments_count - self.assignments_dropped:
            # too many grades; drop lowest assignment
            return sum(self.assignment_scores[self.assignments_dropped:])
        else:
            return sum(self.assignment_scores)
            
    
    def current(self):
        if self.possible == 0:
            return 0
        points = float(self.points())/self.possible
        return points*self.weight

    def projected(self):
        if self.assignment_points() == 0:
            return 0
        points = float(self.points())/self.assignment_points()
        return points*self.weight

    def points_after_drops(self):
        self.scores.sort()
        return sum(self.scores[self.assignments_dropped:])
    def assignment_points_after_drops(self):
        self.assignment_scores.sort()
        return sum(self.assignment_scores[self.assignments_dropped:])

    def max(self):
        # this is more complicated because of the "best k of n" scoring
        
        if self.possible == 0:
            return 0
        remaining = self.possible - self.assignment_points_after_drops()
        if remaining < 0:
            remaining = 0
        points = (self.points_after_drops() + remaining)/self.possible
        return points * self.weight

    def percent(self, points=None, total=None):
        if points == None:
            points = self.points()
        if total == None:
            total = self.assignment_points()
        if total == 0:
            return "0%"
        percent = round((points / total) * 100)
        return "%d%%" % (percent)

class CourseGrade(Grade):
    def __init__(self):
        super(CourseGrade, self ).__init__()
        self.points = 0
        self.projected_pts = 0
        self.max_pts = 0
        
    def current(self):
        return self.points
    
    def projected(self):
        return self.projected_pts
    
    def max(self):
        return self.max_pts

def student_grade(user=None, course=None, assignment_type=None):
    grade = Grade()
    if not user or not course or not assignment_type:
        return grade

    # Check assignment type weight before setting it incase its None
    if assignment_type.weight != None:
        grade.weight = assignment_type.weight
    if assignment_type.points_possible != None:
        grade.possible = assignment_type.points_possible
    if assignment_type.assignments_count:
        grade.assignments_count = int(assignment_type.assignments_count)
    if assignment_type.assignments_dropped:
        grade.assignments_dropped = int(assignment_type.assignments_dropped) 

    assignments = db(db.assignments.id == db.grades.assignment)
    assignments = assignments(db.assignments.course == course.id)
    assignments = assignments(db.grades.auth_user == user.id)
    assignments = assignments(db.assignments.released == True)
    assignments = assignments(db.assignments.assignment_type == assignment_type.id)
    assignments = assignments.select(
        db.assignments.ALL,
        db.grades.ALL,
        orderby=db.assignments.name,
        )
    # print assignments
    for row in assignments:
        grade.scores.append(row.grades.score)
        grade.assignment_scores.append(row.assignments.points)
    return grade

db.define_table('assignment_types',
    Field('name', 'string'),
    Field('grade_type', 'string', default="additive", requires=IS_IN_SET(['additive', 'checkmark', 'use'])),
    Field('weight', 'double', default=1.0),
    Field('points_possible','integer', default=0),
    Field('assignments_count', default=0),
    Field('assignments_dropped', default=0),
    format='%(names)s',
    migrate='runestone_assignment_types.table',
    )

db.define_table('assignments',
    Field('course', db.courses),
    Field('assignment_type', db.assignment_types, requires=IS_EMPTY_OR(IS_IN_DB(db, 'assignment_types.id', '%(name)s'))),
    Field('name', 'string'),
    Field('points', 'integer'),
    Field('threshold', 'integer', default=1),
    Field('released', 'boolean'),
    format='%(name)s',
    migrate='runestone_assignments.table'
    )

class score(object):
    def __init__(self, acid=None, points=0, comment="", user=None):
        self.acid = acid
        self.user = user
        self.points = points
        self.comment = comment

def assignment_get_use_scores(assignment, problem=None, user=None, section_id=None):
    scores = []
    if problem and user:
        pass
    elif problem:
        pass
    elif user:
        attempted_problems = db(db.useinfo.div_id == db.problems.acid)(db.problems.assignment == assignment.id)(db.useinfo.sid == user.username).select(db.problems.acid)
        for problem in db(db.problems.assignment == assignment.id).select(db.problems.acid):
            matches = [x for x in attempted_problems if x.acid == problem.acid]
            points = 0
            if len(matches) > 0:
                points = 1
            scores.append(score(
                points = points,
                acid = problem.acid,
                user = user,
                ))
    else:
        pass
    return scores


def assignment_get_scores(assignment, problem=None, user=None, section_id=None):
    assignment_type = db(db.assignment_types.id == assignment.assignment_type).select().first()
    if assignment_type and assignment_type.grade_type == 'use':
        return assignment_get_use_scores(assignment, problem, user, section_id)
    scores = []
    if problem and user:
        pass
    elif problem:
        grades = db(db.code.sid == db.auth_user.username)(db.code.acid == problem).select(
            db.code.ALL,
            db.auth_user.ALL,
            orderby=db.code.sid | db.code.timestamp,
            distinct=db.code.sid,
            )
        for g in grades:
            scores.append(score(
                points=g.code.grade,
                comment=g.code.comment,
                acid=problem,
                user=g.auth_user,
                ))
    elif user:
        q = db(db.problems.acid == db.code.acid)
        q = q(db.problems.assignment == assignment.id)
        q = q(db.code.sid == user.username)
        grades = q.select(
            db.code.acid,
            db.code.grade,
            db.code.comment,
            db.code.timestamp,
            orderby=db.code.acid | db.code.timestamp,
            distinct=db.code.acid,
            )
        for g in grades:
            scores.append(score(
                points=g.grade,
                comment=g.comment,
                acid=g.acid,
                user=user,
                ))
    else:
        grades = db(db.grades.assignment == assignment.id).select(db.grades.ALL)
        for g in grades:
            scores.append(score(
                points=g.score,
                user=g.auth_user,
                ))
    return scores
db.assignments.scores = Field.Method(lambda row, problem=None, user=None, section_id=None: assignment_get_scores(row.assignments, problem, user, section_id))

def assignment_set_grade(assignment, user):
    # delete the old grades; we're regrading
    db(db.grades.assignment == assignment.id)(db.grades.auth_user == user.id).delete()

    assignment_type = db(db.assignment_types.id == assignment.assignment_type).select().first()
    if not assignment_type:
        print "no assignment type"
        # if we don't know how to grade this assignment, don't grade the assignment.
        return 0

    points = 0.0
    if assignment_type.grade_type == 'use':
        for problem in db(db.problems.assignment == assignment.id).select():
            if db(db.useinfo.div_id == problem.acid)(db.useinfo.sid == user.username).select().first():
                points += 1
    else:
        for prob in assignment.scores(user=user):
            if prob.points:
                points = points + prob.points

    if assignment_type.grade_type in ['checkmark', 'use']:
        # threshold grade
        if points >= assignment.threshold:
            points = assignment.points
        else:
            points = 0
    else:
        # they got the points they earned
        pass

    db.grades.insert(
        auth_user=user.id,
        assignment=assignment.id,
        score=points,
        )
    return points
db.assignments.grade = Field.Method(lambda row, user: assignment_set_grade(row.assignments, user))

def assignment_release_grades(assignment, released=True):
    # update problems
    assignment.released = True
    assignment.update_record()
    return True
db.assignments.release_grades = Field.Method(lambda row, released=True: assignment_release_grades(row.assignments, released))

db.define_table('problems',
    Field('assignment', db.assignments),
    Field('acid', 'string'),
    migrate='runestones_problems.table',
    )

db.define_table('grades',
    Field('auth_user', db.auth_user),
    Field('assignment', db.assignments),
    Field('score', 'double'),
    migrate='runestone_grades.table',
    )

db.define_table('deadlines',
    Field('assignment', db.assignments, requires=IS_IN_DB(db, 'assignments.id', db.assignments._format)),
    Field('section', db.sections, requires=IS_EMPTY_OR(IS_IN_DB(db, 'sections.id', '%(name)s'))),
    Field('deadline', 'datetime'),
    migrate='runestone_deadlines.table',
    )
