
# print current time:--
from datetime import datetime
now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(current_time)
print(now)


import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)



# generate random
import random
x = random.randint(0,19)
y = random.randint(10,15)
print(x)
print(y)

