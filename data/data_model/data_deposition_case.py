from model.model_deposition_case import DepositonCase
import datetime


full_name = f"Test_deposition" + datetime.datetime.now().strftime("%Y-%H-%M-%S")

deposition = [DepositonCase(
    name= full_name,
	#name= "Test_deposition2022-10-30-20",
    deponent="deponent",
	date='11/16/2021',
	attorney='Mark John Decastro SBN #123456',
	address="848 N Rainbow Blvd, # 4544, Las Vegas, NV 89107-1103",
	email="a1@tafmail.com",
	sbn="SBN#123456",
	sbn_op1="120037",
	sbn_voting="120038"
),
]


