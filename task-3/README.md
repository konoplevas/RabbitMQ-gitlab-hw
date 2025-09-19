docker-compose up -d
chmod +x cluster-setup.sh
./cluster-setup.sh
# Отправить сообщение на ноду 1
python producer.py 5672

# Остановить ноду 1
docker-compose stop rabbitmq1

# Получить сообщение с ноды 2
python consumer-ha.py 5673
Нода 1: http://localhost:15672

Нода 2: http://localhost:15673
