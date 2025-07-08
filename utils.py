import os
from dotenv import load_dotenv
from bitcoinrpc.authproxy import AuthServiceProxy

# Load environment variables from .env
load_dotenv()

# Change this to match your `bitcoin.conf`
rpc_user = os.getenv("RPC_USER")
rpc_password = os.getenv("RPC_PASSWORD")
rpc_host = os.getenv("RPC_HOST", "127.0.0.1")
rpc_port = os.getenv("RPC_PORT", "8332")

rpc_url = f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}"
rpc = AuthServiceProxy(rpc_url)

def get_tx(txid):
    return rpc.getrawtransaction(txid, True)

def get_tx_inputs(txid):
    tx = get_tx(txid)
    return tx['vin']

def get_tx_outputs(txid):
    tx = get_tx(txid)
    return tx['vout']
