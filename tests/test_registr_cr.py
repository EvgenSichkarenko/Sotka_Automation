import time

import pytest
from selenium import webdriver
from pages.registr_cr import RegistrCR
from webdriver_manager.chrome import ChromeDriverManager
from data.data_model.data_registr_cr import cr_data

class TestRegistrattorney:

	def setup_method(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.maximize_window()
		self.cr = RegistrCR(self.driver)

	@pytest.mark.parametrize("cr_data", cr_data)
	def test_reg_attorney(self, cr_data):
		self.cr.open()
		self.cr.signup_button_click()
		self.cr.cr_registration_form(cr_data.bar_number)
		assert cr_data.bar_number == self.cr.license_num_input_attribute()
		self.cr.cr_data_form(cr_data.email, cr_data.phone_number, cr_data.full_name, cr_data.issuance,
		cr_data.expiration_data, cr_data.address_one, cr_data.addres_two)
		time.sleep(1)
		self.cr.availability_button()
		self.cr.price_form()







