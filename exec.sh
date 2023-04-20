python3 pixeling.py
scp /home/orion/Code/Python/2DLighting/lightOrder pi@192.168.10.223:
scp /home/orion/Code/Python/2DLighting/lightParse.py pi@192.168.10.223:

exec ssh pi@192.168.10.223 sudo python3 lightParse.py 0.08 10
