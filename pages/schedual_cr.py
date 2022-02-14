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
		ActionChains(wd).move_to_element(
			wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-21, 0).release().perform()
		ActionChains(wd).move_to_element(
			wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_tuesday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn1")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper1']").is_displayed()
		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl1")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-21, 0).release().perform()
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
		).click_and_hold().move_by_offset(-21, 0).release().perform()
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
		).click_and_hold().move_by_offset(-21, 0).release().perform()
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
		).click_and_hold().move_by_offset(-21, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_saturday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn5")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper5']").is_displayed()

		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl5")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-21, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def change_time_sunday(self):
		wd = self.app.wd

		element = wd.find_element(By.NAME, "editTimeBtn6")
		#slider = WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper0']"))).is_displayed()
		slider = wd.find_element(By.CSS_SELECTOR, "div[data-name='editTimeSliderWrapper6']").is_displayed()

		self.check_day(slider,element)
		wrapper_slider = wd.find_element(By.CSS_SELECTOR, ".ant-slider.editTimeSliderCl6")
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-1")
		).click_and_hold().move_by_offset(-21, 0).release().perform()
		ActionChains(wd).move_to_element(wrapper_slider.find_element(By.CSS_SELECTOR, ".ant-slider-handle.ant-slider-handle-2")
		).click_and_hold().move_by_offset(10, 0).release().perform()

	def save_schedual(self):
		wd = self.app.wd
		wd.find_element(By.NAME, "editTimeSaveBtn").click()