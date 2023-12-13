import cv2 as cv

def detect(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 使用绝对路径加载级联分类器文件
    face_detector = cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray)

    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        label, confidence = recognizer.predict(roi_gray)

        # 打印预测标签和置信度
        print(f"Predicted Label: {label}, Confidence: {confidence}")

        # 绘制矩形框
        cv.rectangle(img, (x, y), (x + w, y + h), (100, 255, 0), 2)

        # 计算文本位置
        text_x = x + int(w / 2) - 50
        text_y = y - 20

        # 绘制标签和置信度信息
        label_text = f"Label: {label}, Confidence: {confidence:.2f}"
        cv.putText(img, label_text, (text_x, text_y), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv.imshow('result', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    path = './data/test/'
    detect(cv.imread(path + '9.jpg'))
