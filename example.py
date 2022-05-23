import requests
import json

url = "http://ec2-3-120-152-160.eu-central-1.compute.amazonaws.com:8080/graphql"
# url = "https://apidemo.trialbase.com/graphql"



headers = {
	"qatoken": "JEKA_QA_TEST_TOKEN"
}

#m = "mutation" + "{" + f" deleteDepositionCase(deposition_id: {get_id_deposition_case})" + "{status" + " message }" + "}"
data = "mutation{createFakeDepositionCase(withUnregisterOp: " + "WAITING_FOR_SERVICE" + "{status message} }"

data = {"query": data}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.json())