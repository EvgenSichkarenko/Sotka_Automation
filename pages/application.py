from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
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

		#self.wd = webdriver.Chrome("\\drivers\\chromedriver.exe")
		self.options = webdriver.ChromeOptions()
		#self.chrome_options.add_argument('--no-sandbox')
		##self.chrome_options.add_argument('--window-size=1420,1080')
		self.options.add_argument('--headless')
		self.options.add_argument('--make-default-browse')
		#self.chrome_options.add_argument('--disable-gpu')
		self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
		self.wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
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


	def open_login(self):
		wd = self.wd
		wd.delete_all_cookies()

		#PROD
		#wd.get("https://trialbase.com/login")

		#STAGE
		wd.get("http://stoke-test.s3-website.us-east-2.amazonaws.com/")


	def destroy(self):
		self.wd.quit()