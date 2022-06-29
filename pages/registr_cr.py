import os.path
import os
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
import sys
import imaplib
import email
import re

class RegistrCR:
	def __init__(self, app):
		self.app = app

	def cr_registration_form(self, cr_bar_number):
		wd = self.app.wd
		self.app.open_login()
		wd.find_element(By.NAME, "registrationSignInLink").click()
		wd.find_element(By.NAME, "stepTwoCrBtn").click()
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").send_keys(cr_bar_number)
		wd.find_element(By.CSS_SELECTOR, "span[data-name='stepTwoCheckboxAgreeSpan']").click()
		wd.find_element(By.NAME, "stepTwoContinueBtn").click()


	def license_num_input_attribute(self):
		wd = self.app.wd
		return WebDriverWait(wd, 15).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR , "input[name='license_number']"))).get_attribute("value")
		#self.driver.find_element(By.CSS_SELECTOR , "input[name='license_number']").get_attribute("value") #123789

	def cr_data_form(self, cr_email, cr_phone_number, cr_full_name, cr_issuance_date, cr_expiration_date,
			cr_address_one, cr_address_two):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))).send_keys(cr_email)
		wd.find_element(By.CSS_SELECTOR , "input[name='phone_number']").send_keys(cr_phone_number)
		wd.find_element(By.CSS_SELECTOR , "input[name='full_name']").send_keys(cr_full_name)
		wd.find_element(By.CSS_SELECTOR , "input[name='issuance_date']").click()
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR , "input[name='issuance_date']"
		))).send_keys(cr_issuance_date)
		wd.find_element(By.CSS_SELECTOR , "input[name='expiration_date']").click()
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR , "input[name='expiration_date']"
		))).send_keys(cr_expiration_date)
		wd.find_element(By.CSS_SELECTOR , "input[name='address_one']").send_keys(cr_address_one)
		wd.find_element(By.CSS_SELECTOR , "input[name='address_two']").send_keys(cr_address_two)
		wd.find_element(By.NAME, "stepThreeContinueBtn").click()


	def availability_button(self):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME , "stepFourContinueBtn"))).click()
		# WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "stepFourAvailibleBtn5"))).click()
		# wd.find_element(By.NAME, "stepFourAvailibleBtn1").click()

	def price_form(self):
		wd = self.app.wd
		time.sleep(1)
		# form_price = wd.find_element(By.CSS_SELECTOR, "form[data-name='stepSixForCrForm']")
		# form_price.find_element(By.CSS_SELECTOR, "div[data-name='appearanceFee'] input[name='appearanceFee']").send_keys("22")
		# form_price.find_element(By.CSS_SELECTOR, "div[data-name='pageCost'] input[name='pageCost']").send_keys("2")
		# form_price.find_element(By.CSS_SELECTOR, "div[data-name='expertPageCost'] input[name='expertPageCost']").send_keys("3")
		# form_price.find_element(By.CSS_SELECTOR, "div[data-name='travel'] input[name='travel']").send_keys("3")
		# #form_price.find_element(By.CSS_SELECTOR, "div[data-name='estimated'] input[name='estimated']").send_keys("10")
		# form_price.find_element(By.CSS_SELECTOR, "div[data-name='turnAroundTime'] input[name='turnAroundTime']").send_keys("5")
		# form_price.find_element(By.CSS_SELECTOR, "div[data-name='copy'] input[name='copy']").send_keys("100%")
		wd.find_element(By.CSS_SELECTOR, "button[name='stepSixContinueBtn']").click()

	def upload_photo(self):
		wd = self.app.wd
		image = os.path.abspath("C:\Python\Sotka_auto\data\images\logo.jpg")
		#image = os.path.abspath("/var/lib/jenkins/workspace/Sotka_stage/data/images/logo.jpg")
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.NAME, "uploadPhotoRefReg")))
		wd.find_element(By.NAME, "uploadPhotoRefReg").send_keys(image)
		wd.find_element(By.NAME, "uploadPhotoContinueBtn").click()

	def set_password(self, password):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "input[name='password']"))).clear()
		wd.find_element(By.CSS_SELECTOR,"input[name='password']" ).send_keys(password)
		wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").send_keys(password)
		wd.find_element(By.NAME, "stepSevenContinueBtn").click()

	def check_send_mail(self):
		wd = self.app.wd
		time.sleep(4)
		current_zone = datetime.now()  # 10
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

	def check_confirmation_letter(self,email_reg_cr):
		wd = self.app.wd
		time.sleep(2)
		server = "imap.mail.yahoo.com"
		port = 993
		login = "testqa000000@yahoo.com"
		password = "ksbbaatxxwotyabq"

		mail = imaplib.IMAP4_SSL(server, port)
		mail.login(login, password)
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

		if (new_email.count(email_reg_cr) == 1) and (date_email.count(self.sotka_time) == 1):
			return True
		else:
			return False

	def get_link_from_email(self):
		wd = self.app.wd
		time.sleep(3)
		link = re.search("(?P<url>https?://[^\s]+)", self.text).group("url")
		link = link[0:-1]
		time.sleep(1)
		wd.get(link)
		time.sleep(2)

	def save_btn(self):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='editTimeSaveBtn']"))).click()


	def check_price_dashboard(self, minimum_transcript_charge, page_cost ,expert_page_cost,travel, estimated, cancellation_fee,
	turn_around_page,copy):
		wd = self.app.wd
		time.sleep(2)
		pr_block = wd.find_element(By.CSS_SELECTOR, "div[data-name='pricePricesBlock']")
		minTrCharge = pr_block.find_element(By.CSS_SELECTOR, "div[data-name='priceDataWrapper0'] span").get_attribute("textContent")
		# pageCost = pr_block.find_element(By.CSS_SELECTOR, "div[data-name='priceDataWrapper1'] span").get_attribute("textContent")
		# expertPageCost = pr_block.find_element(By.CSS_SELECTOR, "div[data-name='priceDataWrapper2'] span").get_attribute("textContent")
		# travell = pr_block.find_element(By.CSS_SELECTOR, "div[data-name='priceDataWrapper3'] span").get_attribute("textContent")
		# estimat = pr_block.find_element(By.CSS_SELECTOR, "div[data-name='priceDataWrapper4'] span").get_attribute("textContent")
		# cancelation = pr_block.find_element(By.CSS_SELECTOR, "div[data-name='priceDataWrapper5'] span").get_attribute("textContent")
		# turn_around = pr_block.find_element(By.CSS_SELECTOR, "div[data-name='priceDataWrapper6'] span").get_attribute("textContent")
		# #cancel_term = pr_block.find_element(By.CSS_SELECTOR, "div[data-name='priceDataWrapper7'] span").get_attribute("textContent")
		# copy_page = pr_block.find_element(By.CSS_SELECTOR, "div[data-name='priceDataWrapper8'] span").get_attribute("textContent")
		print(minTrCharge)
		print(type(minTrCharge))
		print(minimum_transcript_charge)
		print(type(minimum_transcript_charge))
		assert minimum_transcript_charge == minTrCharge
		# assert pageCost == page_cost
		# assert expertPageCost == expert_page_cost
		# assert travell == travel
		# assert estimat == estimated
		# assert cancelation == cancellation_fee
		# assert turn_around == turn_around_page
		# assert copy_page == copy

	def delete_att_from_database(self):

		message = "User Executor successfully deleted"

		url = self.app.graphql_url()

		headers = {
			"qatoken": "JEKA_QA_TEST_TOKEN"
		}

		data_query = '''mutation{
  			deleteCrAccount(sbn:"0",withCompany:true){
   			status
    		message
 		 }
		}	
		'''

		data = {"query": data_query}
		response = requests.post(url, headers=headers, data=data)
		response_status = response.json()["data"]["deleteCrAccount"]["status"]
		response_message = response.json()["data"]["deleteCrAccount"]["message"]


		assert response.status_code == 200, f"Incorrect status code. Status code id '{response.status_code}'"
		assert response_status == True, f"Incorrect status. Status response is '{response_status}'"
		assert response_message == message, f"Incorrect status. Status response is '{response_message}'"