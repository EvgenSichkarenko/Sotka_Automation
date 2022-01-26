from selenium.webdriver.common.by import By

class Secretary:
	def __init__(self, driver):
		self.driver = driver

	def add_secret_icon_click(self):
		self.driver.find_element(By.CSS_SELECTOR, ".sc-BXqHe.bwSTre > svg").click()

	def contact_person(self, secr_email, secr_password):
		self.driver.find_element(By.CSS_SELECTOR, ".sc-kstrdz.sc-fodVxV.jlyKYH.cetTfq").click()
		self.driver.find_element(By.CSS_SELECTOR, "input[name='full_name']").clear()
		self.driver.find_element(By.CSS_SELECTOR, "input[name='full_name']").send_keys(secr_email)
		self.driver.find_element(By.CSS_SELECTOR, "input[name='full_name']").clear()
		self.driver.find_element(By.CSS_SELECTOR, "input[name='full_name']").send_keys(secr_password)
		self.driver.find_element(By.XPATH, "//button[text()='Invite']").click()