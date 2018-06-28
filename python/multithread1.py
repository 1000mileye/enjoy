import concurrent.futures
import queue
import sys
import time

q = queue.Queue()

def put():
  i = 0
  while True:
    try:
      q.put('put item no.{}'.format(i))
    except:
      print('put error', sys.exc_info()[0])
    i += 1
    if i == 10:
      q.put('finish')
      break


def get():
  while True:
    try:
      item = q.get()
      print('get item:', item)
      if item == 'finish':
        break
    except:
      print('get error', sys.exc_info()[0])


if __name__ == '__main__':
  executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
  executor.submit(put)
  executor.submit(get)
