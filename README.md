## Table of contents
-  [API documentation](#api-docs)
    - [User/Register](#Register)
    - [User/Login](#Login)
    - [User/ConfirmPassword](#Confirm-password)
    - [User/GetUserPersonalData](#Get-user-personal-data)
    - [User/UpdateUserPersonalDataRequest](#Update-user-personal-data)
    - [User/UpdateUserPasswordRequest](#Update-user-password)
    - [User/UpdateUserEmailRequest](#Update-user-password)
    - [User/Delete](#User-delete)
    - [Avatars/GetAvatar](#Avatar)
    - [Avatars/GetRandomAvatar](#Random-avatar)
    - [Moods/GetMoods](#Moods)
    - [Records/Create a record](#Create-a-record)
    - [Records/Get a record](#Get-a-record)
    - [Records/Update a record](#Update-a-record)
    - [Records/Round statistics](#Round-statistics)
    - [Records/Tabular statistics](#Tabular-statistics)
    - [Records/Data deletion](#Data-deletion)


<a name="api-docs"/></a>
## API documentation
<a name="Register"/></a>
### User/Register
Register a new user account.
#### Method: POST
Endpoint: user/register

Request Body:
```js
{
    "username": "string",
    "email": "user@example.com",
    "birthdate": "20.12.2000",
    "password": "string",
    "registrationDate" : "21.04.2023"
}
```
Response: None

---
<a name="Login"/></a>
### User/Login
Authenticate a user and return a token.
#### Method: POST
Endpoint: user/login

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
<a name="Confirm-password"/></a>
### User/ConfirmPassword
Confirm user password
#### Method: POST
Endpoint: user/confirmPassword

Request Body:
```js
{
    "username": "string",
    "password": "string"
}
```

Response: None

---
<a name="Get-user-personal-data"/></a>
### User/Get user personal data
#### Method: GET
Endpoint: user/getPersonalData

Request header:
```js
{
  "token": "string"
}
```

Request Body:
None

Response:
```js
{
  "Username": "string",
  "FirstName": "string",
  "LastName": "string",
  "Birthdate": "20.12.2000",
  "Sex": "string"
}
```

---
<a name="Update-user-personal-data"/></a>
### User/Update user personal data
#### Method: PUT
Endpoint: user/updateUserPersonalDataRequest

Request header:
```js
{
  "token": "string"
}
```

Request Body:
```js
{
  "newUsername": "string",
  "newFirstName": "string",
  "newLastName": "string",
  "newBirthdate": "20.12.2000",
  "newSex": "string"
}
```

Response: None

---
<a name="Update-user-password"/></a>
### User/Update user password
#### Method: PUT
Endpoint: user/updateUserPasswordRequest

Request header:
```js
{
  "token": "string"
}
```

Request Body:
```js
{
  "newPassword": "string",
  "newPassword": "string",
}
```

Response: None

---
<a name="Update-user-email"/></a>
### User/Update user email
#### Method: PUT
Endpoint: user/updateUserEmailRequest

Request header:
```js
{
  "token": "string"
}
```

Request Body:
```js
{
  "newEmail": "string",
}
```

Response: None

---
<a name="User-delete"/></a>
### User deletion
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
<a name="Header"/></a>
### Avatars/Get Avatar
Get user's avatar and username.
#### Method: GET
Endpoint: user/header

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
  username: "some Tom"
}

```

---
<a name="Random-avatar"/></a>
### Avatars/Get random Avatar and save
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

<a name="Moods"/></a>
### Moods/GetMoods
Get available moods.
#### Method: GET
Endpoint: /moods

Response:

```js
{
    "moods": [
        {
            "mood_id": "1",
            "image": "https://i.imgur.com/aidyse5.png"
        },
        {
            "mood_id": "2",
            "image": "https://i.imgur.com/whXdVTH.png"
        },
        ...
    ]
}
```
---

<a name="Get-a-record"/></a>
### Records/Get a record
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
    "text": "string".
    "date": "12.16.2023"
}
```

---
<a name="Create-a-record"/></a>
### Records/Create a record
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
    "mood_id": "int",
    "text": "string",
    "date": "29.04.2023"
}
```

Response: None

---
<a name="Update-a-record"/></a>
### Records/Update a record
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
    "newMood_id": "int",
    "newText": "string",
    "date": "21.01.2023"
}
```

Response: None

---
<a name="Round-statistics"/></a>
### Records/Round statistics
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
      "Image": "https://i.imgur.com/1.jpeg",
      "count": "12"
    },
    {
      "Image": "https://i.imgur.com/2.jpeg",
      "count": "2"
    },
    {
      "Image": "https://i.imgur.com/3.jpeg",
      "count": "3"
    },
    {
      "Image": "https://i.imgur.com/4.jpeg",
      "count": "10"
    },
    {
      "Image": "https://i.imgur.com/5.jpeg",
      "count": "4"
    }
  ]
}
```

---
<a name="Tabular-statistics"/></a>
### Records/Tabular statistics
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
           "points": "1"
         },
         {
           "date": "02.04.2023",
           "points": "5"
         },         
      ],
}
```

---
<a name="Data-deletion"/></a>
### Records/Data all records
#### Method: DELETE
Endpoint: records/delete

Request header:
```js
{
  "token": "string"
}
```
Response: None
