from selenium import webdriver
from pages.login import Login
from pages.add_seecretary import Secretary
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogin:

	def setup_method(self):
		self.driver = webdriver.Chrome(ChromeDriverManager().install())
		self.driver.maximize_window()
		self.login = Login(self.driver)
		self.secretary = Secretary(self.driver)

	def test_login_attroney(self, login="a1@getnada.com", password="Attorney95",
			secr_email="secretary00zetmail.com", secr_password="123Qwe123"):
		self.login.open()
		self.login.login_attorney(login, password)
		self.login.submit_buttom_click()
		time.sleep(2)
		assert self.login.text_name_attribute() == "Laura Ellen Malkofsky"
		self.secretary.add_secret_icon_click()
		self.secretary.contact_person(secr_email, secr_password)
		self.driver.quit()