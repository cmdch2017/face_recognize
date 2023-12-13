import os

import cv2 as cv
import numpy as np
from PIL import Image


def getImageAndLabels(path):
    # 使用绝对路径加载级联分类器文件
    face_detector = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    faceSamples = []
    ids = []
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    for imagePaths in imagePaths:
        PIL_img = Image.open(imagePaths).convert('L')
        # 图像转为数组
        img_numpy = np.array(PIL_img, 'uint8')
        faces = face_detector.detectMultiScale(img_numpy)
        # 获取每张图像的id
        id = int(os.path.split(imagePaths)[1].split('.')[0])
        for x, y, w, h in faces:
            faceSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)
    return faceSamples, ids


if __name__ == '__main__':
    path = './data/jm/'
    faces, ids = getImageAndLabels(path)
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))
    # 保存文件
    recognizer.write('trainer.yml')
