from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class DepoDetailsCr:
	def __init__(self, app):
		self.app = app

	def open_details(self):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((
			By.XPATH, "/html/body/div/section/div[1]/div[1]/button[2]"))).click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "pastDepositionBtnDetails2"))).click()

	def check_deposition_data(self, name, deponent, attorney):
		wd = self.app.wd
		time.sleep(1)
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
		assert deponent_depo == (deponent + " (deponent)")
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

	def check_invoice(self):
		wd = self.app.wd

		appearance_fee = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoFullNameRow']").get_attribute(
			'textContent')
		page_cost = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoEmailRow']").get_attribute(
			'textContent')
		pages = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoPhoneRow']").get_attribute(
			'textContent')
		travel = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoFullNameRow']").get_attribute(
			'textContent')
		total = wd.find_element(By.CSS_SELECTOR, "div[data-name='PDInfoEmailRow']").get_attribute(
			'textContent')







