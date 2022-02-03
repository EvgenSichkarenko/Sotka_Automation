import os.path
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrAttorney:
	def __init__(self, app):
		self.app = app

	def registration_page(self, bar_number):
		wd = self.app.wd
		self.app.open_login(wd)
		wd.find_element(By.NAME, "registrationSignInLink").click()
		text_attribute = wd.find_element(By.NAME, "barNumber").get_attribute("placeholder")

		if text_attribute == "Bar Number":
			self.add_bar_number(bar_number)
		else:
			wd.find_element(By.NAME, "stepTwoAttorneyBtn").click()
			self.add_bar_number(bar_number)

#Registration page
	def add_bar_number(self, bar_number):
		wd = self.app.wd
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").send_keys(bar_number)
		wd.find_element(By.CSS_SELECTOR, "div.sc-fKFyDc.jFaure").click()
		wd.find_element(By.NAME, "stepTwoContinueBtn").click()

	def fill_form(self, email, bar_number):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "input[name='email']"
		))).send_keys(email)
		value = wd.find_element(By.CSS_SELECTOR, "input[name='sbn']").get_property("value")
		if value == bar_number:
			wd.find_element(By.XPATH, "//button[text()='Continue']").click()

	def assert_secreatry(self):
		wd =self.app.wd
		check_name = WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Add secretary']"))).text
		if check_name == 'Add secretary':
			pass

	def add_secretary(self, name_secretary, email_secretary):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.NAME, "full_name"))).send_keys(name_secretary)
		wd.find_element(By.NAME, "email").send_keys(email_secretary)
		wd.find_element(By.NAME, "addSecretaryContinueBtn").click()
		# WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
		# 	(By.NAME, "addSecretarySkipBtn"))).click()

	def img_account_send(self):
		wd = self.app.wd
		image = os.path.abspath("C:\Python\Sotka_auto\data\images\logo.jpg")
		check_name = WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Your photo account']"))).text
		if check_name == 'Your photo account':
			wd.find_element(By.NAME, "uploadPhotoRef").send_keys(image)
		else:
			print("Photo account page not open")
		wd.find_element(By.XPATH, "//button[text()='Continue']").click()

	def continue_account_button(self):
		wd = self.app.wd
		wd.find_element(By.XPATH, "//button[text()='Continue']").click()

	def password_input_enter(self, valid_password, invalid_password, password_match):
		wd = self.app.wd
		self.confirm_password(invalid_password, password_match)
		valid_pasw = wd.find_element(By.XPATH, "//span[text()='Must Contain 6 Characters']").get_attribute('textContent')
		valid_conf_pasw = wd.find_element(By.XPATH, "//span[text()='Passwords must match']").get_attribute('textContent')
		if valid_pasw and valid_conf_pasw:
			self.confirm_password(valid_password,valid_password)
		else:
			print("Validation password isn't works")

	def confirm_password(self, text1, text2):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "input[name='password']"))).clear()
		wd.find_element(By.CSS_SELECTOR,"input[name='password']" ).send_keys(text1)
		wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").send_keys(text2)
		wd.find_element(By.NAME, "stepSevenContinueBtn").click()

	def login_present(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.visibility_of(wd.find_element(By.CSS_SELECTOR, "div.sc-citwmv.sc-bZSQDF.kajamm.eUgDnc")))