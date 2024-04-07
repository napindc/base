import asyncio
<<<<<<< HEAD
<<<<<<< HEAD
from modules import *


async def deposit_scroll(account_id, key, recipient):
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

from modules import *


async def bridge_base(account_id, key):
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    """
    Deposit from official bridge
    ______________________________________________________
    all_amount - bridge from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

<<<<<<< HEAD
<<<<<<< HEAD
    min_percent = 1
    max_percent = 1

    scroll = Scroll(account_id, key, "ethereum", recipient)
    await scroll.deposit(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def withdraw_scroll(account_id, key, recipient):
    """
    Withdraw from official bridge
    ______________________________________________________
    all_amount - withdraw from min_percent to max_percent
    """

    min_amount = 0.0012
    max_amount = 0.0012
    decimal = 4

    all_amount = True

    min_percent = 10
    max_percent = 10

    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.withdraw(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_orbiter(account_id, key, recipient):
    """
    Bridge from orbiter
    ______________________________________________________
    from_chain – ethereum, base, polygon_zkevm, arbitrum, optimism, zksync, scroll | Select one
    to_chain – ethereum, base, polygon_zkevm, arbitrum, optimism, zksync, scroll | Select one
    """

    from_chain = "scroll"
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    min_percent = 5
    max_percent = 10

    base = Base(account_id, key, "ethereum")
    await base.deposit(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_orbiter(account_id, key):
    """
    Bridge from orbiter
    ______________________________________________________
    from_chain – ethereum, base, polygon_zkevm, arbitrum, optimism, zksync | Select one
    to_chain – ethereum, base, polygon_zkevm, arbitrum, optimism, zksync | Select one
    """

    from_chain = "zksync"
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    to_chain = "base"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = False

    min_percent = 5
    max_percent = 10

<<<<<<< HEAD
<<<<<<< HEAD
    orbiter = Orbiter(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await orbiter.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def bridge_layerswap(account_id, key, recipient):
    """
    Bridge from Layerswap
    ______________________________________________________
    from_chain - Choose any chain: ethereum, arbitrum, optimism, avalanche, polygon, base, scroll
    to_chain - Choose any chain: ethereum, arbitrum, optimism, avalanche, polygon, base, scroll

    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """

    from_chain = "zksync"
    to_chain = "scroll"

    min_amount = 0.003
    max_amount = 0.004

    decimal = 5

    all_amount = True

    min_percent = 5
    max_percent = 5

    layerswap = LayerSwap(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await layerswap.bridge(
        from_chain, to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent
    )


async def bridge_nitro(account_id, key, recipient):
    """
    Bridge from nitro
    ______________________________________________________
    from_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    to_chain – ethereum, arbitrum, optimism, zksync, scroll, base, linea | Select one
    """

    from_chain = "zksync"
    to_chain = "scroll"

    min_amount = 0.005
    max_amount = 0.0051
    decimal = 4

    all_amount = False

    min_percent = 5
    max_percent = 10

    nitro = Nitro(account_id=account_id, private_key=key, chain=from_chain, recipient=recipient)
    await nitro.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def wrap_eth(account_id, key, recipient):
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    orbiter = Orbiter(account_id, key, from_chain)
    await orbiter.bridge(to_chain, min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def wrap_eth(account_id, key):
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    """
    Wrap ETH
    ______________________________________________________
    all_amount - wrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 5
    max_percent = 10

<<<<<<< HEAD
<<<<<<< HEAD
    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.wrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def unwrap_eth(account_id, key, recipient):
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    base = Base(account_id, key, "base")
    await base.wrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def unwrap_eth(account_id, key):
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    """
    Unwrap ETH
    ______________________________________________________
    all_amount - unwrap from min_percent to max_percent
    """

    min_amount = 0.001
    max_amount = 0.002
    decimal = 4

    all_amount = True

    min_percent = 100
    max_percent = 100

<<<<<<< HEAD
<<<<<<< HEAD
    scroll = Scroll(account_id, key, "scroll", recipient)
    await scroll.unwrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


# async def swap_skydrome(account_id, key, recipient, 
#                         from_token="USDC", to_token="ETH",
#                         min_amount=0.0001, max_amount=0.0002, decimal=6, slippage=1,
#                         all_amount=True, min_percent=100, max_percent=100):
#     """
#     Make swap on Skydrome
#     ______________________________________________________
#     from_token – Choose SOURCE token ETH, USDC | Select one
#     to_token – Choose DESTINATION token ETH, USDC | Select one

