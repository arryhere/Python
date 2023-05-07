import time


time_str = 'Sun, 07 May 2023 17:45:51 GMT'
struct_time = time.strptime(time_str, '%a, %d %b %Y %H:%M:%S %Z')
seconds = time.mktime(struct_time)    # 1683461751.0  (in local time)

gmt = time.strftime('%a, %d %b %Y %H:%M:%S %Z', time.gmtime(seconds))
local = time.strftime('%a, %d %b %Y %H:%M:%S %Z', time.localtime(seconds))

print(gmt)    # Sun, 07 May 2023 12:15:51 India Standard Time
print(local)  # Sun, 07 May 2023 17:45:51 India Standard Time


print('-----------------------------------------------------------------------------------------------------------------------------------')
