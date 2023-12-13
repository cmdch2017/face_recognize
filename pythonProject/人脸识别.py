import cv2 as cv


def detect():
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 使用绝对路径加载级联分类器文件
    face_detector = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow('result', img)
    cv.waitKey(0)


img = cv.imread('1.jpeg')
if __name__ == '__main__':
    detect()
