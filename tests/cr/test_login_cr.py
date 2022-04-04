from data.data_model.data_edit_price import edit_price
import pytest


"""add new photo cr"""
def test_add_photo_cr(app):
	app.session.login(login="crtestcr@getnada.com", password="1234Qwer")
	app.add_photo.add_photo()
	assert app.session.text_name_attribute_cr() == "CR Test "
	app.session.logout()

"""edit price cr"""
@pytest.mark.parametrize("edit_price", edit_price)
def test_edit_price(app, edit_price):
	app.session.login(login="crtestcr@getnada.com", password="1234Qwer")
	app.edit_price.change_price(edit_price.appearance_fee, edit_price.page_cost,edit_price.expert_page_cost,
	edit_price.travel,edit_price.estimated,edit_price.turn_around_page,edit_price.copy,
	edit_price.cancellation_fee)
	app.edit_price.save()
	assert app.edit_price.appearance_fee() ==  "$1"
	assert app.edit_price.page_cost() == "$2"
	assert app.edit_price.expert_page_cost() == "$2"
	assert app.edit_price.travel() == "$2"
	assert app.edit_price.estimated_hour() == "2"
	assert app.edit_price.turn_around_time() == "5 days"
	assert app.edit_price.copy() == "100 %"
	assert app.edit_price.cancellation_fees() == "$2"
	app.session.logout()

"""test schedual cr"""
def test_schedual_cr(app):
	app.session.login(login="crtestcr@getnada.com", password="1234Qwer")
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
def test_calendar_cr(app):
	app.session.login(login="crtestcr@getnada.com", password="1234Qwer")
	count_all = app.calendar_cr.count()
	app.calendar_cr.calendar_day()
	day_count = app.calendar_att.count()
	assert day_count < count_all
	app.session.logout()


