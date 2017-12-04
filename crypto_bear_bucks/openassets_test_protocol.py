import asyncio
import bitcoin.rpc
import openassets.protocol

@asyncio.coroutine
def main():
    bitcoin.SelectParams('testnet')

    # Create a RPC client for Bitcoin Core (http://USER:PASS@localhost:PORT)
    rpc_client = bitcoin.rpc.Proxy('http://NateM926:MyAmazinglyLongPasswordThatIsCompletelySecure!@localhost:18332')
    # OutputCache implements the interface required for an output cache provider, but does not perform any caching
    cache = openassets.protocol.OutputCache()
    # The transaction provider is a function returning a transaction given its hash
    transaction_provider = asyncio.coroutine(rpc_client.getrawtransaction)
    # Instantiate the coloring engine
    coloring_engine = openassets.protocol.ColoringEngine(transaction_provider, cache, loop)

    transaction_hash = bitcoin.core.lx('864cbcb4b5e083a98aaeaf94443815025bdfb0d35a6fd00817034018b6752ff5')
    output_index = 1
    colored_output = yield from coloring_engine.get_output(transaction_hash, output_index)

    print(colored_output)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())