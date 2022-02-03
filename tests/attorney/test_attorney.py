import time
import pytest
from data.data_model.data_registr_attorney import regisrt_data


def test_login_attorney(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="a1@tafmail.com", valid_password="123Qwer")
	assert app.session.text_name_attribute_attroney() == "Mark John Decastro"
	app.session.logout()

"""add secretary"""
def test_add_secreatry(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.secretary.attorney_company( secr_old_email="secretary02@zetmail.com",
		secr_current_email='secretary05@zetmail.com', secr_new_email="secretary09@zetmail.com", secr_fullname="Ella Nil")
	assert app.session.text_name_attribute_attroney() == "Mark John Decastro"

"""same bar number"""
def test_add_attorney_company(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.add_art.attorney_company(att_sbn='123456', att_email_old='sotka02@zetmail.com',
		att_phonenumber='+380982542188', new_email='sotka0@zetmail.com')

"""different bar number"""
def test_add_atr_dif_company(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.add_art.attorney_different_company(att_sbn='120001', att_email_old='sotka0@zetmail.com',
		new_email="sotka05@zetmail.com")

"""add credit card"""
def test_add_card_attorney(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.att_credit.credit_card(card_number='1234', expiry_date='10/25', cvv='123')

@pytest.mark.parametrize("regisrt_data", regisrt_data)
def test_registr_attorney(app,regisrt_data):
	app.regAttorney.registration_page(regisrt_data.bar_number)
	app.regAttorney.fill_form(regisrt_data.email, regisrt_data.bar_number)
	app.regAttorney.assert_secreatry()
	app.regAttorney.add_secretary(regisrt_data.name_secretary, regisrt_data.email_secretary)
	app.regAttorney.continue_account_button()
	app.regAttorney.img_account_send()
	app.regAttorney.password_input_enter(regisrt_data.valid_password,regisrt_data.invalid_password,regisrt_data.password_match)
	time.sleep(2)