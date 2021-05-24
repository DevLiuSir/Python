import time
from datetime import datetime


# ------------------ Python3 时间、时间戳	-------------------

def get_now_time_timestamp():
	'''
	获取现在时间，时间戳
	'''
	t = time.time()
	print(int(t))

def convert_time_to_timestamp(data_time):
	'''
	将时间转换成时间戳
	:param data_time: 时间
	'''
	# strptime(): 函数将时间转换成时间数组!!
	# mktime(): 函数将时间数组转换成时间戳!!

	# dt = '2018-08-08 11:11:11'

	# 将时间转换成时间数组
	timeArray = time.strptime(data_time, "%Y-%m-%d %H:%M:%S")
	print(timeArray)  	# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=8, tm_hour=11, tm_min=11, tm_sec=11, tm_wday=2, tm_yday=220, tm_isdst=-1)
	print("年份:", timeArray[0])  # 2018
	# 将时间数组转换成时间戳
	timestamp = time.mktime(timeArray)
	print(int(timestamp))  # 1533697871.0


def convert_timestamp_to_time(timestamp):
	'''
	将时间戳转换成时间
	:param timestamp: 时间戳
	'''
	# localtime()：函数将时间戳转化成时间数组
	# strftime()：函数重新格式化时间
	localtime = time.localtime(timestamp)
	print(localtime)  # time.struct_time(tm_year=2020, tm_mon=5, tm_mday=13, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=134, tm_isdst=0)
	dt = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
	print(dt)  # 2020-05-13 00:00:00


if __name__ == '__main__':

	# convert_timestamp_to_time(1533697871)
	# convert_timestamp_to_time(1618070400)

	convert_time_to_timestamp('2022-01-01 00:00:00')
	# get_now_time_timestamp()
