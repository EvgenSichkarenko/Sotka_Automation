import os.path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrAttorney:
	def __init__(self, app):
		self.app = app

	def registration_page(self, bar_number):
		wd = self.app.wd
		self.app.open_login(wd)
		wd.find_element(By.XPATH, "//a[text()='Sign Up']").click()
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='barNumber']").send_keys(bar_number)
		wd.find_element(By.CSS_SELECTOR, "div.sc-kfzAmx.cEaHKM").click()
		wd.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

	def attorney_button_click(self):
		wd = self.app.wd
		wd.find_element(By.CSS_SELECTOR, "//button[text()='Attorney']").click()

	def fill_form(self, email):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "input[name='email']"
		))).send_keys(email)
		wd.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

	def sbn_input_attribute(self):
		wd = self.app.wd
		wd.find_element(By.CSS_SELECTOR, "input[name='sbn']").get_property("value") #123789

	def skip_secretary_button(self):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "button.sc-kstrdz.sc-fodVxV.jlyKYH.cetTfq")
		)).click()

	def img_account_send(self):
		wd = self.app.wd
		image = os.path.abspath("C:\Python\Sotka_auto\data_model\images\logo.jpg")
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "div.sc-khAkjo.dgxcKs > img")
		)).send_keys(image)

	def continue_account_button(self):
		wd = self.app.wd
		wd.find_element(By.XPATH, "//button[text()='Continue']").click()

	def password_input_enter(self, password):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.visibility_of_element_located(
			(By.CSS_SELECTOR, "input[name='password']"
		))).send_keys(password)
		wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']").send_keys(password)
		wd.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
		# wd.find_element(By.CSS_SELECTOR, ".sc-citwmv.sc-bZSQDF.kajamm.eUgDnc > a").click()
		# assert wd.find_element(By.CSS_SELECTOR, ".sc-eCssSg.hmocIu").get_attribute("textContent") == "Welcome"

	def login_present(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.visibility_of(wd.find_element(By.CSS_SELECTOR, "div.sc-citwmv.sc-bZSQDF.kajamm.eUgDnc")))