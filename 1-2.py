import time
from threading import Thread

start_program1 = time.time()

def get_thread(thread_name):
	time.sleep(1)
	print (f'{thread_name}')

list_names = ['thread_name_1','thread_name_2','thread_name_3','thread_name_4','thread_name_5']

for i in range(len(list_names)):
	get_thread(list_names[i])

finish_program1 = time.time()

t1= finish_program1 - start_program1
print('programm time : ',t1)

start_program2 = time.time()

theards = [Thread(target= get_thread, args= (list_names[i],)) for i in range(len(list_names))]

for t in theards:
	t.start()
for t in theards:
	t.join()

finish_program2 = time.time()

t2 = finish_program2 - start_program2
print('programm time : ', t2)