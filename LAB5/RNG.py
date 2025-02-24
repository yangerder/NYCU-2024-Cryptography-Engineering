import os

random_data = os.urandom(1024*1024)


with open('random.bin', 'wb') as file:
    file.write(random_data)
