import cv2


def get_position(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f'x={x},y={y}')

original_img=cv2.imread(filename=r'/Users/mateusz/PycharmProjects/computer-vision-basics/assets/python_logo.png')

img=original_img.copy()


height, width =img.shape[0:2]


cv2.line(img,pt1=(0,0),pt2=(width,height),color=(0,255,0),thickness=5)
cv2.putText(img,text='Python Logo',org=(50,50),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.5,thickness=3,color=(0,225,0))


cv2.namedWindow('image')

cv2.setMouseCallback('image',get_position)


cv2.imshow(winname='image',mat=img)
cv2.waitKey(delay=0)