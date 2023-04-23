## Table of contents
-  [API documentation](#api-docs)
    - [Register](#Register)
    - [Login](#Login)
    - [Avatar](#Avatar)
    - [Create a record](#Create-a-record)
    - [Get a record](#Get-a-record)
    - [Update a record](#Update-a-record)
    - [Update user data](#Update-user-data)
    - [Data deletion](#Data-deletion)
    - [Get record for a specific date](#Get-record-for-a-specific-date)
    - [Round statistics](#Round-statistics)
    - [Tabular statistics](#Tabular-statistics)

<a name="api-docs"/></a>
## API documentation
<a name="Register"/></a>
### Register
Register a new user account.
#### Method: POST
Endpoint: /register

Request Body:
```js
{
    "email": "user@example.com",
    "password": "string",
    "username": "string",
    "birthdate": "20.12.2000",
    "registrationDate" : "21.04.2023"
}
```
Response: None

---
<a name="Login"/></a>
### Login
Authenticate a user and return a token.
#### Method: POST
Endpoint: /login

Request Body:
```js
{
    "username": "string",
    "password": "string"
}
```

Response:

```js
{
    "token": "string"
}
```

---
<a name="Avatar"/></a>
### Avatar
Get user's avatar.
#### Method: GET
Endpoint: /avatar

Request Header:

```js
{
    "token": "string"
}
```

Response:

```js
{
  avatar: "https://i.imgur.com/dWtx5mc.jpeg"
}

```

---

<a name="Get-a-record"/></a>
### Get a record
Get a mood record.
#### Method: GET
Endpoint: /record

Request Header:

```js
{
    "token": "string"
}
```

Request Body:
```js
{
    "date": "20.09.2023",
}
```

Response:
```js
{
    "emoji": "https://i.imgur.com/1.jpeg",
    "text": "string"
}
```

---
<a name="Create-a-record"/></a>
### Create a record
Add a new mood record.
#### Method: POST
Endpoint: /record

Request Header:

```js
{
    "token": "string"
}
```

Request Body:
```js
{
    "mood": "string",
    "text": "string"
}
```

Response:
```js
{
    "emojis": ["https://i.imgur.com/1.jpeg", "https://i.imgur.com/2.jpeg", ...]
}
```

---
<a name="Update-a-record"/></a>
### Update a record
Update an existing mood record.
#### Method: PUT
Endpoint: /record

Request Header:
```js
{
    "token": "string"
}
```

Request Body:
```js
{
    "newEmoji": "https://i.imgur.com/1.jpeg",
    "newText": "string",
    "date": "21.01.2023"
}
```

Response: None

---
<a name="Update-user-data"/></a>
### Update user data
#### Method: PUT
Endpoint: /settings

Request header:
```js

{
  "token": "string"
}
```

Request Body:
```js

{
  "newEmail": "user@example.com",
  "newPassword": "string",
  "newUsername": "string",
  "newBirthdate": "20.12.2000",
  "newFirstName": "string",
  "newSecondName": "string",
  "newGender": "string"
}
```

Response: None

---
<a name="Data-deletion"/></a>
### Data deletion
#### Method: DELETE
Endpoint: /settings

Request header:
```js
{
  "token": "string"
}
```
Response: None

---
<a name="Get-record-for-a-specific-date"/></a>
### Get record for a specific date
#### Method: GET
Endpoint: /calendar

Request header:
```js

{
  "token": "string"
}
```

Request body:
```js
{
  "date": "21.01.2023"
}
```

Response:
```js
{
  "emoji": "https://i.imgur.com/1.jpeg",
  "text": "string",
  "date": "21.01.2023"
}
```

---
<a name="Round-statistics"/></a>
### Round statistics
#### Method: GET
Endpoint: /statistics/round

Request header:
```js
{
  "token": "string"
}
```

Request body:
```js
{
  "month": "4",
  "year": "2023"
}
```

Response:
```js
{
  "statistics": [
    {
      "id": "1",
      "name": "Extremely happy",
      "count": "12"
    },
    {
      "id": "2",
      "name": "Happy",
      "count": "2"
    },
    {
      "id": "3",
      "name": "Neutral",
      "count": "3"
    },
    {
      "id": "4",
      "name": "Sad",
      "count": "10"
    },
    {
      "id": "5",
      "name": "Extremely sad",
      "count": "4"
    }
  ]
}
```

---
<a name="Tabular-statistics"/></a>
### Tabular statistics
#### Method: GET
Endpoint: /statistics/table

Request header:
```js
{
  "token": "string"
}
```

Request body:
```js
{
  "month": "4",
  "year": "2023"
} 
```

Response:
```js
{
 "statistics": [    
         {
           "date": "01.04.2023",
           "name": "Happy",
           "image": "https://i.imgur.com/6ogcyVF.png"
         },
         {
           "date": "02.04.2023",
           "name": "Excited",
           "image": "https://i.imgur.com/6ogcyVF.png"
         },         
      ],
}
```
