from data.data_model.data_edit_price import edit_price
import pytest
import allure
import time
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email



#Test case 4.1
@allure.description("Test case 4.1, Change a photo in the attorney account" )
def test_add_photo_attorney(app):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.add_photo.add_photo()
	assert app.session.text_name_attribute_attroney() == "Daniel Vlad Tabakh "
	app.session.logout()

#Test case 4.2
@allure.description("Test case 4.2, Add new photo cr")
def test_add_photo_cr(app):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.add_photo.add_photo()
	assert app.session.text_name_attribute_cr() == "AutomationCR "
	app.session.logout()

#Test case 4.3
@allure.description("Test case 4.3, Add credit card to attorney company")
def test_add_card_attorney(app):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.att_credit.credit_card(card_number='4111 1111 1111 1111', expiry_date='06/23', cvv='897')
	app.session.logout()

#Test case 4.4
@allure.description("Test case 4.4, Edit price cr")
#@pytest.mark.skip(reason='need edit')
@pytest.mark.parametrize("edit_price", edit_price, ids=[repr(i) for i in edit_price])
def test_edit_price(app, edit_price):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.edit_price.change_price(edit_price.appearance_fee, edit_price.page_cost,edit_price.expert_page_cost,
	edit_price.travel,edit_price.estimated,edit_price.turn_around_page,edit_price.copy,
	edit_price.cancellation_fee)
	app.edit_price.save()
	assert app.edit_price.appearance_fee() ==  "$400"
	assert app.edit_price.page_cost() == "$6"
	assert app.edit_price.expert_page_cost() == "$6.5"
	assert app.edit_price.travel() == "$1"
	assert app.edit_price.turn_around_time() == "10 days"
	assert app.edit_price.copy() == "50 %"
	app.session.logout()

#Test case 4.5
@pytest.mark.skip(reason="Test don't work, block front-end")
@allure.description("Test case 4.5, Change schedual cr")
def test_schedual_cr(app):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.schedule.open()
	app.schedule.change_time_monday()
	app.schedule.change_time_tuesday()
	app.schedule.change_time_wednesday()
	app.schedule.change_time_thursday()
	app.schedule.change_time_friday()
	app.schedule.change_time_saturday()
	app.schedule.change_time_sunday()
	app.schedule.save_schedual()
	app.schedule.open()
	assert app.schedule.check_data()
	app.schedule.return_data()
	app.schedule.save_schedual()
	app.session.logout()