'''
• time module

• time tuple
  • A time tuple is a named tuple representing a date and time as separate fields
  • The fields of a time tuple include the year, month, day, hour, minute, second, day of the week, day of the year, and whether daylight saving time is in effect
  • A time tuple is represented as a tuple of integers in the following format: (year, month, day, hour, minute, second, day_of_week, day_of_year, is_dst)
  • Here, day_of_week is an integer representing the day of the week, with Monday = 0 and Sunday = 6
  • day_of_year is an integer representing the day of the year, with January 1 = 1
  • is_dst is an integer representing whether daylight saving time is in effect, with 0 for standard time and 1 for daylight saving time
  • 

• struct time
  • struct_time object is a tuple-like object representing a date and time, with each field represented by a named attribute
  • A struct_time object can be created using the time.struct_time() function
  • A struct_time object has the following fields:
    • tm_year   # year
    • tm_mon    # month (1-12)
    • tm_mday   # day of the month (1-31)
    • tm_hour   # hour (0-23)
    • tm_min    # minute (0-59)
    • tm_sec    # second (0-59)
    • tm_wday   # day of the week (0-6, Monday is 0)
    • tm_yday   # day of the year (1-366)
    • tm_isdst  # is daylight saving time in effect? (0 or 1)
  • Note that the tm_wday, tm_yday, and tm_isdst fields are automatically computed based on the other fields, and are not required when creating a struct_time object

• 
'''

import time


'''
• time()

• return the current time in seconds since the Epoch
• 
'''
print(time.time())              # 1683469145.9569552  (seconds)
print(time.time_ns())           # 1683480542388047500  (nano seconds)


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• ctime()

• convert a time expressed in seconds since the epoch to a string form
• 
'''
print(time.ctime())             # Sun May  7 20:14:12 2023
print(time.ctime(0))            # Thu Jan  1 05:30:00 1970
print(time.ctime(1000000000))   # Sun Sep  9 07:16:40 2001


print('-----------------------------------------------------------------------------------------------------------------------------------')

'''
• get_clock_info()

• args = monotonic, perf_counter, process_time, thread_time, time
• 
'''
print(time.get_clock_info('monotonic'))
# namespace(implementation='GetTickCount64()', monotonic=True, adjustable=False, resolution=0.015625)

print(time.get_clock_info('perf_counter'))
# namespace(implementation='QueryPerformanceCounter()', monotonic=True, adjustable=False, resolution=1e-07)

print(time.get_clock_info('process_time'))
# namespace(implementation='GetProcessTimes()', monotonic=True, adjustable=False, resolution=1e-07)

print(time.get_clock_info('thread_time'))
# namespace(implementation='GetThreadTimes()', monotonic=True, adjustable=False, resolution=1e-07)

print(time.get_clock_info('time'))
# namespace(implementation='GetSystemTimeAsFileTime()', monotonic=False, adjustable=True, resolution=0.015625)


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• gmtime()

• convert a time expressed in seconds since the epoch to a struct_time in UTC
• if secs is not provided or None, the current time as returned by time() is used
• 
'''
print(time.gmtime())    # time.struct_time(tm_year=2023, tm_mon=5, tm_mday=7, tm_hour=15, tm_min=4, tm_sec=51, tm_wday=6, tm_yday=127, tm_isdst=0)
print(time.gmtime(0))   # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• localtime()

• convert seconds since the Epoch to a time tuple expressing local time
• when 'seconds' is not passed in, convert the current time instead
• 
'''
print(time.localtime())   # time.struct_time(tm_year=2023, tm_mon=5, tm_mday=7, tm_hour=20, tm_min=34, tm_sec=51, tm_wday=6, tm_yday=127, tm_isdst=0)
print(time.localtime(0))  # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=5, tm_min=30, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• perf_counter()

• performance counter for benchmarking
• return the value (in fractional seconds) of a performance counter, i.e. a clock with the highest available resolution to measure a short duration
• 
'''
print(time.perf_counter())      # 425757.2005158  (seconds)
print(time.perf_counter_ns())   # 425757200595100  (namo seconds)


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• process_time()

• return the value (in fractional seconds) of the sum of the system and user CPU time of the current process
• 
'''
print(time.process_time())      # 0.03125  (seconds)
print(time.process_time_ns())   # 31250000  (namo seconds)


print('-----------------------------------------------------------------------------------------------------------------------------------')

'''
• thread_time()

• return the value (in fractional seconds) of the sum of the system and user CPU time of the current thread
• 
'''
print(time.thread_time())       # 0.015625
print(time.thread_time_ns())    # 15625000


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• sleep()

• suspend execution of the calling thread for the given number of seconds
• the argument may be a floating point number to indicate a more precise sleep time
• 
'''
print(time.sleep(5))


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• mktime()

• convert a time tuple in local time to seconds since the Epoch
• its argument is the struct_time or full 9-tuple 

• Windows specific error: 
  • time.struct_time(tm_year=2023, tm_mon=5, tm_mday=7, tm_hour=10, tm_min=30, tm_sec=0, tm_wday=0, tm_yday=127, tm_isdst=0)
  • structseq() takes at most 2 keyword arguments (9 given)
'''
print(time.mktime((2023, 5, 7, 10, 30, 0, 0, 0, 0)))                    # 1683435600.0
print(time.mktime(time.struct_time((2023, 5, 7, 10, 30, 0, 0, 0, 0))))  # 1683435600.0


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• strftime()

• convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument
• if t is not provided, the current time as returned by localtime() is used
• 
'''
print(time.strftime('%c', (2023, 5, 7, 10, 30, 0, 0, 0, 0)))      # Mon May  7 10:30:00 2023
print(time.strftime('%Y-%m-%d, %A, %H:%M:%S, %Z', time.localtime()))  # 2023-05-07, Sunday, 21:32:34, India Standard Time


'''
• References
• https://docs.python.org/3/library/time.html#time.strftime
• 
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• strptime()

• parse a string representing a time according to a format
• the return value is a struct_time as returned by gmtime() or localtime()
• 
'''

print(time.strptime('2023-05-07, Sunday, 21:32:34', '%Y-%m-%d, %A, %H:%M:%S'))
# time.struct_time(tm_year=2023, tm_mon=5, tm_mday=7, tm_hour=21, tm_min=32, tm_sec=34, tm_wday=6, tm_yday=127, tm_isdst=-1)


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• struct_time()

• the type of the time value sequence returned by gmtime(), localtime(), and strptime()
• it is an object with a named tuple interface: values can be accessed by index and by attribute name
• 
'''
print(time.struct_time((2023, 5, 7, 10, 30, 0, 0, 0, 0)))
# time.struct_time(tm_year=2023, tm_mon=5, tm_mday=7, tm_hour=10, tm_min=30, tm_sec=0, tm_wday=0, tm_yday=0, tm_isdst=0)


'''
• References
• https://docs.python.org/3/library/time.html#time.struct_time
• 
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• asctime()

• Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string of the following form: 'Sun Jun 20 23:21:05 1993'
• 
'''
print(time.asctime(time.localtime()))   # Sun May  7 23:36:14 2023


print('-----------------------------------------------------------------------------------------------------------------------------------')
