import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrCR:
	def __init__(self, app):
		self.app = app

	def cr_registration_form(self, cr_bar_number):
		wd = self.app.wd
		self.app.open_login(wd)
		wd.find_element(By.XPATH, "//a[text()='Sign Up']").click()
		wd.find_element(By.XPATH, "//button[text()='CR']").click()
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").send_keys(cr_bar_number)
		wd.find_element(By.CSS_SELECTOR, "div.sc-kfzAmx.cEaHKM").click()
		wd.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

	# def email_input_enter(self, email):
	# 	WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
	# 		(By.CSS_SELECTOR, "input[name='email']"
	# 	))).send_keys(email)

	def license_num_input_attribute(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR , "input[name='license_number']"))).get_attribute("value")
		#self.driver.find_element(By.CSS_SELECTOR , "input[name='license_number']").get_attribute("value") #123789

	def cr_data_form(self, cr_email, cr_phone_number, cr_full_name, cr_issuance_date, cr_expiration_date,
			cr_address_one, cr_address_two):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"
		))).send_keys(cr_email)
		wd.find_element(By.CSS_SELECTOR , "input[name='phone_number']").send_keys(cr_phone_number)
		wd.find_element(By.CSS_SELECTOR , "input[name='full_name']").send_keys(cr_full_name)
		wd.find_element(By.CSS_SELECTOR , "input[name='issuance_date']").click()
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR , "input[name='issuance_date']"
		))).send_keys(cr_issuance_date)
		wd.find_element(By.CSS_SELECTOR , "input[name='expiration_date']").click()
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR , "input[name='expiration_date']"
		))).send_keys(cr_expiration_date)
		wd.find_element(By.CSS_SELECTOR , "input[name='address_one']").send_keys(cr_address_one)
		wd.find_element(By.CSS_SELECTOR , "input[name='address_two']").send_keys(cr_address_two)
		wd.find_element(By.XPATH , "//button[text()='Continue']").click()

	def availability_button(self):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.XPATH , "//button[text()='Continue']"))).click()

	def price_form(self):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='appearanceFee']")))\
			.send_keys("3")

		wd.find_element(By.CSS_SELECTOR, "input[name='pageCost']").send_keys("3")
		wd.find_element(By.CSS_SELECTOR, "input[name='expertPageCost']").send_keys("3")
		wd.find_element(By.CSS_SELECTOR, "input[name='travel']").send_keys("5")
		wd.find_element(By.CSS_SELECTOR, "input[name='estimated']").send_keys("10")
		wd.find_element(By.CSS_SELECTOR, "input[name='turnAroundTime']").send_keys("5")
		wd.find_element(By.CSS_SELECTOR, "input[name='copy']").send_keys("100%")
		wd.find_element(By.CSS_SELECTOR, "input[name='cancellation']").send_keys("100")
		wd.find_element(By.CSS_SELECTOR, ".sc-kstrdz.sc-hBEYos.jlyKYH.ghVIMM").click()