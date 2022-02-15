from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class DepoDetailsAtt:
	def __init__(self, app):
		self.app = app

	def open_details(self):
		wd = self.app.wd
		WebDriverWait(wd, 5).until((EC.element_to_be_clickable((By.NAME, "attorneyHomePastDepBtn")))).click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "pastDepositionBtnDetails2"))).click()

	def details(self):
		wd = self.app.wd

		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "InfoHeaderButton"))).click()
		title_documents = wd.find_element(By.CSS_SELECTOR, "div[data-name='downloadsTitle']").get_attribute(
			"textContent")
		if title_documents == 'Documents':
			# WebDriverWait(wd, 10).until(
			# EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='fileContainer']")))[1].click()
			# WebDriverWait(wd, 10).until(
			# 	EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='fileTitle']")))[1].click()
			wd.find_element(By.XPATH,
				"/html/body/div/section/div[1]/div[2]/div/div/div[3]/div[2]/div/div[3]/div[1]").click()

	def check_deposition_data(self, name, deponent, attorney):
		wd = self.app.wd
		deposition_name = wd.find_element(By.CSS_SELECTOR, "div[data-name='infoDepositionCaseTitle']").get_attribute('textContent')
		date = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDDateRow']").get_attribute(
			'textContent')
		deponent_depo = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDDeponentRow']").get_attribute(
			'textContent')
		attorney_depo = wd.find_element(By.CSS_SELECTOR, "div[data-name='infoAttorneySbn']").get_attribute(
			'textContent')
		location = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDLocationValue']").get_attribute(
			'textContent')
		time.sleep(2)
		assert deposition_name == name
		#assert deponent_depo == deponent
		assert attorney_depo == attorney

	def check_op_data(self):
		wd = self.app.wd
		#opposing counsel
		name_cr = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoFullNameRow']").get_attribute(
			'textContent')
		email_cr = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoEmailRow']").get_attribute(
			'textContent')
		phone_cr = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoPhoneRow']").get_attribute(
			'textContent')

		assert name_cr
		assert email_cr
		assert phone_cr





