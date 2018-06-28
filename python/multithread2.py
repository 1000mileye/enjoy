import concurrent.futures
import collections
import sys
import time


def put():
  i = 0
  while True:
    try:
      q.append(['put item no.{}'.format(i)])
    except:
      print('put error', sys.exc_info()[0])
    i += 1
    if i == 10:
      q.append(['finish'])
      break


def get():
  while True:
    try:
      item = q.popleft()
      print('pop item:', item[0])
      if item[0] == 'finish':
        break
    except IndexError:
      time.sleep(1)
    except:
      print('get error', sys.exc_info()[0])


if __name__ == '__main__':
  q = collections.deque()
  executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
  executor.submit(get)
  put()
