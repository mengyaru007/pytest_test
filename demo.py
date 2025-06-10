import requests

session = requests.Session()
authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTExMTE5NCwidHMiOiIzY2M1ZGZlMjcyYmEwZTQyIiwiaWF0IjoxNzQ5NTIxMTk0MjYxfQ.IYJjV-lM-yl5DhH0fs1xKCgTZFAaprhs72G3zeG5Ny0"
host = "api.apifox.com"
session.headers = {'Authorization': authorization, 'Host': host}
response = session.request("get", "https://api.apifox.com/api/v1/user-teams")
print(response.json())
session.headers.update({'Content-Type': None})
response = session.request("delete", "https://api.apifox.com/api/v1/teams/3565813")
print(response.json())