import datetime as dt
import pytz

class DateFunctions:
    manila_timezone = pytz.timezone('Asia/Manila')

    def get_datetime(self):
        utc_now = dt.datetime.now(pytz.utc)
        manila_time = utc_now.astimezone(self.manila_timezone)
        return manila_time.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    DateFunctions = DateFunctions()
    print("Current Manila Time:", DateFunctions.get_datetime())