#     Disclaimer - You can swap only ETH to any token or any token to ETH!
#     ______________________________________________________
#     all_amount - swap from min_percent to max_percent
#     """

#     from_token = from_token
#     to_token = to_token

#     min_amount = min_amount
#     max_amount = max_amount
#     decimal = decimal
#     slippage = slippage

#     all_amount = all_amount

#     min_percent = min_percent
#     max_percent = max_percent

#     skydrome = Skydrome(account_id, key, recipient)
#     await skydrome.swap(
#         from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
#     )


# async def swap_zebra(account_id, key, recipient,
#                      from_token="USDC", to_token="ETH",
#                      min_amount=0.0001, max_amount=0.0002, decimal=6, slippage=1,
#                      all_amount=True, min_percent=100, max_percent=100):
#     """
#     Make swap on Zebra
#     ______________________________________________________
#     from_token – Choose SOURCE token ETH, USDC | Select one
#     to_token – Choose DESTINATION token ETH, USDC | Select one

#     Disclaimer - You can swap only ETH to any token or any token to ETH!
#     ______________________________________________________
#     all_amount - swap from min_percent to max_percent
#     """

#     from_token = from_token
#     to_token = to_token

#     min_amount = min_amount
#     max_amount = max_amount
#     decimal = decimal
#     slippage = slippage

#     all_amount = all_amount

#     min_percent = min_percent
#     max_percent = max_percent

#     zebra = Zebra(account_id, key, recipient)
#     await zebra.swap(
#         from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
#     )


async def swap_syncswap(account_id, key, recipient,
                        from_token="USDC", to_token="ETH",
                        min_amount=0.0001, max_amount=0.0002, decimal=6, slippage=1,
                        all_amount=True, min_percent=100, max_percent=100):
    """
    Make swap on SyncSwap

    from_token – Choose SOURCE token ETH, USDC | Select one
    to_token – Choose DESTINATION token ETH, USDC | Select one

    Disclaimer – Don't use stable coin in from and to token | from_token USDC to_token USDT DON'T WORK!!!
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    base = Base(account_id, key, "base")
    await base.unwrap_eth(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_uniswap(account_id, key):
    """
    Make swap on Uniswap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

