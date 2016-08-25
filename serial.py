if __name__ == '__main__':

  import serial
  import threading
  import sys

  print("sys default encoding: ", sys.getdefaultencoding())

  def reading(serial_port):
      print('reading rn')
      sys.stdout.flush()
      raw_data = serial_port.read(size=60)
      print ("raw data: ", raw_data)
      print()
      sys.stdout.flush()
      print ("decoded: ", raw_data.strip().decode()) #UnicodeDecodeError
      sys.stdout.flush()

  try:
    ser = serial.Serial("COM14", 9600, timeout=3) #read will block since timeout=None

  except serial.serialutil.SerialException:
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

    print("nuber of bytes written: ", ser.write('*A\r\n'.encode()))
    print('waiting on read thread')
    sys.stdout.flush()
    thread.join()

    print("serial closed")
    ser.close()


