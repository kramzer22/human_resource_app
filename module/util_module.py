import re
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
    
class CheckerFunctions:
    @staticmethod
    def checklen(text, valid_length):
        return True if len(text) >= valid_length else False
    
    @staticmethod
    def is_user_format(text):
        pattern = r'^[a-zA-Z][a-zA-Z0-9]*$'
        return bool(re.match(pattern, text))
            

    @staticmethod
    def is_email_format(email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def is_mobile_format(number):
        if number[0] == '+':
            pattern = r'^\+[1-9][0-9]{9,12}$'
            return bool(re.match(pattern, number))
        elif number[0].isdigit() and int(number[0]) in range(0, 9):
            pattern = r'^[0-9]{9,11}$'
            return bool(re.match(pattern, number))
        else:
            return False
            
if __name__ == '__main__':
    DateFunctions = DateFunctions()
    print("Current Manila Time:", DateFunctions.get_datetime())
