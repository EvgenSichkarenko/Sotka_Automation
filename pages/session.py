from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Session:
	def __init__(self, app):
		self.app = app

	def login(self, login, password):
		wd = self.app.wd
		self.app.open_login(wd)
		#wd.execute_script("document.body.style.zoom='75%'")
		wd.find_element(By.NAME, "login").clear()
		wd.find_element(By.NAME, "login").send_keys(login)
		wd.find_element(By.NAME, "password").clear()
		wd.find_element(By.NAME, "password").send_keys(password)
		wd.find_element(By.NAME, "registrationSignInBtn").click()

	def logout(self):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.ID, "basic-button"))).click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.XPATH, "//ul/li/div[text()=' Log Out']"))).click()


	def text_name_attribute_attroney(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.ID, "basic-button"))).get_attribute("textContent")

	def text_name_attribute_secretary(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.ID, "basic-button"))).get_attribute("textContent")

	def text_name_attribute_cr(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.ID, "basic-button"))).get_attribute("textContent")

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

