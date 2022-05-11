from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class FindAtt:
	def __init__(self, app):
		self.app = app

	def input(self, name):
		wd = self.app.wd
		input_fields = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='companyAttorneySearchWrapper'] input")))
		input_fields.send_keys(Keys.CONTROL + "a")
		input_fields.send_keys(Keys.BACK_SPACE)
		input_fields.send_keys(name)

	def check_name(self, name_att):
		wd = self.app.wd
		block_name = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div [data-name='companyAttorneysBlock']")))
		return block_name.find_element(By.XPATH, f"//div[text()='{name_att}']").text

	def count(self):
		wd = self.app.wd
		time.sleep(2)
		return len(wd.find_elements(By.CSS_SELECTOR, "div [data-name='companyAttorneysBlock'] > div"))