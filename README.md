# Задание 1 - Установка
cd task-1
docker-compose up -d

# Задание 2 - Работа с сообщениями
cd task-2
pip install -r requirements.txt
python producer.py
python consumer.py

# Задание 3 - HA кластер
cd task-3
docker-compose up -d
chmod +x cluster-setup.sh
./cluster-setup.sh
python producer.py 5672
python consumer-ha.py 5673
RabbitMQ-homework/
├── task-1/          # Установка RabbitMQ
├── task-2/          # Работа с сообщениями
├── task-3/          # HA кластер
└── README.md        # Этот файл
