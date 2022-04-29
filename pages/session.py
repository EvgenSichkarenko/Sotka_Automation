from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

class Session:
	def __init__(self, app):
		self.app = app

	def login(self, login, password):
		wd = self.app.wd
		self.app.open_login()
		time.sleep(1)
		login_input = WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='login']")))
		login_input.send_keys(Keys.CONTROL + "a")
		login_input.send_keys(Keys.BACK_SPACE)
		login_input.send_keys(login)

		password_input = wd.find_element(By.CSS_SELECTOR, "input[name='password']")
		password_input.send_keys(Keys.CONTROL + "a")
		password_input.send_keys(Keys.BACK_SPACE)
		password_input.send_keys(password)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "button[name='registrationSignInBtn']"))).send_keys(Keys.RETURN)

	def logout(self):
		wd = self.app.wd
		time.sleep(1)
		wd.refresh()
		basic = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='basic-button']")))
		time.sleep(1)
		wd.execute_script("arguments[0].click()", basic)
		time.sleep(1)
		log = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-name='dropdownLogout']")))
		time.sleep(1)
		wd.execute_script("arguments[0].click()", log)

	def text_name_attribute_attroney(self):
		wd = self.app.wd
		return WebDriverWait(wd, 15).until(EC.presence_of_element_located((By.ID, "basic-button"))).get_attribute("textContent")

	def text_name_attribute_secretary(self):
		wd = self.app.wd
		return WebDriverWait(wd, 15).until(EC.presence_of_element_located((By.ID, "basic-button"))).get_attribute("textContent")

	def text_name_attribute_cr(self):
		wd = self.app.wd
		return WebDriverWait(wd, 15).until(EC.presence_of_element_located((By.ID, "basic-button"))).get_attribute("textContent")

	def ensure_logout(self):
		wd = self.app.wd
		if self.is_logged_in():
			self.logout()

	def is_logged_in(self):
		wd = self.app.wd
		#return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0
		return len(wd.find_elements(By.CSS_SELECTOR, "div[data-name='headerExitIconDiv']")) > 0


	def is_logged_in_as(self):
		wd = self.app.wd
		return len(wd.find_elements(By.CSS_SELECTOR, "div[data-name='headerCardIconDiv']")) > 0

	def ensure_login(self, login, password):
		wd = self.app.wd
		if self.is_logged_in():
			if self.is_logged_in_as():
				return
			else:
				self.logout()
		self.login(login, password)


''' ----DEV----
	def text_name_attribute_cr(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.presence_of_element_located(
			(By.CSS_SELECTOR, "div.sc-gGmIRh.dfsDm"))).get_attribute("textContent")
'''

