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
![](https://i.imgur.com/u1Yt42w.png)
##
![](https://i.imgur.com/Aq3OlH8.png)

## Royalty Fee Collection

-------------

- Royalty fees are collected by ThorNode Renewal Bot. Beta version can be seen below:
- Thanks to verification API and newly deployed royalty record API of Aegis, the bot can fetch NFT's owner with royalty dept. Note that the bot shows only the NFTs that concern the holder. 
- [Royalty API](https://thornode-metadata.s3.us-west-1.amazonaws.com/royalty.json) to track depts and payments.
- [Sales API](https://thornode-metadata.s3.us-west-1.amazonaws.com/sales.json) to track sales and prevents double records.
- Therefore, member do not need to check mint address, and it also prevents mistakes from being made. As such, the system provides great ease of use. 
- The bot updates the related Royalty API record to "True" if transaction input returns "True". Then NFT's traits are updated and member gets holder role again.
- With Royalty API of Aegis, many applications can be developed to keep royalty statistics such as royalty payment percentage. 

![](https://cdn.discordapp.com/attachments/1049652153062543380/1051604908765364224/image.png)

![](https://cdn.discordapp.com/attachments/1049652153062543380/1051605043649990766/image.png) 

![](https://cdn.discordapp.com/attachments/1049652153062543380/1051606611619233952/image.png)

##
## Thorify: Discord <> NFT Holder Verification 

-------------

- A discord and NFT verification system with full API, developed by Thor Labs.

- It supports all Solana wallets and ledger. Creator can also add multiple collections trait based roles. Also best thing about Thorify is the verifications is taken in action immediately. Also with its powerful API, development projects and holder tracking are so easy to implement.

- https://verify.thornode.io/
- https://discord.gg/thorlabs

![](https://i.imgur.com/O1ed6zs.png)

- Verification bot tracks changes and informs members for feedback. 

![](https://i.imgur.com/CZV9GAO.png)

### Verification API

-------------
- An example function with its documentation to fetch holder info is given below. With API, creators can fetch any info they need from traits, by either using on-chain or off-chain metadata. 
- It is so rare to find a verification tool which provides an API with it. None of the most popular tools do not provide any solution with API. This makes Thor Labs' solution unique relatively. In addition to ease of use, it also facilitates customization.



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
## Helius API Integration

- Thanks to Helius Labs, API integration is done by a simple request function (under `src/utils.py`) as seen below. NFT_SALE request is used to fetch sale data to see if royalty fee is paid or not. Request data returns to `handler.py` and `handler.py` calls some other functions in `utils.py` to compare sale records in Aegis API.
- Webhook integration is also being developed right now for less API credit consumption, using AWS Lambda.

``` python
def helius(mint, api_key):
    try:
        url2 = f"https://api.helius.xyz/v0/addresses/{mint}/transactions?api-key={api_key}&commitment=confirmed&type=NFT_SALE"
        request = requests.get(url2).json()[0]
        return request
    except:
        pass
```
### Webhook:

- Using webhook service of Helius Labs is more cost efficient. Therefore, an AWS Lambda function is used to listen webhook event and pushes the NFT_Sale data to Aegis API. Thus, only last events are fetched and Aegis handler checks last returns. If any new entry is in the API, the royalty shield process runs. 

- AWS lambda function:

``` python
import json,aws,config
def lambda_handler(event, context):
    data={}
    raw_data = json.loads(event['body'])[0] # load helius raw data as json
    data[raw_data['signature']]=raw_data # add it into a dict with signature key
    aws.s3Bucket(S3Key=config.sales_json, Sign=data).UpdateSale() # push to AWS S3
    return {
        'statusCode': 200,
        'transactions': True
    }
```
- Return:
https://thornode-metadata.s3.us-west-1.amazonaws.com/test.json

## Conclusion 

- With this solution, Thor Labs provides creators with the possibility to restrict utilities they offer if royalty fees are not paid. If desired, NFTs can also be frozen, but this is not preferred by the community.
- Thanks to its fast, unique and customizable structure, Aegis:Royalty Shield provides a cheap and easy solution for creators to increase their royalty fee revenue yield.

### Contact 
- Discord: Muhtar 【Ø】 ThorNode#1857
- Twitter: @KriptoMuhtar
