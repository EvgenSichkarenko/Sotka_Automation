import allure
import pytest
from data.data_model.data_deposition_case import deposition
import time



"""test deposition case manually create"""
@allure.description("Create deposition case with time manually")
@pytest.mark.parametrize("deposition", deposition)
def test_deposition_create(app, deposition):
	app.session.login(login="test111111@getnada.com", password="1234Qwer")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition(deposition.address)
	app.deposition.attorneys(deposition.sbn_op1)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	app.deposition.delivery(name_cr="CR Test")
	app.deposition.finish_depo_attorney(deposition.name)
	app.deposition.confirm()
	app.deposition.depo_dashboard(deposition.name)
	app.deposition.finish_depo_attorney(deposition.name)
	app.session.logout()
