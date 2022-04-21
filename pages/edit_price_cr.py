from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time



class EditPrice:
	def __init__(self, app):
		self.app = app

	def change_price(self, appearance_fee, page_cost,expert_page_cost, travel, estimated ,turn_around_page,
	copy_of_origin_transcript,cancellation_fee):
		wd = self.app.wd

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='priceButtonEdit']"))).click()

		appearanceFee = wd.find_element(By.NAME, "appearanceFee")
		pageCost = wd.find_element(By.NAME, "pageCost")
		expertPageCost = wd.find_element(By.NAME, "expertPageCost")
		travels = wd.find_element(By.NAME, "travel")
		estimate = wd.find_element(By.NAME, "estimated")
		turnAroundTime = wd.find_element(By.NAME, "turnAroundTime")
		copy = wd.find_element(By.NAME, "copy")
		cancellation = wd.find_element(By.NAME, "cancellation")

		self.clear_attribute(appearanceFee,appearance_fee)
		self.clear_attribute(pageCost, page_cost)
		self.clear_attribute(expertPageCost, expert_page_cost)
		self.clear_attribute(travels, travel)
		self.clear_attribute(estimate, estimated)
		self.clear_attribute(turnAroundTime, turn_around_page)
		self.clear_attribute(copy, copy_of_origin_transcript)
		#self.clear_attribute(cancellation, cancellation_fee)


	def clear_attribute(self, element, data):
		wd = self.app.wd
		element.click()
		element.send_keys(Keys.CONTROL + "A")
		element.send_keys(Keys.BACK_SPACE)
		element.send_keys(data)

	def appearance_fee(self):
		wd = self.app.wd
		return wd.find_element(By.CSS_SELECTOR, "span[data-name='priceData0']").text

	def page_cost(self):
		wd = self.app.wd
		return wd.find_element(By.CSS_SELECTOR, "span[data-name='priceData1']").text

	def expert_page_cost(self):
		wd = self.app.wd
		return wd.find_element(By.CSS_SELECTOR, "span[data-name='priceData2']").text

	def travel(self):
		wd = self.app.wd
		return wd.find_element(By.CSS_SELECTOR, "span[data-name='priceData3']").text

	def estimated_hour(self):
		wd = self.app.wd
		return wd.find_element(By.CSS_SELECTOR, "span[data-name='priceData4']").text

	def cancellation_fees(self):
		wd = self.app.wd
		return wd.find_element(By.CSS_SELECTOR, "span[data-name='priceData5']").text

	def turn_around_time(self):
		wd = self.app.wd
		return wd.find_element(By.CSS_SELECTOR, "span[data-name='priceData6']").text

	def cancellation_terms(self):
		wd = self.app.wd
		return wd.find_element(By.CSS_SELECTOR, "span[data-name='priceData7']").text

	def copy(self):
		wd = self.app.wd
		return wd.find_element(By.CSS_SELECTOR, "span[data-name='priceData8']").text

	def save(self):
		wd = self.app.wd
		wd.find_element(By.NAME, "editPriceSave").click()
		time.sleep(2)