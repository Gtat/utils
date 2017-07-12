import threading
import sys
import time
import multiprocessing
import os
import queue

flush = sys.stdout.flush



def process_func(name, shared_q):
  '''
  Multiprocessing cannot share the same code and glocal variables
  '''
  print('processes spawned')
  print('arg name: ', name)
  print('mod name: ', __name__)
  print('parent process: ', os.getppid())
  print('process id: ', os.getpid())
  flush()
  shared_q.put(os.getpid())
  time.sleep(3)


def thread_func(stop_event):
  '''
  Threads can share the same code and global variables
  '''
  while(not stop_event.is_set):
    name = threading.currentThread().getName()
    print("name: ", name)
    #local = threading.local()
    #local.my_name = name
    #threading.currentThread().my_Name = name
    flush()
    time.sleep(1)



if __name__ == '__main__':
  print("entering main...")
  q = multiprocessing.Queue()
  flush()

  #t1_stop_event = threading.Event()
  #t1 = threading.Thread(name='t1', target=hey, args=(t1_stop_event, ))
  #t2_stop_event = threading.Event()
  #t2 = threading.Thread(name='t2', target=hey, args=(t2_stop_event, ))
  p1 = multiprocessing.Process(target=process_func, args=('p1', q))
  p2 = multiprocessing.Process(target=process_func, args=('p2', q))

  print('main process starting threads/processes')
  flush()
  #t1.set()
  #t2.set()
  #t1.start()
  #t2.start()
  p1.start()
  p2.start()

  #t1.join()
  #t2.join()
  p1.join()
  p2.join()
  print("joined threads")
  flush()

  time.sleep(1)
  print()
  while True:
    try:
      x = q.get(timeout=0.1)
      print('got value: ', x)
      flush()
    except:
      print("get error: ", sys.exc_info()[0])
      break







