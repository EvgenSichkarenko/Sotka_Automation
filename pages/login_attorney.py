from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginAttroney:
	def __init__(self, driver):
		self.driver = driver

	def open(self):
		return self.driver.get("https://sotka.io/login")

	def login_attorney(self, login, password):
		self.driver.find_element(By.NAME, "login").clear()
		self.driver.find_element(By.NAME, "login").send_keys(login)
		self.driver.find_element(By.NAME, "password").clear()
		self.driver.find_element(By.NAME, "password").send_keys(password)

	def submit_buttom_click(self):
		self.driver.find_element(By.CSS_SELECTOR, "button.sc-kstrdz.sc-hBEYos.jlyKYH.ghVIMM").click()

	def text_name_attribute(self):
		return self.driver.find_element(By.CSS_SELECTOR, "div.sc-gGmIRh.dfsDm").get_attribute("textContent")

	def quit(self):
		self.driver.quit()