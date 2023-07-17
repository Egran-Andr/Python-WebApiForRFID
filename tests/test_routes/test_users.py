import json

def test_read_main(client):
    data = {"Name": "string","Surname": "string","lastname": "string","birthdate": "2023-03-23","gender": 0,"photopath": "string"}
    response = client.post("/users/",json = data)
    assert response.status_code == 200 
    assert response.json()["birthdate"] == "2023-03-23"

def test_сreate_second_user(client):
    data = {"Name": "Name","Surname": "string","lastname": "string","birthdate": "2023-03-23","gender": 0,"photopath": "string"}
    response = client.post("/users/",json = data)
    assert response.status_code == 200 
    assert response.json()["birthdate"] == "2023-03-23"

def test_read_history_no_history(client):
    response = client.get("/users/gethistory/1")
    print(response.status_code)
    assert response.status_code == 404
    assert response.json()["detail"]== "History with this user id:1 does not exist" 

def test_user1_add_history_error(client):
    data = {"workerid": 1,"workplaceid": 1,"entertimestamp": "2023-03-24T12:06:39.201Z"}
    response = client.post("/users/historyadd/1",json = data)
    assert response.status_code == 404

def test_workplace_create(client):
    data = {"Name":"testname"}
    response = client.post("/workplace/",json = data)
    assert response.status_code == 200

def test_user1_add_history_after_workplace_create(client):
    data = {"workerid": 1,"workplaceid": 1,"entertimestamp": "2023-03-24T12:06:39.201Z"}
    response = client.post("/users/historyadd",json = data)
    assert response.status_code == 200

def test_get_all_users(client):
    response =client.get("/users/user/all")
    data = {"Name": "Name","Surname": "string","lastname": "string","birthdate": "2023-03-23","gender": 0,"photopath": "string"}
    client.post("/users/",json = data)
    lst = response.json()
    print(lst)
    assert len(lst) == 2

def test_read_history_clear(client):
    data = {"Name": "string","Surname": "string","lastname": "string","birthdate": "2023-03-23","gender": 0,"photopath": "string"}
    client.post("/users/",json = data)
    response = client.get("/users/gethistory/")
    print(response.status_code)
    assert response.status_code == 200