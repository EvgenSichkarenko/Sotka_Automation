from selenium.webdriver.common.by import By
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Photo:
	def __init__(self, app):
		self.app = app

	def add_photo(self):
		wd = self.app.wd
		image = os.path.abspath("/var/lib/jenkins/workspace/Test_stoke_sotka/data/images/logo.jpg")
		#image = os.path.abspath("C:\Python_project\Sotka_auto\data\images\logo.jpg")
		basic_btn = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='basic-button']")))
		wd.execute_script("arguments[0].click();", basic_btn)
		wd.find_element(By.XPATH, "//div[text()=' Change photo']").click()

		title = wd.find_element(By.XPATH, "//h1[text()='Your photo account']").get_attribute("textContent")

		if title == "Your photo account":
			time.sleep(1)
			wd.find_element(By.CSS_SELECTOR, "input[name='uploadPhotoRef']").send_keys(image)
			time.sleep(1)
			wd.find_element(By.NAME, "uploadPhotoSaveBtn").click()
			time.sleep(1)
			return True
		else:
			return False