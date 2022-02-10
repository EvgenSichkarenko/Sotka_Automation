import pytest
from data.data_model.data_deposition_case import deposition


"""add secretary"""
def test_add_secreatry(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.secretary.contact_person( secr_old_email="secretary02@zetmail.com",
		secr_current_email='secretary05@zetmail.com', secr_new_email="secretary09@zetmail.com", secr_fullname="Ella Nil")
	assert app.session.text_name_attribute_attroney() == "Mark John Decastro"
	app.session.logout()


"""same bar number"""
def test_add_attorney_company(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.add_art.attorney_company(att_sbn='123456', att_email_old='sotka02@zetmail.com',
		att_phonenumber='+380982542188', new_email='sotka0@zetmail.com')
	app.session.logout()


"""different bar number"""
def test_add_atr_dif_company(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.add_art.attorney_different_company(att_sbn='120001', att_email_old='sotka0@zetmail.com',
		new_email="sotka05@zetmail.com")
	app.session.logout()


"""add credit card"""
def test_add_card_attorney(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.att_credit.credit_card(card_number='4111111111111111', expiry_date='08/23', cvv='123')

"""add new photo attorney"""
def test_add_photo_attorney(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.add_photo.add_photo()
	assert app.session.text_name_attribute_attroney() == "Mark John Decastro"
	app.session.logout()

"""test depo info attorney"""
@pytest.mark.parametrize("deposition", deposition)
def test_depo_info(app, deposition):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.depo_info.search_deposition(deposition.name)
	app.depo_info.check_info_deposition(deposition.name, deposition.deponent, deposition.date)

