from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime, timedelta
import time
import imaplib
import email
import sys
import re
import requests


class DepositionCase:
	def __init__(self, app):
		self.app = app


	#global number_of_deposition
	def login_without_open_link(self, login, password):
		wd = self.app.wd
		time.sleep(1)
		login_input = WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='login']")))
		login_input.send_keys(Keys.CONTROL + "a")
		login_input.send_keys(Keys.BACK_SPACE)
		login_input.send_keys(login)

		password_input = wd.find_element(By.CSS_SELECTOR, "input[name='password']")
		password_input.send_keys(Keys.CONTROL + "a")
		password_input.send_keys(Keys.BACK_SPACE)
		password_input.send_keys(password)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "button[name='registrationSignInBtn']"))).send_keys(Keys.RETURN)

	def name_deposition(self, name):
		wd = self.app.wd
		time.sleep(2)
		WebDriverWait(wd,  15).until(EC.element_to_be_clickable((By.NAME, "attorneyHomeNewDepBtn"))).click()
		input = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='caseNameSearchInputWrapper'] input")))
		time.sleep(2)
		self.number_of_deposition = self.get_id_deposition_case()
		input.send_keys(name)
		input.send_keys(Keys.ENTER)
		time.sleep(1)

	#Change link
	def get_id_deposition_case(self):
		wd = self.app.wd
		url = wd.current_url
		#default = "http://stoke-test.s3-website.us-east-2.amazonaws.com/progressCase/"
		default = "https://demo.trialbase.com/progressCase/"
		id_case = url.replace(default, "")
		number = int(id_case)
		return number

	# Change link
	def add_new_link(self):
		wd = self.app.wd
		time.sleep(2)
		WebDriverWait(wd,  15).until(EC.element_to_be_clickable((By.NAME, "attorneyHomeNewDepBtn"))).click()
		#default = "http://stoke-test.s3-website.us-east-2.amazonaws.com/progressCase/"
		default = "https://demo.trialbase.com/progressCase/"
		time.sleep(3)
		new_link =  default + "570"
		wd.get(f"{new_link}")
		time.sleep(2)

	def check_name(self):
		wd = self.app.wd
		time.sleep(1)
		text = wd.find_element(By.XPATH, "//div[text()='You are not allowed to see this case']").text
		return text

	def change_price(self):
		wd = self.app.wd

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='priceButtonEdit']"))).click()
		price = "1"
		appearanceFee = wd.find_element(By.NAME, "appearanceFee")
		pageCost = wd.find_element(By.NAME, "pageCost")
		expertPageCost = wd.find_element(By.NAME, "expertPageCost")
		travels = wd.find_element(By.NAME, "travel")
		estimate = wd.find_element(By.NAME, "estimated")
		turnAroundTime = wd.find_element(By.NAME, "turnAroundTime")
		copy = wd.find_element(By.NAME, "copy")

		self.clear_attribute(appearanceFee,price)
		self.clear_attribute(pageCost, price)
		self.clear_attribute(expertPageCost, price)
		self.clear_attribute(travels, price)
		self.clear_attribute(turnAroundTime, price)
		self.clear_attribute(copy, price)
		time.sleep(1)
		wd.find_element(By.NAME, "editPriceSave").click()
		time.sleep(1)

	def clear_attribute(self, element, data):
		wd = self.app.wd
		element.click()
		element.send_keys(Keys.CONTROL + "A")
		element.send_keys(Keys.BACK_SPACE)
		element.send_keys(data)

	def deponent_deposition(self, deponent):
		wd = self.app.wd
		input = WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div [data-name='caseDeponentInput'] input")))
		input.send_keys(deponent)
		input.send_keys(Keys.RETURN)

	def location_deposition(self):
		wd = self.app.wd
		case_location = WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='caseLocationTitle']"))).text
		assert case_location == 'Select location', "Select location tab isn't working"
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "caseLocationCompanyDifLocationBtn"))).click()
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "caseLocationByZoomBtn"))).click()
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "caseLocationContinueBtn"))).click()

	def attorneys(self,op_sbn, email_voting):
		wd = self.app.wd
		#check data attorney
		#add opposing counsel
		input_sbn_op = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='searchAutocomplete'] input")))
		input_sbn_op.click()
		input_sbn_op.send_keys(op_sbn)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{email_voting}']"))).click()
		time.sleep(1)
		wd.find_element(By.NAME, "caseLocationContinueBtn").click()

	def set_time_manually(self):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Set up time manually']"))).click()
		row = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyRow']")
		row.find_element(By.CSS_SELECTOR, "button[name='TWO_HOURSdurationBtn']").send_keys(Keys.RETURN)

		#Choose current day in calendar
		today = datetime.now()
		month_in_calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyDateBlock']").text
		month = today.strftime("%B")
		time.sleep(1)
		if month_in_calendar.find(month) == -1:
			calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyCalendar']")
			calendar.find_element(By.CSS_SELECTOR, "svg[data-name='calendarArrowLeft']").click()

		day = today.day
		time.sleep(2)
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyCalendar']")
		time.sleep(2)
		calendar.find_element(By.XPATH, f"//button[text()='{day}']").send_keys(Keys.RETURN)
		time.sleep(1)
		#Enter time manually
		hour = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyTime']")
		hour.find_element(By.NAME, "selectTimeBtn").send_keys(Keys.RETURN)
		hour.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.CONTROL + "a")
		hour.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.BACK_SPACE)
		time.sleep(1)
		hour.find_element(By.CSS_SELECTOR, "input").send_keys("9:00 AM")
		self.time_value = hour.find_element(By.CSS_SELECTOR, "input").get_attribute("value")
		time.sleep(1)
		wd.find_element(By.XPATH, "//div[text()='Confirm']").click()

	def upload_doc(self):
		wd = self.app.wd
		image = "C:\Python_project\Sotka_auto\data\doc\DEPO.pdf"
		#image = os.path.abspath("/var/lib/jenkins/workspace/Sotka_pre_prod/data/doc/DEPO.pdf")
		#WebDriverWait(wd, 10).until(EC.element_to_be_clickable(By.NAME, "depoUploadBtn")).click()
		time.sleep(2)
		#wd.find_element(By.XPATH, "//input[@name='inputFileHidden']").send_keys(image)
		wd.find_element(By.CSS_SELECTOR, "input[name='inputFileHidden']").send_keys(image)
		time.sleep(1)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "depoContinueBtn"))).send_keys(Keys.RETURN)

	def check_exists_el(self,name_cr):
		wd = self.app.wd
		try:
			time.sleep(2)
			wd.find_element(By.XPATH, f"//span[text()='{name_cr}']")
			return True
		except NoSuchElementException:
			return False

	def delivery(self, name_cr):
		wd = self.app.wd
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='deliverySearchInput'] input"))).send_keys(f"{name_cr}")

		time.sleep(2)
		while self.check_exists_el(name_cr) == False:
			time.sleep(2)
			self.change_time_manually(name_cr)

		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{name_cr}']"))).click()
		time.sleep(2)
		WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='deliveryContinueBtn']"))).click()

	# def delivery_for_voting(self):
	# 	wd = self.app.wd
	# 	WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
	# 		By.CSS_SELECTOR, "div[data-name='deliverySearchInput'] input"))).send_keys(f"{name_cr}")
	#
	#
	# 	WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{name_cr}']"))).click()
	# 	WebDriverWait(wd, 10).until(
	# 		EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='deliveryContinueBtn']"))).click()

	def change_time_manually(self, name_cr):
		wd = self.app.wd

		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='deliverySearchInput'] input"))).clear()
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "deliveryBackBtn"))).click()
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "depoBackbtn"))).click()
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "manualPickedChangeBtn"))).click()


		today = datetime.now()
		#Choose month
		month_in_calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyDateBlock']").text
		month = today.strftime("%B")
		time.sleep(1)
		if month_in_calendar.find(month) == -1:
			calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyCalendar']")
			calendar.find_element(By.CSS_SELECTOR, "svg[data-name='calendarArrowLeft']").click()
		# Choose current day in calendar
		day = today.day
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyCalendar']")
		calendar.find_element(By.XPATH, f"//button[text()='{day}']").send_keys(Keys.RETURN)
		time.sleep(1)
		#Choose two hours
		row = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyRow']")
		row.find_element(By.CSS_SELECTOR, "button[name='TWO_HOURSdurationBtn']").send_keys(Keys.RETURN)

		hour = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyTime']")
		time_def = wd.find_element(By.CSS_SELECTOR, "button[name='selectTimeBtn'] > div").text

		hour.find_element(By.NAME, "selectTimeBtn").send_keys(Keys.RETURN)

		#Input for date
		input = hour.find_element(By.CSS_SELECTOR, "input")
		input.send_keys(Keys.CONTROL + "a")
		input.send_keys(Keys.BACK_SPACE)

		date_list = ["7:00 AM","7:30 AM",
			"8:00 AM","8:30 AM","9:00 AM","9:30 AM","10:00 AM","10:30 AM","11:00 AM","11:30 AM",
			"12:00 PM","12:30 PM","1:00 PM","1:30 PM","2:00 PM","2:30 PM","3:00 PM",
			"3:30 PM","4:00 PM","4:30 PM","5:00 PM","5:30 PM","6:00 PM"]

		new_time = None
		for item in range(len(date_list)):
			if date_list[item] == time_def:
				new_time = date_list[item + 1]
		time_def = new_time

		input.send_keys(time_def)
		input.send_keys(Keys.RETURN)
		time.sleep(1)
		wd.find_element(By.NAME, "depositionManualConfirmBtn").send_keys(Keys.RETURN)
		wd.find_element(By.NAME, "depoContinueBtn").send_keys(Keys.RETURN)

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='deliverySearchInput'] input"))).send_keys(f"{name_cr}")

	def finish_depo_attorney(self, depo_name, at_name, at_email,at_phone,op_name, op_email, op_phone,
	cr_name,cr_email,cr_phone):
		wd = self.app.wd
		time.sleep(1)
		#Current time
		# current_zone = datetime.now()
		# three_hours = timedelta(hours=3)
		# min_three = current_zone - three_hours
		# current_date = datetime.today().strftime(f'%a, %d %b %Y {min_three.strftime("%H")}')
		# self.sotka_time = f"{current_date}"

		name_depo = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{depo_name}']"))).text
		assert name_depo == depo_name

		#DAY
		try:
			if wd.find_element(By.CSS_SELECTOR, "div[data-name='caseFinishTab']"):
				block = wd.find_element(By.CSS_SELECTOR, "div[data-name='finishDeponentBlock']")
				self.day_deposition = block.find_element(By.CSS_SELECTOR, "div[data-name='contactPersonItem']").get_attribute("textContent")
		except NoSuchElementException:
			pass

		#Attorney info
		name_attorney = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{at_name}']"))).text
		email_finish = wd.find_element(By.XPATH, f"//span[text()='{at_email}']").text
		phone_finish = wd.find_element(By.XPATH, f"//span[text()='{at_phone}']").text

		assert name_attorney == f"{at_name}"
		assert email_finish == f"{at_email}"
		assert phone_finish == f"{at_phone}"

		#Op info
		#op = wd.find_element(By.CSS_SELECTOR, "div[data-name='finishOpposingCounselBloc']")
		name_op = wd.find_element(By.XPATH, f"//h2[text()='{op_name}']").get_attribute("textContent")
		email_op = wd.find_element(By.XPATH, f"//span[text()='{op_email}']").text
		phone_op = wd.find_element(By.XPATH, f"//span[text()='{op_phone}']").text

		assert name_op == f"{op_name}"
		assert email_op == f"{op_email}"
		assert phone_op == f"{op_phone}"

		#Cr info
		name_cr =  WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{cr_name}']"))).text
		email_cr = wd.find_element(By.XPATH, f"//span[text()='{cr_email}']").text
		phone_cr = wd.find_element(By.XPATH,f"//span[text()='{cr_phone}']").text

		assert name_cr == f"{cr_name}"
		assert email_cr == f"{cr_email}"
		assert phone_cr == f"{cr_phone}"

		#Confirm
		try:
			if wd.find_element(By.CSS_SELECTOR, "div[data-name='caseFinishTab']"):
				wd.find_element(By.NAME, "finishConfirmBtn").click()
		except NoSuchElementException:
			pass

		time.sleep(3)

	def name_deposition_case(self, depo_name):
		wd = self.app.wd
		name = depo_name
		return name

	def depo_dashboard_check(self, depo_name, at_name, at_email,at_phone,op_name, op_email, op_phone,
	cr_name,cr_email,cr_phone):
		wd = self.app.wd
		time.sleep(1)
		name_depo = WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.XPATH, f"//div[text()='{depo_name}']"))).text
		assert name_depo == depo_name
		# Attorney info
		name_attorney = WebDriverWait(wd, 15).until(
			EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{at_name}']"))).text
		email_finish = wd.find_element(By.XPATH, f"//span[text()='{at_email}']").text
		phone_finish = wd.find_element(By.XPATH, f"//span[text()='{at_phone}']").text

		assert name_attorney == f"{at_name}"
		assert email_finish == f"{at_email}"
		assert phone_finish == f"{at_phone}"

		# Op info
		print(op_name)
		op = wd.find_element(By.CSS_SELECTOR, "div[data-name='opposingCounselBlock']")
		name_op = op.find_element(By.XPATH, f"//h2[text()='{op_name}']").get_attribute("textContent")
		email_op = op.find_element(By.XPATH, f"//span[text()='{op_email}']").text
		phone_op = op.find_element(By.XPATH, f"//span[text()='{op_phone}']").text

		assert name_op == f"{op_name}"
		assert email_op == f"{op_email}"
		assert phone_op == f"{op_phone}"

		# Cr info
		name_cr = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{cr_name}']"))).text
		email_cr = wd.find_element(By.XPATH, f"//span[text()='{cr_email}']").text
		phone_cr = wd.find_element(By.XPATH, f"//span[text()='{cr_phone}']").text

		assert name_cr == f"{cr_name}"
		assert email_cr == f"{cr_email}"
		assert phone_cr == f"{cr_phone}"

	def depo_dashboard_manualy(self):
		wd = self.app.wd
		time.sleep(2)
		today = datetime.now()
		day = today.day
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyHomePageCalendar']")
		btn_day = calendar.find_element(By.XPATH, f"//button[text()='{day}']")
		btn_day.send_keys(Keys.RETURN)
		depo_present = wd.find_element(By.CSS_SELECTOR, "div[data-name='StatusProcessCaseItem0']")
		if depo_present.is_displayed() == True:
			return True
		else:
			return False

		time.sleep(2)

	def confirm(self):
		wd = self.app.wd

		wd.find_element(By.NAME, "finishConfirmBtn").click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "finishDepositionBtn"))).click()

	def download_transcript(self, depo_name, att_name, depo_deponent, op_name, op_email, op_phone):
		wd = self.app.wd

		#Open past deposition
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "attorneyHomePastDepBtn"))).click()
		# search input
		input_cr_search = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='searchInputBlock']")))
		input_cr_search.send_keys(f"{depo_name}")

		#Found deposition and check data
		cr_depo = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='pdBlockList'] > div")))
		check_name_depo = cr_depo.find_element(By.XPATH, f"//div[text()='{depo_name}']")
		check_name_att = cr_depo.find_element(By.XPATH, f"//div[text()='{att_name}']")
		check_name_deponent = cr_depo.find_element(By.XPATH, f"//div[text()='{depo_deponent}']")

		assert check_name_depo == depo_name
		assert check_name_att == att_name
		assert check_name_deponent == depo_deponent

		#click "Details" button
		cr_depo.find_element(By.XPATH, "//div[text()='Details']").click()

		#check op
		block_op = WebDriverWait(wd, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
		"div[data-name='opposingCounselBlock']")))

		name = block_op.find_element(By.XPATH, f"//h2[text()='{op_name}']").text
		email = block_op.find_element(By.XPATH, f"//span[text()='{op_email}']").text
		phone = block_op.find_element(By.XPATH, f"//span[text()='{op_phone}']").text

		assert name == op_name
		assert email == op_email
		assert phone == op_phone
		#Download transcript
		file_transcript = wd.find_element(By.CSS_SELECTOR, "div[data-name='fileContainer']")
		file_transcript.find_element(By.CSS_SELECTOR, "button").click()

	def download_any_transcript(self):
		wd = self.app.wd
		#Open past deposition
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "attorneyHomePastDepBtn"))).click()
		time.sleep(2)
		wd.find_element(By.XPATH, "//div[text()='Details']").click()
		time.sleep(3)
		# Download transcript
		file_transcript = wd.find_element(By.CSS_SELECTOR, "div[data-name='fileContainer']")
		time.sleep(1)
		file_transcript.find_element(By.CSS_SELECTOR, "button").click()
		time.sleep(2)
		wd.find_element(By.NAME, "closeBtnModal").click()
		time.sleep(2)

	def download_unreg_transcript(self):
		wd = self.app.wd
		time.sleep(1)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='payNoRegisterBuyBtn']"))).click()
		time.sleep(1)
		wd.find_element(By.CSS_SELECTOR, "div[data-name='payNoRegisterCard']").click()
		time.sleep(5)
		wd.find_element(By.CSS_SELECTOR, "div[data-name='payNoRegisterCard'] input").send_keys(
			"4141414142424242")
		time.sleep(5)
		# wd.find_element(By.CSS_SELECTOR, "div[data-name='payNoRegisterCard'] input").send_keys(
		# 	"4242 4242")
		# time.sleep(5)
		# wd.find_element(By.CSS_SELECTOR, "div[data-name='payNoRegisterCard'] input").send_keys(
		# 	"2112 0325")
		# time.sleep(1)
		# wd.find_element(By.CSS_SELECTOR, "div[data-name='payNoRegisterCard'] input").send_keys(
		# 	"123 12345")
		time.sleep(2)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name=''payNoRegisterBtn]"))).click()
		time.sleep(1)
		wd.find_element(By.CSS_SELECTOR, "div[data-name='ModalDeleteBtn']").click()

	def download_depo_document(self):
		wd = self.app.wd
		#Open past deposition
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "attorneyHomePastDepBtn"))).click()

		#search input and click "Details" button
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='searchInputBlock'] input"))).send_keys("Download depo amd transcript")
		time.sleep(1)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable(
			(By.CSS_SELECTOR, "div[data-name='pastDepositionBtnDownloadBlock566'] button"))).send_keys(Keys.RETURN)
		time.sleep(1)
		wd.find_element(By.XPATH, "//div[text()='Download Depo notice']").click()
		time.sleep(1)
		wd.find_element(By.NAME, "closeBtnModal").click()
		time.sleep(1)
		# Download transcript
		wd.find_element(By.CSS_SELECTOR, "button[name='pastDepositionBtnDetails566']").send_keys(Keys.RETURN)
		wd.find_element(By.XPATH, "//div[text()='Download Depo notice']").click()
		time.sleep(2)
		wd.find_element(By.NAME, "closeBtnModal").click()
		time.sleep(1)

	def begin_date_voting(self):
		wd = self.app.wd
		time.sleep(1)
		two_hour = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='TWO_HOURSdurationBtn']")))
		two_hour.click()
		prev_btn = wd.find_element(By.CSS_SELECTOR, "button[data-name='DirectionButtonPrev']")
		time.sleep(1)
		prev_btn.send_keys(Keys.RETURN)
		time.sleep(2)
		prev_btn.send_keys(Keys.RETURN)
		time.sleep(2)
		prev_btn.send_keys(Keys.RETURN)
		time.sleep(2)
		days = wd.find_elements(By.CSS_SELECTOR, "div[data-name='grid0'] button")
		count = 0
		for i in days:
			time.sleep(3)
			if i.text == "Select":
				i.click()
				wd.find_element(By.CSS_SELECTOR, "button[name='depositionModalConfirmBtn']").click()
				count += 1
				if count == 4:
					wd.find_element(By.CSS_SELECTOR, "button[name='calendarVotingBtn']").click()
					time.sleep(2)
					break
		time.sleep(2)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='voteModalApply']"))).click()
		time.sleep(2)

	#Test voting attorney calendar
	def date_and_time_voting(self):
		wd = self.app.wd
		time.sleep(1)
		two_hour = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='TWO_HOURSdurationBtn']")))
		two_hour.click()
		days = wd.find_elements(By.CSS_SELECTOR, "div[data-name='grid0'] button")
		count = 0
		for i in days:
			time.sleep(3)
			if i.text == "Select":
				i.click()
				wd.find_element(By.CSS_SELECTOR, "button[name='depositionModalConfirmBtn']").click()
				count += 1
				if count == 4:
					wd.find_element(By.CSS_SELECTOR, "button[name='calendarVotingBtn']").click()
					time.sleep(2)
					break
		time.sleep(2)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='voteModalApply']"))).click()
		#wd.find_element(By.CSS_SELECTOR, "button[name='voteModalApply']").click()

	def check_el_present(self):
		wd = self.app.wd
		try:
			wd.find_element(By.CSS_SELECTOR, "button[name='confirmDepositionConfirmBtn']")
			return True
		except NoSuchElementException:
			return False

	def get_link_from_email(self):
		wd = self.app.wd
		time.sleep(3)
		link = re.search("(?P<url>https?://[^\s]+)", self.text).group("url")
		self.link = link[0:-1]
		time.sleep(1)
		wd.get(self.link)
		time.sleep(2)


	#For test case 2.40
	def open_link_again(self):
		wd = self.app.wd
		time.sleep(1)
		mas = []
		mas.append(self.link)

	def select_date_op_voting(self):
		wd = self.app.wd
		time.sleep(2)
		days = wd.find_elements(By.CSS_SELECTOR, "div[data-name='grid1'] button")
		for i in days:
			time.sleep(2)
			if i.text == "10:00 AM":
				i.click()
				wd.find_element(By.CSS_SELECTOR, "button[name='confirmDepositionConfirmBtn']").click()
				break
		time.sleep(2)

	def select_date_as_op_suggest(self):
		wd = self.app.wd
		time.sleep(2)
		days = wd.find_elements(By.CSS_SELECTOR, "div[data-name='grid1'] button")
		count = 0
		for i in days:
			time.sleep(2)
			if i.text == "Suggest":
				time.sleep(1)
				i.click()
				wd.find_element(By.CSS_SELECTOR, "button[name='depositionModalConfirmBtn']").click()
				count += 1
				if count == 4:
					time.sleep(1)
					WebDriverWait(wd, 15).until(
						EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='calendarConfirmBtn']"))).click()
					break

		time.sleep(2)

	def login_attorney_voting(self,  login_att, password_att):
		wd = self.app.wd
		time.sleep(2)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='loginHeaderBtn']"))).send_keys(Keys.RETURN)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']"))).send_keys(login_att)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys(password_att)
		wd.find_element(By.CSS_SELECTOR, "button[name='loginModalBtn']").send_keys(Keys.RETURN)
		time.sleep(3)

	def get_message_info(self,message):

		message_text, encoding, mime = "?????? ???????? ??????????????????", "-", "-"
		if message.is_multipart():
			for part in message.walk():
				if part.get_content_type() in ("text/html", "text/plain"):
					message_text, encoding, mime = self.get_part_info(part)
					break  # ???????????? ???????????? ??????????????????
		else:
			message_text, encoding, mime = self.get_part_info(message)

		return message_text, encoding, mime

	def get_part_info(self,part):

		encoding = part.get_content_charset()
		if not encoding:
			encoding = sys.stdout.encoding

		mime = part.get_content_type()
		message = part.get_payload(decode=True).decode(encoding, errors="ignore").strip()

		return message, encoding, mime

	def finish_depo_attorney_voting(self, at_name, at_email,at_phone,op_name, op_email, op_phone,
	cr_name,cr_email,cr_phone):
		wd = self.app.wd
		time.sleep(1)
		#Attorney info
		name_attorney = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{at_name}']"))).text
		email_finish = wd.find_element(By.XPATH, f"//span[text()='{at_email}']").text
		phone_finish = wd.find_element(By.XPATH, f"//span[text()='{at_phone}']").text

		assert name_attorney == f"{at_name}"
		assert email_finish == f"{at_email}"
		assert phone_finish == f"{at_phone}"

		#Op info
		time.sleep(1)
		op = wd.find_element(By.CSS_SELECTOR, "div[data-name='finishOpposingCounselBloc']")
		name_op = op.find_element(By.XPATH, f"//h2[text()='{op_name}']").get_attribute("textContent")
		email_op = op.find_element(By.XPATH, f"//span[text()='{op_email}']").text
		phone_op = op.find_element(By.XPATH, f"//span[text()='{op_phone}']").text

		assert name_op == f"{op_name}"
		assert email_op == f"{op_email}"
		assert phone_op == f"{op_phone}"

		#Cr info
		# time.sleep(1)
		# name_cr =  WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{cr_name}']"))).text
		# email_cr = wd.find_element(By.XPATH, f"//span[text()='{cr_email}']").text
		# phone_cr = wd.find_element(By.XPATH,f"//span[text()='{cr_phone}']").text
		#
		# assert name_cr == f"{cr_name}"
		# assert email_cr == f"{cr_email}"
		# assert phone_cr == f"{cr_phone}"

		#Confirm
		wd.find_element(By.NAME, "finishConfirmBtn").click()

	def edit_date_in_depo(self):
		wd = self.app.wd
		time.sleep(3)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='attorneyHomeBtnEdit']"))).send_keys(Keys.RETURN)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='depoBackbtn']"))).click()
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='manualPickedChangeBtn']"))).click()

		#Choose two hours
		row = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyRow']")
		row.find_element(By.CSS_SELECTOR, "button[name='TWO_HOURSdurationBtn']").send_keys(Keys.RETURN)
		#Change day
		time.sleep(1)
		today = datetime.now()
		tomorrow  = today + timedelta(1)
		tomorrow = tomorrow.day
		time.sleep(1)
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyCalendar']")
		#calendar.find_element(By.XPATH, f"//button[text()='{tomorrow}']")
		WebDriverWait(calendar, 15).until(EC.element_to_be_clickable((By.XPATH, f"//button[text()='{tomorrow}']"))).send_keys(Keys.RETURN)
		time.sleep(1)

		day_new = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyDateBlock']").text

		#Enter time manually
		hour = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyTime']")
		hour.find_element(By.NAME, "selectTimeBtn").send_keys(Keys.RETURN)
		hour.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.CONTROL + "a")
		hour.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.BACK_SPACE)
		time.sleep(1)
		hour.find_element(By.CSS_SELECTOR, "input").send_keys("7:00 AM")
		wd.find_element(By.XPATH, "//div[text()='Confirm']").click()

		#Confirm btn
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='depoContinueBtn']"))).click()
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='deliveryContinueBtn']"))).click()
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='finishConfirmBtn']"))).click()
		print(day_new)

	def cancel_deposition(self):
		wd = self.app.wd
		time.sleep(2)

		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='attorneyHomeBtnCancel4']"))).click()
		time.sleep(1)
		wd.find_element(By.CSS_SELECTOR, "button[name='cancellationConfirmBtn']").click()
		time.sleep(3)

	def confirm_appearance(self, att_email):
		wd = self.app.wd
		time.sleep(2)
		list = wd.find_element(By.CSS_SELECTOR, "div[data-name='appearancesList']")
		time.sleep(1)
		list.find_element(By.XPATH, f"//p[text()='{att_email}']").click()
		time.sleep(2)
		wd.find_element(By.CSS_SELECTOR, "button[name='appearanceDetailsConfirm']").click()
		time.sleep(2)

	def decline_appearence_cr(self, att_email):
		wd = self.app.wd
		time.sleep(2)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='appearancesList']")))
		list = wd.find_element(By.CSS_SELECTOR, "div[data-name='appearancesList']")
		time.sleep(1)
		list.find_element(By.XPATH, f"//p[text()='{att_email}']").click()

		#Decline button
		time.sleep(2)
		wd.find_element(By.CSS_SELECTOR, "button[name='appearanceDetailsDecline']").click()
		time.sleep(4)

	def get_letter_from_email(self, login, password):
		wd = self.app.wd
		time.sleep(4)
		server = "imap.mail.yahoo.com"
		port = 993

		mail = imaplib.IMAP4_SSL(server, port)
		mail.login(login, password)
		mail.select()
		type, data = mail.search(None, "(FROM 'Trialbase')")
		data = data[0].split()
		latest_id = data[-1]
		result, data = mail.fetch(latest_id, "(RFC822)")

		raw_email = data[0][1]
		message = email.message_from_bytes(raw_email)
		self.date_email = message["Date"]
		self.from_message = message["From"] #Trialbase <info@trialbase.com>
		self.to_message = message["To"] #email address ended user
		self.text, encoding, mime = self.get_message_info(message)
		time.sleep(2)

	def compare_from_to_email(self, from_m, to_m):
		assert self.from_message == from_m
		assert self.to_message == to_m

	def current_time(self):
		current_zone = datetime.now()
		three_hours = timedelta(hours=3)
		min_three = current_zone - three_hours
		current_date = datetime.today().strftime(f'%a, %d %b %Y {min_three.strftime("%H")}')
		sotka_time = f"{current_date}"
		return sotka_time

	def compare_email_and_date(self, emails):
		wd = self.app.wd
		time.sleep(2)
		new_email = re.sub(r"\r\n", "", self.text)
		print(new_email)
		if (new_email.count(emails) == 1): #and (self.date_email.count(self.current_time()) == 1):
			return True
		else:
			return False

	def get_current_time(self):
		wd = self.app.wd

		month = {
			"January" : 1,
			"February": 2,

		}

	def	delete_deposition_from_database(self, id_depo):
		wd = self.app.wd
		message = "Deposition case successfully deleted with all relations and files"

		url = self.app.graphql_url()
		headers = {
			"qatoken": "JEKA_QA_TEST_TOKEN"
		}
		#print(self.number_of_deposition)
		data_query = "mutation{deleteDepositionCase(deposition_id:" + f"{id_depo})" + "{status message} }"

		data = {"query": data_query}

		response = requests.post(url, headers=headers, data=data)

		response_status = response.json()["data"]["deleteDepositionCase"]["status"]
		response_message = response.json()["data"]["deleteDepositionCase"]["message"]

		assert response.status_code == 200, f"Incorrect status code. Status code id '{response.status_code}'"
		assert response_status == True, f"Incorrect status. Status response is '{response_status}'"
		assert response_message == message, f"Incorrect status. Status response is '{response_message}'"

	def create_fake_deposition_waiting(self, status):
		wd = self.app.wd

		url = self.app.graphql_url()

		#date
		date = datetime.now()
		today = date.strftime("%Y-%m-%d")
		date_time = f'["{today} 06:00:00.000000"]'
		# Login, Get access token
		qu = """mutation{signIn(email:"qaautomationatt@yahoo.com", password:"ZXcv@123580" ){
		  access_token
		}

		}"""
		data = {"query": qu}
		response = requests.post(url, data=data)
		access_token = response.json()["data"]["signIn"]["access_token"]
		# Create deposition
		auth_header = 'Bearer ' + access_token
		headers = {
			"Authorization": auth_header,
			"qatoken": "JEKA_QA_TEST_TOKEN"
		}

		data1 = 'mutation{createFakeDepositionCase(status:"WAITING_FOR_SERVICE",' + f'withUnregisterOp:{status},' + f"dates:{date_time})" + "{id start_time}}"
		# data1 = 'mutation{createFakeDepositionCase(status:"WAITING_FOR_NEGOTIATION", withUnregisterOp:false)}'
		data2 = {"query": data1}
		response = requests.post(url, headers=headers, data=data2)
		self.id_case = response.json()["data"]["createFakeDepositionCase"]["id"]
		self.start_time = response.json()["data"]["createFakeDepositionCase"]["start_time"]
		assert response.status_code == 200
		wd.refresh()
		time.sleep(2)

	def create_fake_deposition_voting(self, status):
		wd = self.app.wd

		url = self.app.graphql_url()

		#date
		date = datetime.now()
		today = date.strftime("%Y-%m-%d")
		tomorrow_state = date + timedelta(1)
		tomorrow = tomorrow_state.strftime("%Y-%m-%d")
		next_state = tomorrow_state + timedelta(1)
		next_day = next_state.strftime("%Y-%m-%d")
		one_next_st = next_state + timedelta(1)
		one_next = one_next_st.strftime("%Y-%m-%d")
		date_time = f'["{today} 06:00:00.000000","{tomorrow} 06:00:00.000000","{next_day} 06:00:00.000000","{one_next} 06:00:00.000000"]'
		# Login, Get access token
		qu = """mutation{signIn(email:"qaautomationatt@yahoo.com", password:"ZXcv@123580" ){
		  access_token
		}

		}"""
		data = {"query": qu}
		response = requests.post(url, data=data)
		access_token = response.json()["data"]["signIn"]["access_token"]

		# Create deposition
		auth_header = 'Bearer ' + access_token
		headers = {
			"Authorization": auth_header,
			"qatoken": "JEKA_QA_TEST_TOKEN"
		}

		#data1 = 'mutation{createFakeDepositionCase(status:"WAITING_FOR_SERVICE",' + f'withUnregisterOp:{status}' + ")}"
		data1 = 'mutation{createFakeDepositionCase(status:"WAITING_FOR_NEGOTIATION",' + f"withUnregisterOp:{status}," + f"dates:{date_time})" + "{id start_time}}"
		data2 = {"query": data1}
		response = requests.post(url, headers=headers, data=data2)
		self.id_fake_depo = response.json()["data"]["createFakeDepositionCase"]["id"]
		self.start_time_vot = response.json()["data"]["createFakeDepositionCase"]["start_time"]
		wd.refresh()
		time.sleep(2)
