import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import json


class Attorney:
	def __init__(self, app):
		self.app = app

		'''-----DEV-----'''
	def attorney_company(self, att_sbn, registr_email):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='homeAddNewAttorneyIcon']"))).click()

		#search company using bar number
		wd.find_element(By.CSS_SELECTOR, "div[data-name='searchAutocomplete'] input").send_keys(att_sbn)
		time.sleep(5)
		WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[text()='{registr_email}']"))).click()
		#wd.find_element(By.XPATH, f"//span[text()='{registr_email}']").click()
		time.sleep(1)
		wd.find_element(By.CSS_SELECTOR, "button[name='checkOppCounselInfoInvite']").click()
		time.sleep(1)

	def set_password(self, password):
		wd = self.app.wd

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys(password)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='confirmPassword']"))).send_keys(password)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Submit']"))).click()
		time.sleep(1)
		#Click link login
		wd.find_element(By.XPATH, "//a[text()='Login']").click()
		time.sleep(2)

	def delete_att_from_database(self,sbn):

		message_delete = "Attorney successfully deleted"

		url = "http://ec2-3-120-152-160.eu-central-1.compute.amazonaws.com:8080/graphql"

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

		data1 = "mutation{deleteAttorneyAccount(sbn:"+ f'"{sbn}",' + f'withCompany:false)' + "{status, message}}"
		data2 = {"query": data1}

		response = requests.post(url, headers=headers, data=data2)

		status = response.json()["data"]["deleteAttorneyAccount"]["status"]
		message = response.json()["data"]["deleteAttorneyAccount"]["message"]

		assert status == True
		assert message == message_delete

	def attorney_different_company(self, att_sbn, att_email_old, new_email):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='homeAddNewAttorneyIcon']"))).click()

		#search company using bar number
		wd.find_element(By.CSS_SELECTOR, "div [data-name='searchAutocomplete'] input").send_keys(att_sbn)
		wd.find_element(By.NAME, "addNewSearchBtnModal").click()

		#send new email and phone number
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))).send_keys(att_email_old)
		assert wd.find_element(By.CSS_SELECTOR, "input[name='sbn']").get_attribute('value') == att_sbn
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "addNewAttorneyInviteBtnModal"))).click()

		email_exist = WebDriverWait(wd, 5).until(EC.visibility_of_element_located((
			By.XPATH, "//span[text()='Email already registered']"))).get_attribute("textContent")
		#clear email-input field and add new email
		if email_exist:
			WebDriverWait(wd, 15).until(
				EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))).clear()
			WebDriverWait(wd, 15).until(
				EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))).send_keys(new_email)
			WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "addNewAttorneyInviteBtnModal"))).click()