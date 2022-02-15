from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class DepoDownloadAtt:
	def __init__(self, app):
		self.app = app

	def text_name_attroney(self):
		wd = self.app.wd
		return WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH,
		"//div[text()='Mark John Decastro']"))).get_attribute("textContent")


	def search_deposition(self, name):
		wd = self.app.wd
		WebDriverWait(wd, 5).until((EC.element_to_be_clickable((By.NAME, "attorneyHomePastDepBtn")))).click()
		#search input
		wd.find_element(By.NAME, "searchInput").send_keys(name)

		if len(wd.find_elements(By.CSS_SELECTOR, "div[data-name='pdBlockList']")) > 0:
			pass
		else:
			print("Search by name is not work")

	def check_info_deposition(self, name, deponent, date):
		wd = self.app.wd
		name_attorney = self.text_name_attroney()
		#name of deposition case
		time.sleep(1)
		name_dep = wd.find_element(By.CSS_SELECTOR, "h3[data-name='pastDepositionTitle2']").get_attribute("textContent")
		#data
		data_dep = wd.find_element(By.CSS_SELECTOR, "h3[data-name='pastDepositionDate2']").get_attribute("textContent")
		#name creator
		name_cr = wd.find_element(By.CSS_SELECTOR, "h3[data-name='pastDepositionCreatedBy2']").get_attribute("textContent")
		#name deponent
		name_deponent = wd.find_element(By.CSS_SELECTOR, "h3[data-name='pastDepositionPrice2']").get_attribute("textContent")
		#print(name_dep, name, data_dep, date,name_cr, name_attorney,  name_deponent, deponent)
		time.sleep(1)
		if (name_dep == name and data_dep == date):
			time.sleep(1)
			if (name_cr == name_attorney and name_deponent == deponent):
				WebDriverWait(wd, 5).until(EC.element_to_be_clickable(((By.NAME, "pastDepositionBtnDownload2")))).click()
				self.download()
		else:
			print("Deposition info isn't same ")

		time.sleep(1)

	#download transcript through details
	def download(self):
		wd = self.app.wd
		title_documents = wd.find_element(By.CSS_SELECTOR, "div[data-name='downloadsTitle']").text
		time.sleep(1)
		if title_documents == 'Documents':
			time.sleep(1)
			wd.find_element(By.CSS_SELECTOR, "div[data-name='fileTitle']").click()
			ActionChains(wd).move_to_element(
				wd.find_element(By.CSS_SELECTOR, "div[data-name='fileTitle']")
			).move_by_offset(-100, 0).click().release().perform()
		time.sleep(1)