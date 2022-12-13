import boto3
import json
from settings import config


class s3Bucket:

    def __init__(self, NFTid=None, Expired=None, Image=None, Sign=None, S3Key=None, NFTEvent=None):
        """
        Requires AWS CLI Confing and .aws folder in project file.
        :return: __init__ should return True
            :param int NFTid: ID number of NFT
            :param str Expired: True, False or Pending Royalty
            :param str Image: slug of image in bucket url.e.g:"royalty.gif"
            :param str Sign: Signature of Transaction"
            :param str S3Key: S3 file path
            :param dict NFTEvent: {id,tx,status,pending}
        """
        self.id = NFTid
        self.Expired = Expired
        self.Image = Image
        self.Sign = Sign
        self.s3_key = S3Key  # s3 folder/file.json
        self.s3_client = boto3.client('s3')
        self.s3_object = self.s3_client.get_object(Bucket=config.bucket_name, Key=self.s3_key)
        self.NFTEvent = NFTEvent

    def UpdateTrait(self):
        """AWS S3 Update Method
        Inputs: nft_id,Expired, Image
        returns: True """

        nft_id = int(self.id)
        if 43 > nft_id > 10:
            pass_type = "elite"
            json_id = nft_id - 10
        elif 344 > nft_id >= 43:
            pass_type = "classic"
            json_id = nft_id - 44
        else:
            return True

        s3_key = "{}/{}.json".format(pass_type, json_id)
        # read the file
        s3_object = self.s3_client.get_object(Bucket=config.bucket_name, Key=s3_key)
        data = json.loads(s3_object['Body'].read().decode('utf-8'))
        print("DEBUG", data)
        # change in json file
        data['attributes'][1]['value'] = self.Expired
        data['image'] = f"{config.bucket_url}{self.Image}"
        # push to s3 bucket
        self.s3_client.put_object(Body=json.dumps(data), Bucket=config.bucket_name, Key=s3_key, ContentType="application/json")
        return True

    def UpdateSale(self):
        """Update sales or royalties on AWS S3"""
        data = json.loads(self.s3_object['Body'].read().decode('utf-8'))
        if self.Sign is not None and self.NFTEvent is not None:
            print('Error: Both Sign and NFTEvent cannot be used as input.')
            return False
        elif self.Sign is not None:
            data['transactions'].append(self.Sign)
        elif self.NFTEvent is not None:
            event = self.NFTEvent
            data[event['id']] = {'tx': event['tx'], 'status': event['status'], 'pending': event['pending']}
        self.s3_client.put_object(Body=json.dumps(data), Bucket=config.bucket_name, Key=self.s3_key,
                                  ContentType="application/json")
        return True
