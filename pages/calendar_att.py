from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class CalendarAtt:

	def __init__(self, app):
		self.app = app

	def text_no_deposition(self):
		wd = self.app.wd
		no_meeting = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
		return WebDriverWait(no_meeting, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='There are no meetings today']"))).get_attribute("textContent")

	def check_el_present(self,day,locator):
		wd = self.app.wd
		time.sleep(2)
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyHomePageCalendar']")
		child = calendar.find_element(By.XPATH, f"//button[text()='{day}']")
		child.send_keys(Keys.RETURN)
		parent = child.find_element(By.XPATH, "..")
		try:
			parent.find_element(By.CSS_SELECTOR, f"{locator}")
			return True
		except NoSuchElementException:
			return False

	def next_day(self):
		wd = self.app.wd
		time.sleep(1)
		today = datetime.now()
		tomorrow  = today + timedelta(1)
		self.tomorrow = tomorrow.day
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyHomePageCalendar']")
		calendar.find_element(By.XPATH, f"//button[text()='{self.tomorrow}']").send_keys(Keys.RETURN)

	def number_of_element(self):
		wd = self.app.wd
		time.sleep(2)
		assert len(wd.find_elements(By.CSS_SELECTOR, "div[data-name='CircleBlock'] div")) == 1

	def calendar_day(self):
		wd = self.app.wd
		time.sleep(1)
		today = datetime.now()
		self.day = today.day
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyHomePageCalendar']")
		calendar.find_element(By.XPATH, f"//button[text()='{self.day}']").send_keys(Keys.RETURN)

	def show_all_btn(self):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='calendarShowAllBtn']"))).click()

	def count(self):
		wd = self.app.wd
		time.sleep(2)
		return len(wd.find_elements(By.CSS_SELECTOR, "main[data-name='statusProcessMain'] > div > div"))

	def cansel_depo(self):
		wd = self.app.wd
		time.sleep(2)
		wd.find_element(By.CSS_SELECTOR, "button[name='attorneyHomeBtnCancel4']").click()
		time.sleep(1)
