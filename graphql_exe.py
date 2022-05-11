import requests
import json

url = "https://apidemo.trialbase.com/graphql"

data_query = '''mutation{
  signIn(email:"testatt@inboxbear.com", password:"1234Qwer"){
    access_token
  }
}
'''
data = {"query": data_query}
#json_data = json.dumps(data)

response = requests.post(url, data=data)
response.raise_for_status()
api_token = response.json()['data']['signIn']['access_token']
print(api_token)


#GET ID deposition case
data_query2 = '''{
  getDepositionCasesByMonth(company_id:91, day:"05/11/2022"){
    id
    status
  }
}
'''
data = {"query": data_query2}
#json_data = json.dumps(data)

auth_header = 'Bearer ' + api_token

headers = {
	'Authorization': auth_header
}

response2 = requests.post(url,headers=headers, data=data )

print(response2.status_code)
list_response = response2.json()["data"]["getDepositionCasesByMonth"][0]
print(list_response["id"])


"""
get token from localStorage
wd.execute_script("return window.localStorage['token']")
"""
