import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email
from data.data_model.data_edit_price import edit_price
from data.data_model.op_unregistered import op_unreg
import time


#Test case 2.1
@allure.description("Test case 2.1, Create deposition case with time manually")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_2_1_deposition_create_manually(app, deposition, cr_voting, op, att, emails):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op, op.email)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,op.name,op.email
		,op.phone,cr_voting.name,cr_voting.email,cr_voting.phone)
	time.sleep(3)
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_create_depo_manually_op) #email 12
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	assert app.deposition.compare_email_and_date(emails.email_create_depo_manually_cr) #email 7
	app.calendar_att.calendar_day()
	app.deposition.depo_dashboard_manualy()
	app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)


#Test case 2.2
@allure.description("Test case 2.2, Voting process")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
def test_2_2_deposition_create_voting(app, deposition, op, emails, att, cr_voting):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.begin_date_voting()
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_befor_voting_op) #10 email
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	#test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.email_owner_all_op_voting) #24 email
	app.deposition.get_link_from_email()
	app.deposition.login_attorney_voting(login_att="qaautomationatt@yahoo.com", password_att="ZXcv@123580")
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	#check email for op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_op_noticed_depo) #12 email
	#check email for cr new appearance
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	assert app.deposition.compare_email_and_date(emails.email_cr_new_appearance) #7 email
	app.deposition.get_link_from_email()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	time.sleep(2)
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.email_cr_agreed_for_deal) #8 email
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)

#Test case 2.2a
@allure.description("Test case 2.2a block 4 tab")
@pytest.mark.skip("firs of all need fix from front-end side")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
def test_2_2a_deposition_create_voting(app, deposition, op, emails, att, cr_voting):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.date_and_time_voting()
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	#test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	app.deposition.get_link_from_email()
	app.deposition.login_attorney_voting(login_att="qaautomationatt@yahoo.com", password_att="ZXcv@123580")
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)

#Test case 2.3 / 2.39
@allure.description("Test case 2.3, Revoting process")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
def test_2_3revoting(app, emails, att,cr_voting, deposition,op):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.date_and_time_voting()
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_befor_voting_op) #10 email
	app.deposition.get_link_from_email()
	app.deposition.select_date_as_op_suggest()
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	app.deposition.get_link_from_email() #email 19 or 11
	app.deposition.select_date_op_voting() #select new date as attorney
	app.deposition.login_attorney_voting(login_att="qaautomationatt@yahoo.com", password_att="ZXcv@123580" )
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)

#Test case 2.4
@allure.description("Test case, 2.4")
@pytest.mark.parametrize("emails", email)
def test_2_4_cancel_depo(app, emails):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.cancel_deposition()
	app.session.logout()
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	assert app.deposition.compare_email_and_date(emails.email_owner_cancel_depo)  # 18 email
	app.deposition.get_link_from_email()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)


#Test case #2.6 and 2.22
@allure.description("Test case, 2.6, 2.22, create depo and decline cr deposition, check email owner")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("emails", email)
def test_2_6_decline_appearance(app, deposition, cr_voting, op, att, emails):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	print(emails.cr_new_appearance_fake)
	assert app.deposition.compare_email_and_date(emails.cr_new_appearance_fake)  # 7 email
	app.deposition.get_link_from_email()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.decline_appearence_cr(att.email)
	app.session.logout()
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	print(emails.cr_decline_apear_fake)
	assert app.deposition.compare_email_and_date(emails.cr_decline_apear_fake)  # 6 email
	app.deposition.delete_deposition_from_database(app.deposition.id_case)

#Test case 2.9, 2.10, 2.11, 2.16, 2.8
#@pytest.mark.skip(reason="Need add attribute or send in input card data")
@allure.description("Test case 2.8, 2.9, 2.10, 2.11, 2.16")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
def test_cr_upload_transcript(app, att, deposition, op, emails):
	app.deposition.create_fake_deposition_waiting(status="true")
	app.session.login(login = "qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.cr_appear.check_data_appearance(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.cr_appear.confirm_appearance()
	app.cr_appear.past_deposition()
	app.cr_appear.upload_transcript()
	app.session.logout()
	time.sleep(2)
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_op_transcript_add) #email 15
	time.sleep(2)
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	print(emails.email_att_transcript_add)
	assert app.deposition.compare_email_and_date(emails.email_att_transcript_add) #email 14
	#download as attorney Test case 2.10
	app.deposition.login_without_open_link(login = "qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.download_any_transcript()
	app.session.logout()
	#download as op registered Test case 2.11
	app.deposition.login_without_open_link(login = "qaautomationop@yahoo.com", password="ZXcv@123580")
	app.deposition.download_any_transcript()
	app.session.logout()
	#download as op unregistered Test case 2.16
	app.deposition.get_letter_from_email(login="qaautomationopunreg@yahoo.com", password="gvwdvmcqjriiwupp")
	print(emails.email_op_unregist_transcript)
	assert app.deposition.compare_email_and_date(emails.email_op_unregist_transcript) #email 22
	app.deposition.get_link_from_email()
	#app.deposition.download_unreg_transcript()
	app.deposition.delete_deposition_from_database(id_depo=app.deposition.id_case)
	app.cr_appear.delete_att_from_database()

#Test case #2.15
@allure.description("Test case 2.15, Confirm appearance from cr and check data")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("prices", edit_price)
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_2_15cr_confirm_appearances(app, deposition, op, att, emails,prices):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.cr_appear.check_data_appearance(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.cr_appear.check_prices_appearance(prices.minimum_transcript_charge, prices.page_cost, prices.expert_page_cost,
	prices.travel, prices.copy)
	app.cr_appear.confirm_appearance()
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.cr_accept_apear_fake)  #8  email
	app.cr_appear.check_data_dashboard(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)

#Test case 2.17
@allure.description("Test case 2.17, CR Avalibility")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_2_17_cr_availability(app, deposition, cr_voting, op, att):
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

#Need add check email 21. but before ask Vadim about body email
#Test case 2.20 / 2.4
@allure.description("Test case 2.20, CR cansel deposition")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_2_20_cr_cancel_deposition(app, att, emails):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	time.sleep(5)
	app.cr_appear.cancel_cr_depo()
	app.session.logout()
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.email_cr_cancel_depo)  # 21 email
	app.deposition.delete_deposition_from_database(app.deposition.id_case)

