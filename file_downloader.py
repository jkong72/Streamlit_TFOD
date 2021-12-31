import streamlit as st
from pytube import streams
import urllib.request
from urllib.error import URLError, HTTPError
import os
import pytube

from datetime import datetime as dt


def image_downloader(image_url, temp_dir):
    file_list = os.listdir(temp_dir) 
    if len(file_list) > 0: # 경로 내부에 파일이 있을 때
        for file in file_list:
            os.remove (temp_dir+'\\'+file) # 내부의 파일을 삭제
    # file_format = image_url.split('.')[-1]
    file_format = 'jpg'
    current_time = str(dt.now().isoformat().replace(':', '-').replace('.', '`'))
    download_name = current_time+'.'+file_format
    path = temp_dir +'/'+ download_name
    
    try:
        urllib.request.urlretrieve(image_url,path)
    except HTTPError as e:
        code = e.getcode()
        if code == 403 :
            st.warning('이미지 제공 측에서 무분별한 다운로드를 금지한 url입니다.')





def video_downloader(video_url, temp_dir):
    file_list = os.listdir(temp_dir) 
    if len(file_list) > 0: # 경로 내부에 파일이 있을 때
        for file in file_list:
            os.remove (temp_dir+'\\'+file) # 내부의 파일을 삭제


    current_time = dt.now()
    current_time = current_time.isoformat().replace(':', '-')

    pytube.YouTube  (video_url).streams.filter(progressive=True, file_extension="mp4").first().download(temp_dir)
    
    