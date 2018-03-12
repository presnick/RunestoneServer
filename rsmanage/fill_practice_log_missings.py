from rs_grading import do_fill_user_topic_practice_log_missings
import json

userinfo = json.loads(os.environ['RSM_USERINFO'])

do_fill_user_topic_practice_log_missings(db = db,
                    settings = settings,
                    testing_mode = userinfo['test_mode'])