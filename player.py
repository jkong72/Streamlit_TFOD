import streamlit as st
import cv2
import os


cap = cv2.VideoCapture('temp/out.avi')
width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)

print (width)
print (height)
print (fps)
print ('-'*15)
print (cap)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print ('v프레임 수신 불가')
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
    cv2.imshow('test', frame)
    if cv2.waitKey(20) & 0xFF == 27:
        break


# def main() :
#     vid_dir = 'temp/out.avi'
#     video1 = open(vid_dir, 'rb')
#     print ('-'*15)
#     print (video1)
#     print ('-'*15)
#     st.video(video1)

#     video_dir = 'temp'
#     files = os.listdir('temp')
#     file_dir = video_dir +'/'+ files[0]
#     print (file_dir)
#     video2 = open(file_dir, 'rb')
#     st.video(video2)

#     video3 = open('temp/간지나게 오토바이 타는법.mp4', 'rb')
#     st.video(video3)

#     video4 = open('temp/out.avi', 'rb')
#     st.video(video4)

    
#     print (video3)
#     print (video4)



# if __name__ == '__main__':
#     main()