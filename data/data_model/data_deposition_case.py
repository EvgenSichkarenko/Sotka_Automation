from model.model_deposition_case import DepositonCase
import datetime


full_name = f"Test_deposition" + datetime.datetime.now().strftime("%Y-%H-%M-%S")

#PREPROD
deposition = [DepositonCase(
    name= full_name,
	fake_name = "Jeka Test Qa",
	fake_name_case = "JEKA_AUTOMATION_TEST_DEPOSITION",
    deponent="deponent",
	fake_deponent = "JEKA_AUTO_DEP",
	sbn_op="000002",
	sbn_op_unreg="000003"
),
]