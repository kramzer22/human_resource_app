class Applicant:
  def __init__(self, firstname = '', middlename = '', lastname = '', birthdate = None, gender = ''):
    self.__name = {
      'firstname':firstname, 
      'middlename':middlename,
      'lastname':lastname
    }
    self.__birthdate = birthdate
    self.__gender = gender
    
  def __str__(self):
    return f'name: {self.__name['lastname']}, {self.__name['firstname']} {self.__name['middlename']}\nbirthdate: {self.__birthdate}\ngender: {self.__gender}'
  
  @property  
  def firstname(self):
    return self.__name['firstname']
  
  @firstname.setter
  def firstname(self, value):
    self.__name['firstname'] = value
  
  @property  
  def middlename(self):
    return self.__name['middlename']
  
  @middlename.setter
  def middlename(self, value):
    self.__name['middlename'] = value
  
  @property  
  def lastname(self):
    return self.__name['lastname']
  
  @lastname.setter
  def lastname(self, value):
    self.__name['lastname'] = value
  
  @property
  def birthdate(self):
    return self.__birthdate
  
  @birthdate.setter
  def birthdate(self, value):
    self.__birthdate = value
  
  @property
  def gender(self):
    return self.__gender
  
  @gender.setter
  def gender(self, value):
    self.__gender = value