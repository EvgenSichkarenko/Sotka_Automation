from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time
import os


class DepositionCase:
	def __init__(self, app):
		self.app = app


	def name_deposition(self, name):
		wd = self.app.wd
		WebDriverWait(wd,  10).until(EC.element_to_be_clickable((By.NAME, "attorneyHomeNewDepBtn"))).click()
		input = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='caseNameSearchInputWrapper'] input")))
		input.send_keys(name)
		input.send_keys(Keys.ENTER)


	def deponent_deposition(self, deponent):
		wd = self.app.wd
		input = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div [data-name='caseDeponentInput'] input")))
		input.send_keys(deponent)
		input.send_keys(Keys.RETURN)


	def location_deposition(self, address):
		wd = self.app.wd
		case_location = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='caseLocationTitle']"))).text
		assert case_location == 'Select location', "Select location tab isn't working"
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationCompanyDifLocationBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationByZoomBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationContinueBtn"))).click()

	def attorneys(self,op_sbn):
		wd = self.app.wd
		#check data attorney
		#add opposing counsel
		input_sbn_op = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='searchAutocomplete'] input")))
		input_sbn_op.click()
		input_sbn_op.send_keys(op_sbn)
		op = wd.find_element(By.XPATH, "//span[text()='Gregg Michael Missbach']")
		op.click()

		add_op = len(wd.find_elements(By.CSS_SELECTOR, "div[data-name='rightBlockExistedOC'] > div"))

		if add_op > 0:
			wd.find_element(By.NAME, "caseLocationContinueBtn").click()

	def set_time_manually(self):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Set up time manually']"))).click()
		#wd.execute_script("document.body.style.zoom='70%'")
		wd.find_element(By.XPATH, "//div[text()='Confirm']").click()

	def upload_doc(self):
		wd = self.app.wd
		file = os.path.abspath("C:\Python\Sotka_auto\data\doc\DEPO.pdf")
		image_path = "C:\Python\Sotka_auto\data\doc\DEPO.pdf"
		#WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "depoUploadBtn"))).click()
		wd.find_element(By.XPATH, "//input[@name='inputFileHidden']").send_keys(image_path)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "depoContinueBtn"))).click()

	def delivery(self, name_cr):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='deliverySearchInput'] input"))).send_keys(f"{name_cr}")
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{name_cr}']"))).click()
		time.sleep(1)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='deliveryContinueBtn']"))).click()

	def finish_depo_attorney(self, name):
		wd = self.app.wd
		time.sleep(1)
		name_depo = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{name}']"))).text
		assert name_depo == name
		#Attorney info
		name_attorney =  WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[text()='Nancy Ellen Miller']"))).text
		email_finish = wd.find_element(By.XPATH, "//span[text()='test111111@getnada.com']").text
		phone_finish = wd.find_element(By.XPATH, "//span[text()='+38984521236']").text

		assert name_attorney == "Nancy Ellen Miller"
		assert email_finish == "test111111@getnada.com"
		assert phone_finish == "+38984521236"

		#Op info
		name_attorney =  WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[text()='Gregg Michael Missbach']"))).text
		email_finish = wd.find_element(By.XPATH, "//span[text()='testop@getnada.com']").text
		phone_finish = wd.find_element(By.XPATH, "//span[text()='+38984521236']").text

		assert name_attorney == "Gregg Michael Missbach"
		assert email_finish == "testop@getnada.com"
		assert phone_finish == "+38984521236"

		#Cr info
		name_attorney =  WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[text()='CR Test']"))).text
		email_finish = wd.find_element(By.XPATH, "//span[text()='testcr16@getnada.com']").text
		phone_finish = wd.find_element(By.XPATH, "//span[text()='+380964512360']").text

		assert name_attorney == "CR Test"
		assert email_finish == "testcr16@getnada.com"
		assert phone_finish == "+380964512360"

	def depo_dashboard(self,name):
		wd = self.app.wd

		block = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
		block_depo_cases = WebDriverWait(block, 10).until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{name}']")))
		block_depo_cases.click()

	def confirm(self):
		wd = self.app.wd

		wd.find_element(By.NAME, "finishConfirmBtn").click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "finishDepositionBtn"))).click()




	def date_and_time_voting(self):
		wd = self.app.wd

		two_hour = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='TWO_HOURSdurationBtn']")))
		two_hour.send_keys(Keys.RETURN)

		btn = False

		while btn == True:
			date_number = datetime.now().strftime("%d")  # 21
			#datetime.date.today() + datetime.timedelta(days=1)
			day = datetime.now().strftime("%A")  # Monday
			selector_morning = f"{day}_{date_number}morning"  # Monday_21morning
			selector_evening = f"{day}_{date_number}evening"  # Monday_21evening



			morning = wd.find_element(By.CSS_SELECTOR, f"div [data-name='{selector_morning}'] button")
			evening = wd.find_element(By.CSS_SELECTOR, f"div [data-name='{selector_evening}'] button")
			if morning.is_enabled() == True:
				morning.click()
				wd.find_element(By.XPATH, "//div[text()='Confirm']").click()
				if evening.is_enabled() == True:
					evening.click()
					wd.find_element(By.XPATH, "//div[text()='Confirm']").click()
				else:
					pass
			else:
				pass
				#date_number = date_number+datetime.timedelta(1)


			btn = wd.find_element(By.CSS_SELECTOR, "button[name='calendarVotingBtn']").is_enabled()