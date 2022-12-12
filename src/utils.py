import json
from urllib.request import urlopen
import urllib
import requests
from src import thor_api
from settings import config
from src.decorators import retry


def log_royalty(nft, tx, amount, status):
    with open("./logs/royalty", "a") as f:
        f.write(f"{nft},{tx},{amount},{status}\n")
        f.close()
    return


def log_sale(sign):
    with open("./logs/sales", "a") as f:
        f.write(f"{sign}\n")
        f.close()
    return


def check_sales(sign):
    url = f"{config.bucket_url}{config.sales_json}"
    request = requests.get(url).json()
    if sign in request['transactions']:
        print("Old Sale, Skipping...")
        return False  # old sale
    else:
        return True  # new sale


@retry(Exception, tries=10)
def helius(mint, api_key):
    try:
        url2 = f"https://api.helius.xyz/v0/addresses/{mint}/transactions?api-key={api_key}&commitment=confirmed&type=NFT_SALE"
        request = requests.get(url2).json()[0]
        return request
    except:
        pass


@retry(Exception, tries=10)
def token_owner(token):
    url = f"https://api-mainnet.magiceden.io/v2/tokens/{token}"

    request = urllib.request.Request(url, headers=config.headers)
    response = urllib.request.urlopen(request)
    meta_data = json.load(response)
    owner = meta_data['owner']
    return owner


def get_discord_id(w):
    """

    :param str w:
    :return: Discord id or Wallet
    """
    if thor_api.infowallet(w)['success']:
        discord_id = thor_api.infowallet(w)['data']['id']
        return f"<@{discord_id}>"  # if user is verified, return discord id
    else:
        return w  # if user is not verified, return wallet only


def check_royalty(sample):
    """

    :param sample: Helius API NFT Event json
    :return: Array
            **[0] - String. Royalty status message
            **[1] - Boolean. If royalty paid, True else False
            **[2] - Integer. Pending royalty fee in $SOL

    """
    # global full_royalty, paid_royalty
    buyprice = float("{:.3}".format(float(sample['events']['nft']['amount'] / 1000000000)))
    A = []
    for tr in sample['nativeTransfers']:
        A.append(tr['toUserAccount'])
    if config.creator in A:
        i = A.index(config.creator)
        paid_royalty = float("{:.3f}".format(float(sample['nativeTransfers'][i]['amount']) / 1000000000))
    else:
        paid_royalty = 0
    full_royalty = buyprice / 10
    if paid_royalty > full_royalty * 0.99:
        return "Full royalty is paid", True, 0
    else:
        ratio = paid_royalty / full_royalty  # calculate royalty ratio
        pending = "{:.3f}".format(full_royalty - paid_royalty)  # pending amount
        ratio_str = "{:.0%}".format(ratio)
        buyer = get_discord_id(token_owner(sample['events']['nft']['nfts'][0]['mint']))
        string = f"Hey {buyer}! \n" \
                 f"You paid **{ratio_str}** of royalty fee on your purchase.Therefore your access to the nodes is restricted.\n " \
                 f"**Pay full royalty** using <@{config.bot_id}> bot.\n Pending fee: **{pending} $SOL** "
        return string, False, pending


def post_sale_msg(sample):
    sample = sample['description'].split(" ")
    seller = get_discord_id(sample[0])
    nft = sample[3]
    buyer = get_discord_id(sample[5])
    price = sample[7]
    market = sample[10]

    msg = f"{seller} sold ThorNode {nft} to {buyer} for {price} $SOL on {market}"

    return msg
