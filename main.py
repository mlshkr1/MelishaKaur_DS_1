from web3 import Web3
import time

#Connect to Ganache HTTP (default GUI port)
w3 = Web3(Web3.HTTPProvider("http://localhost:7545"))

#Confirm connection
if not w3.isConnected():
    print("❌ Not connected to Ethereum")
    exit()
print("✅ Connected to Ethereum")

#Contract address from Remix deployment
contract_address = Web3.toChecksumAddress('0xb977909b293Ebc8725b6287F6e8d3c06be063eFE')

#Minimal ABI containing only the TokensLocked event
abi = [
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "sender", "type": "address"},
            {"indexed": False, "internalType": "uint256", "name": "amount", "type": "uint256"},
            {"indexed": False, "internalType": "string", "name": "cosmosReceiver", "type": "string"}
        ],
        "name": "TokensLocked",
        "type": "event"
    }
]

#Load the contract
contract = w3.eth.contract(address=contract_address, abi=abi)
event_filter = contract.events.TokensLocked.createFilter(fromBlock='latest')

#Simulated Cosmos ledger to track cETH
cosmos_balances = {}

print("🔁 Listening for TokensLocked events...")

while True:
    for event in event_filter.get_new_entries():
        sender = event['args']['sender']
        amount = w3.fromWei(event['args']['amount'], 'ether')
        cosmos_receiver = event['args']['cosmosReceiver']

        print("\n🔥 Cross-Chain Swap Detected")
        print(f"🔒 {sender} locked {amount} ETH for Cosmos address {cosmos_receiver}")

        # Simulate Cosmos minting
        cosmos_balances[cosmos_receiver] = cosmos_balances.get(cosmos_receiver, 0) + float(amount)
        print(f"✅ Cosmos Minted: {amount} cETH to {cosmos_receiver}")
        print(f"📊 Current Cosmos Balance: {cosmos_balances[cosmos_receiver]} cETH")

    time.sleep(1)