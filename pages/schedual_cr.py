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
		WebDriverWait(wd, 5).until(
			EC.element_to_be_clickable((By.XPATH, "//div[text()='Schedule']"))).click()

	def check_day(self,slider, element):
		if slider == False:
			element.click()

	def change_time_monday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn0")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']").is_displayed()

		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl0")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_tuesday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn1")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper1']").is_displayed()
		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl1")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_wednesday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn2")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper2']").is_displayed()

		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl2")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_thursday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn3")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper3']").is_displayed()

		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl3")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_friday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn4")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper4']").is_displayed()

		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl4")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_saturday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn5")
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper5']").is_displayed()

		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl5")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_sunday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn6")
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper6']").is_displayed()

		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl6")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
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
			assert monday == "Monday9:00 AM - 5:00 PM"
			assert tuesday == "Tuesday9:00 AM - 5:00 PM"
			assert wednesday == "Wednesday9:00 AM - 5:00 PM"
			assert thursday == "Thursday9:00 AM - 5:00 PM"
			assert friday == "Friday9:00 AM - 5:00 PM"
			assert saturday == "Saturday9:00 AM - 5:00 PM"
			assert sunday == "Sunday9:00 AM - 5:00 PM"
			return True

	def return_data(self):
		wd = self.app.wd
		#Monday
		wrapper_slider1 = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl0")
		ActionChains(wd).move_to_element(wrapper_slider1.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider1.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Tuesday
		wrapper_slider2 = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl1")
		ActionChains(wd).move_to_element(wrapper_slider2.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider2.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Wednesday
		wrapper_slider3 = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl2")
		ActionChains(wd).move_to_element(wrapper_slider3.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider3.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Thursday
		wrapper_slider4 = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl3")
		ActionChains(wd).move_to_element(wrapper_slider4.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider4.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Friday
		wrapper_slider5 = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl4")
		ActionChains(wd).move_to_element(wrapper_slider5.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider5.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		#Saturday
		wrapper_slider6 = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl5")
		ActionChains(wd).move_to_element(wrapper_slider6.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider6.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		wd.find_element(By.NAME, "editTimeBtn5").click()
		#Sunday
		wrapper_slider7 = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl6")
		ActionChains(wd).move_to_element(wrapper_slider7.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(10, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider7.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(-10, 0).release().perform()
		wd.find_element(By.NAME, "editTimeBtn6").click()