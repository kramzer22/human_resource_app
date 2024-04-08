class ApplicantHelper:
  def __init__(self) -> None:
    self._GENDERS = ['male', 'female', 'others']
  
  def get_genders(self) -> list:
    return self._GENDERS