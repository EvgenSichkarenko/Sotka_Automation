from data.data_model.data_edit_price import edit_price
import pytest
import allure
import time
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email


"""add new photo cr"""
@allure.description("Add new photo cr")
def test_add_photo_cr(app):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.add_photo.add_photo()
	assert app.session.text_name_attribute_cr() == "AutomationCR "
	app.session.logout()

"""edit price cr"""
@allure.description("Edit price cr")
@pytest.mark.parametrize("edit_price", edit_price, ids=[repr(i) for i in edit_price])
def test_edit_price(app, edit_price):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.edit_price.change_price(edit_price.appearance_fee, edit_price.page_cost,edit_price.expert_page_cost,
	edit_price.travel,edit_price.estimated,edit_price.turn_around_page,edit_price.copy,
	edit_price.cancellation_fee)
	app.edit_price.save()
	assert app.edit_price.appearance_fee() ==  "$1"
	assert app.edit_price.page_cost() == "$2"
	assert app.edit_price.expert_page_cost() == "$2"
	assert app.edit_price.travel() == "$2"
	assert app.edit_price.turn_around_time() == "5 days"
	assert app.edit_price.copy() == "100 %"
	app.session.logout()

"""test schedual cr"""
#@pytest.mark.skip(reason="Test don't work, block front-end")
@allure.description("Change schedual cr")
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

"""test calendar cr"""
@allure.description("Check display deposition on dashboard cr")
def test_calendar_cr(app):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	count_all = app.calendar_cr.count()
	app.calendar_cr.calendar_day()
	day_count = app.calendar_att.count()
	assert day_count <= count_all
	app.session.logout()


#Test case 2.17
@allure.description("CR Avalibility")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_cr_availability(app, deposition, cr_voting, op, att):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.schedule.disable_day()
	app.session.logout()
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op, op.email)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	assert app.schedule.delivery_check_cr(cr_voting.name) == False
	app.session.logout()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.schedule.enable_day()
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)