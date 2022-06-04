from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time


class CrAppearance:
	def __init__(self, app):
		self.app = app

	def confirm_appear(self, att_name, att_email, att_phone, op_name, op_email, op_phone):
		wd = self.app.wd

		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((
			By.CSS_SELECTOR, "div[data-name='appearancesList']")))
		list = wd.find_element(By.CSS_SELECTOR, "div[data-name='appearancesList']")
		time.sleep(1)
		list.find_element(By.XPATH, f"//p[text()='{att_email}']").click()
		# Attorney info
		name_attorney = WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.XPATH, f"//h2[text()='{att_name}']"))).text
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


		#search deposition in dashboard cr
		# block = wd.find_element(By.CSS_SELECTOR, "main[data-name='statusProcessMain']")
		# block_depo_cases = WebDriverWait(block, 15).until(EC.element_to_be_clickable((By.XPATH, f"//p[text()='{self.name_deposition}']")))
		# block_depo_cases.click()

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

		time.sleep(1)

	def past_deposition(self):
		wd = self.app.wd
		#click button past deposition
		time.sleep(2)
		WebDriverWait(wd, 15).until(EC.element_to_be_clickable((By.NAME, "crHomePastDepositionsBtn"))).click()
		#Found deposition and check data
		time.sleep(2)
		wd.find_element(By.XPATH, "//div[text()='Details']").click()
		time.sleep(2)


	def element_present(self):
		wd = self.app.wd
		try:
			wd.find_element(By.CSS_SELECTOR, "button[name='InfoHeaderButton']")
			return True
		except NoSuchElementException:
			return False

	def upload_transcript(self):
		wd = self.app.wd
		time.sleep(2)
		#upload transcript
		# image_path = r"/var/lib/jenkins/workspace/Test_stoke_sotka/data/doc/transcript.pdf"
		image_path = r"C:\Python_project\Sotka_auto\data\doc\transcript.pdf"
		wd.find_element(By.NAME, "InfoHeaderButton").click()
		time.sleep(2)
		wd.find_element(By.NAME, "pages_count").send_keys("2")
		time.sleep(2)
		wd.find_element(By.CSS_SELECTOR, "input[name='file']").send_keys(image_path)
		time.sleep(2)
		wd.find_element(By.NAME, "downloadExpertConfirmBtn").send_keys(Keys.RETURN)
		time.sleep(5)
		wd.find_element(By.CSS_SELECTOR, "button[name='invoiceBillingBtn']").click()
		time.sleep(1)
		wd.find_element(By.CSS_SELECTOR, "button[name='closeBtnModal']").click()
		time.sleep(1)