import streamlit as st
import os

def main() :


    vid_dir = 'temp\\out.avi'
    video = open(str(vid_dir), 'rb')
    st.video(video)
    print ('-'*15)
    print (video)
    print ('-'*15)

if __name__ == '__main__':
    main()