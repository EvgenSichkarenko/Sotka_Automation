from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.keys import Keys

class CalendarCr:

	def __init__(self, app):
		self.app = app


	def day(self):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='26']"))).click()

	def text_no_deposition(self):
		wd = self.app.wd
		no_meeting = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
		return WebDriverWait(no_meeting, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='There are no meetings today']"))).get_attribute("textContent")

	def calendar_day(self):
		wd = self.app.wd
		today = datetime.now()
		day = today.day
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyHomePageCalendar']")
		calendar.find_element(By.XPATH, f"//button[text()='{day}']").send_keys(Keys.RETURN)

	def show_all_btn(self):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='calendarShowAllBtn']"))).click()

	def count(self):
		wd = self.app.wd
		return len(wd.find_elements(By.CSS_SELECTOR, "main[data-name='statusProcessMain'] main"))