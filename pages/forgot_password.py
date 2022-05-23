from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class ForgotPassword:
	def __init__(self, app):
		self.app = app

	def forgot_ui(self, email):
		wd = self.app.wd
		self.app.open_login()
		wd.find_element(By.CSS_SELECTOR, "a[name='registrationForgotPassLink']").click()
		email_input = wd.find_element(By.CSS_SELECTOR, "input[name='email']")
		email_input.send_keys(email)
		time.sleep(2)
		wd.find_element(By.CSS_SELECTOR, "button[name='restoreConfirmBtn']").click()
		time.sleep(3)
		text = wd.find_element(By.XPATH, "//div[text()='Please check your mailbox. We have sent you a email']").get_attribute("textContent")
		time.sleep(1)
		if text == 'Please check your mailbox. We have sent you a email':
			return True
		else:
			return False, f"Cannot find '{text}' in last screen"

	def set_new_credentials(self, password):
		wd =self.app.wd
		time.sleep(2)
		input_enter = wd.find_element(By.CSS_SELECTOR, "input[name='password']")
		input_enter.send_keys(password)
		input_confirm = wd.find_element(By.CSS_SELECTOR, "input[name='confirmPassword']")
		input_confirm.send_keys(password)
		wd.find_element(By.CSS_SELECTOR, "button[name='newPasswordChangeBtn']").click()
		time.sleep(2)
		wd.find_element(By.XPATH, "//a[text()='Login']").click()
		time.sleep(2)

	def login(self, login, password):
		wd = self.app.wd
		time.sleep(2)
		login_input = WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='login']")))
		login_input.send_keys(Keys.CONTROL + "a")
		login_input.send_keys(Keys.BACK_SPACE)
		login_input.send_keys(login)

		password_input = wd.find_element(By.CSS_SELECTOR, "input[name='password']")
		password_input.send_keys(Keys.CONTROL + "a")
		password_input.send_keys(Keys.BACK_SPACE)
		password_input.send_keys(password)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "button[name='registrationSignInBtn']"))).send_keys(Keys.RETURN)