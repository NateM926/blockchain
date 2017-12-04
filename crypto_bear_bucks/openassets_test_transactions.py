import asyncio
import bitcoin.rpc
import openassets.protocol
import openassets.transactions

@asyncio.coroutine
def main():
    bitcoin.SelectParams('testnet')

    # Create a RPC client for Bitcoin Core
    rpc_client = bitcoin.rpc.Proxy('http://NateM926:MyAmazinglyLongPasswordThatIsCompletelySecure!@localhost:18332')

    # Output script corresponding to address myLPe3P8SE2DyqRwABRwqezxdZxhkYxXYu (in testnet)
    output_script = bitcoin.core.x('76a914c372d85bc2c54384dbc2cb9ef365eb7f15d4a9b688ac')

    # Initialize the coloring engine
    transaction_provider = asyncio.coroutine(rpc_client.getrawtransaction)
    engine = openassets.protocol.ColoringEngine(transaction_provider, openassets.protocol.OutputCache(), loop)

    # Obtain the unspent output for the local wallet
    unspent_outputs = []
    for output in rpc_client.listunspent():
        if output['scriptPubKey'] == output_script:
            unspent_outputs.append(openassets.transactions.SpendableOutput(
                bitcoin.core.COutPoint(output['outpoint'].hash, output['outpoint'].n),
                (yield from engine.get_output(output['outpoint'].hash, output['outpoint'].n))
            ))

    # The minimum valid value for an output is set to 600 satoshis
    builder = openassets.transactions.TransactionBuilder(600)

    # Create the issuance parameters
    issuance_parameters = openassets.transactions.TransferParameters(
        unspent_outputs=unspent_outputs,    # Unspent outputs the coins are issued from
        to_script=output_script,            # The issued coins are sent back to the same address
        change_script=output_script,        # The bitcoin change is sent back to the same address
        amount=1500)                        # Issue 1,500 units of the asset

    # Create the issuance transaction
    # The metadata is left empty and the fees are set to 0.0001 BTC
    transaction = builder.issue(issuance_parameters, metadata=b'', fees=10000)

    print(transaction)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())