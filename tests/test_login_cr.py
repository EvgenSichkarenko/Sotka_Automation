from selenium import webdriver
from pages.login_cr import LoginCr
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLoginCR:

	def setup_method(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.maximize_window()
		self.cr = LoginCr(self.driver)

	def test_login_cr(self, login="cr@givmail.com", password="Counsel10"):
		self.cr.open()
		self.cr.login_attorney(login, password)
		self.cr.submit_buttom_click()
		assert self.cr.text_name_attribute() == "Peter Popov"
