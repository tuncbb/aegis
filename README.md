## Features

Aegis is a Royalty Shield solution developed by Thor Labs. Holder tracking is done using the holder verification and API also developed by Thor Labs. Royalty fee tracking is provided by the API developed by Helius Labs. If a royalty fee is not paid in a trade, it is detected by Aegis. It checks if the wallet holder is on the Thor Labs server and sends a message by tagging them on the public channel. Aegis updates the holder's NFT traits (off-chain) to restrict access to the holder-specific facilities of the server. The bot used in the monthly node subscription membership, also developed by Thor Labs, has been updated, allowing users to reactivate their NFTs by paying the royalty fee. Aegis has also been coded to allow the use of freeze authority (on-chain) if desired. Both sales and royalty data are stored as API using AWS S3 service. Thus, Renewal Bot accesses the royalty fee payment records and keeps accurate records. Thanks to the massive infrastructure of the project, it works very stably. At the same time, since we have access to holder information, we have the chance to warn people by tagging them. This gives a reminder to members who have forgotten to pay royalty fees.

![](https://cdn.discordapp.com/attachments/1016334190331035649/1050926818934407178/aegis_logo.png)

## Requirements
Python 3.8+
Helius Labs API Key
Thorify Verification Setup
AWS S3 Bucket and Key configuration
Discord Bot and Token
Update Authority(optional)

## Setup
Run `$ pip install -r /path/to/requirements.txt`
Edit `/settings/config.txt`
Run `python3 bot.py`

![](https://media.discordapp.net/attachments/1016334190331035649/1051625336460292176/image.png)

## Renewal Fee Collection
Renewal fees are collected by ThorNode Renewal Bot as seen below:

![](https://cdn.discordapp.com/attachments/1049652153062543380/1051604908765364224/image.png)

![](https://cdn.discordapp.com/attachments/1049652153062543380/1051605043649990766/image.png) 

![](https://cdn.discordapp.com/attachments/1049652153062543380/1051606611619233952/image.png)


