from brownie import FundMe
from scripts.helpful_scripts import get_account, get_priceFeed_address, get_verify


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract
    price_feed_address = get_priceFeed_address(account)
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=get_verify(),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()



