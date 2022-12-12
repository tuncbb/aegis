## Introduction

-------------

- Aegis is a Royalty Shield solution developed by Thor Labs. Holder tracking is done using the holder verification and API, also developed by Thor Labs. 
- Royalty fee tracking is provided by the API developed by Helius Labs. If a royalty fee is not paid in a trade, it is detected by Aegis. It checks if the wallet holder is on the Thor Labs server and sends a message by tagging them on the public channel. Aegis updates the holder's NFT traits (off-chain) to restrict access to the holder-specific facilities of the server.
- The bot used in the monthly node subscription membership, also developed by Thor Labs, has been updated to allow users to reactivate their NFTs by paying the royalty fee. Aegis has also been coded to allow the use of freeze authority (on-chain) if desired. Both sales and royalty data are stored as an API using AWS S3 service. Renewal Bot accesses the royalty fee payment records and keeps accurate records.
- Thanks to the massive infrastructure of the project, it works very stably. At the same time, since we have access to holder information, we have the chance to warn members by tagging them if they forget to pay royalty fees.

###
![](https://cdn.discordapp.com/attachments/1016334190331035649/1050926818934407178/aegis_logo.png)
###
## Requirements
- Python 3.8+ 
- Helius Labs API Key
- Thorify Verification Setup
- AWS S3 Bucket and Key configuration
- Discord Bot and Token
- Update Authority(optional)

## Setup

-------------
- Run:
  - `$ pip install -r /path/to/requirements.txt`
- Create a config file as seen in sample config:
  - `/settings/config.txt`
- Run:
  - `$ python3 bot.py`
  ###
![](https://media.discordapp.net/attachments/1016334190331035649/1051625336460292176/image.png)

## Royalty Fee Collection

-------------

Royalty fees are collected by ThorNode Renewal Bot as seen below:

![](https://cdn.discordapp.com/attachments/1049652153062543380/1051604908765364224/image.png)

![](https://cdn.discordapp.com/attachments/1049652153062543380/1051605043649990766/image.png) 

![](https://cdn.discordapp.com/attachments/1049652153062543380/1051606611619233952/image.png)

##
## Thorify: Discord <> NFT Holder Verification 

-------------

A discord and NFT verification system with full API, developed by Thor Labs.

It supports all Solana wallets and ledger. Creator can also add multiple collections trait based roles. Also best thing about Thorify is the verifications is taken in action immediately. Also with its powerful API, development projects and holder tracking are so easy to implement.

https://verify.thornode.io/

![](https://i.imgur.com/O1ed6zs.png)

Verification bot tracks changes and informs members for feedback. 

![](https://i.imgur.com/CZV9GAO.png)

### Verification API

-------------
An example function with its documentation to fetch holder info is given below. With API, creators can fetch any info they need from traits, by either using on-chain or off-chain metadata.



``` python
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
```

## Conclusion 

- With this solution, Thor Labs provides creators with the possibility to restrict utilities if royalty fees are not paid. If desired, NFTs can also be frozen, but this is not preferred by the community.
- Thanks to its fast, unique and customizable structure, Aegis provides a cheap and easy solution for creators to increase their royalty fee revenue yield.