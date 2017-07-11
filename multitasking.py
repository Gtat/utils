import threading
import sys
import time
import multiprocessing


flush = sys.stdout.flush


def process_func():
  '''
  Multiprocessing cannot share the same code and glocal variables
  '''
  print('processing....')
  flush()
  time.sleep(3)

if __name__ == '__main__':

  print("entering main...")
  flush()

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
      time.sleep(3)

  #t1_stop_event = threading.Event()
  #t1 = threading.Thread(name='t1', target=hey, args=(t1_stop_event, ))
  #t2_stop_event = threading.Event()
  #t2 = threading.Thread(name='t2', target=hey, args=(t2_stop_event, ))
  p1 = multiprocessing.Process(target=process_func)
  p2 = multiprocessing.Process(target=process_func)

  print('starting threads/processes')
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



