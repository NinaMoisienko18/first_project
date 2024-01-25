import datetime as dt
from datetime import datetime as dtdt
import time as T

# print("Module Datatime")
# time_now = dtdt.now()
# print(time_now)

# ss = dtdt(2022, 7, 8, 14, 4, 50)
# print(ss)
#
# x = dt.date(2022, 7, 9)
# print(x)
# string = "01-02-23 12:23:56"
# x = dtdt.strptime(string, '%d-%m-%y %H:%M:%S')
# print(x)

x = T.time()
print(x)

xx = T.ctime(x)
print(xx)
print(type(xx))

for i in "HELLO NINA":
    print(i, end="")
    T.sleep(.5)
