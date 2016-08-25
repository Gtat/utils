if __name__ == '__main__':

  import serial
  import threading
  import sys
  import time
  
  print("sys default encoding: ", sys.getdefaultencoding())

  def reading(serial_port):
      print('reading rn')
      sys.stdout.flush()
      raw_data = serial_port.read(size=98)
      print ("raw data: ", raw_data)
      print()
      sys.stdout.flush()
      #print ("decoded: ", raw_data.strip().decode()) #UnicodeDecodeError
      #sys.stdout.flush()

  try:
    ser = serial.Serial("COM16", 9600, timeout=5) #read will block since timeout=None

  except serial.SerialException:
    print('exception raised')

  else:
    print(ser.name)
    if ser.isOpen():
      print('serial is open!')

    thread = threading.Thread(target=reading, args=(ser,))
    thread.start()

    #print("heallo".encode('utf-8'))
    #print('@=B'.encode('utf-8'))
    #print("new line \n")
    #sys.stdout.flush()

    print("number of bytes written: ", ser.write('*@=B\r\n'.encode()))
    #print("number of bytes written: ", ser.write('*@=@\r\n'.encode()))
    #print("number of bytes written: ", ser.write('C\r\n'.encode()))
    time.sleep(.1)
    print("number of bytes written: ", ser.write('B\r\n'.encode()))


    print('waiting on read thread')
    sys.stdout.flush()
    thread.join()

    print("serial closed")
    ser.close()


