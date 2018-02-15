# Crypto Bear Bucks on the Blockchain
### OS
Ubuntu 16.04 LTS

### Versions
* python3 (3.5.2)
* pip3 (8.1.1)
* django (2.0.0)
* celery (4.1.0)

### Running bitcoin core server with RPC and testnet.
`bitcoind --txindex=1 --server=1 --testnet` (possibly need --reindex)

### Running Django
`python3 manage.py migrate --run-syncdb`

`python3 manage.py runserver` 

### Open Assets Protocol

### Django-CC
`celery -A django_cc.cc.tasks worker -l info`

`celery worker -A crypto_bear_bucks`

`celery call cc.tasks.refill_addresses_queue`

`call celery_tasks.tasks.add --args='[1,2]'`

### TODO
1. get some task to successfully run.
2. Make sure cc is imported successfully in celery
3. run cc task


### SOMEDAY
clean up cc? Make it into a single app? Commit before ofc.