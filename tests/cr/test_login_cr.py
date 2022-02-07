

def test_login_cr(app):
	app.login.login(invalid_login="a13", invalid_password="13",
		valid_login="crdev@givmail.com", valid_password="1234Qwer")
	assert app.session.text_name_attribute_cr() == "Евгений Сичкаренко"


"""add new photo cr"""
def test_add_photo_cr(app):
	app.session.login(login="crdev@givmail.com", password="1234Qwer")
	app.add_photo.add_photo()
	assert app.session.text_name_attribute_cr() == "Евгений Сичкаренко"
	app.session.logout()
