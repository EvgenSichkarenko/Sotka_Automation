import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Creditcard:
	def __init__(self, app):
		self.app = app


	def credit_card(self, card_number, expiry_date, cvv):
		wd = self.app.wd
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
		"div[data-name='headerCardIconDiv']"))).click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME,
		"companyPaymentAddNewCardBtn"))).click()
		title = WebDriverWait(wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-name='ModalPaymentTitle']"))).text
		if title == 'Modal Payment':
			wd.find_element(By.NAME, "modalPaymentCardNumber").click()
			wd.find_element(By.NAME, "modalPaymentCardNumber").send_keys(card_number)
			wd.find_element(By.NAME, "modalPaymentExpDate").click()
			wd.find_element(By.NAME, "modalPaymentExpDate").send_keys(expiry_date)
			wd.find_element(By.NAME, "modalPaymentCvv").click()
			wd.find_element(By.NAME, "modalPaymentCvv").send_keys(cvv)
			wd.find_element(By.NAME, "modalPaymentSaveCardBtn").click()
		WebDriverWait(wd, 5).until(EC.element_to_be_clickable((By.NAME, "cardDeleteCardBtn"))).click()
