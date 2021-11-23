from bt_proximity import BluetoothRSSI
import time
import sys
import math

BT_ADDR = '70:00:9E:73:1A:97'  # You can put your Bluetooth address here.  E.g: 'a4:70:d6:7d:ee:00'
BT_ADDRS = ['70:00:9E:73:1A:97', '44:C6:5D:57:66:70']
NUM_LOOP = 30

def print_usage():
    print "Usage: python test_address.py <bluetooth-address> [number-of-requests]"


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
    sum_error = 0
    sum_error_1 = 0
    count = 0


    for i in range(1, num):
        #rssi_bt = float(btrssi.get_rssi())
	rssi_bt_1 = float(btrssi_1.get_rssi())
	rssi_bt_2 = float(btrssi_2.get_rssi())
	print(rssi_bt_1)
	print(rssi_bt_2)
        if( (rssi_bt_1!=0 or rssi_bt_2!=0) and i>10):                    #reduces initial false values of RSSI using initial delay of 10sec
            count=count+1
            #x = float((rssi_bt-A0)/(-10*n))         #Log Normal Shadowing Model considering d0 =1m where
	    x_1 = float((rssi_bt_1-A0_1)/(-10*n))
	    x_2 = float((rssi_bt_2-A0_2)/(-10*n))
            #distance = (math.pow(10,x) * 100) + c
	    distance_1 = (math.pow(10,x_1) * 100) + c
	    distance_2 = (math.pow(10,x_2) * 100) + c
	    distance_1_2 = abs(distance_1 - distance_2)
            #error = abs(actual_dist - distance)
	    error_1 = abs(act_dist - distance_1_2)
            #sum_error = sum_error + error
	    sum_error_1 = sum_error_1 + error_1
            #avg_error = sum_error/count
	    avg_error_1 = sum_error_1/count
            #print "Average Error=  " + str(avg_error)
            #print "Error=  " + str(error)
            #print "Approximate Distance:" + str(distance)
	    print "Average Error 1 =  " + str(avg_error_1)
            print "Error 1=  " + str(error_1)
            print "Approximate Distance 1:" + str(distance_1_2)
            #print "RSSI: " + str(rssi_bt)
	    print "RSSI 1: " + str(rssi_bt_1)
	    print "RSSI 2: " + str(rssi_bt_2)
            print "Count: " + str(count)
            print " "
        time.sleep(1)




if __name__ == '__main__':
    main()

