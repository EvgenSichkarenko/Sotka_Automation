import time
from data.data_model.data_deposition_case import deposition
from data.data_model.data_edit_price import edit_price
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_op import op
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
	edit_price.cancellation_fee)
	app.edit_price.save()
	time.sleep(1)
	assert app.edit_price.appearance_fee() ==  "$1"
	assert app.edit_price.page_cost() == "$2"
	assert app.edit_price.expert_page_cost() == "$2"
	assert app.edit_price.travel() == "$2"
	assert app.edit_price.estimated_hour() == "2"
	assert app.edit_price.turn_around_time() == "5 days"
	assert app.edit_price.copy() == "100 %"
	assert app.edit_price.cancellation_fees() == "$2"

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
	app.schedule.open()
	assert app.schedule.check_data()
	app.schedule.return_data()
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


"""test calendar cr"""
def test_calendar_cr(app):
	app.session.login(login="crdev@givmail.com", password="1234Qwer")
	app.calendar_cr.day()
	assert app.calendar_cr.text_no_deposition() == 'There are no meetings today'
	app.calendar_cr.show_all_btn()
	assert app.calendar_cr.count() == 1


"""test deposition info cr"""
@pytest.mark.parametrize("attorneys", attorneys)
@pytest.mark.parametrize("deposition", deposition)
@pytest.mark.parametrize("op", op)
def test_info_deposition_att(app, attorneys, op, deposition):
	app.session.login(login="crdev@givmail.com", password="1234Qwer")
	assert app.cr_finish_depo.deposition_info(deposition.attorney, deposition.address)
	assert app.cr_finish_depo.op_info(op.name, op.email, op.phone)
	assert app.cr_finish_depo.att_info(attorneys.name, attorneys.email, attorneys.phone)
	#assert app.cr_finish_depo.price_info()


