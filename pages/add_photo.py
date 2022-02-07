from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Photo:
	def __init__(self, app):
		self.app = app

	def add_photo(self):
		wd = self.app.wd
		image = os.path.abspath("C:\Python\Sotka_auto\data\images\logo.jpg")

		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-name='headerPhotoIconUpload']"))).click()

		title = wd.find_element(By.CSS_SELECTOR, "div[data-name='uploadPhotoTitle']").text

		if title == "Your photo account":
			wd.find_element(By.NAME, "uploadPhotoRef").send_keys(image)
		else:
			print("Photo account page not open")

		wd.find_element(By.NAME, "uploadPhotoSaveBtn").click()

