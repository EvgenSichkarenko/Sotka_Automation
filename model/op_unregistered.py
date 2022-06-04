class OPUnregistered:
	def __init__(self, name=None, email=None, phone=None, sbn=None):
		self.name = name
		self.email = email
		self.phone = phone
		self.sbn = sbn

	def __repr__(self):
		return "%s : %s;%s" % (self.name, self.email, self.phone)