import pytest
from selenium import webdriver
from pages.registr_attorney_page import RegistrAttorney
from data.data_model.data_registr_attorney import regisrt_data
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrattorney:

	def setup_method(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.maximize_window()
		self.regAttorney = RegistrAttorney(self.driver)

	@pytest.mark.parametrize("regisrt_data", regisrt_data)
	def test_reg_attorney(self, regisrt_data):
		self.regAttorney.open()
		self.regAttorney.signup_button_click()
		#self.regAttorney.attorney_button_click()
		self.regAttorney.bar_numb_input_enter(regisrt_data.bar_number)
		self.regAttorney.agree_checkbox_mark()
		self.regAttorney.submit_button_click()
		self.regAttorney.email_input_enter(regisrt_data.email)
		#assert self.regAttorney.sbn_input_attribute() == regisrt_data.bar_number
		#print(self.regAttorney.sbn_input_attribute())
		self.regAttorney.submit_form_button_click()
		self.regAttorney.skip_secretary_button()
		#self.regAttorney.img_account_send()
		self.regAttorney.continue_account_button()
		self.regAttorney.password_input_enter(regisrt_data.password)
		self.regAttorney.continue_button_click()





