from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime

class Schedual:
	def __init__(self, app):
		self.app = app

	def open(self):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.XPATH, "//div[text()='Schedule']"))).click()
		time.sleep(1)

	def check_day(self,slider, element):
		if slider == False:
			element.click()
			time.sleep(1)

	def change_time_monday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "MONDAYenabled")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']").is_displayed()
		self.check_day(slider,element)
		wd.implicitly_wait(10)
		#slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']")
		slider1 = WebDriverWait(wd, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']")))
		time.sleep(2)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_tuesday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "TUESDAYenabled")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper1']").is_displayed()
		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper1']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_wednesday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "WEDNESDAYenabled")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper2']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper2']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_thursday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "THURSDAYenabled")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper3']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper3']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_friday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "FRIDAYenabled")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper4']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper4']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_saturday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "SATURDAYenabled")
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper5']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper5']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_sunday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "SUNDAYenabled")
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper6']").is_displayed()

		self.check_day(slider,element)
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper6']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		time.sleep(1)
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def save_schedual(self):
		wd = self.app.wd
		wd.find_element(By.NAME, "editTimeSaveBtn").click()
		time.sleep(1)

	def check_data(self):
		wd = self.app.wd
		monday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='editTimeBtnBlock0']"))).get_attribute(
			"textContent")
		tuesday =  WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='editTimeBtnBlock1']"))).get_attribute(
			"textContent")
		wednesday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='editTimeBtnBlock2']"))).get_attribute(
			"textContent")
		thursday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='editTimeBtnBlock3']"))).get_attribute(
			"textContent")
		friday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='editTimeBtnBlock4']"))).get_attribute(
			"textContent")
		saturday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='editTimeBtnBlock5']"))).get_attribute(
			"textContent")
		sunday = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='editTimeBtnBlock6']"))).get_attribute(
			"textContent")
		if True:
			assert monday == "Monday7:30 AM - 7:00 PM"
			assert tuesday == "Tuesday7:30 AM - 7:00 PM"
			assert wednesday == "Wednesday7:30 AM - 7:00 PM"
			assert thursday == "Thursday7:30 AM - 7:00 PM"
			assert friday == "Friday7:30 AM - 7:00 PM"
			# assert saturday == "Saturday7:30 AM - 7:00 PM"
			# assert sunday == "Sunday7:30 AM - 7:00 PM"
			return True

	def return_data(self):
		wd = self.app.wd
		#Monday
		slider1 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']")
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(slider1.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Tuesday
		slider2 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper1']")
		ActionChains(wd).move_to_element(slider2.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(slider2.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Wednesday
		slider3 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper2']")
		ActionChains(wd).move_to_element(slider3.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(slider3.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Thursday
		slider4 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper3']")
		ActionChains(wd).move_to_element(slider4.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(slider4.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Friday
		slider5 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper4']")
		ActionChains(wd).move_to_element(slider5.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(slider5.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Saturday
		# slider6 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper5']")
		# ActionChains(wd).move_to_element(slider6.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		# ).click_and_hold().move_by_offset(-10, 0).release().perform()
		# ActionChains(wd).move_to_element(slider6.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		# ).click_and_hold().move_by_offset(-10, 0).release().perform()
		# wd.find_element(By.NAME, "SATURDAYenabled").click()
		# #Sunday
		# slider7 = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper6']")
		# ActionChains(wd).move_to_element(slider7.find_element(By.CSS_SELECTOR, "span[data-index='0']")
		# ).click_and_hold().move_by_offset(-10, 0).release().perform()
		# ActionChains(wd).move_to_element(slider7.find_element(By.CSS_SELECTOR, "span[data-index='1']")
		# ).click_and_hold().move_by_offset(-10, 0).release().perform()
		# wd.find_element(By.NAME, "SUNDAYenabled").click()

	def disable_day(self):
		wd = self.app.wd
		time.sleep(1)
		self.open() #open schedule
		today = datetime.today().strftime("%A")
		time.sleep(2)
		attributes = {
			"Monday":"editTimeBtnWrapper0",
			"Tuesday":"editTimeBtnWrapper1",
			"Wednesday":"editTimeBtnWrapper2",
			"Thursday": "editTimeBtnWrapper3",
			"Friday":"editTimeBtnWrapper4",
			"Saturday": "editTimeBtnWrapper5",
			"Sunday": "editTimeBtnWrapper6"
		}
		self.data_name = attributes[f"{today}"]
		count_span = len(wd.find_elements(By.CSS_SELECTOR, f"div[data-name='{self.data_name}'] span"))
		time.sleep(2)
		if count_span != 0:
			wd.find_element(By.CSS_SELECTOR, f"div[data-name='{self.data_name}'] div ").click()
			time.sleep(2)
			self.save_schedual()
		else:
			time.sleep(2)
			self.save_schedual()

	def enable_day(self):
		wd = self.app.wd
		time.sleep(1)
		today = datetime.today().strftime("%A")
		self.open() #open schedule
		wd.find_element(By.CSS_SELECTOR, f"div[data-name='{self.data_name}'] div ").click()
		time.sleep(2)
		self.save_schedual()

	def delivery_check_cr(self, name_cr):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='deliverySearchInput'] input"))).send_keys(f"{name_cr}")
		try:
			time.sleep(2)
			wd.find_element(By.XPATH, f"//span[text()='{name_cr}']")
			return True
		except NoSuchElementException:
			return False