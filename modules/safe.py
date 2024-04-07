import time
<<<<<<< HEAD
<<<<<<< HEAD
=======
from typing import Dict
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
from typing import Dict
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

from loguru import logger
from config import SAFE_ABI, SAFE_CONTRACT, ZERO_ADDRESS
from utils.gas_checker import check_gas
from utils.helpers import retry
from .account import Account


class GnosisSafe(Account):
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, account_id: int, private_key: str, recipient: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="scroll", recipient=recipient)
=======
    def __init__(self, account_id: int, private_key: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="base")
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
    def __init__(self, account_id: int, private_key: str) -> None:
        super().__init__(account_id=account_id, private_key=private_key, chain="base")
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

        self.contract = self.get_contract(SAFE_CONTRACT, SAFE_ABI)

    @retry
    @check_gas
    async def create_safe(self):
        logger.info(f"[{self.account_id}][{self.address}] Create gnosis safe")

        setup_data = self.contract.encodeABI(
            fn_name="setup",
            args=[
                [self.address],
                1,
                ZERO_ADDRESS,
                "0x",
<<<<<<< HEAD
<<<<<<< HEAD
                self.w3.to_checksum_address("0xf48f2B2d2a534e402487b3ee7C18c33Aec0Fe5e4"),
=======
                self.w3.to_checksum_address("0x017062a1dE2FE6b99BE3d9d37841FeD19F573804"),
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
                self.w3.to_checksum_address("0x017062a1dE2FE6b99BE3d9d37841FeD19F573804"),
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
                ZERO_ADDRESS,
                0,
                ZERO_ADDRESS
            ]
        )

        tx_data = await self.get_tx_data()

        transaction = await self.contract.functions.createProxyWithNonce(
<<<<<<< HEAD
<<<<<<< HEAD
            self.w3.to_checksum_address("0x3E5c63644E683549055b9Be8653de26E0B4CD36E"),
=======
            self.w3.to_checksum_address("0xfb1bffC9d739B8D520DaF37dF666da4C687191EA"),
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
            self.w3.to_checksum_address("0xfb1bffC9d739B8D520DaF37dF666da4C687191EA"),
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
            setup_data,
            int(time.time()*1000)
        ).build_transaction(tx_data)

        signed_txn = await self.sign(transaction)

        txn_hash = await self.send_raw_transaction(signed_txn)

        await self.wait_until_tx_finished(txn_hash.hex())
