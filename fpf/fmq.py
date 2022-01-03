"""
This module handles the event based environment configurations e.g. setting kafka consumer and producer parameters
"""
from json import dumps
from kafka import KafkaProducer, KafkaConsumer
import sys
from fpf.flo import fortiatelog

global microservicename, microserviceacronym, hostenvkafka
global consumer, producer

filename = 'fmq.py'


# Function 1 - Setmicroservice
def setmicroservice(name, acronym, hostkafka):
    """
    This function sets the microservice name, acronym and the kafka host
    :param name:
    :param acronym:
    :param hostkafka:
    :return:
    """
    global microservicename, microserviceacronym, consumer, producer
    microservicename = name
    microserviceacronym = acronym
    producer = kafkaproducer(hostkafka)
    consumer = kafkaconsumer(hostkafka)
    return consumer


# Function 2 - SetConsumer
def kafkaconsumer(hostenvkafka_local):
    """
    This function sets the kafka environment variables
    :param hostenvkafka_local: 
    :return: 
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'kafka consumer'
    try:
        consumer = KafkaConsumer(group_id=microservicename, bootstrap_servers=[hostenvkafka_local],
                                 auto_offset_reset='earliest')
        return consumer
    except Exception as e:
        fortiatelog(hostenvkafka_local, '401', 'info', filename, method)
        fortiatelog(e, '402', 'error', filename, method)
        sys.exit(1)


# Function 3 - Producer
def kafkaproducer(hostenvkafka_local):
    """
    This function sets the kafka producer details
    :param hostenvkafka_local:
    :return:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'kafka producer'
    try:
        producer = KafkaProducer(bootstrap_servers=[hostenvkafka_local],
                                 value_serializer=lambda x: dumps(x).encode('utf-8'))
        return producer
    except Exception as e:
        fortiatelog(e, '403', 'error', filename, method)
        sys.exit(1)


# Function 4 - Send event to topic Imported
def sendeventtoimported(fjoobj):
    """
    This function sends an event to the topic "imported" - to start data transfer from watcher to preprocessor
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoimported'
    try:
        producer.send('imported', value=fjoobj)
        fortiatelog("Event Sent to topic Imported", '404', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '405', 'error', filename, method)


# Function 5 - Send event to topic processed
def sendeventtoprocessed(fjoobj):
    """
    This function sends an event to the topic "processed" - to start data cleaning, from preprocessor to cleaner
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoprocessed'
    try:
        producer.send('processed', value=fjoobj)
        fortiatelog("Event Sent to topic Processed", '406', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '407', 'error', filename, method)


# Function 6 - Send event to topic cleaned_for_parsing
def sendeventtocleanedforparsing(fjoobj):
    """
    This function sends an event to the topic "cleaned_for_parsing" - to start parsing
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleanedforparsing'
    try:
        producer.send('cleaned_for_parsing', value=fjoobj)
        fortiatelog("Event Sent to topic cleaned_for_parsing", '408', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '409', 'error', filename, method)


# Function 7 - Send event to topic cleaned_for_packing
def sendeventtocleanedforpacking(fjoobj):
    """
    This function sends an event to the topic "cleaned_for_packing" - to start packing
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleanedforpacking'
    try:
        producer.send('cleaned_for_packing', value=fjoobj)
        fortiatelog("Event Sent to topic cleaned_for_packing", '410', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '411', 'error', filename, method)


# Function 8 - Send event to topic cleaned_for_separating
def sendeventtocleanedforseparating(fjoobj):
    """
    This function sends an event to the topic "cleaned_for_separating" - to start separating file merchant wise
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleanedforseparating'
    try:
        producer.send('cleaned_for_separating', value=fjoobj)
        fortiatelog("Event Sent to topic cleaned_for_separating", '412', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '413', 'error', filename, method)


# Function 9 - Send event to topic cleaned_for_trm
def sendeventtocleanedfortrm(fjoobj):
    """
    This function sends an event to the topic "cleaned_for_trm" - to start trm
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleanedfortrm'
    try:
        producer.send('cleaned_for_trm', value=fjoobj)
        fortiatelog("Event Sent to topic cleaned_for_trm", '414', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '415', 'error', filename, method)


# Function 10 - Send event to topic cleaned
def sendeventtocleaned(fjoobj):
    """
    This function sends an event to the topic "cleaned" - to start next step
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocleaned'
    try:
        producer.send('cleaned', value=fjoobj)
        fortiatelog("Event Sent to topic Cleaned", '416', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '417', 'error', filename, method)


# Function 11 - Send event to topic labelled
def sendeventtolabelled(fjoobj):
    """
    This function sends an event to the topic "labelled" - to start labelling
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtolabelled'
    try:
        producer.send('labelled', value=fjoobj)
        fortiatelog("Event Sent to topic Labelled", '418', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '419', 'error', filename, method)


