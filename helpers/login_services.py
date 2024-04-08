import requests as req
import dotenv
import os
import threading

dotenv.load_dotenv()

class LoginServices:
  def __init__(self) -> None: 
    self._URL = os.getenv('SERVER_URL')
    self._res = None

  def test_connection(self) -> None:
    print(f'{LoginServices._URL}/api/user/login')
    self.res = req.post(f'{LoginServices._URL}/api/user/login')
    if self.res.status_code == 200:
      print(self.res.text)
    else:
      print(f'failed to fetch data: {self.res.status_code} {self.res.text}')
      
  def user_login(self, user_data:any, method: callable) -> None:
    threading.Thread(target=self.initialize_user_login, daemon=True, args=(user_data, method,))
      
  def initialize_user_login(self, user_data:any, method:callable):
    self._res = None
    
    data = {
        'username': user_data.username,
        'password': user_data.password,
      }
    print(data)
    
    try:
      self._res = req.post(f'{self._URL}/api/user/login', data=data)  
    except Exception as e:
      self._res = None
    finally:
      self.user_login_result(method)
      
    print(self._res)
    
  def user_login_result(self, method:callable) -> tuple:
    if not self._res:
      print('Unable to login. No server connection', self.res)
      method( False, { 'field': 'username', 'message': 'Unable to connect to server'})
    elif self._res.status_code == 200:
      method(True, None)
    elif self._res.status_code == 400:
      error_data = self.res.json()
      method(False, error_data)
    elif self._res.status_code == 401 or self.res._status_code == 404:
      error_data = self.res.json()
      print(error_data)
      method(False, error_data)
    else:
      method(False, None)

    
    
  
    
    
    
    
    