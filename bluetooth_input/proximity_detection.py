from bt_rssi import BluetoothRSSI
import time
import sys
import math
import random

sys.path.append('/home/reuben/csc4008-teamg/')
import alert.alert as Alert

BT_ADDR = '70:00:9E:73:1A:97'  # You can put your Bluetooth address here.  E.g: 'a4:70:d6:7d:ee:00'
BT_ADDRS = ['70:00:9E:73:1A:97', '44:C6:5D:57:66:70']
NUM_LOOP = 100

def print_usage():
    print( "Usage: python test_address.py <bluetooth_input-address> [number-of-requests]")

def create_alert(duration):
    print('Duration  = {}'.format(duration))
    camera = random.randint(0,2)
    Alert.sendBluetoothAlert(camera, 2, duration)

def main():
    if len(sys.argv) > 1:
        addr = sys.argv[1]
    elif BT_ADDR:
        addr = BT_ADDR
        addrs = BT_ADDRS
    else:
        print_usage()
        return
    if len(sys.argv) == 3:
        num = int(sys.argv[2])
    else:
        num = NUM_LOOP
    btrssi = BluetoothRSSI(addr=addr)
    btrssi_1 = BluetoothRSSI(addr = addrs[0])
    btrssi_2 = BluetoothRSSI(addr = addrs[1])

    n=3    #Path loss exponent(n) = 3
    c = 10   #Environment constant(C) = 10
    A0 = 2   #Average RSSI value at d0
    A0_1 = 1.5
    A0_2 = 0.4
    actual_dist = 37   #Static distance between transmitter and Receiver in cm
    act_dist = 61
    sum_error_1 = 0
    count = 0
    start_time = 0


    for i in range(1, num):
        if (btrssi_1.request_rssi() is not None and btrssi_2.request_rssi() is not None):
            rssi_bt_1 = float(btrssi_1.request_rssi()[0])
            rssi_bt_2 = float(btrssi_2.request_rssi()[0])
            if( (rssi_bt_1!=0 or rssi_bt_2!=0)):                    #reduces initial false values of RSSI using initial delay of 10sec
                count=count+1
                x_1 = float((rssi_bt_1-A0_1)/(-10*n))
                x_2 = float((rssi_bt_2-A0_2)/(-10*n))
                distance_1 = (math.pow(10,x_1) * 100) + c
                distance_2 = (math.pow(10,x_2) * 100) + c
                distance_1_2 = abs(distance_1 - distance_2)
                if (distance_1_2 < 50 and start_time <= 0):
                    start_time = time.clock()
                if (distance_1_2 >= 50 and start_time > 0):
                    end_time = time.clock()
                    print ("Duration" + str(end_time - start_time))
                    create_alert(end_time-start_time)
                    start_time = 0
                    end_time = 0
                print ("Approximate Distance:" + str(distance_1_2))
                print( "RSSI 1: " + str(rssi_bt_1))
                print ("RSSI 2: " + str(rssi_bt_2))
                print( "Count: " + str(count))
                print (" ")
            time.sleep(1)




if __name__ == '__main__':
    main()
