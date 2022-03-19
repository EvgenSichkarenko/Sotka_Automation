from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pyautogui


class DepositionCase:
	def __init__(self, app):
		self.app = app


	def name_deposition(self, name):
		wd = self.app.wd
		WebDriverWait(wd,  10).until(EC.element_to_be_clickable((By.NAME, "attorneyHomeNewDepBtn"))).click()
		input = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='caseNameSearchInputWrapper'] input")))
		input.send_keys(name)
		input.send_keys(Keys.ENTER)
		# WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseDeponentPrevBtn"))).click()
		# WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseNameContinueBtn"))).click()


	def deponent_deposition(self, deponent):
		wd = self.app.wd
		input = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div [data-name='caseDeponentInput'] input")))
		input.send_keys(deponent)
		input.send_keys(Keys.RETURN)
		# WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationPrevBtn"))).click()
		# WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseDeponentContinueBtn"))).click()

	def location_deposition(self, address):
		wd = self.app.wd

		case_location = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='caseLocationTitle']"))).text
		assert case_location == 'Select location', "Select location tab isn't working"
		#company address
		# address_company = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
		# "span[data-name='companyLocationAddress']")))
		# add = address_company.get_attribute("textContent")
		# assert address == add
		#different location
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationCompanyDifLocationBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationByZoomBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationContinueBtn"))).click()

	def attorneys(self,op_sbn):
		wd = self.app.wd
		#check data attorney
		#add opposing counsel
		input_sbn_op = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='searchAutocomplete'] input")))
		input_sbn_op.click()
		input_sbn_op.send_keys(op_sbn)
		op = wd.find_element(By.XPATH, "//span[text()='Gregg Michael Missbach']")
		op.click()

		add_op = len(wd.find_elements(By.CSS_SELECTOR, "div[data-name='rightBlockExistedOC'] > div"))

		if add_op > 0:
			wd.find_element(By.NAME, "caseLocationContinueBtn").click()

	def set_time_manually(self):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Set up time manually']"))).click()
		#wd.execute_script("document.body.style.zoom='70%'")
		wd.find_element(By.XPATH, "//div[text()='Confirm']").click()

	def upload_doc(self):
		wd = self.app.wd
		file = os.path.abspath("C:\Python\Sotka_auto\data\doc\DEPO.pdf")
		image_path = "C:\Python\Sotka_auto\data\doc\DEPO.pdf"
		#WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "depoUploadBtn"))).click()
		wd.find_element(By.XPATH, "//input[@name='inputFileHidden']").send_keys(image_path)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "depoContinueBtn"))).click()

	def delivery(self):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='deliverySearchInput'] input"))).send_keys("CR Test")
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='CR Test']"))).click()
		time.sleep(1)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='deliveryContinueBtn']"))).click()


	def finish_depo(self):
		wd = self.app.wd
		time.sleep(1)
		#Attorney info
		name_attorney =  WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[text()='Joel William Meskin']"))).text
		email_finish = wd.find_element(By.XPATH, "//span[text()='testatt@inboxbear.com']").text
		phone_finish = wd.find_element(By.XPATH, "//span[text()='440-333-6300']").text

		assert name_attorney == "Joel William Meskin"
		assert email_finish == "testatt@inboxbear.com"
		assert phone_finish == "440-333-6300"

		#Op info
		name_attorney =  WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[text()='Gregg Michael Missbach']"))).text
		email_finish = wd.find_element(By.XPATH, "//span[text()='testop@getnada.com']").text
		phone_finish = wd.find_element(By.XPATH, "//span[text()='+38984521236']").text

		assert name_attorney == "Gregg Michael Missbach"
		assert email_finish == "testop@getnada.com"
		assert phone_finish == "+38984521236"

		#Cr info
		name_attorney =  WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[text()='CR Test']"))).text
		email_finish = wd.find_element(By.XPATH, "//span[text()='crtestcr@getnada.com']").text
		phone_finish = wd.find_element(By.XPATH, "//span[text()='+380964512360']").text

		assert name_attorney == "CR Test"
		assert email_finish == "crtestcr@getnada.com"
		assert phone_finish == "+380964512360"

	def confirm(self):
		wd = self.app.wd

		wd.find_element(By.NAME, "finishConfirmBtn").click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "finishDepositionBtn"))).click()
