import streamlit as st
import os

def main() :
    vid_dir = 'temp\\out.avi'
    video = open(str(vid_dir), 'rb')
    st.video(video)
    print ('-'*15)
    print (video)
    print ('-'*15)

    video_dir = 'temp'
    files = os.listdir('temp')
    file_dir = video_dir +'/'+ files[0]
    video = open(str(vid_dir), 'rb')
    st.video(video)

if __name__ == '__main__':
    main()