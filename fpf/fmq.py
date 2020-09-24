from json import dumps
from kafka import KafkaProducer, KafkaConsumer
import sys
from fpf.flo import fortiatelog

global microservicename, microserviceacronym, hostenvkafka
global consumer, producer

filename = 'fmq.py'


# Function 1 - Setmicroservice
def setmicroservice(name, acronym, hostkafka):
    global microservicename, microserviceacronym, consumer, producer
    microservicename = name
    microserviceacronym = acronym
    producer = kafkaproducer(hostkafka)
    consumer = kafkaconsumer(hostkafka)
    return consumer


# Function 2 - SetConsumer
def kafkaconsumer(hostenvkafka):
    global microservicename, microserviceacronym, consumer, producer
    method = 'kafka consumer'
    try:
        consumer = KafkaConsumer(group_id=microservicename, bootstrap_servers=[hostenvkafka],
                                 auto_offset_reset='earliest')
        return consumer
    except Exception as e:
        fortiatelog(hostenvkafka, '401', 'info', filename, method)
        fortiatelog(e, '402', 'error', filename, method)
        sys.exit(1)


# Function 3 - Producer
def kafkaproducer(hostenvkafka):
    global microservicename, microserviceacronym, consumer, producer
    method = 'kafka producer'
    try:
        producer = KafkaProducer(bootstrap_servers=[hostenvkafka], value_serializer=lambda x: dumps(x).encode('utf-8'))
        return producer
    except Exception as e:
        fortiatelog(e, '403', 'error', filename, method)
        sys.exit(1)


