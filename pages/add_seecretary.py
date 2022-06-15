from selenium.webdriver.common.by import By
import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import json


class Secretary:
	def __init__(self, app):
		self.app = app

	def contact_person(self, secr_new_email, secr_old_email,  secr_fullname):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='homeAddNewContactPersonIcon']"))).click()
		wd.find_element(By.CSS_SELECTOR, "input[name='full_name']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='full_name']").send_keys(secr_fullname)
		self.add_input_data(secr_old_email)
		#check validation secretary with this email is registered User with email: testSecattr@inboxbear.com is exists
		validation_exist = wd.find_element(By.XPATH, f"//div[text()='User with email: {secr_old_email} is exists']")\
			.get_attribute("textContent")
		if validation_exist:
			with allure.step(f"New email for secretary is '{secr_new_email}''"):
				self.add_input_data(secr_new_email)
				valid = wd.find_element(By.XPATH,
					"//div[text()='Contact person was invited successfully']") \
					.get_attribute("textContent")
				assert valid == "Contact person was invited successfully"
				time.sleep(2)
#Contact person was invited successfully
#User with email: testSecattr@inboxbear.com is exists

	def add_input_data(self, text):
		wd = self.app.wd
		input_email = wd.find_element(By.CSS_SELECTOR, "input[name='email']")
		input_email.send_keys(Keys.CONTROL + "a")
		input_email.send_keys(Keys.BACK_SPACE)
		wd.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(text)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "addSecretaryInvite"))).click()
		time.sleep(1)

	def set_password(self, password):
		wd = self.app.wd
		time.sleep(2)
		wd.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
		time.sleep(1)
		wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").send_keys(password)
		time.sleep(1)
		wd.find_element(By.XPATH, "//div[text()='Confirm']").click()
		time.sleep(1)
		#Click link login
		wd.find_element(By.XPATH, "//a[text()='Login']").click()
		time.sleep(2)

	def login(self, login, password):
		wd = self.app.wd
		time.sleep(1)
		login_input = WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='login']")))
		login_input.send_keys(login)

		password_input = wd.find_element(By.CSS_SELECTOR, "input[name='password']")
		password_input.send_keys(password)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "button[name='registrationSignInBtn']"))).send_keys(Keys.RETURN)

	def check_secr_on_dashboard(self):
		wd = self.app.wd
		time.sleep(2)
		contact_person = wd.find_element(By.CSS_SELECTOR, "div[data-name='contactPersonWrapper']")
		time.sleep(1)
		name = contact_person.find_element(By.XPATH, "//div[text()='Secretary QA']").text
		time.sleep(1)
		email = contact_person.find_element(By.XPATH, "//p[text()='qaautomationsecrdel@yahoo.com']").text
		if (name and email):
			return True
		else:
			return False

	def delete_secretary_from_database(self,secr_new_email):

		message_delete = "Secretary was successfully deleted"
		url = "https://apidemo.trialbase.com/graphql"
		#url = "http://ec2-3-120-152-160.eu-central-1.compute.amazonaws.com:8080/graphql"

		qu = """mutation{signIn(email:"qaautomationatt@yahoo.com", password:"ZXcv@123580" ){
		  access_token
		}

		}"""
		data = {"query": qu}
		response = requests.post(url, data=data)
		access_token = response.json()["data"]["signIn"]["access_token"]
		#Deleet from database
		auth_header = 'Bearer ' + access_token
		headers = {
			"Authorization": auth_header,
			"qatoken": "JEKA_QA_TEST_TOKEN"
		}

		data1 = "mutation{deleteSecretaryFromCompany(email:" + f'"{secr_new_email}")' + "{status, message}}"
		data2 = {"query": data1}

		response = requests.post(url, headers=headers, data=data2)

		status = response.json()["data"]["deleteSecretaryFromCompany"]["status"]
		message = response.json()["data"]["deleteSecretaryFromCompany"]["message"]

		assert status == True
		assert message == message_delete
