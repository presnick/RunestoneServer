# Files in the model directory are loaded in alphabetical order.  This one needs to be loaded after db.py

db.define_table(
    "useinfo",
    Field("timestamp", "datetime"),
    Field("sid", "string"),
    Field("event", "string"),
    Field("act", "string"),
    Field("div_id", "string"),
    Field("course_id", "string"),
    migrate=table_migrate_prefix + "useinfo.table",
)

# stores student's saved code and, unfortunately, comments and grades, which really should be their own table linked to this
db.define_table(
    "code",
    Field("acid", "string"),
    Field("code", "text"),
    Field("emessage", "text"),
    Field("course_id", "integer"),
    Field("grade", "double"),
    Field("sid", "string"),
    Field("timestamp", "datetime"),
    Field("comment", "text"),
    Field("language", "text", default="python"),
    migrate=table_migrate_prefix + "code.table",
)

# Stores the source code for activecodes, including prefix and suffix code, so that prefixes and suffixes can be run when grading
# Contents of this table are filled when processing activecode directives, in activecod.py
db.define_table(
    "source_code",
    Field("acid", "string", required=True),
    Field("course_id", "string"),
    Field(
        "includes", "string"
    ),  # comma-separated string of acid main_codes to include when running this source_code
    Field(
        "available_files", "string"
    ),  # comma-separated string of file_names to make available as divs when running this source_code
    Field("main_code", "text"),
    Field("suffix_code", "text"),  # hidden suffix code
    migrate=table_migrate_prefix + "source_code.table",
)

db.define_table(
    "acerror_log",
    Field("timestamp", "datetime"),
    Field("sid", "string"),
    Field("div_id", "string"),
    Field("course_id", "string"),
    Field("code", "text"),
    Field("emessage", "text"),
    migrate=table_migrate_prefix + "acerror_log.table",
)

##table to store the last position of the user. 1 row per user, per course
db.define_table(
    "user_state",
    Field("user_id", "integer"),
    Field("course_id", "string"),
    Field("last_page_url", "string"),
    Field("last_page_hash", "string"),
    Field("last_page_chapter", "string"),
    Field("last_page_subchapter", "string"),
    Field("last_page_scroll_location", "string"),
    Field("last_page_accessed_on", "datetime"),
    migrate=table_migrate_prefix + "user_state.table",
)

# Table to match instructor(s) to their course(s)
db.define_table(
    "course_instructor",
    Field("course", db.courses),
    Field("instructor", db.auth_user),
    Field(
        "verified", "boolean"
    ),  # some features we want to take the extra step of verifying an instructor - such as instructor guide
    Field("paid", "boolean"),  # in the future some instructor features will be paid
    migrate=table_migrate_prefix + "course_instructor.table",
)

db.define_table(
    "timed_exam",
    Field("timestamp", "datetime"),
    Field("div_id", "string"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("correct", "integer"),
    Field("incorrect", "integer"),
    Field("skipped", "integer"),
    Field("time_taken", "integer"),
    Field("reset", "boolean"),
    migrate=table_migrate_prefix + "timed_exam.table",
)

db.define_table(
    "mchoice_answers",
    Field("timestamp", "datetime"),
    Field("div_id", "string"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("answer", "string", length=50),
    Field("correct", "boolean"),
    migrate=table_migrate_prefix + "mchoice_answers.table",
)

db.define_table(
    "fitb_answers",
    Field("timestamp", "datetime"),
    Field("div_id", "string"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("answer", "string"),
    Field("correct", "boolean"),
    migrate=table_migrate_prefix + "fitb_answers.table",
)
db.define_table(
    "dragndrop_answers",
    Field("timestamp", "datetime"),
    Field("div_id", "string"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("answer", "string"),
    Field("correct", "boolean"),
    Field("minHeight", "string"),
    migrate=table_migrate_prefix + "dragndrop_answers.table",
)
db.define_table(
    "clickablearea_answers",
    Field("timestamp", "datetime"),
    Field("div_id", "string"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("answer", "string"),
    Field("correct", "boolean"),
    migrate=table_migrate_prefix + "clickablearea_answers.table",
)
db.define_table(
    "parsons_answers",
    Field("timestamp", "datetime"),
    Field("div_id", "string"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("answer", "string"),
    Field("source", "string"),
    Field("correct", "boolean"),
    migrate=table_migrate_prefix + "parsons_answers.table",
)
db.define_table(
    "codelens_answers",
    Field("timestamp", "datetime"),
    Field("div_id", "string"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("answer", "string"),
    Field("source", "string"),
    Field("correct", "boolean"),
    migrate=table_migrate_prefix + "codelens_answers.table",
)

db.define_table(
    "shortanswer_answers",
    Field("timestamp", "datetime"),
    Field("div_id", "string"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("answer", "text"),
    migrate=table_migrate_prefix + "shortanswer_answers.table",
)

db.define_table(
    "payments",
    Field("user_courses_id", db.user_courses, required=True),
    # A `Stripe charge ID <https://stripe.com/docs/api/charges/object#charge_object-id>`_. Per the `Stripe docs <https://stripe.com/docs/upgrades>`_, this is always 255 characters or less.
    Field("charge_id", "string", length=255, required=True),
    migrate=table_migrate_prefix + "payments.table",
)

db.define_table(
    "lp_answers",
    Field("timestamp", "datetime"),
    Field("div_id", "string"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("answer", "text"),
    Field("correct", "double"),
    migrate=table_migrate_prefix + "lp_answers.table",
)

db.define_table(
    "invoice_request",
    Field("timestamp", "datetime"),
    Field("sid", "string"),
    Field("course_name", "string"),
    Field("email", "string"),
    Field("processed", "boolean"),
    migrate=table_migrate_prefix + "invoice_request.table",
)

# The course attribute table allows us to add parameters to each course without having
# to add columns to the courses table every time we have something new to store.
# for example we could have a "source" key value pair to indicate if a course is built
# with runestone or pretext, or to store the latex macros for a pretext course
# TODO: migrate allow_pairs, download_enabled, and others from courses to this table.
#
db.define_table(
    "course_attributes",
    Field("course_id", db.courses),
    Field("attr", "string"),
    Field("value", "text"),
    migrate=table_migrate_prefix + "course_attributes.table",
)
