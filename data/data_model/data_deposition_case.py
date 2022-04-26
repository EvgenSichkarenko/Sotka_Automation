from model.model_deposition_case import DepositonCase
import datetime


full_name = f"Test_deposition" + datetime.datetime.now().strftime("%Y-%H-%M-%S")

#PREPROD
deposition = [DepositonCase(
    name= full_name,
    deponent="deponent",
	sbn_op1="256698",
	sbn_voting="256697"
),
]