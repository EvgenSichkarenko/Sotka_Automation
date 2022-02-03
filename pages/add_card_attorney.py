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
		".MuiButtonBase-root.MuiIconButton-root.sc-GqfZa.emfPRz.MuiIconButton-colorPrimary"))).click()
		if len(wd.find_element(By.CSS_SELECTOR, ".sc-jQbIHB.gTZZqe")) > 0 :
			wd.find_element(By.CSS_SELECTOR, ".MuiButton-startIcon.MuiButton-iconSizeMedium").click()
			wd.find_element(By.XPATH, "//span[text()='Card number']").send_keys(card_number)
			wd.find_element(By.XPATH, "//span[text()='Expiry date']").send_keys(expiry_date)
			wd.find_element(By.XPATH, "//span[text()='Card number']").send_keys(cvv)
			wd.find_element(By.XPATH, "//span[text()='save card']").click()
		else:
			print("Modal card isn't opened")
