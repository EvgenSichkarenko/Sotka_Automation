class DepositonCase:
	def __init__(self, name=None, deponent=None,sbn_op=None, fake_deponent=None, fake_name_case=None, fake_name=None,
	sbn_op_unreg=None):
		self.name = name
		self.deponent = deponent
		self.sbn_op = sbn_op
		self.fake_deponent = fake_deponent
		self.fake_name_case = fake_name_case
		self.fake_name = fake_name
		self.sbn_op_unreg = sbn_op_unreg

	def __repr__(self):
		return "%s : %s;%s;%s" % (self.name, self.deponent, self.sbn_op, self.sbn_op_unreg )