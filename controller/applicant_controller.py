# from view.applicant_form import ApplicationForm as applicantform
from model.applicant import Applicant

from helpers.applicant_helper import ApplicantHelper

from helpers.services import Services

class ApplicantController:
  def __init__(self, view: any) -> None:
    self._applicant = Applicant()
    self._applicant_helper = ApplicantHelper()
    self._view = view
    
    # self._services = Services()
    
  def get_genders(self) -> list:
    return self._applicant_helper.get_genders()
    
  def save_applicant(self, applicant, applicant_form):
    self.set_applicant(applicant=applicant, applicant_form=applicant_form)
    #self._services.save_applicant(applicant=applicant)
  
  def set_applicant(self, applicant, applicant_form) -> None:
    pass
    # applicant.firstname = applicant_form['name']['firstname']
    # applicant.middlename = applicant_form['name']['middlename']
    # applicant.lastname = applicant_form['name']['lastname']
    # applicant.birthdate = applicant_form['birthdate']
    # applicant.gender = applicant_form['gender']
    # print(applicant)