from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Photo:
	def __init__(self, app):
		self.app = app

	def add_photo(self):
		wd = self.app.wd
		image = os.path.abspath("C:\Python_project\Sotka_auto\data\images\logo.jpg")

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.ID, "basic-button"))).click()
		wd.find_element(By.XPATH, "//div[text()=' Change photo']").click()

		title = wd.find_element(By.XPATH, "//h1[text()='Your photo account']").text

		if title == "Your photo account":
			wd.find_element(By.NAME, "uploadPhotoRef").send_keys(image)
			wd.find_element(By.NAME, "uploadPhotoSaveBtn").click()
			return True
		else:
			return False