#!/bin/bash

echo "Setting up RabbitMQ HA Cluster..."
sleep 10

echo "Stopping app on node 2..."
docker exec rmq02 rabbitmqctl stop_app

echo "Resetting node 2..."
docker exec rmq02 rabbitmqctl reset

echo "Joining node 2 to cluster..."
docker exec rmq02 rabbitmqctl join_cluster rabbit@rmq01

echo "Starting app on node 2..."
docker exec rmq02 rabbitmqctl start_app

echo "Setting HA policy..."
docker exec rmq01 rabbitmqctl set_policy ha-all ".*" '{"ha-mode":"all"}'

echo "Cluster setup completed!"
echo "Cluster status:"
docker exec rmq01 rabbitmqctl cluster_status
docker exec rmq02 rabbitmqctl cluster_status
