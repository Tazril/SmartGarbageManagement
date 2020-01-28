# SmartGarbageManagement

## Description
We have made basically making a hardware+software based system for implementing smart Garbage sensor. There is a network of Arduino based sensors (slaves) attached to dustbin which would sense the fill percentage of the dustbin and send the data upon state change to a Raspberry Pi hosted AP (master) through zigbee and LoRa technology. Master would be an Access Point which would further send data to control room server with state of the dustbin.

<img src="https://github.com/Tazril/SmartGarbageManagement/blob/master/network-image.png" width="720" height="320" />

## Software
### Technology Stack:
* Docker
* Mosquitto
* Telegraf
* InfluxDB
* Grafana

We would be having a control room server which will be hosting container based applications with the help of Docker which wrap up software and its dependencies into a standardized unit for software development that includes everything it needs to run: code, runtime, system tools and libraries. We would make the server as the message broker with Mosquitto which implements the MQTT protocol for receiving/sending data. 

Telegraf (a plugin-driven server agent for collecting and sending metrics and events from databases, systems, and IoT sensors) is the intermediate software for receiving and forwarding data to InfluxDB. InfluxDB is a time series database useful to storage to fill percentage of the dustbins. Grafana is a visualiser tool for real time analysis.

##  Hardware
###  Hardware Used:
* Arduino nano
* Raspberry Pi 3
* XBee Radio Module
* LoRa Radio Module
* Ultrasonic Sensors
* Relay

Raspberry Pi here mimics the AP using the two radios: XBee and LoRa. Pi will receive data from various sensor units using either LoRa or XBee. We will be making a One such example asa smart garbage sensor connecting over a LoRa protocol to the wireless Access Point and a Docker based application executing on the Access Point( Raspberry Pi here ) sensing that the garbage can may be full and needs attention. Upon making such an inference, the application may choose to unlock a Zigbee lock attached to the door as well as turning on a Zigbee light in the location closest to the garbage bin.

## Additional Info
### MQTT (Message Queuing Telemetry Transport) broker
It is a message broker is an intermediary program that translates messages from the formal messaging protocol of the publisher to the formal messaging protocol of the receiver. Message broker programs are sometimes known as middleware .
This means that the publishing device, which might be a sensor, does not need to know anything about subscribers; It only has to send messages to the broker and then the broker manages and distributes the messages. Because subscribers and publishers never communicate directly with each other, there is less risk of a publisher being directly attacked by a subscriber. The message broker, on the other hand, can become a target for attacks if not configured properly.             

In our Project, Publisher is the arduino device that sends data to the broker i.e RaspberryPi. Subscriber is our control room which is subscribed to the topics sent by publisher.
We are using eclipse-mosquitto.

It is a lightweight publish and subscribe system where you can publish and receive messages as a client. MQTT is a simple messaging protocol, designed for constrained devices with low-bandwidth. The MQTT protocol is a good choice for wireless networks that experience varying levels of latency due to occasional bandwidth constraints or unreliable connections.

Eclipse Paho is a MQTT (Message Queuing Telemetry Transport) implementation. We are using the python implementation.

### Telegraf 
Telegraf is an agent written in Go for collecting performance metrics from the system it's running on and the services running on that system. The collected metrics are output to InfluxDB or or other supported data stores.
StatsD, collectd, Zabbix, Prometheus, and Sensu are the most popular alternatives and competitors to Telegraf.
Telegraf is a daemon** that can run on any server and collect a wide variety of metrics from the system (cpu, memory, swap, etc.), common services (mysql, redis, postgres, etc.), or third-party APIs (coming soon). It is plugin-driven for both collection and output of data so it is easily extendable.

** 
a daemon is a computer program that runs as a background process, rather than being under the direct control of an interactive user.
**

### InfluxDB:
InfluxDB is developed by InfluxData. It is an open source, big data, NoSQL database that allows for massive scalability, high availability, fast write, and fast read. As a NoSQL, InfluxDB stores time-series data, which has a series of data points over time.
Why build a database specifically for time series?
The implication was that a general SQL database can act as a TSDB by ordering on some time column. Or you can build on top of a distributed database like Cassandra. While it’s possible to use these solutions for solving time series problems, they’re incredibly time consuming and require significant development effor.


### Grafana 
Grafana is the open source analytics & monitoring solution for every database.
Grafana is an open source metric analytics & visualization suite. It is most commonly used for visualizing time series data for infrastructure and application analytics but many use it in other domains including industrial sensors, home automation, weather, and process control

### Docker
Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package.

## Bugs and Feedback

For bugs, feature requests, and discussion please use [GitHub Issues][issues].






 [issues]: https://github.com/Cyber-Labs/ism-app-android/issues
