# built upon https://github.com/mk-gurucharan/Social-Distancing-Detector

import numpy as np
import cv2
import imutils
import time

# global variables
LABELS = open('../yolo/coco.names').read().strip().split("\n")
net = cv2.dnn.readNetFromDarknet('../yolo/yolov3.cfg', '../yolo/yolov3.weights')
input_file = "../video/virat.mp4"
output_file = "../video/output.mp4"
frame_counter = 0
cap = cv2.VideoCapture(input_file)


# TODO: Display footage in real time
# TODO: Use threads for better performance
def check(a, b):
    dist = ((a[0] - b[0]) ** 2 + 550 / ((a[1] + b[1]) / 2) * (a[1] - b[1]) ** 2) ** 0.5
    calibration = (a[1] + b[1]) / 2
    if 0 < dist < 0.25 * calibration:
        return True
    else:
        return False


def getOutputLayerNames():
    ln = net.getLayerNames()
    return [ln[i - 1] for i in net.getUnconnectedOutLayers()]


def detectPerson(layers, w, h):
    confidences = []
    outline = []

    for output in layers:
        for detection in output:
            scores = detection[5:]
            maxi_class = np.argmax(scores)
            confidence = scores[maxi_class]
            if LABELS[maxi_class] == "person":
                if confidence > 0.5:
                    box = detection[0:4] * np.array([w, h, w, h])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    outline.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))

    return confidences, outline


def drawBox(box_line, outline, frame):
    if len(box_line) > 0:
        flat_box = box_line.flatten()
        pairs = []
        center = []
        status = []
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
    return frame


def image_process(image):
    global processedImg
    (H, W) = (None, None)
    frame = image.copy()
    if W is None or H is None:
        (H, W) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_outputs = net.forward(getOutputLayerNames())

    confidences, outline = detectPerson(layer_outputs, W, H)
    # perform non-maxima supression
    box_line = cv2.dnn.NMSBoxes(outline, confidences, 0.5, 0.3)

    frame = drawBox(box_line, outline, frame)
    processedImg = frame.copy()


if __name__ == '__main__':
    while True:

        ret, frame = cap.read()
        if not ret:
            break
        current_img = frame.copy()
        current_img = imutils.resize(current_img, width=480)
        video = current_img.shape
        frame_counter += 1

        # if frame_counter % 2 == 0 or frame_counter == 1:
        getOutputLayerNames()
        image_process(current_img)
        Frame = processedImg

        cv2.imshow('Output', Frame)

        keyRet = cv2.waitKey(1)
        if 0xFF == ord('s') or keyRet == 81 or keyRet == 113 or keyRet == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
