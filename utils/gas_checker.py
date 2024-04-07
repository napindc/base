import asyncio
<<<<<<< HEAD
import time
import random

from web3 import Web3
from web3.eth import AsyncEth
=======
import random

from web3 import AsyncWeb3
from web3.middleware import async_geth_poa_middleware
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

from config import RPC
from settings import CHECK_GWEI, MAX_GWEI
from loguru import logger


async def get_gas():
    try:
<<<<<<< HEAD
        w3 = Web3(
            Web3.AsyncHTTPProvider(random.choice(RPC["ethereum"]["rpc"])),
            modules={"eth": (AsyncEth,)},
        )
        gas_price = await w3.eth.gas_price
        gwei = w3.from_wei(gas_price, 'gwei')
=======
        w3 = AsyncWeb3(
            AsyncWeb3.AsyncHTTPProvider(random.choice(RPC["ethereum"]["rpc"])),
            middlewares=[async_geth_poa_middleware],
        )

        gas_price = await w3.eth.gas_price
        gwei = w3.from_wei(gas_price, 'gwei')

>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
        return gwei
    except Exception as error:
        logger.error(error)


async def wait_gas():
    logger.info("Get GWEI")
    while True:
        gas = await get_gas()

        if gas > MAX_GWEI:
            logger.info(f'Current GWEI: {gas} > {MAX_GWEI}')
            await asyncio.sleep(60)
        else:
            logger.success(f"GWEI is normal | current: {gas} < {MAX_GWEI}")
            break


def check_gas(func):
    async def _wrapper(*args, **kwargs):
        if CHECK_GWEI:
            await wait_gas()
        return await func(*args, **kwargs)

    return _wrapper
