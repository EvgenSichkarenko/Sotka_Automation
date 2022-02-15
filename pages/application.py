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
from pages.past_depo_att_download import DepoDownloadAtt
from pages.edit_price_cr import EditPrice
from pages.past_depo_att_details import DepoDetailsAtt
from pages.schedual_cr import Schedual
from pages.past_depo_cr_download import DepoDownloadCR
from pages.past_depo_cr_details import DepoDetailsCr

class Application:

	def __init__(self):
		self.wd = webdriver.Chrome(ChromeDriverManager().install())
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
		self.depo_info_att = DepoDownloadAtt(self)
		self.edit_price = EditPrice(self)
		self.depo_details_att = DepoDetailsAtt(self)
		self.schedule = Schedual(self)
		self.depo_info_cr = DepoDownloadCR(self)
		self.depo_details_cr = DepoDetailsCr(self)

	def is_valid(self):
		try:
			self.wd.current_url
			return True
		except:
			return False

	def open_login(self, wd):
		wd = self.wd
		wd.get("http://stoke-test.s3-website.us-east-2.amazonaws.com/")
		#wd.get("http://sotka.io")

	def destroy(self):
		self.wd.quit()