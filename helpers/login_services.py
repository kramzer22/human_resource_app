import requests as req
import dotenv
import os

dotenv.load_dotenv()

class LoginServices:
  _URL = os.getenv('SERVER_URL')
  
  @staticmethod
  def test_connection() -> None:
    print(f'{LoginServices._URL}/api/user/login')
    res = req.post(f'{LoginServices._URL}/api/user/login')
    if res.status_code == 200:
      print(res.text)
    else:
      print(f'failed to fetch data: {res.status_code} {res.text}')
      
  @staticmethod
  def login_user(user):
    data = {
      'username': user.username,
      'password': user.password,
    }
    
    try:
      res = req.post(f'{LoginServices._URL}/api/user/login', data=data)
        
      print(res)
      if res.status_code == 200:
        return True, None
      elif res.status_code == 400:
        error_data = res.json()
        return False, error_data
      elif res.status_code == 401 or res.status_code == 404:
        error_data = res.json()
        print(error_data)
        return False, error_data
      else:
        return False, None
    except Exception as e:
      print('Unable to login. No server connection')
      return False, { 'field': 'username', 'message': 'Unable to connect to server'}
    
    