#Test case 2.27, old test case must be in database
@allure.description("Test case 2.27,Check depo restrictions")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
def test_2_27_check_depo_restrict(app, deposition):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.add_new_link()
	assert app.deposition.check_name() == "You are not allowed to see this case"
	time.sleep(2)

#Test case 2.32
@allure.description("Test case 2.32")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
def test_case_2_32_depo_from_att_finish_secr(app, emails, att, cr_voting, deposition, op):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op, op.email)
	app.deposition.begin_date_voting()
	#app.deposition.date_and_time_voting()
	app.session.logout()
	# test email voting as op
	app.deposition.get_letter_from_email(login="qaautomationop@yahoo.com", password="jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_befor_voting_op)  # 10 email
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	# test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login="qaautomationatt@yahoo.com", password="emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.email_owner_all_op_voting)  # 24 email
	app.session.login(login="qaautomationsecr@yahoo.com", password="ZXcv@123580")
	app.secretary.edit_depo_from_secretary()
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	#check email for op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_op_noticed_depo) #12 email
	app.session.logout()
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	#check email for cr new appearance
	assert app.deposition.compare_email_and_date(emails.email_cr_new_appearance) #7 email
	app.deposition.get_link_from_email()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	app.session.logout()
	time.sleep(2)
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.email_cr_agreed_for_deal) #8 email
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)

#Test case 2.33
@allure.description("Test case 2.33")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
def test_2_33_start_depo_from_ser_fin_att(app, emails, att, cr_voting, deposition, op):
	app.session.login(login="qaautomationsecr@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op, op.email)
	app.deposition.begin_date_voting()
	#app.deposition.date_and_time_voting()
	app.session.logout()
	# test email voting as op
	app.deposition.get_letter_from_email(login="qaautomationop@yahoo.com", password="jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_befor_voting_op)  # 10 email
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	#test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login="qaautomationsecr@yahoo.com", password="fnasmhrlsacdmozz")
	#print(emails.email_secr_op_confirm_depo)
	assert app.deposition.compare_email_and_date(emails.email_secr_op_confirm_depo) #11 email
	app.deposition.get_link_from_email()
	app.deposition.login_attorney_voting(login_att="qaautomationatt@yahoo.com", password_att="ZXcv@123580")
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_op_noticed_depo) #12 email
	app.session.logout()
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	#check email for cr new appearance
	assert app.deposition.compare_email_and_date(emails.email_cr_new_appearance) #7 email
	app.deposition.get_link_from_email()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	app.session.logout()
	time.sleep(2)
	app.deposition.get_letter_from_email(login = "qaautomationsecr@yahoo.com", password = "fnasmhrlsacdmozz")
	assert app.deposition.compare_email_and_date(emails.email_secretary_cr_accept) #8 email
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)

#Test case 2.38
@allure.description("Test case 2.38")
@pytest.mark.parametrize("edit_price", edit_price, ids=[repr(i) for i in edit_price])
@pytest.mark.parametrize("prices", edit_price)
@pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
def test_2_38(app, edit_price, att, prices):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.change_price()
	app.deposition.confirm_appearance(att.email)
	app.cr_appear.check_prices_appearance(prices.minimum_transcript_charge, prices.page_cost, prices.expert_page_cost,
	prices.travel, prices.copy)
	app.edit_price.change_price(edit_price.appearance_fee, edit_price.page_cost,edit_price.expert_page_cost,
	edit_price.travel,edit_price.estimated,edit_price.turn_around_page,edit_price.copy,
	edit_price.cancellation_fee)
	app.edit_price.save()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)


#Test case 2.40
@allure.description("Test case 2.40")
@pytest.mark.skip("need fix from Anton side ")
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("op_unreg", op_unreg, ids=[repr(x) for x in op_unreg])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
def test_2_40(app, att, emails, deposition, op_unreg, op, cr_voting):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.regAttorney.add_op_unregister(deposition.sbn_op_unreg, op_unreg.sbn)
	app.deposition.begin_date_voting()
	app.session.logout()
	app.deposition.get_letter_from_email(login="qaautomationopunreg@yahoo.com", password="gvwdvmcqjriiwupp")
	#email 10 for op unregistered
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	#test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	app.deposition.get_link_from_email()
	app.deposition.login_attorney_voting(login_att="qaautomationatt@yahoo.com", password_att="ZXcv@123580")
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op_unreg.name,op_unreg.email,op_unreg.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	print(app.deposition.open_link_again())
	# app.cr_appear.past_deposition()
	# app.cr_appear.upload_transcript()
	# app.session.logout()
	# #download as op unregistered Test case 2.16
	# app.deposition.get_letter_from_email(login="qaautomationopunreg@yahoo.com", password="gvwdvmcqjriiwupp")
	# #email 22
	# app.deposition.get_link_from_email()
	#app.deposition.open_link_again()
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)
	app.cr_appear.delete_att_from_database()
