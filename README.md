# Python-WebApiForRFID
This is an repository for Web APi for C# RFID-Reader App

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites

What things you need to install the software and how to install them



```
pip3 install requirements.txt
```
Connect server to db by creating .env file in root foulder and configuring it in format:

```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=YOUR_PASSWORD
POSTGRES_SERVER=SERVER
POSTGRES_PORT=YOUR_PORT
POSTGRES_DB=YOUR_DATABASENAME
```

### Installing

A step by step series of examples that tell you how to get a development env running

```
git clone https://github.com/Egran-Andr/Python-WebApiForRFID cd 
```

## Database Structure
![image](https://github.com/user-attachments/assets/dad9e1f4-5d4c-41d4-9d2b-0f4daee9b07b)

## Api-Commands
| Command  | Type | Description |
| ------------- | ------------- | ------------- |
| /balance/ | POST  | Get user balance|
| /balance/update/{id}/{balance} | PUT  | Update user balance  |
| /balance/all | GET  | Get list of all users balances |
| /balance/by_id | GET  | Get balance by user id |
| /users/ | POST  | Create new employee in database |
| /users/historyadd | POST  | Create new employee timestamp |
| /users/cardconnect | POST  | Create new card ID for employee |
| /users/upload_image | POST  | Upload user photo to server |
| /users/image | GET  | Get user image from server |
| /users/gethistory/{id} | GET | Load user work history.{id} optional,will filter by id. If none -> return all users history  |
| /users/user/all | GET | Get list of all users  |
| /users/cardlist/ | GET | get Dict of all card unique IDs {"{user id}":{card id}} |
| /users/gethistory/{datebegin}/{dateend} | GET | get user history. Optional:filter by date |
| /users/update/{id} | PUT | Update user info |
| /users/delete/{id} | DELETE | Delete user |
| /userworkpace/ | POST | Connect user to work division |
| /userworkpace/update/{id}/{workplaceid} | PUT | Update user division |
| /userworkpace/{id} | GET | Get user division |
| /workplace/ | POST | Create new division |
| /workplace/all | GET | Get list of all divisions |
