from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class DepoDownloadCR:
	def __init__(self, app):
		self.app = app

	def search_deposition_cr(self, name):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((
			By.XPATH, "/html/body/div/section/div[1]/div[1]/button[2]"))).click()
		#search input
		wd.find_element(By.NAME, "searchInput").send_keys(name)
		if len(wd.find_elements(By.CSS_SELECTOR, "div[data-name='pdBlockList']")) == 1:
			pass


	def check_info_deposition_cr(self, name, deponent, date):
		wd = self.app.wd
		name_attorney = "Mark John Decastro"
		#name of deposition case
		time.sleep(1)
		name_dep = wd.find_element(By.CSS_SELECTOR, "h3[data-name='pastDepositionTitle2']").get_attribute("textContent")
		#data
		data_dep = wd.find_element(By.CSS_SELECTOR, "h3[data-name='pastDepositionDate2']").get_attribute("textContent")
		#name creator
		name_att = wd.find_element(By.CSS_SELECTOR, "h3[data-name='pastDepositionCreatedBy2']").get_attribute("textContent")
		#name deponent
		name_deponent = wd.find_element(By.CSS_SELECTOR, "h3[data-name='pastDepositionPrice2']").get_attribute("textContent")
		#print(name_dep, name, data_dep, date,name_cr, name_attorney,  name_deponent, deponent)
		time.sleep(1)
		if (name_dep == name and data_dep == date):
			time.sleep(1)
			if (name_att == name_attorney and name_deponent == deponent):
				WebDriverWait(wd, 5).until(EC.element_to_be_clickable(((By.NAME, "pastDepositionBtnDownload2")))).click()
				WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='fileTitle']"))).click()
		time.sleep(1)

