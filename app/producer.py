from kafka import KafkaProducer

# Define server with port
from kafka.admin import NewTopic

#bootstrap_servers = ['host.docker.internal:9092']
bootstrap_servers = ['localhost:9092']

# Define topic name where the message will publish
topicName = 'example_topic'

# Initialize producer variable
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
producer.send(topicName, b'DOCKER HELLO')
producer.flush()
