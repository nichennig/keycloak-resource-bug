import requests

########################################################################################
#                                                                                      #
#  Change the following values as described in the README                              #
#                                                                                      #
########################################################################################
client_id = "<client id of the created Keycloak client>"
client_secret = "<client secret>"
########################################################################################

token_endpoint = "http://localhost:8080/auth/realms/master/protocol/openid-connect/token"

body = {
    'grant_type':'client_credentials',
    'client_id':client_id,
    'client_secret':client_secret
}
  
result = requests.post(url = token_endpoint, data = body)
  
data = result.json()
token = data['access_token']
resource_set = "http://localhost:8080/auth/realms/master/authz/protection/resource_set"
headers = {
    'Authorization': 'Bearer '+token,
    'Content-Type': 'application/json',
    'Host': 'localhost:8080'
    }

print("------------------------------------------------------------------------------------\n")
print("Post resources to "+resource_set+"\n")
print("------------------------------------------------------------------------------------\n")
for i in range(120):
    resource_name = 'Resource'+str(i)
    body = {
        'name':resource_name,
    }
    r= requests.post(url=resource_set,json=body,headers=headers)
    print(r.json())
print("------------------------------------------------------------------------------------\n")
print("End of resource creation \n")
print("------------------------------------------------------------------------------------\n")
print("Get all resources from  "+resource_set+"\n")
print("------------------------------------------------------------------------------------\n")
r = requests.get(url=resource_set,headers=headers)
data = r.json()
print(data)
print("array length:`" + str(len(data)))
