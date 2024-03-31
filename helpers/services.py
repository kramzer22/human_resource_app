import requests as req
import datetime as dt

class Services:
  def __init__(self):
    self.__url = 'https://recruitement-info-server.onrender.com'
    self.__url = 'http://localhost:3001'


  def test_connection(self) -> None:
    res = req.get(self.__url)
    if res.status_code == 200:
      print(res.text)
    else:
      print(f'failed to fetch data: {res.status_code} {res.text}')
      
  def save_applicant(self, applicant) -> None:
    data = {
      'firstname': applicant.firstname,
      'middlename': applicant.middlename,
      'lastname': applicant.lastname,
      'birthdate': applicant.birthdate,
      'gender': applicant.gender
      }
    
    
    
    res = req.post(f'{self.__url}/api/applicant/register', data=data)
    if res.status_code == 201:
      print(res.text)
    else:
      print(f'failed to fetch data: {res.status_code} {res.text}')