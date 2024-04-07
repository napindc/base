import random
<<<<<<< HEAD
from typing import Union

from loguru import logger
from config import SCROLL_TOKENS
=======

from loguru import logger
from config import BASE_TOKENS
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
from modules import *
from utils.sleeping import sleep


class Multiswap(Account):
<<<<<<< HEAD
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)

        self.swap_modules = {
            "syncswap": SyncSwap,
            "skydrome": Skydrome,
            "zebra": Zebra,
            "xyswap": XYSwap,
=======
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
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
        }

    def get_swap_module(self, use_dex: list):
        swap_module = random.choice(use_dex)

        return self.swap_modules[swap_module]

    async def swap(
            self,
            use_dex: list,
            sleep_from: int,
            sleep_to: int,
            min_swap: int,
            max_swap: int,
<<<<<<< HEAD
            slippage: Union[int, float],
=======
            slippage: int,
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
            random_swap_token: bool,
            min_percent: int,
            max_percent: int
    ):
        quantity_swap = random.randint(min_swap, max_swap)

        if random_swap_token:
<<<<<<< HEAD
            path = [random.choice(["ETH", "USDC"]) for _ in range(0, quantity_swap)]
            usdc_balance = await self.get_balance(SCROLL_TOKENS["USDC"])
            if path[0] == "USDC" and usdc_balance["balance"] <= 1:
                path[0] = "ETH"
        else:
            path = ["ETH" if _ % 2 == 0 else "USDC" for _ in range(0, quantity_swap)]
=======
            path = [random.choice(["ETH", "USDBC"]) for _ in range(0, quantity_swap)]
            USDBC_balance = await self.get_balance(BASE_TOKENS["USDBC"])
            if path[0] == "USDBC" and USDBC_balance["balance"] <= 1:
                path[0] = "ETH"
        else:
            path = ["ETH" if _ % 2 == 0 else "USDBC" for _ in range(0, quantity_swap)]
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

        logger.info(f"[{self.account_id}][{self.address}] Start MultiSwap | quantity swaps: {quantity_swap}")

        for _, token in enumerate(path):
            if token == "ETH":
                decimal = 6
<<<<<<< HEAD
                to_token = "USDC"
=======
                to_token = "USDBC"
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

                balance = await self.w3.eth.get_balance(self.address)

                min_amount = float(self.w3.from_wei(int(balance / 100 * min_percent), "ether"))
                max_amount = float(self.w3.from_wei(int(balance / 100 * max_percent), "ether"))
            else:
                decimal = 18
                to_token = "ETH"

<<<<<<< HEAD
                balance = await self.get_balance(SCROLL_TOKENS["USDC"])
=======
                balance = await self.get_balance(BASE_TOKENS["USDBC"])
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

                min_amount = balance["balance"] if balance["balance"] <= 1 else balance["balance"] / 100 * min_percent
                max_amount = balance["balance"] if balance["balance"] <= 1 else balance["balance"] / 100 * max_percent

<<<<<<< HEAD
            swap_module = self.get_swap_module(use_dex)(self.account_id, self.private_key, self.recipient)
=======
            swap_module = self.get_swap_module(use_dex)(self.account_id, self.private_key)
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
            await swap_module.swap(
                token,
                to_token,
                min_amount,
                max_amount,
                decimal,
                slippage,
                False,
                min_percent,
                max_percent
            )

            if _ + 1 != len(path):
                await sleep(sleep_from, sleep_to)
