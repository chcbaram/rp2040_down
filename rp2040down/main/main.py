import os
import sys
import time
import serial
import argparse
import platform
import rp2040down


root_path = os.path.dirname(rp2040down.__file__)



def open_port(port, baudrate=1200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False):
    ser = serial.Serial()

    ser.port = port
    ser.baudrate = baudrate
    ser.bytesize = bytesize
    ser.parity = parity
    ser.stopbits = stopbits
    ser.timeout = timeout
    ser.xonxoff = xonxoff
    ser.rtscts = rtscts
    ser.dsrdtr = dsrdtr

    try:      
      ser.open()    
      ser.close()    
    except:
      pass
    return ser

def show_help():
  print(' ')
  print('ex) rp2040down -f esp32_fw [-p com1]')

def get_tool_path():
  tool_path = None
  print('System  : ' + platform.system())
  print('Machine : ' + platform.machine())
  if platform.system() == "Windows":
    tool_path = root_path + '/tools/win/'
  else:
    if platform.system() == "Darwin":
      tool_path = root_path + '/tools/mac/'
      os.chmod (tool_path + 'picotool', 755)
      os.chmod (tool_path + 'rp2040load', 755)
    else:
      print('error')      
      print('  Not Supported System')
      exit()
  return tool_path

def main():
  print('Version : 1.0.0')
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--port', help=' com1       ')
  parser.add_argument('-f', '--file', help=' File Name  ')

  args = parser.parse_args()

  tool_path = get_tool_path()

  if args.file is None:
    print('error')
    print('  -f : No input file')
    show_help()
    exit()

    
  if args.port is not None:  
    open_port(args.port)
    print("reset pico..")   
    time.sleep(0.5)  

  file_name = os.getcwd() + '/' + args.file
  os.chdir(tool_path)
  os.system(tool_path + 'rp2040load' + " -v -D " + file_name)


if __name__ == '__main__':
  main()



  