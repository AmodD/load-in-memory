### Pre-requisites

1. should have conda installed
2. conda activate Fortiate_env
3. conda install redis

### installing redis

install redis database
       
       in Fortiate/Build/Databases/
       
inside Databases folder open terminal
       
       wget http://download.redis.io/releases/redis-5.0.6.tar.gz
       tar xzf redis-5.0.6.tar.gz
       cd redis-5.0.6
       make
       src/redis-server

# Running in terminal

in the same terminal where you activated Fortiate_env 
        
        cd Fortiate/Build/Workspace/Python
        
if you already have currencyCode-decimals-redis

        cd currency-code-decimals-redis
        git pull

to get the latest code

else
        
        git clone https://github.com/fortiate/currency-code-decimals-redis.git

        cd currency-code-decimals-redis
check if you are inside your conda env

        python 3 redisCurrencyCodeDecimalsInserter.py
        
now your redis database will contain a 
        
        hashmap named : currencyCodeMapping

access it by using 
        
        redisClient.hgetall('currencyCodeMapping') 
 