<<<<<<< HEAD
<<<<<<< HEAD
    from_token = from_token
    to_token = to_token

    min_amount = min_amount
    max_amount = max_amount
    decimal = decimal
    slippage = slippage

    all_amount = all_amount

    min_percent = min_percent
    max_percent = max_percent

    syncswap = SyncSwap(account_id, key, recipient)
    await syncswap.swap(
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    from_token = "USDBC"
    to_token = "ETH"

    min_amount = 0.001
    max_amount = 0.002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    uniswap = Uniswap(account_id, key)
    await uniswap.swap(
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


<<<<<<< HEAD
<<<<<<< HEAD
# async def swap_xyswap(account_id, key, recipient,
#                       from_token="USDC", to_token="ETH",
#                       min_amount=0.0001, max_amount=0.0002, decimal=6, slippage=1,
#                       all_amount=True, min_percent=100, max_percent=100):
#     """
#     Make swap on XYSwap
#     ______________________________________________________
#     from_token – Choose SOURCE token ETH, WETH, USDC | Select one
#     to_token – Choose DESTINATION token ETH, WETH, USDC | Select one

#     Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
#     ______________________________________________________
#     all_amount - swap from min_percent to max_percent
#     """

#     from_token = from_token
#     to_token = to_token

#     min_amount = min_amount
#     max_amount = max_amount
#     decimal = decimal
#     slippage = slippage

#     all_amount = all_amount

#     min_percent = min_percent
#     max_percent = max_percent

#     xyswap = XYSwap(account_id, key, recipient)
#     await xyswap.swap(
#         from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
#     )


async def deposit_layerbank(account_id, key, recipient):
    """
    Make deposit on LayerBank
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
async def swap_pancake(account_id, key):
    """
    Make swap on PancakeSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.001
    max_amount = 0.002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    pancake = Pancake(account_id, key)
    await pancake.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_woofi(account_id, key):
    """
    Make swap on WooFi
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    woofi = WooFi(account_id, key)
    await woofi.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_baseswap(account_id, key):
    """
    Make swap on BaseSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDBC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    baseswap = BaseSwap(account_id, key)
    await baseswap.swap(from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent,
                        max_percent)


async def swap_alienswap(account_id, key):
    """
    Make swap on AlienSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one

    Disclaimer - You can swap only ETH to any token or any token to ETH!
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 100
    max_percent = 100

    alienswap = AlienSwap(account_id, key)
    await alienswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_odos(account_id, key):
    """
    Make swap on Odos
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDBC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "USDBC"
    to_token = "ETH"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    odos = Odos(account_id, key)
    await odos.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_inch(account_id, key):
    """
    Make swap on 1inch
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDBC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    inch_dex = Inch(account_id, key)
    await inch_dex.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_openocean(account_id, key):
    """
    Make swap on OpenOcean
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDBC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    openocean = OpenOcean(account_id, key)
    await openocean.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_xyswap(account_id, key):
    """
    Make swap on XYSwap
    ______________________________________________________
    from_token – Choose SOURCE token ETH, WETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, WETH, USDBC | Select one

    Disclaimer - If you use True for use_fee, you support me 1% of the transaction amount
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    xyswap = XYSwap(account_id, key)
    await xyswap.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def swap_maverick(account_id, key):
    """
    Make swap on Maverick
    ______________________________________________________
    from_token – Choose SOURCE token ETH, USDBC | Select one
    to_token – Choose DESTINATION token ETH, USDBC | Select one
    ______________________________________________________
    all_amount - swap from min_percent to max_percent
    """

    from_token = "ETH"
    to_token = "USDBC"

    min_amount = 0.0001
    max_amount = 0.0001
    decimal = 6
    slippage = 1

    all_amount = True

    min_percent = 1
    max_percent = 1

    maverick = Maverick(account_id, key)
    await maverick.swap(
        from_token, to_token, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent
    )


async def bungee_refuel(account_id, key):
    """
    Make refuel on Bungee
    ______________________________________________________
    to_chain – Choose DESTINATION chain: BSC, OPTIMISM, GNOSIS, POLYGON, ZKSYNC, ARBITRUM, AVALANCHE, AURORA, ZK_EVM

    Disclaimer - The chain will be randomly selected
    ______________________________________________________
    random_amount – True - amount random from min to max | False - use min amount
    """

    chain_list = ["GNOSIS"]

    random_amount = False

    bungee = Bungee(account_id, key)
    await bungee.refuel(chain_list, random_amount)


async def stargate_bridge(account_id, key):
    """
    Stargate bridge ETH
    ______________________________________________________
    to_chain – Choose DESTINATION chain: arbitrum, optimism, linea

    Disclaimer - The chain will be randomly selected
    ______________________________________________________
    random_amount – True - amount random from min to max | False - use min amount
    """

    chain_list = ["arbitrum", "optimism"]

<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

<<<<<<< HEAD
<<<<<<< HEAD
    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = True

    min_percent = 5
    max_percent = 10

    layerbank = LayerBank(account_id, key, recipient)
    await layerbank.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def deposit_aave(account_id, key, recipient):
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    slippage = 1

    all_amount = True

    min_percent = 10
    max_percent = 10

    stargate = Stargate(account_id, key)
    await stargate.bridge(chain_list, min_amount, max_amount, decimal, slippage, all_amount, min_percent, max_percent)


async def deposit_aave(account_id, key):
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    """
    Make deposit on Aave
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = True

    min_percent = 5
    max_percent = 10

<<<<<<< HEAD
<<<<<<< HEAD
    aave = Aave(account_id, key, recipient)
=======
    aave = Aave(account_id, key)
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
    aave = Aave(account_id, key)
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    await aave.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


<<<<<<< HEAD
<<<<<<< HEAD
async def mint_zerius(account_id, key, recipient):
    """
    Mint + bridge Zerius NFT
    ______________________________________________________
    chains - list chains for random chain bridge: arbitrum, optimism, polygon, bsc, avalanche
    Disclaimer - The Mint function should be called "mint", to make sure of this, look at the name in Rabby Wallet or in explorer
    """

    chains = ["arbitrum"]
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
async def deposit_moonwell(account_id, key):
    """
    Make deposit on MoonWell
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 5
    sleep_to = 24

    make_withdraw = True

    all_amount = True

    min_percent = 5
    max_percent = 10

    moonwell = MoonWell(account_id, key)
    await moonwell.deposit(
        min_amount, max_amount, decimal, sleep_from, sleep_to, make_withdraw, all_amount, min_percent, max_percent
    )


async def deposit_rocketsam(account_id, key):
    """
    Make deposit on RocketSam
    ______________________________________________________
    make_withdraw - True, if need withdraw after deposit

    all_amount - deposit from min_percent to max_percent
    """
    contracts = [
        "0x634607B44e21F4b71e7bD5e19d5b8E4dC99Ab9C4",
        "0x1077df51A4059477826549101a30a70b9579A08B",
        "0x802DbB9efE447f8e4f578EB7add3F7e43E89C529",
        "0x0c9Bfb785E6582A15d6523252675abaA7350Bf76",
        "0x288df8088905D71Ff052bf052f3A0ff11A6CDa46",
        "0x2B4a7822F3de8bd6cb0552f562b40a391890E945",
        "0x553a8EFa12d333c864c89CB809D68268C836B70a",
        "0x5ae3cB086887A6FB7662eE58Cf1d5113E69bBA62",
        "0x1feF777Fb93Aa45a6Cefcf5507c665b64b301FB3",
        "0x0557D4C04BB994719b087d2950841BF25cf39899",
    ]

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    sleep_from = 1
    sleep_to = 1

    make_withdraw = True

    all_amount = True

    min_percent = 1
    max_percent = 1

    rocketsam = RocketSam(account_id, key)
    await rocketsam.deposit(
        contracts, min_amount, max_amount, decimal, sleep_from, sleep_to,
        make_withdraw, all_amount, min_percent, max_percent
    )


async def withdraw_rocketsam(account_id, key):
    """
    Make withdraw from RocketSam
    """
    contracts = [
        "0x634607B44e21F4b71e7bD5e19d5b8E4dC99Ab9C4",
        "0x1077df51A4059477826549101a30a70b9579A08B",
        "0x802DbB9efE447f8e4f578EB7add3F7e43E89C529",
        "0x0c9Bfb785E6582A15d6523252675abaA7350Bf76",
        "0x288df8088905D71Ff052bf052f3A0ff11A6CDa46",
        "0x2B4a7822F3de8bd6cb0552f562b40a391890E945",
        "0x553a8EFa12d333c864c89CB809D68268C836B70a",
        "0x5ae3cB086887A6FB7662eE58Cf1d5113E69bBA62",
        "0x1feF777Fb93Aa45a6Cefcf5507c665b64b301FB3",
        "0x0557D4C04BB994719b087d2950841BF25cf39899",
    ]

    sleep_from = 10
    sleep_to = 30

    rocketsam = RocketSam(account_id, key)
    await rocketsam.withdraw(contracts, sleep_from, sleep_to)


async def bridge_nft(account_id, key):
    """
    Make mint NFT and bridge NFT on L2Telegraph
    """

    sleep_from = 5
    sleep_to = 20

    l2telegraph = L2Telegraph(account_id, key)
    await l2telegraph.bridge(sleep_from, sleep_to)


async def mint_mintfun(account_id, key):
    """
    Mint NFT on Mint.Fun
    ______________________________________________________
    Disclaimer - The Mint function should be called "mint", to make sure of this, look at the name in Rabby Wallet or in explorer
    """

    nft_contracts_data = {
        "0x69b69cc6e9f99c62a003fd9e143c126504d49dc2": 1,
        "0xea0b3e39ccd46d7F2B338D784De8519902f7E17E": 3,
    }

    mintfun = MintFun(account_id, key)
    await mintfun.mint(nft_contracts_data)


async def mint_zerius(account_id, key):
    """
    Mint + bridge Zerius NFT
    ______________________________________________________
    chains - list chains for random chain bridge: arbitrum, optimism, polygon, bsc, avalanche, zora
    Disclaimer - The Mint function should be called "mint", to make sure of this, look at the name in Rabby Wallet or in explorer
    """

    chains = ["zora"]
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

    sleep_from = 10
    sleep_to = 20

<<<<<<< HEAD
<<<<<<< HEAD
    zerius = Zerius(account_id, key, recipient)
    await zerius.bridge(chains, sleep_from, sleep_to)


async def mint_l2pass(account_id, key, recipient):
    """
    Mint L2Pass NFT
    """

    contract = "0x0000049f63ef0d60abe49fdd8bebfa5a68822222"

    l2pass = L2Pass(account_id, key, recipient)
    await l2pass.mint(contract)


async def mint_nft(account_id, key, recipient):
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    zerius = Zerius(account_id, key)
    await zerius.bridge(chains, sleep_from, sleep_to)


async def mint_nft(account_id, key):
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    """
    Mint NFT on NFTS2ME
    ______________________________________________________
    contracts - list NFT contract addresses
    """

    contracts = [""]

<<<<<<< HEAD
<<<<<<< HEAD
    minter = Minter(account_id, key, recipient)
    await minter.mint_nft(contracts)


async def mint_zkstars(account_id, key, recipient):
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    minter = Minter(account_id, key)
    await minter.mint_nft(contracts)


async def mint_zkstars(account_id, key):
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    """
    Mint ZkStars NFT
    """

    contracts = [
<<<<<<< HEAD
<<<<<<< HEAD
        "0x609c2f307940b8f52190b6d3d3a41c762136884e",
        "0x16c0baa8a2aa77fab8d0aece9b6947ee1b74b943",
        "0xc5471e35533e887f59df7a31f7c162eb98f367f7",
        "0xf861f5927c87bc7c4781817b08151d638de41036",
        "0x954e8ac11c369ef69636239803a36146bf85e61b",
        "0xa576ac0a158ebdcc0445e3465adf50e93dd2cad8",
        "0x17863384c663c5f95e4e52d3601f2ff1919ac1aa",
        "0x4c2656a6d1c0ecac86f5024e60d4f04dbb3d1623",
        "0x4e86532cedf07c7946e238bd32ba141b4ed10c12",
        "0x6b9db0ffcb840c3d9119b4ff00f0795602c96086",
        "0x10d4749bee6a1576ae5e11227bc7f5031ad351e4",
        "0x373148e566e4c4c14f4ed8334aba3a0da645097a",
        "0xdacbac1c25d63b4b2b8bfdbf21c383e3ccff2281",
        "0x2394b22b3925342f3216360b7b8f43402e6a150b",
        "0xf34f431e3fc0ad0d2beb914637b39f1ecf46c1ee",
        "0x6f1e292302dce99e2a4681be4370d349850ac7c2",
        "0xa21fac8b389f1f3717957a6bb7d5ae658122fc82",
        "0x1b499d45e0cc5e5198b8a440f2d949f70e207a5d",
        "0xec9bef17876d67de1f2ec69f9a0e94de647fcc93",
        "0x5e6c493da06221fed0259a49beac09ef750c3de1"
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
        "0x4c78c7d2f423cf07c6dc2542ac000c4788f03657",
        "0x657130a14e93731dfecc772d210ae8333303986c",
        "0x004416bef2544df0f02f23788c6ada0775868560",
        "0x39b06911d22f4d3191827ed08ae35b84f68843e4",
        "0x8a6a9ef84cd819a54eee3cf7cfd351d21ab6b5fe",
        "0x8fb3225d0a85f2a49714acd36cdcd96a7b2b7fbc",
        "0x91ad9ed35b1e9ff6975aa94690fa438efb5a7160",
        "0x32d8eeb70eab5f5962190a2bb78a10a5a0958649",
        "0xab62313752f90c24405287ad8c3bcf4c25c26e57",
        "0x6f562b821b5cb93d4de2b0bd558cc8e46b632a08",
        "0xb63159a26664a89abce783437fc17786af8bb46d",
        "0x7e6b32d7eecddb6be496f232ab9316a5bf9f4e17",
        "0xcb03866371fb149f3992f8d623d5aaa4b831e2fd",
        "0x78c85441f53a07329e2380e49f1870199f70cee1",
        "0x54c49cb80a0679e3217f86d891859b4e477b56c3",
        "0xad6f16f5ff3461c83d639901bae1fb2a8a68aa31",
        "0x023a7c97679f2c121a31bacf37292dabf7ab97e9",
        "0x5dabff127cad8d075b5cea7f795dcbae1ddf471d",
        "0xd3c6386362dabab1a30acc2c377d9ac2cc8b7b16",
        "0xed0407d6b84b2c86418cac16a347930b222b505c"
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    ]

    mint_min = 1
    mint_max = 1

    mint_all = False

    sleep_from = 5
    sleep_to = 10

<<<<<<< HEAD
<<<<<<< HEAD
    zkkstars = ZkStars(account_id, key, recipient)
    await zkkstars.mint(contracts, mint_min, mint_max, mint_all, sleep_from, sleep_to)


async def make_transfer(_id, key, recipient):
    """
    Transfer ETH
    """

    min_amount = 0.0001
    max_amount = 0.0002
    decimal = 5

    all_amount = True

    min_percent = 10
    max_percent = 10

    transfer = Transfer(_id, key, recipient)
    await transfer.transfer(min_amount, max_amount, decimal, all_amount, min_percent, max_percent)


async def swap_tokens(account_id, key, recipient):
    """
    SwapTokens module: Automatically swap tokens to ETH
    ______________________________________________________
    use_dex - Choose any dex: syncswap, skydrome, zebra, xyswap
    """

    use_dex = [
        "syncswap", "skydrome", "zebra"
    ]

    use_tokens = ["USDC"]

    sleep_from = 1
    sleep_to = 5

    slippage = 0.1
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    zkkstars = ZkStars(account_id, key)
    await zkkstars.mint(contracts, mint_min, mint_max, mint_all, sleep_from, sleep_to)


async def swap_tokens(account_id, key):
    """
    SwapTokens module: Automatically swap tokens to ETH
    ______________________________________________________
    use_dex - Choose any dex: uniswap, pancake, woofi, baseswap, alienswap, maverick, odos, inch, xyswap, openocean
    """

    use_dex = [
        "uniswap", "pancake", "woofi", "baseswap",
        "alienswap", "maverick", "odos", "inch",
        "xyswap", "openocean"
    ]

    use_tokens = ["USDBC"]

    sleep_from = 300
    sleep_to = 600

    slippage = 1
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

    min_percent = 100
    max_percent = 100

<<<<<<< HEAD
<<<<<<< HEAD
    swap_tokens = SwapTokens(account_id, key, recipient)
    await swap_tokens.swap(use_dex, use_tokens, sleep_from, sleep_to, slippage, min_percent, max_percent)


async def swap_multiswap(account_id, key, recipient):
    """
    Multi-Swap module: Automatically performs the specified number of swaps in one of the dexes.
    ______________________________________________________
    use_dex - Choose any dex: syncswap, skydrome, zebra, xyswap
    quantity_swap - Quantity swaps
    ______________________________________________________
    random_swap_token - If True the swap path will be [ETH -> USDC -> USDC -> ETH] (random!)
    If False the swap path will be [ETH -> USDC -> ETH -> USDC]
    """

    use_dex = ["syncswap", "skydrome", "zebra"]

    min_swap = 3
    max_swap = 4
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    swap_tokens = SwapTokens(account_id, key)
    await swap_tokens.swap(use_dex, use_tokens, sleep_from, sleep_to, slippage, min_percent, max_percent)


async def swap_multiswap(account_id, key):
    """
    Multi-Swap module: Automatically performs the specified number of swaps in one of the dexes.
    ______________________________________________________
    use_dex - Choose any dex: uniswap, pancake, woofi, baseswap, alienswap, maverick, odos, inch, xyswap, openocean
    quantity_swap - Quantity swaps
    ______________________________________________________
    random_swap_token - If True the swap path will be [ETH -> USDBC -> USDBC -> ETH] (random!)
    If False the swap path will be [ETH -> USDBC -> ETH -> USDBC]
    """

    use_dex = ["uniswap", "pancake", "woofi", "baseswap", "odos"]

    min_swap = 1
    max_swap = 2
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

    sleep_from = 3
    sleep_to = 7

<<<<<<< HEAD
<<<<<<< HEAD
    slippage = 0.1
=======
    slippage = 1
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
    slippage = 1
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944

    random_swap_token = True

    min_percent = 5
    max_percent = 10

<<<<<<< HEAD
<<<<<<< HEAD
    multi = Multiswap(account_id, key, recipient)
=======
    multi = Multiswap(account_id, key)
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
    multi = Multiswap(account_id, key)
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    await multi.swap(
        use_dex, sleep_from, sleep_to, min_swap, max_swap, slippage, random_swap_token, min_percent, max_percent
    )


<<<<<<< HEAD
<<<<<<< HEAD
async def custom_routes(account_id, key, recipient):
    """
    BRIDGE:
        – deposit_scroll
        – withdraw_scroll
        – bridge_orbiter
        – bridge_layerswap
        – bridge_nitro
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
async def custom_routes(account_id, key):
    """
    BRIDGE:
        – bridge_base
        – bridge_orbiter
        – bungee_refuel
        – stargate_bridge
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    WRAP:
        – wrap_eth
        – unwrap_eth
    DEX:
<<<<<<< HEAD
<<<<<<< HEAD
        – swap_skydrome
        – swap_syncswap
        – swap_zebra
    LIQUIDITY:
    LANDING:
        – depost_layerbank
        – withdraw_layerbank
        – deposit_aave
        – withdraw_aave
    NFT/DOMAIN:
        – mint_zerius
        – mint_zkstars
        – create_omnisea
        – mint_nft
        – mint_l2pass
    ANOTHER:
        – swap_multiswap
        – swap_tokens
        – send_mail (Dmail)
        – create_safe
        – rubyscore_vote
        – deploy_contract
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
        – swap_uniswap
        – swap_pancake
        – swap_woofi
        – swap_baseswap
        – swap_alienswap
        – swap_maverick
        – swap_odos
        – swap_inch
        – swap_openocean
        – swap_xyswap
    LANDING:
        – deposit_aave
        – deposit_moonwell
        – withdraw_aave
        – withdraw_moonwell
        – deposit_rocketsam
        – withdraw_rocketsam
    NFT/DOMAIN:
        – mint_zerius
        – mint_zkstars
        – mint_mintfun
        – mint_nft
    ANOTHER:
        – send_message
        – send_mail (Dmail)
        – bridge_nft
        – create_portfolio
        – swap_tokens
        – swap_multiswap
        – create_safe
        – mint_nft
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    ______________________________________________________
    Disclaimer - You can add modules to [] to select random ones,
    example [module_1, module_2, [module_3, module_4], module 5]
    The script will start with module 1, 2, 5 and select a random one from module 3 and 4

    You can also specify None in [], and if None is selected by random, this module will be skipped

    You can also specify () to perform the desired action a certain number of times
    example (send_mail, 1, 10) run this module 1 to 10 times
    """

    use_modules = [
<<<<<<< HEAD
<<<<<<< HEAD
        create_omnisea,
        [create_omnisea, mint_zerius, None],
        (create_omnisea, 1, 3),
    ]

    sleep_from = 300
    sleep_to = 700

    random_module = True

    routes = Routes(account_id, key, recipient)
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
        [bridge_nft, deposit_aave, None],
        (bridge_nft, 1, 3),
    ]

    sleep_from = 10
    sleep_to = 20

    random_module = True

    routes = Routes(account_id, key)
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
    await routes.start(use_modules, sleep_from, sleep_to, random_module)


#########################################
########### NO NEED TO CHANGE ###########
#########################################
<<<<<<< HEAD
<<<<<<< HEAD

async def withdraw_layerbank(account_id, key, recipient):
    layerbank = LayerBank(account_id, key, recipient)
    await layerbank.withdraw()


async def withdraw_aave(account_id, key, recipient):
    aave = Aave(account_id, key, recipient)
    await aave.withdraw()


async def send_mail(account_id, key, recipient):
    dmail = Dmail(account_id, key, recipient)
    await dmail.send_mail()


async def create_omnisea(account_id, key, recipient):
    omnisea = Omnisea(account_id, key, recipient)
    await omnisea.create()


async def create_safe(account_id, key, recipient):
    gnosis_safe = GnosisSafe(account_id, key, recipient)
    await gnosis_safe.create_safe()


async def deploy_contract(account_id, key, recipient):
    deployer = Deployer(account_id, key, recipient)
    await deployer.deploy_token()


async def rubyscore_vote(account_id, key, recipient):
    rubyscore = RubyScore(account_id, key, recipient)
    await rubyscore.vote()


def get_tx_count(wallets):
    asyncio.run(check_tx(wallets))
=======
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
async def send_mail(account_id, key):
    dmail = Dmail(account_id, key)
    await dmail.send_mail()

async def withdraw_aave(account_id, key):
    aave = Aave(account_id, key)
    await aave.withdraw()


async def withdraw_moonwell(account_id, key):
    moonwell = MoonWell(account_id, key)
    await moonwell.withdraw()


async def send_message(account_id, key):
    l2telegraph = L2Telegraph(account_id, key)
    await l2telegraph.send_message()


async def create_portfolio(account_id, key):
    rai = Rai(account_id, key)
    await rai.create()


async def create_safe(account_id, key):
    gnosis_safe = GnosisSafe(account_id, key)
    await gnosis_safe.create_safe()


def get_tx_count():
    asyncio.run(check_tx())
<<<<<<< HEAD
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
=======
>>>>>>> 30c15bba68552d47a53a5f7d4cd386cad749b944