# Function 4 - Send event to topic Imported
def sendeventtoimported(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoimported'
    try:
        producer.send('imported', value=fjoobj)
        fortiatelog("Event Sent to topic Imported", '404', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '405', 'error', filename, method)


# Function 5 - Send event to topic Processed
def sendeventtoprocessed(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoprocessed'
    try:
        producer.send('processed', value=fjoobj)
        fortiatelog("Event Sent to topic Processed", '406', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '407', 'error', filename, method)


# Function 6 - Send event to topic cleaned_for_parsing
def sendeventtocleanedforparsing(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleanedforparsing'
    try:
        producer.send('cleaned_for_parsing', value=fjoobj)
        fortiatelog("Event Sent to topic cleaned_for_parsing", '408', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '409', 'error', filename, method)


# Function 7 - Send event to topic cleaned_for_packing
def sendeventtocleanedforpacking(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleanedforpacking'
    try:
        producer.send('cleaned_for_packing', value=fjoobj)
        fortiatelog("Event Sent to topic cleaned_for_packing", '410', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '411', 'error', filename, method)


# Function 8 - Send event to topic cleaned_for_separating
def sendeventtocleanedforseparating(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleanedforseparating'
    try:
        producer.send('cleaned_for_separating', value=fjoobj)
        fortiatelog("Event Sent to topic cleaned_for_separating", '412', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '413', 'error', filename, method)


# Function 9 - Send event to topic cleaned_for_trm
def sendeventtocleanedfortrm(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleanedfortrm'
    try:
        producer.send('cleaned_for_trm', value=fjoobj)
        fortiatelog("Event Sent to topic cleaned_for_trm", '414', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '415', 'error', filename, method)


# Function 10 - Send event to topic Cleaned
def sendeventtocleaned(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleaned'
    try:
        producer.send('cleaned', value=fjoobj)
        fortiatelog("Event Sent to topic Cleaned", '416', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '417', 'error', filename, method)


# Function 11 - Send event to topic Labelled
def sendeventtolabelled(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtolabelled'
    try:
        producer.send('labelled', value=fjoobj)
        fortiatelog("Event Sent to topic Labelled", '418', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '419', 'error', filename, method)


# Function 12 - Send event to topic Separated
def sendeventtoseparated(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoseparated'
    try:
        producer.send('separated', value=fjoobj)
        fortiatelog("Event Sent to topic Separated", '420', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '421', 'error', filename, method)


# Function 13 - Send event to topic transactionmodelled
def sendeventtotransactionmodelled(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtotransactionmodelled'
    try:
        producer.send('transactionmodelled', value=fjoobj)
        fortiatelog("Event Sent to topic transactionmodelled", '422', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '423', 'error', filename, method)


# Function 14 - Send event to topic merchantmodelled
def sendeventtomerchantmodelled(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtomerchantmodelled'
    try:
        producer.send('merchantmodelled', value=fjoobj)
        fortiatelog("Event Sent to topic merchantmodelled", '424', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '425', 'error', filename, method)


# Function 15 - Send event to topic merchantforecasted
def sendeventtomerchantforecasted(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtomerchantforecasted'
    try:
        producer.send('merchantforecasted', value=fjoobj)
        fortiatelog("Event Sent to topic merchantforecasted", '426', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '427', 'error', filename, method)


# Function 16 - Send event to topic Exported
def sendeventtoexported(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoexported'
    try:
        producer.send('exported', value=fjoobj)
        fortiatelog("Event Sent to topic Exported", '428', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '429', 'error', filename, method)


# Function 17 - Send event to topic Email Notification
def sendeventtoemailnotifier(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoemailnotifier'
    try:
        producer.send('emailnotification', value=fjoobj)
        fortiatelog("Event Sent to topic emailnotification", '430', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '431', 'error', filename, method)


# Function 18 - Send event to topic Status Notification
def sendeventtostatusnotifier(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtostatusnotifier'
    try:
        producer.send('statusnotification', value=fjoobj)
        fortiatelog("Event Sent to topic statusnotification", '432', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '433', 'error', filename, method)


# Function 19 - Send event to topic parsed_data
def sendeventtoparseddata(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoparseddata'
    try:
        producer.send('parsed_data', value=fjoobj)
        fortiatelog("Event Sent to topic parsed_data", '434', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '435', 'error', filename, method)


# Function 20 - Send event to topic csvtoparseddatadone
def sendeventtocsvtoparseddatadone(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocsvtoparseddatadone'
    try:
        producer.send('csv_to_parsed_data_done', value=fjoobj)
        fortiatelog("Event Sent to topic csvtoparseddatadone", '436', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '437', 'error', filename, method)

# Function 21 - Send event to topic velocity_error
def sendeventtovelocityerror(fjoobj):
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtovelocityerror'
    try:
        producer.send('velocity_error', value=fjoobj)
        fortiatelog("Event Sent to topic sendeventtovelocityerror", '438', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '439', 'error', filename, method)



# Function 1 - subscribe to topic import
def subscribetotopicimported():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['imported'])
    except Exception as e:
        raise


# Function 2 - subscribe to topic processed
def subscribetotopicprocessed():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['processed'])
    except Exception as e:
        raise


# Function 3 - subscribe to topic cleaned_for_parsing
def subscribetotopiccleanedforparsing():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned_for_parsing'])
    except Exception as e:
        raise


# Function 4 - subscribe to topic cleaned_for_packing
def subscribetotopiccleanedforpacking():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned_for_packing'])
    except Exception as e:
        raise


# Function 5 - subscribe to topic cleaned_for_separating
def subscribetotopiccleanedforseparating():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned_for_separating'])
    except Exception as e:
        raise


# Function 6 - subscribe to topic cleaned_for_trm
def subscribetotopiccleanedfortrm():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned_for_trm'])
    except Exception as e:
        raise


# Function 7 - subscribe to topic cleaned
def subscribetotopiccleaned():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned'])
    except Exception as e:
        raise


# Function 8 - subscribe to topic separated
def subscribetotopicseparated():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['separated'])
    except Exception as e:
        raise


# Function 9 - subscribe to topic merchantmodelled
def subscribetotopicmerchantmodelled():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['merchantmodelled'])
    except Exception as e:
        raise


# Function 10 - subscribe to topic case7
def subscribetotopiccase7():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['case7'])
    except Exception as e:
        raise


# Function 11 - subscribe to topic parsed_data
def subscribetotopicparseddata():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['parsed_data'])
    except Exception as e:
        raise


# Function 12 - subscribe to topic csv_to_parsed_data_done
def subscribetotopiccsvtoparseddatadone():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['csv_to_parsed_data_done'])
    except Exception as e:
        raise

# Function 13 - subscribe to topic rupay_generated_data
def subscribetotopicrupaygenerateddata():
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['rupay_generated_data'])
    except Exception as e:
        raise

