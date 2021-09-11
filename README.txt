API Information

Get a list of existing users
GET http://127.0.0.1:8000/api/all_users

Create a new user:
POST http://127.0.0.1:8000/api/all_users    required fields = username,  password

Get authentication token
POST http://127.0.0.1:8000/api/auth/    required fields = username,  password

View user information:
GET http://127.0.0.1:8000/api/all_users/id (authentication token required)

Modify user information:
PATCH http://127.0.0.1:8000/api/all_users/id (authentication token required)

Delete user:
DELETE http://127.0.0.1:8000/api/all_users/id (authentication token required)

Get a list of existing groups :
GET http://127.0.0.1:8000/api/all_groups (authentication token required)

Create group:
POST http://127.0.0.1:8000/api/all_groups/	required fields = group_name, group_description (authentication token required)

Modify group information:
PATCH http://127.0.0.1:8000/api/all_groups/id/ (authentication token required)

Delete group:
DELETE  http://127.0.0.1:8000/api/all_groups/id/ (authentication token required)