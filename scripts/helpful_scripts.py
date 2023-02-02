from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3


FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]  # import account from local ganache
    else:
        return accounts.add(config["wallets"]["from_key"])  # import from config file


def get_priceFeed_address(account):
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]  # import from config file
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")
        if (
            len(MockV3Aggregator) <= 0
        ):  # MockV3Aggregator is a list of all the contracts deployed
            MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})
            # Web3.toWei(STARTING_PRICE, "ether")
        print("Mocks Deployed!")
        return MockV3Aggregator[-1].address


def get_verify():  # verify a contract in ethereum by pushing the code. Only works in Real networks
    return config["networks"][network.show_active()].get(
        "verify"
    )  # .get returns none rather than index error if verify is not entered in config

