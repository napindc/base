import random
<<<<<<< HEAD
<<<<<<< HEAD
from typing import List, Union

from loguru import logger
from config import SCROLL_TOKENS
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
from typing import List

from loguru import logger
from config import BASE_TOKENS
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
from modules import *
from utils.sleeping import sleep


class SwapTokens(Account):
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

        self.swap_modules = {
            "syncswap": SyncSwap,
            "skydrome": Skydrome,
            "zebra": Zebra,
            "xyswap": XYSwap,
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    def __init__(self, account_id: int, private_key: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="base")

        self.swap_modules = {
            "uniswap": Uniswap,
            "pancake": Pancake,
            "woofi": WooFi,
            "baseswap": BaseSwap,
            "alienswap": AlienSwap,
            "maverick": Maverick,
            "odos": Odos,
            "inch": Inch,
            "xyswap": XYSwap,
            "openocean": OpenOcean,
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
        }

    def get_swap_module(self, use_dex: list):
        swap_module = random.choice(use_dex)
        return self.swap_modules[swap_module]

    async def swap(
            self,
            use_dex: List,
            tokens: List,
            sleep_from: int,
            sleep_to: int,
<<<<<<< HEAD
<<<<<<< HEAD
            slippage: Union[int, float],
=======
            slippage: int,
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
            slippage: int,
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
            min_percent: int,
            max_percent: int,
    ):
        random.shuffle(tokens)

        logger.info(f"[{self.account_id}][{self.address}] Start swap tokens")

        for _, token in enumerate(tokens, start=1):
            if token == "ETH":
                continue

<<<<<<< HEAD
<<<<<<< HEAD
            balance = await self.get_balance(SCROLL_TOKENS[token])

            if balance["balance_wei"] > 0:
                swap_module = self.get_swap_module(use_dex)(self.account_id, self.private_key, self.recipient)
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
            balance = await self.get_balance(BASE_TOKENS[token])

            if balance["balance_wei"] > 0:
                swap_module = self.get_swap_module(use_dex)(self.account_id, self.private_key)
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
                await swap_module.swap(
                    token,
                    "ETH",
                    balance["balance"],
                    balance["balance"],
                    balance["decimal"],
                    slippage,
                    True,
                    min_percent,
                    max_percent
                )

            if _ != len(tokens):
                await sleep(sleep_from, sleep_to)
