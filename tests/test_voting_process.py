import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
import time

"""test deposition case voting create"""
@allure.description("Create deposition case with time manually")
@pytest.mark.parametrize("deposition", deposition)
@pytest.mark.parametrize("op", op)
def test_deposition_create(app, deposition, op):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_voting,op.name_voting)
	app.deposition.date_and_time_voting()
	app.session.logout()



