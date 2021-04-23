# Example to reproduce size limitation of the KeyCloak resource_set endpoint

## Description

With the setup descriped in this document and the script in this repostoriy, I want to demonstrate that a request to:
` GET http://<url>/auth/realms/<realm>/authz/protection/resource_set `, will only
display up to 100 resources even if more resources are registered.  

## Steps to reproduce

- run a fresh KeyCloak Server with the official docker image: `docker run -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin quay.io/keycloak/keycloak:12.0.4`
- Login to the admin console of the under `http://localhost8080` with user: "admin" and password "admin".
- create a new client
- change his access type to confidential
- enable authorization for this client
- add `http://localhost8080` to the valid redirect uris and save the client.
- go to the credentials tap of this client and copy the client id and client secret into the designated place in the ResourceCreationScript.py
- use the dockerfile to run the python script described in the following, or just install the requests requirements and run the python script with your local python installation.
  - run `docker build -t resource_set_example .`
  - run `docker run --network="host" resource_set_example`
- The script will post 120 resources to `http://localhost:8080/auth/realms/master/authz/protection/resource_set` and then perform a get request on `http://localhost:8080/auth/realms/master/authz/protection/resource_set`.
- the array should have an length of 120 but only 100 id's will be in the response. You can also now manually perform a GET request on the resource_set to verify that not all 120 resources are visible.

Note: to run the script multiple times you first need to delete all created resources.
