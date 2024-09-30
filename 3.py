import requests
import time
from threading import Thread


def get_html(link):
	r = requests.get(link)
	r.text
	print(len(link))
	

urls = ['http://www.google.com','https://ya.ru','https://ru.wikipedia.org','https://mail.ru/','https://www.rambler.ru/']

start_program1 = time.time()
jobs = [get_html(url) for url in urls]
finish_program1 = time.time()
t1= finish_program1 - start_program1

print('programm time : ',t1)

start_program2 = time.time()
theards = [Thread(target= get_html, args= (urls[i],)) for i in range(len(urls))]
for t in theards:
	t.start()
for t in theards:
	t.join()

finish_program2 = time.time()
t2= finish_program2 - start_program2
print('programm time : ',t2)