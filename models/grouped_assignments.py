db.define_table('assignment_types',
	Field('name','string'),
	Field('grade_type', 'string', default="additive", requires=IS_IN_SET(['additive','checkmark'])),
	format = '%(names)s',
	migrate='runestone_assignment_types.table',
	)

db.define_table('assignments',
	Field('course',db.courses),
	Field('assignment_type', db.assignment_types, requires=IS_EMPTY_OR(IS_IN_DB(db,'assignment_types.id','%(name)s'))),
	Field('name', 'string'),
	Field('points', 'integer'),
	Field('threshold', 'integer', default=1),
	Field('released','boolean'),
	format='%(name)s',
	migrate='runestone_assignments.table'
	)

class score(object):
	def __init__(self, acid=None, points=0, comment="", user=None):
		self.acid = acid
		self.user = user
		self.points = points
		self.comment = comment

def assignment_get_scores(assignment, problem=None, user=None, section_id=None):
	scores = []
	if problem and user:
		pass
	elif problem:
		grades = db(db.code.sid == db.auth_user.username)(db.code.acid == problem).select(
			db.code.ALL,
			db.auth_user.ALL,
			orderby = db.code.sid,
			distinct = db.code.sid,
			)
		for g in grades:
			scores.append(score(
				points = g.code.grade,
				comment = g.code.comment,
				acid = problem,
				user = g.auth_user,
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
			orderby=db.code.acid|db.code.timestamp,
			distinct = db.code.acid,
			)
		for g in grades:
			scores.append(score(
				points = g.grade,
				comment = g.comment,
				acid = g.acid,
				user = user,
				))
	else:
		grades = db(db.grades.assignment == assignment.id).select(db.grades.ALL)
		for g in grades:
			scores.append(score(
				points = g.score,
				user = g.auth_user,
				))
	return scores
db.assignments.scores = Field.Method(lambda row, problem=None, user=None, section_id=None: assignment_get_scores(row.assignments, problem, user, section_id))

def assignment_set_grade(assignment, user):
	# delete the old grades; we're regrading
	db(db.grades.assignment == assignment.id)(db.grades.auth_user == user.id).delete()

	assignment_type = db(db.assignment_types.id == assignment.id).select().first()
	if not assignment_type:
		# if we don't know how to grade this assignment, don't grade the assignment.
		return 0
	
	points = 0.0
	for prob in assignment.scores(user = user):
		points = points + prob.points

	if assignment_type.grade_type == 'checkmark':
		#threshold grade
		if points >= assignment.threshold:
			points = assignment.points
		else:
			points = 0
	else:
		# they got the points they earned
		pass

	db.grades.insert(
		auth_user = user.id,
		assignment = assignment.id,
		score = points,
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
	Field('assignment',db.assignments),
	Field('acid','string'),
	migrate='runestones_problems.table',
	)

db.define_table('grades',
	Field('auth_user', db.auth_user),
	Field('assignment', db.assignments),
	Field('score', 'double'),
	migrate='runestone_grades.table',
	)

db.define_table('deadlines',
	Field('assignment', db.assignments, requires=IS_IN_DB(db,'assignments.id',db.assignments._format)),
	Field('section', db.sections, requires=IS_EMPTY_OR(IS_IN_DB(db,'sections.id','%(name)s'))),
	Field('deadline','datetime'),
	migrate='runestone_deadlines.table',
	)