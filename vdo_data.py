import cv2

# 영상 데이터에 대한 좌표 추출 준비과정
cap = cv2.VideoCapture('test_data/test2.mp4')
num = 0

# Mouse Callback함수; 영상 데이터에 대한 좌표 추출
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret:
		cv2.imshow('frame', frame)
		#  이미지의 각 이름을 자동으로 지정
		path = 'data/vdo_data/img_' + str(num) + '.jpg'
		cv2.imwrite(path, frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	num += 1
cap.release()
cv2.destroyAllWindows()