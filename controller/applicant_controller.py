from helpers.services import Services

class ApplicantController:
  def __init__(self):
    self.__services = Services()
    
  def save_applicant(self, applicant, applicant_form):
    
    self.set_applicant(applicant=applicant, applicant_form=applicant_form)
    self.__services.save_applicant(applicant=applicant)
  
  def set_applicant(self, applicant, applicant_form):
    applicant.firstname = applicant_form['name']['firstname']
    applicant.middlename = applicant_form['name']['middlename']
    applicant.lastname = applicant_form['name']['lastname']
    applicant.birthdate = applicant_form['birthdate']
    applicant.gender = applicant_form['gender']
    print(applicant)