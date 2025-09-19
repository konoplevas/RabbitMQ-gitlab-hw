# Задание 1 - Установка
cd task-1
docker-compose up -d

<img width="1286" height="806" alt="1" src="https://github.com/user-attachments/assets/fbf89893-cc9a-4ce8-8f7f-28341e0e3e2a" />

# Задание 2 - Работа с сообщениями
cd task-2
pip install -r requirements.txt
python producer.py
python consumer.py

<img width="660" height="143" alt="2" src="https://github.com/user-attachments/assets/02d2b709-9991-430e-9495-f1fded09343a" />

<img width="1273" height="761" alt="2 1" src="https://github.com/user-attachments/assets/6c1205b2-9f73-41a1-89c3-7896165d4c74" />

# Задание 3 - HA кластер
cd task-3
docker-compose up -d
chmod +x cluster-setup.sh
./cluster-setup.sh
python producer.py 5672
python consumer-ha.py 5673

<img width="1279" height="763" alt="3" src="https://github.com/user-attachments/assets/e2528129-d0f6-42d3-98f8-099a3ca278e8" />

<img width="1278" height="756" alt="3 1" src="https://github.com/user-attachments/assets/5620acf3-f006-4d3d-9b2d-ec77b92b32d9" />

<img width="1277" height="770" alt="3 2" src="https://github.com/user-attachments/assets/b025a4af-1ad7-49bd-98b4-8d8d003245cf" />

<img width="1282" height="772" alt="3 3" src="https://github.com/user-attachments/assets/01b3759d-a385-4366-a2fc-0c58ed87275d" />


RabbitMQ-homework/
├── task-1/          # Установка RabbitMQ
├── task-2/          # Работа с сообщениями
├── task-3/          # HA кластер
└── README.md        # Этот файл
