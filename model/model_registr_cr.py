class ModelRegistrCR:
	def __init__(self, cr_bar_numbe=None, cr_email=None,
			cr_phone_number=None, cr_full_name=None, cr_issuance_date=None,
			cr_expiration_date=None, cr_address_one=None, cr_address_two=None, cr_valid_password=None):
		self.bar_number = cr_bar_numbe
		self.email = cr_email
		self.phone_number = cr_phone_number
		self.full_name = cr_full_name
		self.issuance = cr_issuance_date
		self.expiration_data = cr_expiration_date
		self.address_one = cr_address_one
		self.addres_two = cr_address_two
		self.valid_password = cr_valid_password

