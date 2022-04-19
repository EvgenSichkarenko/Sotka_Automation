from model.model_deposition_case import DepositonCase
import datetime


full_name = f"Test_deposition" + datetime.datetime.now().strftime("%Y-%H-%M-%S")

#DEV
deposition = [DepositonCase(
    name= full_name,
    deponent="deponent",
	sbn_op1="120037",
	sbn_voting="120038"
),
]


#PROD
# deposition = [DepositonCase(
#     name= full_name,
#     deponent="deponent",
# 	sbn_op1="256662",
# 	sbn_voting="256652"
# ),
# ]