import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
import time

"""create depo and decline cr deposition, check email owner"""
@allure.description("create depo and decline cr deposition, check email owner")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_deposition_create_decline_appearence(app, deposition, cr_voting, op, att):
	app.session.login(login="attorney0@yahoo.com", password="1234Qwer")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_voting,op.name_voting)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney(deposition.name,att.name_voting,att.email_voting,att.phone_voting,
		op.name_voting,op.email_voting, op.phone_voting,cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	time.sleep(2)
	app.session.login(login="cr1auto@getnada.com", password="1234Qwer")
	app.deposition.decline_appearence_cr(att.email_voting)

# """test deposition case voting create"""
# @allure.description("Add op and voting")
# @pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
# @pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
# def test_deposition_create(app, deposition, op):
# 	app.session.login(login="attorney0@yahoo.com", password="1234Qwer")
# 	app.deposition.name_deposition(deposition.name)
# 	app.deposition.deponent_deposition(deposition.deponent)
# 	app.deposition.location_deposition()
# 	app.deposition.attorneys(deposition.sbn_voting,op.name_voting)
# 	app.deposition.date_and_time_voting()
# 	app.session.logout()
#
# @allure.description("Get email link from op email and voting")
# def test_email_voting_as_op(app):
# 	app.deposition.get_link_from_email_op()
#
# @allure.description("Get email link from attorney and finish deposition case")
# @pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
# @pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
# @pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
# def test_email_voting_as_attorney(app, cr_voting, op, att):
# 	app.deposition.get_link_from_email_attorney(password_att="1234Qwer", login_att="attorney0@yahoo.com")
# 	app.deposition.upload_doc()
# 	app.deposition.delivery(cr_voting.name)
# 	app.deposition.finish_depo_attorney_voting(att.name_voting,att.email_voting,att.phone_voting,op.name_voting,op.email_voting
# 		,op.phone_voting, cr_voting.name,cr_voting.email,cr_voting.phone)
# 	app.session.logout()