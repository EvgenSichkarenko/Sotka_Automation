import requests
import json

# url = "http://ec2-3-120-152-160.eu-central-1.compute.amazonaws.com:8080/graphql"
# # url = "https://apidemo.trialbase.com/graphql"
#
# #Login, Get access token
# qu = """mutation{signIn(email:"qaautomationatt@yahoo.com", password:"ZXcv@123580" ){
#   access_token
# }
#
# }"""
# data = {"query": qu}
# response = requests.post(url, data=data)
# access_token = response.json()["data"]["signIn"]["access_token"]
# print(access_token)
#Create deposition
# auth_header = 'Bearer ' + access_token
# headers = {
# 	"Authorization": auth_header,
# 	"qatoken": "JEKA_QA_TEST_TOKEN"
# }
#
# data1 = 'mutation{createFakeDepositionCase(status:"WAITING_FOR_SERVICE", withUnregisterOp:false)}'
# #data1 = 'mutation{createFakeDepositionCase(status:"WAITING_FOR_NEGOTIATION", withUnregisterOp:false)}'
# data2 = {"query": data1}
#
# response = requests.post(url, headers=headers, data=data2)
# print(response.status_code)
# print(response.json()["data"]["createFakeDepositionCase"])
status = "false"

#date_time = ["2022-06-13 10:00:00.000000", "2022-06-14 10:00:00.000000", "2022-06-15 10:00:00.000000",
	#"2022-06-16 10:00:00.000000"]
date_time = '["2022-06-13 10:00:00.000000"]'

data1 = 'mutation{createFakeDepositionCase(status:"WAITING_FOR_NEGOTIATION",' + f"withUnregisterOp:{status}," + \
		f'dates:{date_time})' + "{id start_time}}"

print(data1)