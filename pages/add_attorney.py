import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Attorney:
	def __init__(self, app):
		self.app = app

		'''-----DEV-----'''
	def attorney_company(self, att_sbn, att_email_old, att_phonenumber, new_email):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='homeAddNewAttorneyIcon']"))).click()

		#search company using bar number
		wd.find_element(By.CSS_SELECTOR, "input[name='sbn']").send_keys(att_sbn)
		wd.find_element(By.NAME, "addNewSearchBtnModal").click()

		#send new email and phone number
		WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))).send_keys(att_email_old)
		wd.find_element(By.CSS_SELECTOR, "input[name='phone_number']").send_keys(att_phonenumber)
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