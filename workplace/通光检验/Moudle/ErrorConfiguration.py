from functools import wraps
import datetime


class Logits(object):
    def __init__(self, logfile="report.log"):
        self.logfile = logfile
        time_now = datetime.datetime.now()
        self.now_time = time_now.strftime("%Y-%m-%d %H:%M:%S")

    def __call__(self, func):
        @wraps(func)
        def error_report(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(func.__name__, e)
                with open(self.logfile, mode="a+") as file:
                    errorline = e.__traceback__.tb_lineno
                    file.write(f"[Func:{func.__name__}] [Error:{str(e)}] [Line:{errorline}] [Time:{self.now_time}]\n")
        return error_report