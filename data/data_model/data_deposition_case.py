from model.model_deposition_case import DepositonCase
import datetime


full_name = f"Test_deposition" + datetime.datetime.now().strftime("%Y-%H-%M-%S")

#PREPROD
deposition = [DepositonCase(
    name= full_name,
    deponent="deponent",
	sbn_op="000002"
),
]