# Function 12 - Send event to topic separated
def sendeventtoseparated(fjoobj):
    """
    This function sends an event to the topic "separated" - to start next step after separating data
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoseparated'
    try:
        producer.send('separated', value=fjoobj)
        fortiatelog("Event Sent to topic Separated", '420', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '421', 'error', filename, method)


# Function 13 - Send event to topic transactionmodelled
def sendeventtotransactionmodelled(fjoobj):
    """
    This function sends an event to the topic "transactionmodelled" - to confirm modelling is completed
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtotransactionmodelled'
    try:
        producer.send('transactionmodelled', value=fjoobj)
        fortiatelog("Event Sent to topic transactionmodelled", '422', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '423', 'error', filename, method)


# Function 14 - Send event to topic merchantmodelled
def sendeventtomerchantmodelled(fjoobj):
    """
    This function sends an event to the topic "merchantmodelled" - to confirm modelling is completed
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtomerchantmodelled'
    try:
        producer.send('merchantmodelled', value=fjoobj)
        fortiatelog("Event Sent to topic merchantmodelled", '424', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '425', 'error', filename, method)


# Function 15 - Send event to topic merchantforecasted
def sendeventtomerchantforecasted(fjoobj):
    """
    This function sends an event to the topic "merchantforecasted" - to confirm forecasting is completed
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtomerchantforecasted'
    try:
        producer.send('merchantforecasted', value=fjoobj)
        fortiatelog("Event Sent to topic merchantforecasted", '426', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '427', 'error', filename, method)


# Function 16 - Send event to topic exported
def sendeventtoexported(fjoobj):
    """
    This function sends an event to the topic "exported" - to confirm data exporting is completed
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoexported'
    try:
        producer.send('exported', value=fjoobj)
        fortiatelog("Event Sent to topic Exported", '428', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '429', 'error', filename, method)


# Function 17 - Send event to topic Email Notification
def sendeventtoemailnotifier(fjoobj):
    """
    This function sends an event to the topic "emailnotification" - to ask notifier to shoot an email
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoemailnotifier'
    try:
        producer.send('emailnotification', value=fjoobj)
        fortiatelog("Event Sent to topic emailnotification", '430', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '431', 'error', filename, method)


# Function 18 - Send event to topic statusnotification
def sendeventtostatusnotifier(fjoobj):
    """
    This function sends an event to the topic "statusnotification" - to confirm forecasting is completed
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtostatusnotifier'
    try:
        producer.send('statusnotification', value=fjoobj)
        fortiatelog("Event Sent to topic statusnotification", '432', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '433', 'error', filename, method)


# Function 19 - Send event to topic rupay_parsed_data
def sendeventtoparseddata(fjoobj):
    """
    This function sends an event to the topic "rupay_parsed_data" - to confirm posting of parsed data
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoparseddata'
    try:
        producer.send('rupay_parsed_data', value=fjoobj)
        fortiatelog("Event Sent to topic parsed_data", '434', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '435', 'error', filename, method)


# Function 20 - Send event to topic csv_to_parsed_data_done
def sendeventtocsvtoparseddatadone(fjoobj):
    """
    This function sends an event to the topic "csv_to_parsed_data_done" - to confirm parsing of csv is done
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtocsvtoparseddatadone'
    try:
        producer.send('csv_to_parsed_data_done', value=fjoobj)
        fortiatelog("Event Sent to topic csvtoparseddatadone", '436', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '437', 'error', filename, method)


# Function 21 - Send event to topic velocity_error
def sendeventtovelocityerror(fjoobj):
    """
    This function sends an event to the topic "velocity_error" - to confirm error in calculating velocity
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtovelocityerror'
    try:
        producer.send('velocity_error', value=fjoobj)
        fortiatelog("Event Sent to topic sendeventtovelocityerror", '438', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '439', 'error', filename, method)


# Function 22 - Send event to topic start_labelling
def sendeventtostartlabelling(fjoobj):
    """
    This function sends an event to the topic "start_labelling" - to start labelling data
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtostartlabelling'
    try:
        producer.send('start_labelling', value=fjoobj)
        fortiatelog("Event Sent to topic start_labelling", '440', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '441', 'error', filename, method)


# Function 23 - Send event to topic start_training
def sendeventtostarttraining(fjoobj):
    """
    This function sends an event to the topic "start_training" - to start training data
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtostartlabelling'
    try:
        producer.send('start_training', value=fjoobj)
        fortiatelog("Event Sent to topic start_training", '440', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '441', 'error', filename, method)


