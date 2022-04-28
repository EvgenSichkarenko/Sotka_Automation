from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FindAtt:
	def __init__(self, app):
		self.app = app

	def input(self, name):
		wd = self.app.wd
		input = wd.find_element(By.CSS_SELECTOR, "div[data-name='companyAttorneySearchWrapper'] input")
		input.send_keys(name)

	def result(self):
		wd = self.app.wd
		return WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div [data-name='itemAttorneyName2']")
		)).get_attribute("textContent")

	def count(self):
		wd = self.app.wd
		return len(wd.find_elements(By.CSS_SELECTOR, "div [data-name='companyAttorneysBlock'] > div"))