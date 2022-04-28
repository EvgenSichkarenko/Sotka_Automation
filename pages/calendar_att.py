from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CalendarAtt:

	def __init__(self, app):
		self.app = app

	def saturday(self):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='26']"))).click()

	def text_no_deposition(self):
		wd = self.app.wd
		no_meeting = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
		return WebDriverWait(no_meeting, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='There are no meetings today']"))).get_attribute("textContent")

	def calendar_day(self):
		wd = self.app.wd
		today = datetime.now()
		day = today.day
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyHomePageCalendar']")
		calendar.find_element(By.XPATH, f"//button[text()='{day}']").send_keys(Keys.RETURN)

	def show_all_btn(self):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='calendarShowAllBtn']"))).click()


	def count(self):
		wd = self.app.wd
		time.sleep(2)
		return len(wd.find_elements(By.CSS_SELECTOR, "main[data-name='statusProcessMain'] > div > div"))