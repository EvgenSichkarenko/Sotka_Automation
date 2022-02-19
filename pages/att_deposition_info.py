from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AttDepoInfo:
	def __init__(self, app):
		self.app = app

	def deposition_info(self, name, address):
		wd = self.app.wd
		#10000000000000000
		name_deposition = wd.find_element(By.CSS_SELECTOR, "div[data-name='finishBlockNameTitle']").get_attribute("textContent")
		#Date:Apr 13, 2022
		date_dep = wd.find_element(By.CSS_SELECTOR, "div[data-name='finishBlockNameValue']").get_attribute("textContent")
		#location
		location_depo = wd.find_element(By.CSS_SELECTOR, "div[data-name='finishBlockMeetLocationValue']").get_attribute("textContent")

		if (name_deposition == name) and (location_depo == address):
			return True
		else:
			return False
		#assert date_dep == date, f"Incorrect {date_dep}"

	def op_info(self, name, email, phone):
		wd = self.app.wd
		name_op = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyCompFullName20']").get_attribute(
			"textContent")
		email_op = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyCompEmail20'] div").get_attribute(
			"textContent")
		phone_op = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyCompPhoneName20'] div").get_attribute(
			"textContent")
		if (name_op == name) and (email_op == email) and (phone_op == phone):
			return True
		else:
			return False


	def att_info(self, name, email, phone):
		wd = self.app.wd
		name_att = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyCompFullName1']").get_attribute(
			"textContent")
		email_att = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyCompEmail1'] div").get_attribute(
			"textContent")
		phone_att = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyCompPhoneName1'] div").get_attribute(
			"textContent")

		if (name_att == name) and (email_att == email) and (phone_att == phone):
			return True
		else:
			return False


	def cr_info(self, name, email, phone, address):
		wd = self.app.wd
		name_cr = wd.find_element(By.CSS_SELECTOR, "div[data-name='executorAttorneyName']").get_attribute(
			"textContent")
		email_cr = wd.find_element(By.CSS_SELECTOR, "p[data-name='executorAttorneyEmail']").get_attribute(
			"textContent")
		phone_cr = wd.find_element(By.CSS_SELECTOR, "div[data-name='executorAssistantPhone'] div").get_attribute(
			"textContent")
		addres_cr = wd.find_element(By.CSS_SELECTOR, "div[data-name='executorAssistantAddress'] div").get_attribute(
			"textContent")

		if (name_cr == name) and (email_cr == email) and (phone_cr == phone) and (addres_cr == address):
			return True
		else:
			return False

	def price_info(self, ):
		wd = self.app.wd
		appearance_price = wd.find_element(By.CSS_SELECTOR, "div[data-name='executorAssistantPriceContainer0'] div").get_attribute(
			"textContent")
		travel_price = wd.find_element(By.CSS_SELECTOR, "div[data-name='executorAssistantTravelValue']").get_attribute(
			"textContent")
		page_price = wd.find_element(By.CSS_SELECTOR, "div[data-name='executorAssistantCostValue']").get_attribute(
			"textContent")
		total_price = wd.find_element(By.CSS_SELECTOR, "div[data-name='executorAssistantTotalValue']").get_attribute(
			"textContent")
