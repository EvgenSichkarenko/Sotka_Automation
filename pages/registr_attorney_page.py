import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrAttorney:
	def __init__(self, driver):
		self.driver = driver

	def open(self):
		return self.driver.get("https://sotka.io/")

	def signup_button_click(self):
		self.driver.find_element(By.XPATH, "//a[text()='Sign Up']").click()

	def attorney_button_click(self):
		self.driver.find_element(By.CSS_SELECTOR, "//button[text()='Attorney']").click()

	def bar_numb_input_enter(self, bar_number):
		self.driver.find_element(By.CSS_SELECTOR, "input[name='barNumber']").clear()
		self.driver.find_element(By.CSS_SELECTOR, "input[name='barNumber']").send_keys(bar_number)

	def agree_checkbox_mark(self):
		self.driver.find_element(By.CSS_SELECTOR, "div.sc-kfzAmx.cEaHKM").click()

	def submit_button_click(self):
		self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

	def email_input_enter(self, email):
		WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "input[name='email']"
		)))
		self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(email)

	def sbn_input_attribute(self):
		self.driver.find_element(By.CSS_SELECTOR, "input[name='sbn']").get_property("value") #123789

	def submit_form_button_click(self):
		self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

	def skip_secretary_button(self):
		WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "button.sc-kstrdz.sc-fodVxV.jlyKYH.cetTfq")
		)).click()

	def img_account_send(self):
		image = os.path.abspath("C:\Python\Sotka_auto\data_model\images\logo.jpg")
		WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "div.sc-khAkjo.dgxcKs > img")
		)).send_keys(image)

	def continue_account_button(self):
		self.driver.find_element(By.XPATH, "//button[text()='Continue']").click()

	def password_input_enter(self, password):
		self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
		self.driver.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").send_keys(password)

	def continue_button_click(self):
		self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

	def login_present(self):
		return WebDriverWait(self.driver, 5).until(EC.visibility_of(self.driver.find_element(By.CSS_SELECTOR, "div.sc-citwmv.sc-bZSQDF.kajamm.eUgDnc")))