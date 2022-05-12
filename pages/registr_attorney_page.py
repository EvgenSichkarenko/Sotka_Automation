import os.path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import json

class RegistrAttorney:
	def __init__(self, app):
		self.app = app

	def registration_page(self, bar_number):
		wd = self.app.wd
		self.app.open_login()
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
		wd.find_element(By.CSS_SELECTOR, "span[data-name='stepTwoCheckboxAgreeSpan']").click()
		wd.find_element(By.NAME, "stepTwoContinueBtn").click()

	def fill_form(self, email, bar_number,phone_number, address_two):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "input[name='email']"
		))).send_keys(email)

		#Check phone number field
		phone = WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.NAME, "phone_number")))
		phone_value = phone.get_property("value")
		if phone_value == "":
			phone.send_keys(phone_number)

		#Check address two field
		address = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "address_two")))
		address_value = address.get_property("value")
		if address_value == "":
			address.send_keys(address_two)

		#Check bar number
		value = wd.find_element(By.CSS_SELECTOR, "input[name='sbn']").get_property("value")
		if value == bar_number:
			wd.find_element(By.NAME, "stepThreeAttorneyContinue").click()

	def assert_secreatry(self):
		wd =self.app.wd
		check_name = WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Add secretary']"))).text
		if check_name == 'Add secretary':
			pass

	def add_secretary(self, name_secretary, email_secretary):
		wd = self.app.wd
		# WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.NAME, "full_name"))).send_keys(name_secretary)
		# wd.find_element(By.NAME, "email").send_keys(email_secretary)
		wd.find_element(By.NAME, "addSecretaryContinueBtn").click()
		# WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
		# 	(By.NAME, "addSecretarySkipBtn"))).click()

	def img_account_send(self):
		wd = self.app.wd
		image = os.path.abspath("C:\Python_project\Sotka_auto\data\images\logo.jpg")
		#image = os.path.abspath("/var/lib/jenkins/workspace/Sotka_pre_prod/data/images/logo.jpg")
		check_name = WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Your photo account']"))).text
		if check_name == 'Your photo account':
			wd.find_element(By.NAME, "uploadPhotoRef").send_keys(image)
		else:
			print("Photo account page not open")
		wd.find_element(By.NAME, "uploadPhotoContinueBtn").click()

	def bank_account_button(self):
		wd = self.app.wd
		wd.find_element(By.NAME, "stepSixContinueBtn").click()

	def password_input_enter(self, valid_password, invalid_password, password_match):
		wd = self.app.wd
		self.confirm_password(invalid_password, password_match)
		valid_pasw = wd.find_element(By.XPATH, "//span[text()='This field should contain at least 6 characters']").get_attribute('textContent')
		valid_conf_pasw = wd.find_element(By.XPATH, "//span[text()='Passwords must match']").get_attribute('textContent')
		if valid_pasw and valid_conf_pasw:
			self.confirm_password(valid_password,valid_password)
		else:
			print("Validation password isn't works")

	def confirm_password(self, text1, text2):
		wd = self.app.wd
		input = WebDriverWait(wd, 15).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "input[name='password']")))
		input.send_keys(Keys.CONTROL + "a")
		input.send_keys(Keys.BACK_SPACE)
		wd.find_element(By.CSS_SELECTOR,"input[name='password']" ).send_keys(text1)
		second_input = wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']")
		second_input.send_keys(Keys.CONTROL + "a")
		time.sleep(1)
		second_input.send_keys(Keys.BACK_SPACE)
		wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").send_keys(text2)
		wd.find_element(By.NAME, "stepSevenContinueBtn").click()

	def login_present(self):
		wd = self.app.wd
		#return WebDriverWait(wd, 5).until(EC.visibility_of((By.CSS_SELECTOR, "a[data-name='endStepLinkLink']"))).get_attribute("textContent")
		#return wd.find_element(By.CSS_SELECTOR, "a[data-name='endStepLinkLink']").get_attribute("textContent")
		return WebDriverWait(wd, 10).until(EC.visibility_of_element_located((
			By.CSS_SELECTOR, "a[data-name='endStepLinkLink']"))).get_attribute("textContent")

	def delete_att_from_database(self):
		wd = self.app.wd

		url = "https://apidemo.trialbase.com/graphql"

		headers = {
			"qa_token":"JEKA_QA_TEST_TOKEN"
		}

		data_query ='''mutation{
  			deleteUser(sbn:"000000"){
   			 status
    		message
 		 }
		}	
		'''

		data = {"query": data_query}
		response = requests.post(url, headers=headers,data=data)


		print(response.status_code)
		print(response.json())