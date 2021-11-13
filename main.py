import camera.camera_detection as cam_detector

if __name__ == '__main__':
    camera1 = cam_detector.CameraDetection('video/test.mp4', 0)
    camera2 = cam_detector.CameraDetection('video/virat.mp4', 1)
    camera1.start()
    print("here")
    camera2.start()
    while True:
        pass
