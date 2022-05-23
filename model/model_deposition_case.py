class DepositonCase:
	def __init__(self, name=None, deponent=None,sbn_op=None):
		self.name = name
		self.deponent = deponent
		self.sbn_op = sbn_op

	def __repr__(self):
		return "%s : %s;%s" % (self.name, self.deponent, self.sbn_op, )