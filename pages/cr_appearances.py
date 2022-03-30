from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CrAppearance:
	def __init__(self, app):
		self.app = app

	def confirm_appear(self, att_name, att_email, att_phone, op_name, op_email, op_phone):
		wd = self.app.wd

		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='appearancesList'] div"))).click()

		# Attorney info
		name_attorney = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{att_name}']"))).text
		email_finish = wd.find_element(By.XPATH, f"//span[text()='{att_email}']").text
		phone_finish = wd.find_element(By.XPATH, f"//span[text()='{att_phone}']").text

		assert name_attorney == f"{att_name}"
		assert email_finish == f"{att_email}"
		assert phone_finish == f"{att_phone}"

		# Op info
		name_attorney = wd.find_element(By.XPATH, f"//h2[text()='{op_name}']").text
		email_finish = wd.find_element(By.XPATH, f"//span[text()='{op_email}']").text
		phone_finish = wd.find_element(By.XPATH, f"//span[text()='{op_phone}']").text

		assert name_attorney == f"{op_name}"
		assert email_finish == f"{op_email}"
		assert phone_finish == f"{op_phone}"

		self.name_deposition = wd.find_element(By.CSS_SELECTOR, "div[data-name='appearanceDetailsCaseName']").text
		#confirm appearance click to button
		wd.find_element(By.CSS_SELECTOR, "button[name='appearanceDetailsConfirm']").click()

	def check_data_dashboard(self, att_name, att_email, att_phone, op_name, op_email, op_phone):
		wd = self.app.wd

		time.sleep(1.5)
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "calendarShowAllBtn"))).click()
		time.sleep(1.5)
		#search deposition in dashboard cr
		# block = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
		# block_depo_cases = WebDriverWait(block, 10).until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{self.name_deposition}']")))
		# block_depo_cases.click()

		block = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
		tags_p = block.find_elements(By.CSS_SELECTOR, "p")
		for p in tags_p:
			print(p.text)
			# if p.text == "Test_7AM_new":
			# 	element = p
			# 	element.click()
			# 	element.send_keys(Keys.RETURN)
			# 	break

		time.sleep(1)
		#WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='Test_7AM_new']"))).click()


		time.sleep(2)
		#Check executor
		executor = wd.find_element(By.CSS_SELECTOR, "div[data-name='personContactBlock']")
		name_attorney =  executor.find_element(By.XPATH, f"//h2[text()='{att_name}']").text
		email_finish = executor.find_element(By.XPATH, f"//span[text()='{att_email}']").text
		phone_finish = executor.find_element(By.XPATH, f"//span[text()='{att_phone}']").text

		assert name_attorney == f"{att_name}"
		assert email_finish == f"{att_email}"
		assert phone_finish == f"{att_phone}"

		#Check op
		op = wd.find_element(By.CSS_SELECTOR, "div[data-name='opposingCounselBlock']")
		name_op = op.find_element(By.XPATH, f"//h2[text()='{op_name}']").text
		email_finish = op.find_element(By.XPATH, f"//span[text()='{op_email}']").text
		phone_finish = op.find_element(By.XPATH, f"//span[text()='{op_phone}']").text

		assert name_op == f"{op_name}"
		assert email_finish == f"{op_email}"
		assert phone_finish == f"{op_phone}"

	def past_deposition(self, depo_deponent, att_name):
		wd = self.app.wd

		#click button past deposition
		WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "crHomePastDepositionsBtn"))).click()
		#search input
		input_cr_search = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-name='searchInputBlock'] input")))
		#input_cr_search.send_keys("Test_7AM_new")
		input_cr_search.send_keys(f"{self.name_deposition}")

		#Found deposition and check data
		cr_depo = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='pdBlockList'] > div")))

		check_name_depo = cr_depo.find_element(By.XPATH, f"//div[text()='{self.name_deposition}").text
		check_name_att = cr_depo.find_element(By.XPATH, f"//div[text()='{att_name}']").text
		check_name_deponent = cr_depo.find_element(By.XPATH, f"//div[text()='{depo_deponent}']").text

		assert check_name_depo == {self.name_deposition}
		assert check_name_att == att_name
		assert check_name_deponent == depo_deponent

		#click "Details" button
		cr_depo.find_element(By.CSS_SELECTOR, "button").click()

	def upload_transcript(self, op_name, op_email, op_phone):
		wd = self.app.wd
		time.sleep(2)
		#check op data
		block_op = WebDriverWait(wd, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
		"div[data-name='opposingCounselBlock']")))

		name = block_op.find_element(By.XPATH, f"//h2[text()='{op_name}']").text
		email = block_op.find_element(By.XPATH, f"//span[text()='{op_email}']").text
		phone = block_op.find_element(By.XPATH, f"//span[text()='{op_phone}']").text

		assert name == op_name
		assert email == op_email
		assert phone == op_phone

		#upload transcript
		image_path = "C:\Python\Sotka_auto\data\doc\transcript.pdf"
		wd.find_element(By.NAME, "InfoHeaderButton").click()
		wd.find_element(By.NAME, "downloadExpertPageUploadBtn").send_keys(image_path)
		wd.find_element(By.NAME, "downloadExpertConfirmBtn").click()
		#wd.find_element(By.XPATH, "//input[@name='inputFileHidden']")