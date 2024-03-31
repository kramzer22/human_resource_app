import datetime as dt
import pytz

class DateFunctions:
    manila_timezone = pytz.timezone('Asia/Manila')

    def get_datetime(self):
        utc_now = dt.datetime.now(pytz.utc)
        manila_time = utc_now.astimezone(self.manila_timezone)
        return manila_time.strftime("%Y-%m-%d %H:%M:%S")
    
class DisplayFunctions:
    def centerposition(self, width, height, root):
        # Calculate center coordinates
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = (screen_width - width) // 2
        y_coordinate = (screen_height - height) // 2
        
        return (x_coordinate, y_coordinate)

if __name__ == '__main__':
    DateFunctions = DateFunctions()
    print("Current Manila Time:", DateFunctions.get_datetime())
