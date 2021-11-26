import sqlite3

import camera.camera_detection as cam_detector

if __name__ == '__main__':
    # camera1 = cam_detector.CameraDetection(0, 'http://210.148.114.53/-wvhttp-01-/GetOneShot?image_size=640x480'
    #                                         '&frame_count=1000000000')
    camera2 = cam_detector.CameraDetection(1, 'video/virat.mp4')
    # camera1.start()
    camera2.start()

    conn = sqlite3.connect('C:\\Users\\gclel\\AppData\\Local\\Packages\\2d9c71c5-52e8-4d37-b305'
                           '-126e7d9d8246_39mwtv5tpn0xy\\LocalState\\CameraStreams.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("SELECT stream FROM streams ORDER BY ID DESC LIMIT 1")
    previous = cursor.fetchone()[0]

    # camera3 = cam_detector.CameraDetection(2, row)
    # camera3.start()

    while True:
        cursor.execute("SELECT stream FROM streams ORDER BY ID DESC LIMIT 1")
        new = cursor.fetchone()[0]
        if new != previous:
            camera3 = cam_detector.CameraDetection(2, new)
            camera3.start()
            previous = new
        pass
