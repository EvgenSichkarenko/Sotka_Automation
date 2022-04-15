from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.add_seecretary import Secretary
from pages.registr_attorney_page import RegistrAttorney
from pages.registr_cr import RegistrCR
from pages.session import Session
from pages.add_attorney import Attorney
from pages.login import Login
from pages.add_card_attorney import Creditcard
from pages.add_photo import Photo
from pages.edit_price_cr import EditPrice
from pages.schedual_cr import Schedual
from pages.deposition_case import DepositionCase
from pages.calendar_att import CalendarAtt
from pages.calendar_cr import CalendarCr
from pages.cr_deposition_info import CrDepoInfo
from pages.att_search_att import FindAtt
from pages.cr_appearances import CrAppearance

class Application:

	def __init__(self):
		#self.wd = webdriver.Chrome(ChromeDriverManager().install())
		self.wd = webdriver.Chrome("/usr/bin/chromedriver")
		self.wd.implicitly_wait(5)
		self.wd.maximize_window()
		self.secretary = Secretary(self)
		self.session = Session(self)
		self.regAttorney = RegistrAttorney(self)
		self.cr = RegistrCR(self)
		self.add_art = Attorney(self)
		self.login = Login(self)
		self.att_credit = Creditcard(self)
		self.add_photo = Photo(self)
		self.edit_price = EditPrice(self)
		self.schedule = Schedual(self)
		self.deposition = DepositionCase(self)
		self.calendar_att = CalendarAtt(self)
		self.calendar_cr = CalendarCr(self)
		self.cr_finish_depo = CrDepoInfo(self)
		self.find_att = FindAtt(self)
		self.cr_appear = CrAppearance(self)


	def is_valid(self):
		try:
			self.wd.current_url
			return True
		except:
			return False

	def open_login(self):
		wd = self.wd
		wd.delete_all_cookies()
		#wd.get('chrome://settings/')
		#wd.execute_script('chrome.settingsPrivate.setDefaultZoom(0.90)')

		#PROD
		wd.get("https://trialbase.com/login")

		#wd.delete_all_cookies()
		#wd.execute_script("document.body.style.transform = 'scale(1, 1)'")
		# wd.execute_script("document.body.style.zoom='80%'")
		# wd.refresh()

		#STAGE
		#wd.get("http://stoke-test.s3-website.us-east-2.amazonaws.com/")

		# time.sleep(5)
		# WebDriverWait(wd, 10).until(
		# 	lambda wd: wd.execute_script('return document.readyState') == 'complete')
		#wd.execute_script("document.body.style.zoom='75%'")

		#wd.refresh()
		#wd.get("http://sotka.io")

	def destroy(self):
		self.wd.quit()