from selenium.webdriver.common.by import By


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
	def contact_person(self, secr_email, secr_fullname):
		wd = self.app.wd
		wd.find_element(By.CSS_SELECTOR, ".sc-fTNIDv.ieXpgb > svg").click()
		wd.find_element(By.CSS_SELECTOR, ".sc-kstrdz.sc-fodVxV.jlyKYH.cetTfq").click()
		wd.find_element(By.CSS_SELECTOR, "input[name='full_name']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='full_name']").send_keys(secr_fullname)
		wd.find_element(By.CSS_SELECTOR, "input[name='email']").clear()
		wd.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(secr_email)
		wd.find_element(By.XPATH, "//button[text()='Invite']").click()