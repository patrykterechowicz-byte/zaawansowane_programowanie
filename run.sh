rm queue.lock queue.txt
python producer.py queue.txt
sleep 5
python consumer.py queue.txt &
python consumer.py queue.txt &
python consumer.py queue.txt &
python consumer.py queue.txt &
python consumer.py queue.txt &
