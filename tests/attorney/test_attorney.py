import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr import cr
import time


"""add credit card"""
@allure.description("Add credit card to attorney company")
def test_add_card_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.att_credit.credit_card(card_number='4111111111111111', expiry_date='08/23', cvv='123')
	app.session.logout()

"""add new photo attorney"""
@allure.description("Change a photo in the attorney account" )
def test_add_photo_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	assert app.add_photo.add_photo()
	assert app.session.text_name_attribute_attroney() == "Joel William Meskin "
	app.session.logout()

"""test calendar attorney"""
@allure.description("Test, check deposition cases current day and shows all deposition")
def test_calendar_att(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	count_depo = app.calendar_att.count()
	app.calendar_att.show_all_btn()
	assert app.calendar_att.count() > count_depo
	app.session.logout()

"""test search attorney"""
@allure.description("Test search attorney in a company")
def test_search_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.find_att.input(name="Lindsay")
	assert app.find_att.count() == 1
	app.session.logout()

#
# """test deposition case create"""
# @allure.description("Create deposition case with time manually")
# @pytest.mark.parametrize("deposition", deposition)
# def test_deposition_create(app, deposition):
# 	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
# 	app.deposition.name_deposition(deposition.name)
# 	app.deposition.deponent_deposition(deposition.deponent)
# 	app.deposition.location_deposition(deposition.address)
# 	app.deposition.attorneys(deposition.sbn_op1)
# 	app.deposition.set_time_manually()
# 	app.deposition.upload_doc()
# 	app.deposition.delivery()
# 	app.deposition.finish_depo()
# 	app.deposition.confirm()
# 	time.sleep(1)


"""test depo info attorney"""
@pytest.mark.parametrize("deposition", deposition)
def test_depo_info(app, deposition):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.depo_info_att.search_deposition(deposition.name)
	app.depo_info_att.check_info_deposition(deposition.name, deposition.deponent, deposition.date)
	app.session.logout()


"""test depo details info attorney"""
@pytest.mark.parametrize("deposition", deposition)
def test_detail_depo(app, deposition):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.depo_details_att.open_details()
	app.depo_details_att.check_deposition_data(deposition.name, deposition.deponent, deposition.attorney)
	app.depo_details_att.check_op_data()
	app.depo_details_att.details()
	time.sleep(1)
