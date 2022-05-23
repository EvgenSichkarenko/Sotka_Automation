class Attorneys:
	def __init__(self, name=None, email=None, phone=None):
		self.name = name
		self.email = email
		self.phone = phone

	def __repr__(self):
		return "%s : %s;%s" % (self.name, self.email, self.phone)