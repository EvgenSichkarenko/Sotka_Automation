import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Attorney:
	def __init__(self, app):
		self.app = app

		'''-----DEV-----'''
	def contact_person(self, att_sbn, att_email, att_phonenumber):
		wd = self.app.wd
		wd.find_element(By.CSS_SELECTOR, ".sc-fTNIDv.ieXpgb > svg").click()
		wd.find_element(By.CSS_SELECTOR, "input[name='sbn']").send_keys(att_sbn)
		wd.find_element(By.XPATH, "//button[text()='Search']").click()
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))).send_keys(att_email)
		wd.find_element(By.CSS_SELECTOR, "input[name='phone_number']").send_keys(att_phonenumber)
		assert wd.find_element(By.CSS_SELECTOR, "input[name='sbn']").get_attribute('value') == att_sbn
		wd.find_element(By.XPATH, "//button[text()='Invite']").click()