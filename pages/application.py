from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.add_seecretary import Secretary
from pages.registr_attorney_page import RegistrAttorney
from pages.registr_cr import RegistrCR
from pages.session import Session
from pages.add_attorney import Attorney

class Application:

	def __init__(self):
		self.wd = webdriver.Chrome(ChromeDriverManager().install())
		self.wd.maximize_window()
		self.secretary = Secretary(self)
		self.session = Session(self)
		self.regAttorney = RegistrAttorney(self)
		self.cr = RegistrCR(self)
		self.add_art = Attorney(self)

	def open_login(self, wd):
		wd = self.wd
		wd.get("http://stoke-test.s3-website.us-east-2.amazonaws.com/")

	def destroy(self):
		self.wd.quit()