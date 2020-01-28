//initialise docker
dockerd
//run mqtt
sudo docker run -it -p 1883:1883 -p 9001:9001 eclipse-mosquitto
//run influx db and create an external volume
sudo docker run -d -p 8086:8086 -v influxdb:/var/lib/influxdb --name influxdb influxdb
//exec influx
sudo docker exec -it influxdb influx
//setup account and sensor table
create database sensors
CREATE USER telegraf WITH PASSWORD 'telegraf' 
grant all on sensors to telegraf
// install and configure telegraph
sudo docker pull telegraf
//configure telegraph
sudo docker run --rm telegraf telegraf config > telegraf.conf
//add changes to tag [mqtt_consumer]
servers = ["tcp://localhost:1883"]

topics = [

  "sensors"

]

data_format = "influx"

// modify outputs.infuxdb


urls = ["http://raspberry_pi_ip:8086"]

database = "sensors"

skip_database_creation = true

username = "telegraf"

password = "telegraf"

//run telegraf
sudo docker run  -v /home/taz/:/etc/telegraf:ro telegraf
