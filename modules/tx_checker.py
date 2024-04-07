import asyncio
import random

from eth_typing import ChecksumAddress
from loguru import logger
<<<<<<< HEAD
<<<<<<< HEAD
from web3 import AsyncWeb3, AsyncHTTPProvider
from web3.middleware import async_geth_poa_middleware
from eth_account import Account as EthereumAccount
from tabulate import tabulate

from config import RPC
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
from web3 import AsyncWeb3
from eth_account import Account as EthereumAccount
from tabulate import tabulate
from web3.middleware import async_geth_poa_middleware

from config import ACCOUNTS, RPC
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944


async def get_nonce(address: ChecksumAddress):
    web3 = AsyncWeb3(
<<<<<<< HEAD
<<<<<<< HEAD
        AsyncHTTPProvider(random.choice(RPC["scroll"]["rpc"])),
=======
        AsyncWeb3.AsyncHTTPProvider(random.choice(RPC["base"]["rpc"])),
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
        AsyncWeb3.AsyncHTTPProvider(random.choice(RPC["base"]["rpc"])),
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
        middlewares=[async_geth_poa_middleware],
    )

    nonce = await web3.eth.get_transaction_count(address)

    return nonce


<<<<<<< HEAD
<<<<<<< HEAD
async def check_tx(wallets: list[str]):
=======
async def check_tx():
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
async def check_tx():
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    tasks = []

    logger.info("Start transaction checker")

<<<<<<< HEAD
<<<<<<< HEAD
    for _id, pk in enumerate(wallets, start=1):
=======
    for _id, pk in enumerate(ACCOUNTS, start=1):
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
    for _id, pk in enumerate(ACCOUNTS, start=1):
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
        account = EthereumAccount.from_key(pk)

        tasks.append(asyncio.create_task(get_nonce(account.address), name=account.address))

    await asyncio.gather(*tasks)

    table = [[k, i.get_name(), i.result()] for k, i in enumerate(tasks, start=1)]

    headers = ["#", "Address", "Nonce"]

    print(tabulate(table, headers, tablefmt="github"))
