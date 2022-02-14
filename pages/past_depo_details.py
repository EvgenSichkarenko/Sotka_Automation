from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class DepoDetails:
	def __init__(self, app):
		self.app = app

	def details(self):
		wd = self.app.wd
		WebDriverWait(wd, 5).until((EC.element_to_be_clickable((By.NAME, "attorneyHomePastDepBtn")))).click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "pastDepositionBtnDetails2"))).click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "InfoHeaderButton"))).click()
		title_documents = wd.find_element(By.CSS_SELECTOR, "div[data-name='downloadsTitle']").get_attribute(
			"textContent")
		if title_documents == 'Documents':
			WebDriverWait(wd, 5).until(
				EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='fileTitle']"))).click()
		else:
			print("Transcript not found")

	def check_data(self):
		wd = self.app.wd
		deposition_name = wd.find_element(By.CSS_SELECTOR, "div[data-name='infoDepositionCaseTitle']").get_attribute('textContent')
		date = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDDateRow']").get_attribute(
			'textContent')
		deponent = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDDeponentRow']").get_attribute(
			'textContent')
		attorney = wd.find_element(By.CSS_SELECTOR, "div[data-name='infoAttorneySbn']").get_attribute(
			'textContent')
		location = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDLocationValue']").get_attribute(
			'textContent')

		#opposing counsel
		name_cr = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoFullNameRow']").get_attribute(
			'textContent')
		email_cr = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoEmailRow']").get_attribute(
			'textContent')
		phone_cr = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoPhoneRow']").get_attribute(
			'textContent')





