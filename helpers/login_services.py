import requests as req
import dotenv
import os
import threading
import time

from helpers.pinger import Pinger

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
    threading.Thread(target=self.initialize_user_login, daemon=True, args=(user_data, method,)).start()
      
  def initialize_user_login(self, user_data:any, method:callable):
    self._res = None
    
    data = {
        'username': user_data.username,
        'password': user_data.password,
      }
    print(data)
    
    if Pinger.test_server_response():
      try:
        self._res = req.post(f'{self._URL}/api/user/login', data=data)  
      except Exception as e:
        self._res = None
  
    self.user_login_result(method)  
    
  def user_login_result(self, method:callable):
    if self._res.status_code == 500:
      print('Internal server problem', self._res)
      method( False, { 'field': 'username', 'message': 'Internal server problem'})
    elif self._res.status_code == 200:
      method(True, None)
    elif self._res.status_code == 400:
      error_data = self._res.json()
      method(False, error_data)
    elif self._res.status_code == 401 or self._res.status_code == 404:
      error_data = self._res.json()
      print(error_data)
      method(False, error_data)
    else:
      method( False, { 'field': 'username', 'message': 'Unable to connect to server'})

    
    
  
    
    
    
    
    