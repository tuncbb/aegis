from src import utils, aws
from settings import config


def handler(mint):
    result = utils.helius(mint, config.helius_key)
    print(result)
    if result is not None and result['type'] == "NFT_SALE":
        nft_id = result['description'].split(" ")[3].replace('#', '')
        sign = result['signature']
        if utils.check_sales(result['signature']):
            aws.s3Bucket(Sign=sign, S3Key=config.sales_json).UpdateSale()
            royalty = utils.check_royalty(result)
            print('ROYALTY', royalty)
            utils.log_sale(sign)
            utils.log_royalty(nft_id, sign, royalty[1], royalty[2])
            event = {'id': nft_id, 'tx': sign, 'status': royalty[1], 'pending': royalty[2]}
            print("EVENT", event)
            aws.s3Bucket(S3Key=config.royalty_json, NFTEvent=event).UpdateSale()
            string = royalty[0]
            title = f"Aegis Activated for ThorNode #{nft_id} "
            if royalty[1]:
                return False, False  # royalty
            if not royalty[1]:
                aws.s3Bucket(S3Key=config.royalty_json,NFTid=nft_id,Expired="Pending Royalty", Image="aegis.png").UpdateTrait()
                return title, string
