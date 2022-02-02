from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Session:
	def __init__(self, app):
		self.app = app

	def login(self, login, password):
		wd = self.app.wd
		self.app.open_login(wd)
		wd.find_element(By.NAME, "login").clear()
		wd.find_element(By.NAME, "login").send_keys(login)
		wd.find_element(By.NAME, "password").clear()
		wd.find_element(By.NAME, "password").send_keys(password)
		wd.find_element(By.CSS_SELECTOR, "button.sc-kstrdz.sc-hBEYos.jlyKYH.ghVIMM").click()

	def logout(self):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
		".MuiButtonBase-root.MuiIconButton-root.sc-fbkhIv.jsBTxA.MuiIconButton-colorPrimary"))).click()


	def text_name_attribute_attroney(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.sc-lcujXC.bnKPcn"))).get_attribute("textContent")


	def text_name_attribute_cr(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.presence_of_element_located(
			(By.CSS_SELECTOR, "div.sc-lcujXC.bnKPcn"))).get_attribute("textContent")

''' ----DEV----
	def text_name_attribute_cr(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.presence_of_element_located(
			(By.CSS_SELECTOR, "div.sc-gGmIRh.dfsDm"))).get_attribute("textContent")
'''

