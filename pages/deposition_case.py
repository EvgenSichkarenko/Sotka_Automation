from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class DepositionCase:
	def __init__(self, app):
		self.app = app


	def name_deposition(self, name):
		wd = self.app.wd
		WebDriverWait(wd,  10).until(EC.element_to_be_clickable((By.NAME, "attorneyHomeNewDepBtn"))).click()
		input = wd.find_element(By.CSS_SELECTOR, "input[data-name='caseNameSearchInput']")
		input.send_keys(name)
		#open deponent page
		input.send_keys(Keys.ENTER)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseDeponentPrevBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseNameContinueBtn"))).click()


	def deponent_deposition(self, deponent):
		wd = self.app.wd
		input = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[data-name='caseDeponentInput']")))
		input.send_keys(deponent)
		input.send_keys(Keys.RETURN)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationPrevBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseDeponentContinueBtn"))).click()

	def location_deposition(self, address):
		wd = self.app.wd
		#company address
		address_company = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
		"span[data-name='companyLocationAddress']")))
		add = address_company.get_attribute("textContent")
		assert address == add
		#different location
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationCompanyDifLocationBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationByZoomBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationContinueBtn"))).click()


		# WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationContinueBtn"))).click()
		# WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationContinueBtn"))).click()


