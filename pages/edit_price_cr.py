from selenium.webdriver.common.by import By
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

		wd.find_element(By.NAME, "appearanceFee").clear()
		wd.find_element(By.NAME, "appearanceFee").send_keys(appearance_fee)
		wd.find_element(By.NAME, "pageCost").clear()
		WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "pageCost"))).send_keys(page_cost)
		wd.find_element(By.NAME, "expertPageCost").clear()
		wd.find_element(By.NAME, "expertPageCost").send_keys(expert_page_cost)
		wd.find_element(By.NAME, "travel").clear()
		wd.find_element(By.NAME, "travel").send_keys(travel)
		wd.find_element(By.NAME, "estimated").clear()
		WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "estimated"))).send_keys(estimated)
		wd.find_element(By.NAME, "turnAroundTime").clear()
		WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "turnAroundTime"))).send_keys(turn_around_page)
		wd.find_element(By.NAME, "copy").clear()
		WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "copy"))).send_keys(copy_of_origin_transcript)
		wd.find_element(By.NAME, "cancellation").clear()
		WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.NAME, "cancellation"))).send_keys(cancellation_fee)

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