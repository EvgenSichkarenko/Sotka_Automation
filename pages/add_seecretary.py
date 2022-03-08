from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Secretary:
	def __init__(self, app):
		self.app = app

		'''-----PROD----'''
	# def contact_person(self, secr_email, secr_password):
	# 	wd = self.app.wd
	# 	wd.find_element(By.CSS_SELECTOR, ".sc-BXqHe.bwSTre > svg").click()
	# 	wd.find_element(By.CSS_SELECTOR, ".sc-kstrdz.sc-fodVxV.jlyKYH.cetTfq").click()
	# 	wd.find_element(By.CSS_SELECTOR, "input[name='full_name']").clear()
	# 	wd.find_element(By.CSS_SELECTOR, "input[name='full_name']").send_keys(secr_email)
	# 	wd.find_element(By.CSS_SELECTOR, "input[name='email']").clear()
	# 	wd.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(secr_password)
	# 	wd.find_element(By.XPATH, "//button[text()='Invite']").click()

		'''-----DEV-----'''


	def contact_person(self, secr_new_email, secr_old_email,  secr_fullname, secr_current_email):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='homeAddNewAttorneyIcon']"))).click()
		wd.find_element(By.NAME, "addNewCPBtnModal").click()
		wd.find_element(By.CSS_SELECTOR, "input[name='full_name']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='full_name']").send_keys(secr_fullname)
		self.add_input_data(secr_old_email)
		time.sleep(1)
		#check validation secretary with this email is registered
		validation_exist = wd.find_element(By.XPATH, f"//span[text()='User with email: {secr_old_email} is exists']")\
			.get_attribute("textContent")
		if validation_exist:
			self.add_input_data(secr_current_email)
			time.sleep(1)
			#check validation secretary was send email with letter
			validation_sendbox = wd.find_element(By.XPATH,
				f"//span[text()='Invite for email: {secr_current_email} is exists, please check your mail box']").get_attribute("textContent")
			if validation_sendbox:
				self.add_input_data(secr_new_email)



	def add_input_data(self, text):
		wd = self.app.wd
		wd.find_element(By.CSS_SELECTOR, "input[name='email']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(text)
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "addNewCpInviteBtn"))).click()