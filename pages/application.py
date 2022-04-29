import platform
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
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

		# options = Options()
		# # a few usefull options
		# options.add_argument("--disable-infobars")
		# options.add_argument("start-maximized")
		# options.add_argument("--disable-extensions")
		# options.add_argument("--headless")  # if you want it headless
		#
		# if platform.system() == "Linux" :
		# 	# if raspi
		# 	options.BinaryLocation = ("/usr/bin/google-chrome")
		# 	service = Service("/home/ubuntu/drivers/chromedriver")
		# else:  # if not raspi and considering you're using Chrome
		# 	service = Service(ChromeDriverManager().install())
		#
		# self.wd = webdriver.Chrome(
		# 	service=service,
		# 	options=options
		# )
		self.options = webdriver.ChromeOptions()
		self.options.add_argument('--no-sandbox')
		self.options.add_argument('--window-size=1280,720')
		self.options.add_argument('--headless')
		self.options.add_argument('start-maximized')
		self.options.add_argument('disable-infobars')
		self.options.add_argument('--make-default-browse')
		self.options.add_argument('--disable-gpu')
		self.options.add_argument("--disable-extensions")
		self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
		#self.options.binary_location = "/usr/bin/google-chrome"
		#self.chrome_driver_binary = "/home/ubuntu/drivers/chromedriver"
		#self.wd = webdriver.Chrome(service=Service(self.chrome_driver_binary), options=self.options)
		self.wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
		#self.wd = webdriver.Chrome(service=Service(ChromeDriverManager(self.chrome_driver_binary).install()), options=self.options, executable_path="/home/ubuntu/drivers/chromedriver")
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
		time.sleep(1)
		#STAGE2
		#wd.get("http://ec2-3-120-152-160.eu-central-1.compute.amazonaws.com:8080/")

	def destroy(self):
		self.wd.quit()