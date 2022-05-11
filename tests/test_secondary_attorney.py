import time
import pytest
import allure
from data.data_model.data_test_attorney import attorneys

"""add credit card"""
@allure.description("Add credit card to attorney company")
def test_add_card_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.att_credit.credit_card(card_number='4242424242424242', expiry_date='06/23', cvv='123')
	app.session.logout()

"""add new photo attorney"""
@allure.description("Change a photo in the attorney account" )
def test_add_photo_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.add_photo.add_photo()
	assert app.session.text_name_attribute_attroney() == "Danielle Theresa Kennedy "
	app.session.logout()

"""test calendar attorney"""
@allure.description("Test, check deposition cases current day and shows all deposition")
def test_calendar_att(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	count_all = app.calendar_att.count()
	app.calendar_att.calendar_day()
	today_all = app.calendar_att.count()
	app.calendar_att.show_all_btn()
	assert today_all <= count_all
	app.session.logout()

"""test search attorney"""
@allure.description("Test search attorney in a company")
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_search_attorney(app, att):
	app.session.login(login="attorney0@yahoo.com", password="1234Qwer")
	app.find_att.input(name="  ")
	assert app.find_att.count() == 1
	app.find_att.input(name="Daniel")
	assert app.find_att.count() == 2
	assert app.find_att.check_name(att.name_voting) == att.name_voting
	app.session.logout()

