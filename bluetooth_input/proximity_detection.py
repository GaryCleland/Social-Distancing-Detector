from bt_rssi import BluetoothRSSI
import time
import sys
import math
import random

sys.path.append('/home/reuben/csc4008-teamg/')
import alert.alert as Alert

BT_ADDRS = ['a0:28:ed:c4:57:08', '90:CD:B6:0B:B8:36']  # Bluetooth addresses of devices to be detected
NUM_LOOP = 1000


def print_usage():
    print("Usage: python test_address.py <bluetooth_input-address> [number-of-requests]")


def create_alert(duration):
    print('Duration  = {}'.format(duration))
    camera = random.randint(0, 2)
    Alert.sendBluetoothAlert(camera, 2, duration)
    print('Alert generated and sent to database.')


def main():
    if BT_ADDRS:
        addrs = BT_ADDRS
    else:
        print_usage()
        return
    if len(sys.argv) == 3:
        num = int(sys.argv[2])
    else:
        num = NUM_LOOP
    btrssi_1 = BluetoothRSSI(addr=addrs[0])
    btrssi_2 = BluetoothRSSI(addr=addrs[1])

    n = 3  # Path loss exponent(n) = 3
    c = 10  # Environment constant(C) = 10
    a0_device_1 = 1.5  # Average RSSI value of first device value at 1m
    a0_device_2 = 0.4  # Average RSSI value of second device value at 1m
    start_time = 0

    for i in range(1, num):
        if btrssi_1.request_rssi() is not None and btrssi_2.request_rssi() is not None:
            rssi_device_1 = float(btrssi_1.request_rssi()[0])
            rssi_device_2 = float(btrssi_2.request_rssi()[0])
            if rssi_device_1 != 0 or rssi_device_2 != 0:  # Ensures at least 1 devices has a non 0 RSSI value
                x_device_1 = float((rssi_device_1 - a0_device_1) / (-10 * n))
                x_device_2 = float((rssi_device_2 - a0_device_2) / (-10 * n))
                distance_device_1 = (math.pow(10, x_device_1) * 100) + c
                distance_device_2 = (math.pow(10, x_device_2) * 100) + c
                distance_between_devices = abs(distance_device_1 - distance_device_2)
                if distance_between_devices < 20 and start_time <= 0:
                    start_time = time.perf_counter()
                if distance_between_devices >= 20 and start_time > 0:
                    end_time = time.perf_counter()
                    create_alert(end_time - start_time)
                    start_time = 0
                    end_time = 0
                print("RSSI 1: " + str(rssi_device_1))
                print("RSSI 2: " + str(rssi_device_2))
                print("Approximate Distance:" + str(distance_between_devices))
                print(" ")
            time.sleep(1)


if __name__ == '__main__':
    main()
