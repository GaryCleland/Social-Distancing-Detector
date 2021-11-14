import camera.camera_detection as cam_detector

if __name__ == '__main__':
    camera1 = cam_detector.CameraDetection(0, 'http://210.148.114.53/-wvhttp-01-/GetOneShot?image_size=640x480'
                                              '&frame_count=1000000000')
    camera2 = cam_detector.CameraDetection(1, 'input/test.mp4')
    camera1.start()
    camera2.start()
    while True:
        pass
