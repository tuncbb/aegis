import requests
from settings.config import verify_token


def infoid(arg):
    """ id: String - User's Discord ID (optional)
        address: String - User's Wallet Address (optional)
    response:
[
    {
    "success": true,
    "data": {
        "name": "Test#2040",
        "id": "504943583723061279",
        "picture": "https://discord.com/assets/6f26ddd1bf59740c536d2274bb834a05.png",
        "adress": "9qpSts1qJeWLyRDBnESE9d54N61v8or9kWWtTUKPU4RA",
        "tokens": {
            "count": 1,
            "passes": ["Elite"]
        }
    }
}
{
    "success": false,
    "error": "Couldn't find any user with that id"
}
] """
    header = {
        "token": verify_token,
    }
    r = requests.get("https://verify.thornode.io/api/getuser/?id={}".format(arg), headers=header)
    # print(r.json())
    return r.json()


def infowallet(arg):
    """ id: String - User's Discord ID (optional)
        address: String - User's Wallet Address (optional)
    response:
[
    {
    "success": true,
    "data": {
        "name": "Test#2040",
        "id": "504943583723061279",
        "picture": "https://discord.com/assets/6f26ddd1bf59740c536d2274bb834a05.png",
        "adress": "9qpSts1qJeWLyRDBnESE9d54N61v8or9kWWtTUKPU4RA",
        "tokens": {
            "count": 1,
            "passes": ["Elite"]
        }
    }
}
{
    "success": false,
    "error": "Couldn't find any user with that id"
}
] """
    header = {
        "token": verify_token,
    }
    r = requests.get("https://verify.thornode.io/api/getuser/?address={}".format(arg), headers=header)
    return r.json()


def getusers():
    """ Fetch all users info in discord server.
    response:
[
    {
    "success": Bool (true or false),
    "data": Array (of user Objects),
    "error": String
}
{
    "success": false,
    "error": "Invalid token"
}
] """
    header = {
        "token": verify_token,
    }
    r = requests.get("https://verify.thornode.io/api/getusers", headers=header)
    return r.json()
