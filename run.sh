rm -f queue.lock queue.txt
python consumer.py queue.txt &
python consumer.py queue.txt &
python consumer.py queue.txt &
python consumer.py queue.txt &
python consumer.py queue.txt &
sleep 5

python producer.py queue.txt

for n in seq 100
do
    python producer.py queue.txt
done
