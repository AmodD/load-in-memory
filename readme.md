##### Table of Contents  
+ [Introduction](#introduction) 
+ [Prerequisite](#prerequisite) 
+ [Input](#input)
+ [Output](#output) 
+ [Dependency](#dependancy)
+ [Limitation](#limitation)
+ [Getting the code](#getting_the_code)
+ [How To Run](#how_to_run)
+ [How To Access](#how_to_access)
    + [For Accessing terminal.py](#for-accessing-terminalpy)
    + [For Accessing api.py](#for-accessing-apipy)
    + [For Accessing eventApi.py](#for-accessing-eventapipy)

<a name="introduction"/>

## Introduction
+ This is the loadcache application where you can load the memory with currency codes and its number of decimal places
+ It uses redis database to load the currency codes and number of decimal places in memory
+ The loadcache is a microservice in PYTHON framework.
> loadcache can be accessed via following techniques
- [x] **Terminal** (standalone terminal application)


<a name="prerequiste"/> 

## Prerequisite


1. Should have conda installed

    https://www.digitalocean.com/community/tutorials/how-to-install-anaconda-on-ubuntu-18-04-quickstart
    refer this for installation till step - 8

2. Should install redis database
       
       in fortiate/build/databases/
       
    inside Databases folder open terminal
       
       wget http://download.redis.io/releases/redis-5.0.6.tar.gz
       tar xzf redis-5.0.6.tar.gz
       cd redis-5.0.6
       make
       src/redis-server 
 

<a name="input"/> 

## Input

+ currency codes and its number of decimal places are pre-defined for now

<a name="output"/>

## Output

+ Output is a redis hash-map containing key and value pair
+ By mentioning the hash-map name followed by the currency code one can 
get the number of decimal places for that particular currency code 

<a name="dependancy"/>

## Dependency
> redis-database

<a name="limitation"/>

## Limitation

+ Currently the currency code and number of decimals are hard coded and 
in future we will get the currency codes and number of decimal places 
from an api

<a name="getting_the_code"/>

## Getting the code
    
+ Should open command prompt in the python workspace direcrory
+ If you already have loadcache folder in the python workspace then type    
        
      git pull
    inside the loadcache folder on terminal
    
+ else type
    
      git clone https://github.com/fortiate/loadcache.git 

    
+ Type the following command in the command prompt inside the folder containing
    
> redisCurrencyCodeDecimalsInserter.py
    
    conda env list
    conda activate <your environment name>
    conda activate Fortiate_env
    
+ Then you should see a environment created as (Fortiate_env)

> Then inside that fortiate_env type

    conda install redis


<a name="how_to_run"/>

## How To Run
+ Terminal

        python3 redisCurrencyCodeDecimalsInserter.py

<a name="how_to_access"/>

## How To Access

<a name="for-accessing-terminalpy"/>

+ ##### For Accessing redisCurrencyCodeDecimalsInserter.py

    + redisCurrencyCodeDecimalsInserter.py creates a hash-map named : currencyCodeMapping 
 
    + currencyCodeMapping hash-map has keys as currency codes and values as number of decimal places
    

+ ##### accessing the hash-map by python 
        
        redisClient.hgetall('currencyCodeMapping')
        redisClient.hget('currencyCodeMapping','356') 
 
+ ##### accessing the hash-map by redis
 
        hgetall currencyCodeMapping
        hget currencyCodeMapping <currency code>

+ ##### accessing the hash-map by java

Installation

how to set up Redis Java driver.

    You need to download the jar from the path Download jedis.jar. Make sure to download the latest release of it.

    You need to include the jedis.jar into your classpath.
    
    import redis.clients.jedis.Jedis; 

refer [Redis Java Keys Example] -> https://www.tutorialspoint.com/redis/redis_java.htm
