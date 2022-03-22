import allure
import pytest
from data.data_model.data_deposition_case import deposition
import time





"""test deposition case voting create"""
@allure.description("Create deposition case with time manually")
@pytest.mark.parametrize("deposition", deposition)
def test_deposition_create(app, deposition):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition(deposition.address)
	app.deposition.attorneys(deposition.sbn_op1)
#date.today().strftime("%A")