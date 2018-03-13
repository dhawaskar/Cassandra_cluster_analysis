# Cassandra_cluster_analysis
This project aims at doing performace analysis of cassandra with respect to delay,offset and read/write latency of data bases created in the 
clusters.

Install the following packages
sudo apt-get install python
sudo apt-get install python-pip
pip install matplotlib
sudo apt-get install python-tk


#To install cassandra manually
1. sudo apt-get update
2. sudo apt-get install default-jdk
3. wget http://apache.cs.utah.edu/cassandra/3.11.2/apache-cassandra-3.11.2-bin.tar.gz

or
1. echo "deb http://www.apache.org/dist/cassandra/debian 22x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
2. echo "deb-src http://www.apache.org/dist/cassandra/debian 22x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
3. gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D
4. gpg --export --armor F758CE318D77295D | sudo apt-key add -
5. gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00
6. gpg --export --armor 2B5C1B00 | sudo apt-key add -
7. gpg --keyserver pgp.mit.edu --recv-keys 0353B12C
8. gpg --export --armor 0353B12C | sudo apt-key add -
9. sudo apt-get update
10. sudo apt-get install cassandra


#Add docker
docker run --name cn2 -d -e CASSANDRA_BROADCAST_ADDRESS=192.168.89.3 -p 9042:9042 -e CASSANDRA_SEEDS=192.168.89.2 cassandra:latest
docker container start cn2
docker exec -it cn2 bash

#add stress test

cassandra-stress write n=10000                 \
  cl=quorum -mode native cql3 -rate threads=4 -schema keyspace="stress1"  \
  "replication(factor=2)" -pop seq=20001..30000 -log file=~/Test_10Kwrite_001.log    \
  -node 192.168.89.2,192.168.89.3,192.168.89.4
  
  #########
  Following needs to be modified in the cassandra.yaml file
  1. cluster name
  2. num_tokens should be set to some value
  3.seeds should be set to string of ip's
  4. rpc_address should be 0.0.0.0
  5.listen_address should be set ip of machine
  6. broadcast_rpc_address should be also set to local machine ip address
