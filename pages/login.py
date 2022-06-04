from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time, os


class Login:
	def __init__(self, app):
		self.app = app

	def change_time_zone(self):
		wd = self.app.wd

		print(time.strftime('%Y-%m-%d %H:%M:%S'))  # before timezone change
		os.system('tzutil /s "Central America Standard Time"')


	def login(self, invalid_login, invalid_password, valid_login, valid_password):
		wd = self.app.wd
		self.app.open_login()
		self.check_valid_login(invalid_login, invalid_password)
		invalid_email = WebDriverWait(wd, 15).until(EC.presence_of_element_located((By.XPATH ,
		"//span[text()='login must be a valid email']")))
		invalid_pasword = WebDriverWait(wd, 15).until(EC.presence_of_element_located((By.XPATH ,
		"//span[text()='This field should contain at least 6 characters']")))
		if invalid_email and invalid_pasword:
			self.check_valid_login(valid_login, valid_password)
		else:
			print("validation isn't works")

	def check_valid_login(self, text1, text2):
		wd = self.app.wd

		login = WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='login']")))
		login.send_keys(Keys.CONTROL + "a")
		login.send_keys(Keys.BACK_SPACE)
		login.send_keys(text1)

		password = wd.find_element(By.CSS_SELECTOR, "input[name='password']")
		password.send_keys(Keys.CONTROL + "a")
		password.send_keys(Keys.BACK_SPACE)
		password.send_keys(text2)
		wd.find_element(By.CSS_SELECTOR, "button[name='registrationSignInBtn']").click()

	def logout(self):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.ID, "basic-button"))).click()
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, "//ul/li/div[text()=' Log Out']"))).click()