# Function 24 - Send event to topic propensitymodelled
def sendeventtoprpensitymodelled(fjoobj):
    """
    This function sends an event to the topic "propensitymodelled" - to confirm propensity modelling is done
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoprpensitymodelled'
    try:
        producer.send('propensitymodelled', value=fjoobj)
        fortiatelog("Event Sent to topic propensitymodelled", '442', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '443', 'error', filename, method)


# Function 25 - Send event to topic merchant_transformed_data
def sendeventtomerchanttransformeddata(fjoobj):
    """
    This function sends an event to the topic "merchant_transformed_data" - to transform merchant data
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtomerchanttransformeddata'
    try:
        producer.send('merchant_transformed_data', value=fjoobj)
        fortiatelog("Event Sent to topic merchant_transformed_data", '444', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '445', 'error', filename, method)


# Function 26 - Send event to topic consumer_transformed_data
def sendeventtoconsumertransformeddata(fjoobj):
    """
    This function sends an event to the topic "consumer_transformed_data" - to transform consumer data
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtoconsumertransformeddata'
    try:
        producer.send('consumer_transformed_data', value=fjoobj)
        fortiatelog("Event Sent to topic consumer_transformed_data", '446', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '447', 'error', filename, method)


# Function 27 - Send event to topic transaction_transformed_data
def sendeventtotransactiontransformeddata(fjoobj):
    """
    This function sends an event to the topic "transaction_transformed_data" - to transform transaction data
    :param fjoobj:
    """
    global microservicename, microserviceacronym, consumer, producer
    method = 'sendeventtotransactiontransformeddata'
    try:
        producer.send('transaction_transformed_data', value=fjoobj)
        fortiatelog("Event Sent to topic transaction_transformed_data", '448', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '449', 'error', filename, method)


# Function 28 - subscribe to topic import
def subscribetotopicimported():
    """
    This function tells microservice to subscribe to event "imported"
    """
    method = 'subscribetotopicimported'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['imported'])
        fortiatelog("Successfully subscribed to topic : imported ", '450', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '451', 'error', filename, method)
        raise


# Function 29 - subscribe to topic processed
def subscribetotopicprocessed():
    """
    This function tells microservice to subscribe to event "processed"
    """
    method = 'subscribetotopicprocessed'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['processed'])
        fortiatelog("Successfully subscribed to topic : processed ", '452', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '453', 'error', filename, method)
        raise


# Function 30 - subscribe to topic cleaned_for_parsing
def subscribetotopiccleanedforparsing():
    """
    This function tells microservice to subscribe to event "cleaned_for_parsing"
    """
    method = 'subscribetotopiccleanedforparsing'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned_for_parsing'])
        fortiatelog("Successfully subscribed to topic : cleaned_for_parsing ", '454', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '455', 'error', filename, method)
        raise


# Function 31 - subscribe to topic cleaned_for_packing
def subscribetotopiccleanedforpacking():
    """
    This function tells microservice to subscribe to event "cleaned_for_packing"
    """
    method = 'subscribetotopiccleanedforpacking'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned_for_packing'])
        fortiatelog("Successfully subscribed to topic : cleaned_for_packing ", '456', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '457', 'error', filename, method)
        raise


# Function 32 - subscribe to topic cleaned_for_separating
def subscribetotopiccleanedforseparating():
    """
    This function tells microservice to subscribe to event "cleaned_for_separating"
    """
    method = 'subscribetotopiccleanedforseparating'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned_for_separating'])
        fortiatelog("Successfully subscribed to topic : cleaned_for_separating ", '458', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '459', 'error', filename, method)
        raise


# Function 33 - subscribe to topic cleaned_for_trm
def subscribetotopiccleanedfortrm():
    """
    This function tells microservice to subscribe to event "cleaned_for_trm"
    """
    method = 'subscribetotopiccleanedfortrm'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned_for_trm'])
        fortiatelog("Successfully subscribed to topic : cleaned_for_trm ", '460', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '461', 'error', filename, method)
        raise


# Function 34 - subscribe to topic cleaned
def subscribetotopiccleaned():
    """
    This function tells microservice to subscribe to event "cleaned"
    """
    method = 'subscribetotopiccleaned'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['cleaned'])
        fortiatelog("Successfully subscribed to topic : cleaned ", '462', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '463', 'error', filename, method)
        raise


# Function 35 - subscribe to topic separated
def subscribetotopicseparated():
    """
    This function tells microservice to subscribe to event "separated"
    """
    method = 'subscribetotopicseparated'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['separated'])
        fortiatelog("Successfully subscribed to topic : separated ", '464', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '465', 'error', filename, method)
        raise


# Function 36 - subscribe to topic merchantmodelled
def subscribetotopicmerchantmodelled():
    """
    This function tells microservice to subscribe to event "merchantmodelled"
    """
    method = 'subscribetotopicmerchantmodelled'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['merchantmodelled'])
        fortiatelog("Successfully subscribed to topic : merchantmodelled ", '466', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '467', 'error', filename, method)
        raise


# Function 37 - subscribe to topic case7
def subscribetotopiccase7():
    """
    This function tells microservice to subscribe to event "case7"
    """
    method = 'subscribetotopiccase7'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['case7'])
        fortiatelog("Successfully subscribed to topic : case7 ", '468', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '469', 'error', filename, method)
        raise


# Function 38 - subscribe to topic rupay_parsed_data
def subscribetotopicparseddata():
    """
    This function tells microservice to subscribe to event "rupay_parsed_data"
    """
    method = 'subscribetotopicparseddata'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['rupay_parsed_data'])
        fortiatelog("Successfully subscribed to topic : rupay_parsed_data ", '470', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '471', 'error', filename, method)
        raise


# Function 39 - subscribe to topic csv_to_parsed_data_done
def subscribetotopiccsvtoparseddatadone():
    """
    This function tells microservice to subscribe to event "csv_to_parsed_data_done"
    """
    method = 'subscribetotopiccsvtoparseddatadone'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['csv_to_parsed_data_done'])
        fortiatelog("Successfully subscribed to topic : csv_to_parsed_data_done ", '472', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '473', 'error', filename, method)
        raise


# Function 40 - subscribe to topic rupay_generated_data
def subscribetotopicrupaygenerateddata():
    """
    This function tells microservice to subscribe to event "rupay_generated_data"
    """
    method = 'subscribetotopicrupaygenerateddata'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['rupay_generated_data'])
        fortiatelog("Successfully subscribed to topic : rupay_generated_data ", '474', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '475', 'error', filename, method)
        raise


# Function 41 - subscribe to topic csv_to_parsed_data and start_labelling
def subscribetotopicparseddataandstartlabeller():
    """
    This function tells microservice to subscribe to event "csv_to_parsed_data_done" and "start_labelling"
    """
    method = 'subscribetotopicparseddataandstartlabeller'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['csv_to_parsed_data_done', 'start_labelling'])
        fortiatelog("Successfully subscribed to topic : csv_to_parsed_data_done, start_labelling ", '476', 'info',
                    filename, method)
    except Exception as e:
        fortiatelog(e, '477', 'error', filename, method)
        raise


# Function 42 - subscribe to topic start_training
def subscribetotopicstarttraining():
    """
    This function tells microservice to subscribe to event "start_training"
    """
    method = 'subscribetotopicstarttraining'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['start_training'])
        fortiatelog("Successfully subscribed to topic : start_training", '478', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '479', 'error', filename, method)
        raise


# Function 43 - subscribe to topic merchant_transformed_data
def subscribetotopicmerchanttransformeddata():
    """
    This function tells microservice to subscribe to event "merchant_transformed_data"
    """
    method = 'subscribetotopicmerchanttransformeddata'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['merchant_transformed_data'])
        fortiatelog("Successfully subscribed to topic : merchant_transformed_data", '480', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '481', 'error', filename, method)
        raise


# Function 44 - subscribe to topic consumer_transformed_data
def subscribetotopicconsumertransformeddata():
    """
    This function tells microservice to subscribe to event "consumer_transformed_data"
    """
    method = 'subscribetotopicconsumertransformeddata'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['consumer_transformed_data'])
        fortiatelog("Successfully subscribed to topic : consumer_transformed_data", '482', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '483', 'error', filename, method)
        raise


# Function 45 - subscribe to topic transaction_transformed_data
def subscribetotopictransactiontransformedddat():
    """
    This function tells microservice to subscribe to event "transaction_transformed_data"
    """
    method = 'subscribetotopictransactiontransformedddat'
    global microservicename, microserviceacronym, consumer, producer
    try:
        consumer.subscribe(['transaction_transformed_data'])
        fortiatelog("Successfully subscribed to topic : transaction_transformed_data", '484', 'info', filename, method)
    except Exception as e:
        fortiatelog(e, '485', 'error', filename, method)
        raise
