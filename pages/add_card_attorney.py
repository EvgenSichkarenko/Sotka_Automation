import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Creditcard:
	def __init__(self, app):
		self.app = app


	def credit_card(self, card_number, expiry_date, cvv):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.ID,"basic-button"))).click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.XPATH,
		"//ul/li//div[text()='Add new credit card']"))).click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME,"companyPaymentAddNewCardBtn"))).click()
		title = WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.XPATH, "//h1 [text()='Add your credit card']"))).text
		if title == 'Add your credit card':
			wd.find_element(By.NAME, "modalPaymentCardNumber").click()
			wd.find_element(By.NAME, "modalPaymentCardNumber").send_keys(card_number)
			wd.find_element(By.NAME, "modalPaymentExpDate").click()
			wd.find_element(By.NAME, "modalPaymentExpDate").send_keys(expiry_date)
			wd.find_element(By.NAME, "modalPaymentCvv").click()
			wd.find_element(By.NAME, "modalPaymentCvv").send_keys(cvv)
			wd.find_element(By.NAME, "modalPaymentSaveCardBtn").click()

		successfully_add_card = WebDriverWait(wd, 5).until(EC.presence_of_element_located((
			By.XPATH, "//div [text()='Card has been successfully added']"))).text
		assert successfully_add_card == 'Card has been successfully added'

		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "cardDeleteCardBtn"))).click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "companyPaymentCloseBtn"))).click()

