from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Schedual:
	def __init(self, app):
		self.app = app

	def change_time(self):
		wd = self.app.wd
		ActionChains(wd).move_to_element(wd.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(wd.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

