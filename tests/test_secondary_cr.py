from data.data_model.data_edit_price import edit_price
import pytest
import allure
import time
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email




"""test calendar cr"""
@allure.description("Check display deposition on dashboard cr")
def test_calendar_cr(app):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	count_all = app.calendar_cr.count()
	app.calendar_cr.calendar_day()
	day_count = app.calendar_att.count()
	assert day_count <= count_all
	app.session.logout()


