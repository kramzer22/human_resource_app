import requests as req
import dotenv
import os

dotenv.load_dotenv()

class RegistrationServices:
    _URL = os.getenv('SERVER_URL')
    
    @staticmethod
    def test_connection() -> None:
      print(RegistrationServices._URL)
      res = req.get(RegistrationServices._URL)
      if res.status_code == 200:
        print(res.text)
      else:
        print(f'failed to fetch data: {res.status_code} {res.text}')
    
    @staticmethod
    def save_user(user):
      data = {
        'username': user.username,
        'email': user.email,
        'mobile': user.mobile,
        'password': user.password,
        }
      
      res = req.post(f'{RegistrationServices._URL}/api/user/register', data=data)
      if res.status_code == 201:
        print(res.text)
        
        return True, None
      elif res.status_code == 400:
        error_data = res.json()
        print("Error:", error_data)
        
        return False, error_data
      else:
        print(f'failed to save user: code({res.status_code}) - error({res.text})')
        
        return False, None