from typing import List
import datetime as dt

class Applicant:
  def __init__(self, first_name:str='', middle_name:str='', last_name:str='', birth_date:dt.date= None, gender:str=''):
    
    self._first_name:str = first_name
    self._middle_name:str = middle_name
    self._last_name:str = last_name
    self._birthdate:dt.date = birth_date
    self._gender:str = gender
      
  @property  
  def first_name(self) -> str:
    return self._first_name
    
  @first_name.setter
  def first_name(self, value:str):
    self._first_name = value
      
  @property  
  def middle_name(self) -> str:
    return self._middle_name
    
  @middle_name.setter
  def middle_name(self, value:str):
    self.middle_name = value
    
  @property  
  def last_name(self) -> str:
    return self.__name['lastname']
    
  @last_name.setter
  def last_name(self, value:str):
    self._last_name = value
    
  @property
  def birth_date(self) -> dt.date:
    return self._birthdate
    
  @birth_date.setter
  def birth_date(self, value:dt.date):
    self._birth_date = value
    
  @property
  def gender(self) -> str:
    return self._gender
    
  @gender.setter
  def gender(self, value:str):
    self._gender = value
    
  def get_genders(self) -> List[str]:
    return self.genders
  
  
  
  