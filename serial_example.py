if __name__ == '__main__':

  import serial
  import serial.tools.list_ports
  import threading
  import sys
  import time


  def reading(serial_port, stop_event, size):
      print('reading rn')
      sys.stdout.flush()
      while(not stop_event.is_set()):
        raw_data = serial_port.read(size=size)
        print()
        print ("raw data: ", raw_data)
        sys.stdout.flush()
        print ("decoded: ", raw_data.strip().decode()) #UnicodeDecodeError
        sys.stdout.flush()


  print("sys default encoding: ", sys.getdefaultencoding())
  devs = serial.tools.list_ports.comports()

  print("Choose from the connecting ports")
  for dev in devs:
      print("\t", dev.device)

  com = str(input("which port do you want to open> "))
  baudrate = int(input("what is the baudrate> "))
  read_timeout = int(input("what is read timeout (input 0 to wait forever)> "))
  if (read_timeout == 0):
      read_timeout = None
  print("openning ", com, "with baudrate ", baudrate, " and read timouet=", read_timeout)

  try:
    ser = serial.Serial(com, baudrate, timeout=read_timeout) #read will block if timeout=None
  except serial.SerialException:
    print('exception raised')
  else:
    print(ser.name)
    if ser.isOpen():
      print('serial is open!')

    size = int(input("what is the read buffer size in bytes> "))
    thread_stop = threading.Event()
    thread = threading.Thread(target=reading, args=(ser, thread_stop, size))
    thread.start()


    while(1):

        query = str(input("type your query> "))
        wr_term = int(input("write terminator: input 0 for CR and 1 for CRLF> "))
        if (wr_term):
            wr_term = '\r\n'
        else:
            wr_term = '\r'
        if (query == "exit"):
            thread_stop.set()
            break
        else:
            print("number of bytes written: ", ser.write((query + wr_term).encode()))


    print('waiting on read thread')
    sys.stdout.flush()
    thread.join()

    print("serial is closing")
    sys.stdout.flush()
    ser.close()


