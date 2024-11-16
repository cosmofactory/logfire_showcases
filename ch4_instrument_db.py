users = {
    1: {
        "dob": "1990-02-14",
        "status": "active",
        "first_name": "Philip",
        "last_name": "Fry",
        "email": "email@gmail.com",
        "role": "admin",
    },
    2: {
        "dob": "1998-07-01",
        "status": "inactive",
        "first_name": "Eric",
        "last_name": "Cartman",
        "email": "some@gmail.com",
        "role": "user",
    },
    3: {
        "dob": "1977-12-12",
        "status": "active",
        "first_name": "Peter",
        "last_name": "Griffin",
        "email": "another@gmail.com",
        "role": "user",
    },
}

permissions = {
    "admin": {
        "read": True,
        "write": True,
        "delete": True,
    },
    "user": {
        "read": True,
        "write": False,
        "delete": False,
    },
}
