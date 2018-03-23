# Bear Bucks on the Blockchain

### Versions
* Ubuntu 16.04 LTS
* python3 (3.5.2)
* pip3 (8.1.1)
* django (2.0.0)
* celery (4.1.0)

## Run all three services in separate terminal windows

### 1. Running Bitcoin core server with RPC and testnet
* `bitcoind --txindex=1 --server=1 --testnet --reindex` testnet uses port 18332

### 2. Running Django
* `python3 manage.py migrate --run-syncdb` may have to run this first
* `python3 manage.py runserver` 

### 3. Running Celery Worker
* `celery worker -A celery_tasks --loglevel=INFO` or DEBUG

### How to Start Using Bear Bucks on the Blockchain
* Create a user and sign into: `http://127.0.0.1:8000/admin/`
* Create a Currency (such as BBUX)
* Set api_url field in the format of `http://username:password@localhost:18332` (from bitcoin.conf)
* Create a Wallet and run the `refil_addresses_queue` task to assign it an address
* Add testnet coins to your wallet address for free with: `https://testnet.manu.backend.hamburg/faucet`

### Here are some of the different tasks you can call
* `celery call cc.tasks.refill_addresses_queue`
* `celery call cc.tasks.query_transaction --args='[ticker,txid]'`
* `celery call cc.tasks.query_transaction -a=[BTC,c810d50a0dc84bf7f62b398896578ddc881ad2a71fa00d2dc59e485ff159d1f1]`
* `curl -d "param1=value1&param2=value2" -X POST http://localhost:8080/getbalance`
