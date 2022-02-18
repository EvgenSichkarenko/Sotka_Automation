import time
from data.data_model.data_deposition_case import deposition
from data.data_model.data_edit_price import edit_price
import pytest



"""add new photo cr"""
def test_add_photo_cr(app):
	app.session.login(login="crdev@givmail.com", password="1234Qwer")
	app.add_photo.add_photo()
	assert app.session.text_name_attribute_cr() == "Евгений Сичкаренко"
	app.session.logout()

"""edit price cr"""
@pytest.mark.parametrize("edit_price", edit_price)
def test_edit_price(app, edit_price):
	app.session.login(login="crdev@givmail.com", password="1234Qwer")
	app.edit_price.change_price(edit_price.appearance_fee, edit_price.page_cost,edit_price.expert_page_cost,
	edit_price.travel,edit_price.estimated,edit_price.turn_around_page,edit_price.copy,
	edit_price.cancellation_fee,edit_price.cancellation_terms)
	assert app.edit_price.appearance_fee() in  edit_price.appearance_fee
	assert app.edit_price.page_cost() in edit_price.page_cost
	assert app.edit_price.expert_page_cost() in edit_price.expert_page_cost
	assert app.edit_price.travel() in edit_price.travel
	assert app.edit_price.estimated_hour() in edit_price.estimated
	assert app.edit_price.turn_around_time() in edit_price.turn_around_page
	assert app.edit_price.copy() in edit_price.copy
	assert app.edit_price.cancellation_fees() in edit_price.cancellation_fee
	assert app.edit_price.cancellation_terms() in edit_price.cancellation_terms
	app.session.logout()

"""test schedual cr"""
def test_schedual_cr(app):
	app.session.login(login="crdev@givmail.com", password="1234Qwer")
	app.schedule.open()
	app.schedule.change_time_monday()
	app.schedule.change_time_tuesday()
	app.schedule.change_time_wednesday()
	app.schedule.change_time_thursday()
	app.schedule.change_time_friday()
	app.schedule.change_time_saturday()
	app.schedule.change_time_sunday()
	app.schedule.save_schedual()
	app.session.logout()

"""test search and download transcript cr"""
@pytest.mark.parametrize("deposition", deposition)
def test_search_download_transcript(app, deposition):
	app.session.login(login="crdev@givmail.com", password="1234Qwer")
	app.depo_info_cr.search_deposition_cr(deposition.name)
	app.depo_info_cr.check_info_deposition_cr(deposition.name, deposition.deponent, deposition.date)
	app.session.logout()

"""test past deposition details cr"""
@pytest.mark.parametrize("deposition", deposition)
@pytest.mark.parametrize("edit_price", edit_price)
def test_past_depodetails(app, deposition, edit_price):
	app.session.login(login="crdev@givmail.com", password="1234Qwer")
	app.depo_details_cr.open_details()
	app.depo_details_cr.check_deposition_data(deposition.name, deposition.deponent, deposition.attorney)
	app.depo_details_cr.check_op_data()
	app.depo_details_cr.check_invoice(edit_price.appearance_fee, edit_price.page_cost, edit_price.expert_page_cost, edit_price.travel)
