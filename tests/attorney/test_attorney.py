import allure


"""add credit card"""
@allure.description("Add credit card to attorney company")
def test_add_card_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.att_credit.credit_card(card_number='4111111111111111', expiry_date='08/23', cvv='123')
	app.session.logout()

"""add new photo attorney"""
@allure.description("Change a photo in the attorney account" )
def test_add_photo_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	assert app.add_photo.add_photo()
	assert app.session.text_name_attribute_attroney() == "Joel William Meskin "
	app.session.logout()

"""test calendar attorney"""
@allure.description("Test, check deposition cases current day and shows all deposition")
def test_calendar_att(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	count_all = app.calendar_att.count()
	app.calendar_att.calendar_day()
	today_all = app.calendar_att.count()
	app.calendar_att.show_all_btn()
	assert today_all < count_all
	app.session.logout()

"""test search attorney"""
@allure.description("Test search attorney in a company")
def test_search_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.find_att.input(name="Lindsay")
	assert app.find_att.count() == 1
	app.session.logout()

