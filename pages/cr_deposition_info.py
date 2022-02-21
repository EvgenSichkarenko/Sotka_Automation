from selenium.webdriver.common.by import By


class CrDepoInfo:
	def __init__(self, app):
		self.app = app

	def deposition_info(self, attorney, address):
		wd = self.app.wd
		name_sbn = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorAttorneyText1']").get_attribute("textContent")
		#Date:Apr 13, 2022
		#date_dep = wd.find_element(By.CSS_SELECTOR, "div[data-name='finishBlockNameValue']").get_attribute("textContent")
		#location
		location_depo = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorLocationText']").get_attribute("textContent")

		if (name_sbn == attorney) and (location_depo == address):
			return True
		else:
			return False


	def op_info(self, name, email, phone):
		wd = self.app.wd
		name_op = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorOpposingName']").get_attribute(
			"textContent")
		email_op = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorOpposingEmailValue']").get_attribute(
			"textContent")
		phone_op = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorOpposingPhoneValue']").get_attribute(
			"textContent")
		if (name_op == name) and (email_op == email) and (phone_op == phone):
			return True
		else:
			return False


	def att_info(self, name, email, phone):
		wd = self.app.wd
		name_att = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorCreatedByValue']").get_attribute(
			"textContent")
		email_att = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorEmailValue']").get_attribute(
			"textContent")
		phone_att = wd.find_element(By.XPATH, "//div[text()='+380982542177']").get_attribute(
			"textContent")

		if (name_att == name) and (email_att == email) and (phone_att == phone):
			return True
		else:
			return False

	def price_info(self, ):
		wd = self.app.wd
		appearance_price = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorPriceAppearanceFeeValue']").get_attribute(
			"textContent")
		page_cost_price = wd.find_element(By.CSS_SELECTOR,
			"div[data-name='forExecutorPricePageCostValue']").get_attribute(
			"textContent")
		travel_price = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorPriceTravelValue']").get_attribute(
			"textContent")
		expert_page_price = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorPriceExpertPageCostValue']").get_attribute(
			"textContent")
		estimate_total_price = wd.find_element(By.CSS_SELECTOR, "div[data-name='forExecutorPriceEstimatedTotalValue']").get_attribute(
			"textContent")
