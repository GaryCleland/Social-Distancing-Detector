# built upon https://github.com/mk-gurucharan/Social-Distancing-Detector
from threading import Thread

import cv2
import imutils
import numpy as np
import time
import copy

import alert.alert as Alert


def check(a, b):
    dist = ((a[0] - b[0]) ** 2 + 550 / ((a[1] + b[1]) / 2) * (a[1] - b[1]) ** 2) ** 0.5
    calibration = (a[1] + b[1]) / 2
    if 0 < dist < 0.25 * calibration:
        return True
    else:
        return False


class CameraDetection:
    def __init__(self, cam, video_input):
        print(video_input)
        self.cap = cv2.VideoCapture(video_input)
        self.cam = cam
        self.LABELS = open('yolo/coco.names').read().strip().split("\n")
        self.net = cv2.dnn.readNetFromDarknet('yolo/yolov3.cfg', 'yolo/yolov3.weights')
        self.output_file = "video/output.mp4"
        self.frame_counter = 0
        self.duration = [0] * 10
        self.groups = [set() for i in range(18)]
        self.frame_rate = 0

    def start(self):
        new_thread = Thread(target=self.run_detector, args=())
        new_thread.daemon = True
        new_thread.start()
        return self

    def getOutputLayerNames(self):
        ln = self.net.getLayerNames()
        return [ln[i - 1] for i in self.net.getUnconnectedOutLayers()]

    def createGroups(self, vio, i, j):
        if i not in vio and j not in vio:
            for x in range(0, len(self.groups)):
                if len(self.groups[x]) == 0:
                    self.groups[x].add(i)
                    self.groups[x].add(j)
                    break
        else:
            for x in self.groups:
                if i in x or j in x:
                    x.add(i)
                    x.add(j)
                    break

    def detectPerson(self, layers, w, h):
        confidences = []
        outline = []

        for output in layers:
            for detection in output:
                scores = detection[5:]
                maxi_class = np.argmax(scores)
                confidence = scores[maxi_class]
                if self.LABELS[maxi_class] == "person":
                    if confidence > 0.5:
                        box = detection[0:4] * np.array([w, h, w, h])
                        (centerX, centerY, width, height) = box.astype("int")
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))
                        outline.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))

        return confidences, outline

    def createAlert(self, frames, group_size):
        duration = frames / self.frame_rate
        if duration > 0:
            Alert.sendAlert(self.cam, group_size, frames / self.frame_rate)

    def getDuration(self, temp):
        for x in range(0, len(self.groups)):
            if len(self.groups[x]) == len(temp[x]) and len(self.groups[x]) != 0:
                self.duration[x] += 1
            elif len(self.groups[x]) != len(temp[x]) and len(temp[x]) != 0:
                self.createAlert(self.duration[x], len(temp[x]))
                self.duration[x] = 0

    def drawBox(self, box_line, outline, frame):
        if len(box_line) > 0:
            flat_box = box_line.flatten()
            pairs = []
            center = []
            status = []
            temp_group = copy.deepcopy(self.groups)
            self.groups = [set() for i in range(18)]
            violations = set()
            for i in flat_box:
                (x, y) = (outline[i][0], outline[i][1])
                (w, h) = (outline[i][2], outline[i][3])
                center.append([int(x + w / 2), int(y + h / 2)])
                status.append(False)
            for i in range(len(center)):
                for j in range(len(center)):
                    close = check(center[i], center[j])

                    if close:
                        pairs.append([center[i], center[j]])
                        self.createGroups(violations, tuple(center[i]), tuple(center[j]))
                        violations.add(tuple(center[i]))
                        violations.add(tuple(center[j]))
                        status[i] = True
                        status[j] = True

            index = 0
            for i in flat_box:
                (x, y) = (outline[i][0], outline[i][1])
                (w, h) = (outline[i][2], outline[i][3])
                if status[index]:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 150), 2)
                elif not status[index]:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                index += 1
            for h in pairs:
                cv2.line(frame, tuple(h[0]), tuple(h[1]), (0, 0, 255), 2)
            self.getDuration(temp_group)
        return frame

    def image_process(self, image):
        (H, W) = (None, None)
        frame = image.copy()
        if W is None or H is None:
            (H, W) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        layer_outputs = self.net.forward(self.getOutputLayerNames())

        confidences, outline = self.detectPerson(layer_outputs, W, H)
        # perform non-maxima suppression
        box_line = cv2.dnn.NMSBoxes(outline, confidences, 0.5, 0.3)

        return self.drawBox(box_line, outline, frame)

    def run_detector(self):
        while True:
            start_time = time.time()
            frame = None
            while frame is None:
                ret, frame = self.cap.read()
            if not ret:
                break
            current_img = frame.copy()
            current_img = imutils.resize(current_img, width=480)
            video = current_img.shape
            self.frame_counter += 1

            # if frame_counter % 2 == 0 or frame_counter == 1:
            self.getOutputLayerNames()
            Frame = self.image_process(current_img)

            cv2.imshow('Output', Frame)
            group_count = 0
            group_sizes = []
            for x in self.groups:
                if len(x) != 0:
                    group_count += 1
                    group_sizes.append(len(x))

            end_time = time.time()
            self.frame_rate = 1.0 / (end_time - start_time)

            keyRet = cv2.waitKey(1)
            if 0xFF == ord('s') or keyRet == 81 or keyRet == 113 or keyRet == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()
