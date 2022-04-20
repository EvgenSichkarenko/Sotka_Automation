from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
import time
import os
import imaplib
import email
import sys
import re


class DepositionCase:
	def __init__(self, app):
		self.app = app

	def name_deposition(self, name):
		wd = self.app.wd
		time.sleep(1)
		WebDriverWait(wd,  15).until(EC.element_to_be_clickable((By.NAME, "attorneyHomeNewDepBtn"))).click()
		input = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='caseNameSearchInputWrapper'] input")))
		time.sleep(2)
		input.send_keys(name)
		input.send_keys(Keys.ENTER)

	def deponent_deposition(self, deponent):
		wd = self.app.wd
		input = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div [data-name='caseDeponentInput'] input")))
		input.send_keys(deponent)
		input.send_keys(Keys.RETURN)

	def location_deposition(self):
		wd = self.app.wd
		case_location = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-name='caseLocationTitle']"))).text
		assert case_location == 'Select location', "Select location tab isn't working"
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationCompanyDifLocationBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationByZoomBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "caseLocationContinueBtn"))).click()

	def attorneys(self,op_sbn, name_voting):
		wd = self.app.wd
		#check data attorney
		#add opposing counsel
		input_sbn_op = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='searchAutocomplete'] input")))
		input_sbn_op.click()
		input_sbn_op.send_keys(op_sbn)
		op = wd.find_element(By.XPATH, f"//span[text()='{name_voting}']")
		op.click()

		add_op = len(wd.find_elements(By.CSS_SELECTOR, "div[data-name='rightBlockExistedOC'] > div"))

		if add_op > 0:
			wd.find_element(By.NAME, "caseLocationContinueBtn").click()

	def set_time_manually(self):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Set up time manually']"))).click()
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
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyCalendar']")
		calendar.find_element(By.XPATH, f"//button[text()='{day}']").send_keys(Keys.RETURN)
		time.sleep(1)
		#Enter time manually
		hour = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyTime']")
		hour.find_element(By.NAME, "selectTimeBtn").send_keys(Keys.RETURN)
		hour.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.CONTROL + "a")
		hour.find_element(By.CSS_SELECTOR, "input").send_keys(Keys.BACK_SPACE)
		time.sleep(1)
		hour.find_element(By.CSS_SELECTOR, "input").send_keys("7:00 AM")
		self.time_value = hour.find_element(By.CSS_SELECTOR, "input").get_attribute("value")
		time.sleep(1)
		wd.find_element(By.XPATH, "//div[text()='Confirm']").click()

	def upload_doc(self):
		wd = self.app.wd
		file = os.path.abspath("data/doc/DEPO.pdf")
		#image_path = "C:\Python_project\Sotka_auto\data\doc\DEPO.pdf"
		#WebDriverWait(wd, 10).until(EC.element_to_be_clickable(By.NAME, "depoUploadBtn")).click()
		time.sleep(1)
		input = wd.find_element(By.XPATH, "//input[@name='inputFileHidden']")
		input.send_keys("data/doc/DEPO.pdf")
		time.sleep(1)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "depoContinueBtn"))).click()

	def check_exists_el(self,name_cr):
		wd = self.app.wd
		try:
			wd.find_element(By.XPATH, f"//span[text()='{name_cr}']")
			return True
		except NoSuchElementException:
			return False

	def delivery(self, name_cr):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='deliverySearchInput'] input"))).send_keys(f"{name_cr}")

		while self.check_exists_el(name_cr) == False:
			self.change_time_manually(name_cr)

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{name_cr}']"))).click()
		WebDriverWait(wd, 10).until(
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

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='deliverySearchInput'] input"))).clear()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "deliveryBackBtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "depoBackbtn"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "manualPickedChangeBtn"))).click()


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

		name_depo = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{depo_name}']"))).text
		assert name_depo == depo_name

		#DAY
		try:
			if wd.find_element(By.CSS_SELECTOR, "div[data-name='caseFinishTab']"):
				block = wd.find_element(By.CSS_SELECTOR, "div[data-name='finishDeponentBlock']")
				self.day_deposition = block.find_element(By.CSS_SELECTOR, "div[data-name='contactPersonItem']").get_attribute("textContent")
		except NoSuchElementException:
			pass

		#Attorney info
		name_attorney = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{at_name}']"))).text
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

	def name_deposition_case(self, depo_name):
		wd = self.app.wd
		name = depo_name
		return name

	def depo_dashboard_check(self, depo_name, at_name, at_email,at_phone,op_name, op_email, op_phone,
	cr_name,cr_email,cr_phone):
		wd = self.app.wd
		time.sleep(1)
		name_depo = WebDriverWait(wd, 10).until(
			EC.element_to_be_clickable((By.XPATH, f"//div[text()='{depo_name}']"))).text
		assert name_depo == depo_name
		# Attorney info
		name_attorney = WebDriverWait(wd, 10).until(
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
		name_cr = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{cr_name}']"))).text
		email_cr = wd.find_element(By.XPATH, f"//span[text()='{cr_email}']").text
		phone_cr = wd.find_element(By.XPATH, f"//span[text()='{cr_phone}']").text

		assert name_cr == f"{cr_name}"
		assert email_cr == f"{cr_email}"
		assert phone_cr == f"{cr_phone}"

	def depo_dashboard_manualy(self,depo_name):
		wd = self.app.wd
		try:
			block = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
			block_depo_cases = WebDriverWait(block, 10).until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{depo_name}']")))
			block_depo_cases.click()
		except TimeoutException:
			block = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
			block.find_element(By.CSS_SELECTOR, "button[name='loadMoreBtn']").click()
			time.sleep(2)
			block_depo_cases = WebDriverWait(block, 10).until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{depo_name}']")))
			block_depo_cases.click()

	def confirm(self):
		wd = self.app.wd

		wd.find_element(By.NAME, "finishConfirmBtn").click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "finishDepositionBtn"))).click()

	def download_transcript(self, depo_name, att_name, depo_deponent, op_name, op_email, op_phone):
		wd = self.app.wd

		#Open past deposition
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "attorneyHomePastDepBtn"))).click()
		# search input
		input_cr_search = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='searchInputBlock']")))
		input_cr_search.send_keys(f"{depo_name}")

		#Found deposition and check data
		cr_depo = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
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
		block_op = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
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
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "attorneyHomePastDepBtn"))).click()

		#search input and click "Details" button
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='searchInputBlock'] input"))).send_keys("Anton Sanya Jeka Good Developers test Payment")
		time.sleep(1)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
		"div[data-name='pastDepositionBtnDownloadBlock2364'] button"))).send_keys(Keys.RETURN)
		time.sleep(1)
		wd.find_element(By.CSS_SELECTOR, "div[data-name='fileContainer'] button").click()
		time.sleep(1)
		wd.find_element(By.NAME, "closeBtnModal").click()
		time.sleep(1)
		# Download transcript
		wd.find_element(By.CSS_SELECTOR, "button[name='pastDepositionBtnDetails2364']").send_keys(Keys.RETURN)
		file_transcript = wd.find_element(By.CSS_SELECTOR, "div[data-name='fileContainer']")
		time.sleep(1)
		file_transcript.find_element(By.CSS_SELECTOR, "button").click()
		time.sleep(2)
		wd.find_element(By.NAME, "closeBtnModal").click()
		time.sleep(1)

	def download_depo_document(self):
		wd = self.app.wd
		#Open past deposition
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "attorneyHomePastDepBtn"))).click()

		#search input and click "Details" button
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='searchInputBlock'] input"))).send_keys("Anton Sanya Jeka Good Developers test Payment")
		time.sleep(1)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable(
			(By.CSS_SELECTOR, "div[data-name='pastDepositionBtnDownloadBlock2364'] button"))).send_keys(Keys.RETURN)
		time.sleep(1)
		wd.find_element(By.XPATH, "//div[text()='Download Depo notice']").click()
		time.sleep(1)
		wd.find_element(By.NAME, "closeBtnModal").click()
		time.sleep(1)
		# Download transcript
		wd.find_element(By.CSS_SELECTOR, "button[name='pastDepositionBtnDetails2364']").send_keys(Keys.RETURN)
		wd.find_element(By.XPATH, "//div[text()='Download Depo notice']").click()
		time.sleep(2)
		wd.find_element(By.NAME, "closeBtnModal").click()
		time.sleep(1)

	#Test voting attorney calendar
	def date_and_time_voting(self):
		wd = self.app.wd
		two_hour = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='TWO_HOURSdurationBtn']")))
		two_hour.click()
		days = wd.find_elements(By.CSS_SELECTOR, "div[data-name='grid0'] button")
		count = 0
		for i in days:
			time.sleep(2)
			if i.text == "Select":
				i.click()
				wd.find_element(By.CSS_SELECTOR, "button[name='depositionModalConfirmBtn']").click()
				count += 1
				if count == 4:
					wd.find_element(By.CSS_SELECTOR, "button[name='calendarVotingBtn']").click()
					time.sleep(2)
					break

		wd.find_element(By.CSS_SELECTOR, "button[name='voteModalApply']").click()

	def check_el_present(self):
		wd = self.app.wd
		try:
			wd.find_element(By.CSS_SELECTOR, "button[name='confirmDepositionConfirmBtn']")
			return True
		except NoSuchElementException:
			return False

	#Email
	def get_link_from_email_op(self):
		wd = self.app.wd
		server = "imap.mail.yahoo.com"
		port = 993
		login = "evgen20@yahoo.com"
		password = "udxyliiyxemzfjww"
		#Susan Calabrese Miller
		mail = imaplib.IMAP4_SSL(server, port)
		mail.login(login, password)
		mail.select()
		type, data = mail.search(None, "(FROM 'Trialbase')")
		data = data[0].split()
		latest_id = data[-1]
		result, data = mail.fetch(latest_id, "(RFC822)")
		raw_email = data[0][1]

		message = email.message_from_bytes(raw_email)
		text, encoding, mime = self.get_message_info(message)
		#link = re.search('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
		link = re.search("(?P<url>https?://[^\s]+)", text).group("url")
		link = link[0:-1]
		print(link)
		wd.get(link)
		time.sleep(1)

		#Select date opposing counsel
		days = wd.find_elements(By.CSS_SELECTOR, "div[data-name='grid1'] button")
		for i in days:
			time.sleep(2)
			if i.text == "10:00 AM":
				i.click()
				wd.find_element(By.CSS_SELECTOR, "button[name='confirmDepositionConfirmBtn']").click()
				break
		time.sleep(1)

	def get_link_from_email_attorney(self, login_att, password_att):
		wd = self.app.wd

		server = "imap.mail.yahoo.com"
		port = 993
		login = "attorney0@yahoo.com"
		password = "iqdollxuiqxwxozf"

		mail = imaplib.IMAP4_SSL(server, port)
		mail.login(login, password)
		mail.select()
		type, data = mail.search(None, "(FROM 'Trialbase')")
		data = data[0].split()
		latest_id = data[-1]
		result, data = mail.fetch(latest_id, "(RFC822)")

		raw_email = data[0][1]
		message = email.message_from_bytes(raw_email)
		text, encoding, mime = self.get_message_info(message)
		#link = re.search('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
		link = re.search("(?P<url>https?://[^\s]+)", text).group("url")
		link = link[0:-1]
		print(link)
		wd.get(link)
		time.sleep(2)

		#Login
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='loginHeaderBtn']"))).send_keys(Keys.RETURN)

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']"))).send_keys(login_att)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']"))).send_keys(password_att)
		wd.find_element(By.CSS_SELECTOR, "button[name='loginModalBtn']").send_keys(Keys.RETURN)
		time.sleep(2)

	def get_message_info(self,message):

		message_text, encoding, mime = "Нет тела сообщения", "-", "-"
		if message.is_multipart():
			for part in message.walk():
				if part.get_content_type() in ("text/html", "text/plain"):
					message_text, encoding, mime = self.get_part_info(part)
					break  # Только первое вхождение
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
		name_attorney = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{at_name}']"))).text
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
		time.sleep(1)
		name_cr =  WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{cr_name}']"))).text
		email_cr = wd.find_element(By.XPATH, f"//span[text()='{cr_email}']").text
		phone_cr = wd.find_element(By.XPATH,f"//span[text()='{cr_phone}']").text

		assert name_cr == f"{cr_name}"
		assert email_cr == f"{cr_email}"
		assert phone_cr == f"{cr_phone}"

		#Confirm
		wd.find_element(By.NAME, "finishConfirmBtn").click()

	def edit_date_in_depo(self):
		wd = self.app.wd

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='attorneyHomeBtnEdit']"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='depoBackbtn']"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='manualPickedChangeBtn']"))).click()

		#Choose two hours
		row = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyRow']")
		row.find_element(By.CSS_SELECTOR, "button[name='TWO_HOURSdurationBtn']").send_keys(Keys.RETURN)
		#Change day
		time.sleep(1)
		today = datetime.now()
		tomorrow  = today + timedelta(1)
		tomorrow = tomorrow.day
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='depositionManuallyCalendar']")
		calendar.find_element(By.XPATH, f"//button[text()='{tomorrow}']").send_keys(Keys.RETURN)
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
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='depoContinueBtn']"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='deliveryContinueBtn']"))).click()
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='finishConfirmBtn']"))).click()

		assert self.day_deposition != day_new

		print(self.day_deposition)
		print(day_new)

	def cansel_deposition(self, depo_name):
		wd = self.app.wd

		time.sleep(2)
		today = datetime.now()
		day = today.day
		calendar = wd.find_element(By.CSS_SELECTOR, "div[data-name='attorneyHomePageCalendar']")
		btn_day = calendar.find_element(By.XPATH, f"//button[text()='{day}']")
		btn_day.send_keys(Keys.RETURN)
		time.sleep(1)

		parents = wd.find_element(By.XPATH,f"//button[text()='{day}']/.." )
		assert self.chech_status_approve(parents) == True

		#Find depo on dahsboard

		try:
			block = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
			WebDriverWait(block, 10).until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{depo_name}']"))).click()
		except NoSuchElementException:
			block = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
			time.sleep(1)
			block.find_element(By.CSS_SELECTOR, "button[name='loadMoreBtn']").send_keys(Keys.RETURN)
			WebDriverWait(block, 10).until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{depo_name}']"))).click()

		time.sleep(1)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='attorneyHomeBtnCancel4']"))).click()
		time.sleep(1)
		wd.find_element(By.XPATH, "//div[text()='Yes, cancel']").click()
		time.sleep(3)

		parents = wd.find_element(By.XPATH,f"//button[text()='{day}']/.." )

		assert self.chech_status_approve(parents) == False

	def chech_status_approve(self, parents):
		try:
			return parents.find_element(By.CSS_SELECTOR, "div[data-name='CircleApproved']").is_enabled()
		except NoSuchElementException:
			return False

	def decline_appearence_cr(self, att_email):
		wd = self.app.wd
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='appearancesList']")))
		list = wd.find_element(By.CSS_SELECTOR, "div[data-name='appearancesList']")
		time.sleep(1)
		list.find_element(By.XPATH, f"//p[text()='{att_email}']").click()

		#Decline button
		wd.find_element(By.CSS_SELECTOR, "button[name='appearanceDetailsDecline']").click()
		time.sleep(4)
		server = "imap.mail.yahoo.com"
		port = 993
		login = "attorney0@yahoo.com"
		password = "iqdollxuiqxwxozf"

		mail = imaplib.IMAP4_SSL(server, port)
		mail.login(login, password)
		mail.select()
		type, data = mail.search(None, "(FROM 'Trialbase')")
		data = data[0].split()
		latest_id = data[-1]
		result, data = mail.fetch(latest_id, "(RFC822)")

		raw_email = data[0][1]
		message = email.message_from_bytes(raw_email)
		text, encoding, mime = self.get_message_info(message)

		new_email = re.sub(r"\r\n", " ", text)
		str_email = "You are all set for this deposition, but you can always make" \
				  " an alternative selection by visiting your Trialbase account:"

		assert new_email.count(str_email) == 1