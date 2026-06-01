#!/usr/bin/env python3
"""Public-safe Base starter script.
No personal wallet, API key, token, email, or server IP is stored in this repository.
Use .env locally and never commit it.
"""

import os
import re
from datetime import datetime, timezone

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"
BASE_RPC_URL = "https://mainnet.base.org"


def load_local_env() -> None:
    if load_dotenv:
        load_dotenv()


def get_wallet_from_user() -> str:
    env_wallet = os.getenv("WALLET_ADDRESS", "").strip()
    if env_wallet and env_wallet != ZERO_ADDRESS:
        return env_wallet
    wallet = input("Enter a Base wallet address, or press Enter to use a safe demo address: ").strip()
    return wallet or ZERO_ADDRESS


def is_valid_address(address: str) -> bool:
    return bool(re.fullmatch(r"0x[a-fA-F0-9]{40}", address))


def main() -> None:
    load_local_env()
    rpc_url = os.getenv("BASE_RPC_URL", BASE_RPC_URL)
    wallet = get_wallet_from_user()

    print("Base public-safe starter")
    print("Generated at:", datetime.now(timezone.utc).isoformat())
    print("RPC:", rpc_url)
    print("Wallet address is valid:", is_valid_address(wallet))
    print("Wallet used:", wallet if wallet == ZERO_ADDRESS else wallet[:6] + "..." + wallet[-4:])
    print("No personal data is committed. Put real values only in local .env files.")


if __name__ == "__main__":
    main()
