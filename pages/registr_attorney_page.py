import os.path
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import sys
import imaplib
import email
import json
import re

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
	def registr_op_unreg(self,bar_number):
		wd = self.app.wd
		wd.find_element(By.NAME, "registrationSignInLink").click()
		text_attribute = wd.find_element(By.NAME, "barNumber").get_attribute("placeholder")

		if text_attribute == "Bar Number":
			self.add_bar_number(bar_number)
		else:
			wd.find_element(By.NAME, "stepTwoAttorneyBtn").click()
			self.add_bar_number(bar_number)

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

	def next_step(self):
		wd = self.app.wd
		time.sleep(1)
		wd.find_element(By.NAME, "stepThreeAttorneyContinue").click()
		time.sleep(1)

	def assert_secreatry(self):
		wd =self.app.wd
		check_name = WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Add secretary']"))).text
		if check_name == 'Add secretary':
			pass

	def skip_secretary(self):
		wd = self.app.wd
		wd.find_element(By.NAME, "addSecretaryContinueBtn").click()

	def add_secretary_skip(self, name_secretary, email_secretary):
		wd = self.app.wd
		time.sleep(2)
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.NAME, "full_name"))).send_keys(name_secretary)
		wd.find_element(By.NAME, "email").send_keys(email_secretary)
		wd.find_element(By.NAME, "addSecretarySkipBtn").click()

	def check_input_secr(self):
		wd = self.app.wd
		time.sleep(1)
		full_name = wd.find_element(By.CSS_SELECTOR, "input[name='full_name']").get_attribute("value")
		email = wd.find_element(By.CSS_SELECTOR, "input[name='email']").get_attribute("value")
		wd.find_element(By.NAME, "addSecretaryContinueBtn").click()
		if (full_name == "" and email == ""):
			return True
		else:
			return False

	def return_back(self):
		wd = self.app.wd
		wd.find_element(By.XPATH, "//div[text()='Back']").click()

	def add_secretary(self, name_secretary, email_secretary):
		wd = self.app.wd
		time.sleep(2)
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.NAME, "full_name"))).send_keys(name_secretary)
		wd.find_element(By.NAME, "email").send_keys(email_secretary)
		wd.find_element(By.NAME, "addSecretaryContinueBtn").click()

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

	def check_send_mail(self):
		wd = self.app.wd
		time.sleep(4)

		current_zone = datetime.now()
		three_hours = timedelta(hours=3)
		min_three = current_zone - three_hours
		current_date = datetime.today().strftime(f'%a, %d %b %Y {min_three.strftime("%H")}')
		self.sotka_time = f"{current_date}"

		text = wd.find_element(By.XPATH, "//div[text()='Please check your mailbox. We have sent you a confirmation email']").get_attribute("textContent")

		if text == 'Please check your mailbox. We have sent you a confirmation email':
			return True
		else:
			return False, f"Cannot find '{text}' in last screen"

	def get_message_info(self,message):

		message_text, encoding, mime = "Нет тела сообщения", "-", "-"
		if message.is_multipart():
			for part in message.walk():
				if part.get_content_type() in ("text/html", "text/plain"):
					message_text, encoding, mime = self.get_part_info(part)
					break  # Только первое вхождение
		else:
			message_text, encoding, mime = self.get_part_info(message)

		return message_text, encoding, mime

	def get_part_info(self,part):

		encoding = part.get_content_charset()
		if not encoding:
			encoding = sys.stdout.encoding

		mime = part.get_content_type()
		message = part.get_payload(decode=True).decode(encoding, errors="ignore").strip()

		return message, encoding, mime

	def check_confirmation_letter(self, email_reg_att, log, password):
		wd = self.app.wd
		time.sleep(2)
		server = "imap.mail.yahoo.com"
		port = 993

		mail = imaplib.IMAP4_SSL(server, port)
		mail.login(log, password)
		mail.select()
		type, data = mail.search(None, "(FROM 'Trialbase')")
		data = data[0].split()
		latest_id = data[-1]
		result, data = mail.fetch(latest_id, "(RFC822)")

		raw_email = data[0][1]
		message = email.message_from_bytes(raw_email)
		date_email = message["Date"]

		self.text, encoding, mime = self.get_message_info(message)

		new_email = re.sub(r"\r\n", "", self.text)
		if (new_email.count(email_reg_att) == 1):
			return True
		else:
			return False

	def delete_att_from_database(self):

		time.sleep(2)
		message = "Attorney and company successfully deleted"

		url = self.app.graphql_url()

		headers = {
			"qatoken":"JEKA_QA_TEST_TOKEN"
		}

		data_query ='''mutation{
  			deleteAttorneyAccount(sbn:"000000", withCompany:true){
   			status
    		message
 		 }
		}	
		'''

		data = {"query": data_query}
		response = requests.post(url, headers=headers,data=data)

		response_status = response.json()["data"]["deleteAttorneyAccount"]["status"]
		response_message = response.json()["data"]["deleteAttorneyAccount"]["message"]

		assert response.status_code == 200, f"Incorrect status code. Status code id '{response.status_code}'"
		assert response_status == True, f"Incorrect status. Status response is '{response_status}'"
		assert response_message == message, f"Incorrect status. Status response is '{response_message}'"

	def create_acc_unregistr(self):
		wd = self.app.wd
		time.sleep(2)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='createTrialbase']"))).click()
		time.sleep(1)

	def delete_op_from_database(self):
		time.sleep(2)
		message = "Attorney and company successfully deleted"

		url = self.app.graphql_url()

		headers = {
			"qatoken": "JEKA_QA_TEST_TOKEN"
		}

		data_query = '''mutation{deleteAttorneyAccount(sbn:"000003",withCompany:true){   status   message } 		}	
				'''

		data = {"query": data_query}
		response = requests.post(url, headers=headers, data=data)

		response_status = response.json()["data"]["deleteAttorneyAccount"]["status"]
		response_message = response.json()["data"]["deleteAttorneyAccount"]["message"]

		assert response.status_code == 200, f"Incorrect status code. Status code id '{response.status_code}'"
		assert response_status == True, f"Incorrect status. Status response is '{response_status}'"
		assert response_message == message, f"Incorrect status. Status response is '{response_message}'"

	def add_op_unregister(self,op_sbn, email_voting):
		wd =self.app.wd
		time.sleep(1)
		input_sbn_op = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='searchAutocomplete'] input")))
		input_sbn_op.click()
		input_sbn_op.send_keys(op_sbn)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{email_voting}']"))).click()
		time.sleep(2)
		wd.find_element(By.CSS_SELECTOR, "button[name='checkOppCounselInfoInvite']").click()
		time.sleep(1)
		wd.find_element(By.NAME, "caseLocationContinueBtn").click()