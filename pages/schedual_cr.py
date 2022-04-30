from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class Schedual:
	def __init__(self, app):
		self.app = app

	def open(self):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.XPATH, "//div[text()='Schedule']"))).click()

	def check_day(self,slider, element):
		if slider == False:
			element.click()
			time.sleep(1)

	def change_time_monday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn0")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']").is_displayed()
		self.check_day(slider,element)
		time.sleep(1)
		#slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']")
		slider1 = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']")))
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0'] > input")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1'] > input")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_tuesday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn1")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper1']").is_displayed()
		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper1']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_wednesday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn2")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper2']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper2']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_thursday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn3")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper3']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper3']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_friday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn4")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper4']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper4']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_saturday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn5")
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper5']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper5']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_sunday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn6")
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper6']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper6']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def save_schedual(self):
		wd = self.app.wd
		wd.find_element(By.NAME, "editTimeSaveBtn").click()

	def check_data(self):
		wd = self.app.wd
		monday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "editTimeBtn0"))).get_attribute(
			"textContent")
		tuesday =  WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "editTimeBtn1"))).get_attribute(
			"textContent")
		wednesday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "editTimeBtn2"))).get_attribute(
			"textContent")
		thursday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "editTimeBtn3"))).get_attribute(
			"textContent")
		friday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "editTimeBtn4"))).get_attribute(
			"textContent")
		saturday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "editTimeBtn5"))).get_attribute(
			"textContent")
		sunday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "editTimeBtn6"))).get_attribute(
			"textContent")

		if True:
			assert monday == "Monday8:30 AM - 5:00 PM"
			assert tuesday == "Tuesday8:30 AM - 5:00 PM"
			assert wednesday == "Wednesday8:30 AM - 5:00 PM"
			assert thursday == "Thursday8:30 AM - 5:00 PM"
			assert friday == "Friday8:30 AM - 5:00 PM"
			assert saturday == "Saturday8:30 AM - 5:00 PM"
			assert sunday == "Sunday8:30 AM - 5:00 PM"
			return True

	def return_data(self):
		wd = self.app.wd
		#Monday
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Tuesday
		slider2 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper1']")
		ActionChains(wd).move_to_element(slider2.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(slider2.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Wednesday
		slider3 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper2']")
		ActionChains(wd).move_to_element(slider3.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(slider3.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Thursday
		slider4 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper3']")
		ActionChains(wd).move_to_element(slider4.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(slider4.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Friday
		slider5 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper4']")
		ActionChains(wd).move_to_element(slider5.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(slider5.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Saturday
		slider6 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper5']")
		ActionChains(wd).move_to_element(slider6.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(slider6.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		wd.find_element(By.NAME, "editTimeBtn5").click()
		#Sunday
		slider7 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper6']")
		ActionChains(wd).move_to_element(slider7.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(slider7.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		wd.find_element(By.NAME, "editTimeBtn6").click()