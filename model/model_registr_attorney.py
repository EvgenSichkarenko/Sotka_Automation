class ModelRegisrtAttorney:
	def __init__(self, bar_number=None, email=None, password=None, valid_password=None, invalid_password=None,
			password_match=None, name_secretary= None, email_secretary=None, phone_number=None, address_two=None ):
		self.bar_number = bar_number
		self.email = email
		self.password = password
		self.valid_password = valid_password
		self.invalid_password = invalid_password
		self.password_match = password_match
		self.name_secretary = name_secretary
		self.email_secretary = email_secretary
		self.phone_number = phone_number
		self.address_two = address_two

	def __repr__(self):
		return "%s : %s;%s;%s;%s;%s;%s;%s" % (self.bar_number, self.email, self.password,
		self.valid_password, self.invalid_password, self.password_match, self.phone_number, self.address_two)