import os.path
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrCR:
	def __init__(self, app):
		self.app = app

	def cr_registration_form(self, cr_bar_number):
		wd = self.app.wd
		self.app.open_login(wd)
		wd.find_element(By.NAME, "registrationSignInLink").click()
		wd.find_element(By.NAME, "stepTwoCrBtn").click()
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").send_keys(cr_bar_number)
		wd.find_element(By.CSS_SELECTOR, "span[data-name='stepTwoCheckboxAgreeSpan']").click()
		wd.find_element(By.NAME, "stepTwoContinueBtn").click()

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
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))).send_keys(cr_email)
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
		wd.find_element(By.NAME, "stepThreeContinueBtn").click()


	def availability_button(self):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME , "stepFourContinueBtn"))).click()
		# WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "stepFourAvailibleBtn5"))).click()
		# wd.find_element(By.NAME, "stepFourAvailibleBtn1").click()

	def price_form(self):
		wd = self.app.wd
		form_price = wd.find_element(By.CSS_SELECTOR, "form[data-name='stepSixForCrForm']")
		form_price.find_element(By.CSS_SELECTOR, "div[data-name='appearanceFee'] input[name='appearanceFee']").send_keys("22")
		form_price.find_element(By.CSS_SELECTOR, "div[data-name='pageCost'] input[name='pageCost']").send_keys("2")
		form_price.find_element(By.CSS_SELECTOR, "div[data-name='expertPageCost'] input[name='expertPageCost']").send_keys("3")
		form_price.find_element(By.CSS_SELECTOR, "div[data-name='travel'] input[name='travel']").send_keys("3")
		form_price.find_element(By.CSS_SELECTOR, "div[data-name='estimated'] input[name='estimated']").send_keys("10")
		form_price.find_element(By.CSS_SELECTOR, "div[data-name='turnAroundTime'] input[name='turnAroundTime']").send_keys("5")
		form_price.find_element(By.CSS_SELECTOR, "div[data-name='copy'] input[name='copy']").send_keys("100%")
		cancellation = wd.find_element(By.CSS_SELECTOR, "div[data-name='cancellation'] input[name='cancellation']")
		cancellation.click()
		cancellation.send_keys("$10")
		wd.find_element(By.NAME, "stepSixContinueBtn").click()

	def upload_photo(self):
		wd = self.app.wd
		image = os.path.abspath("C:\Python\Sotka_auto\data\images\logo.jpg")
		WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "uploadPhotoRefReg")))
		wd.find_element(By.NAME, "uploadPhotoRefReg").send_keys(image)
		wd.find_element(By.NAME, "uploadPhotoContinueBtn").click()

	def set_password(self, password):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "input[name='password']"))).clear()
		wd.find_element(By.CSS_SELECTOR,"input[name='password']" ).send_keys(password)
		wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").send_keys(password)
		wd.find_element(By.NAME, "stepSevenContinueBtn").click()

	def check_send_mail(self):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-name='endStepLinkLink']")))
		login_text = wd.find_element(By.CSS_SELECTOR, "a[data-name='endStepLinkLink']").get_attribute("textContent")
		if login_text == 'Login':
			return True
		else:
			return False, f"Cannot find '{login_text}' in last screen"