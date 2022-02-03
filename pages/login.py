from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
	def __init__(self, app):
		self.app = app

	def login(self, invalid_login, invalid_password, valid_login, valid_password):
		wd = self.app.wd
		self.app.open_login(wd)
		self.check_valid_login(invalid_login, invalid_password)
		invalid_email = WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH ,
		"//span[text()='login must be a valid email']")))
		invalid_passwor = WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH ,
		"//span[text()='Min 6']")))

		if invalid_email and invalid_passwor:
			self.check_valid_login(valid_login, valid_password)

	def check_valid_login(self, text1, text2):
		wd = self.app.wd
		wd.find_element(By.NAME, "login").clear()
		wd.find_element(By.NAME, "login").send_keys(text1)
		wd.find_element(By.NAME, "password").clear()
		wd.find_element(By.NAME, "password").send_keys(text2)
		wd.find_element(By.NAME, "registrationSignInBtn").click()
