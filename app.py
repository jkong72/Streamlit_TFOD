import streamlit as st
from PIL import Image
import pandas as pd
import os
import urllib.request
from datetime import datetime as dt

from TFOD_process import TFOD_image
from TFOD_process import TFOD_video
from file_downloader import image_downloader, video_downloader
from file_uploader import image_uploader, video_uploader
from about import about_show

# from datetime import datetime as dt

def main() :
    # 레이아웃
    # 사이드바
        
    ### 처리 영상 선택
    image_list = ['정지 영상 (그림 및 사진)', '동영상', '대시보드 정보']
    image_sel = st.sidebar.selectbox('메뉴', image_list)
    image_type_list = ['image', 'video']
    if image_sel == image_list[0]:
        image_type = image_type_list[0]
    elif image_sel == image_list[1]:
        image_type = image_type_list[1]
    elif image_sel == image_list[-1]:
        image_type = image_list[-1]
        
    ### 모델 선택
    model_list = ['기본 모델', '저품질 속성 모델', '느린 정밀 모델', '직접 입력']
    model_sel = st.sidebar.selectbox('메뉴', model_list)
    if model_sel == model_list[0]:
        model_url = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet101_v1_fpn_1024x1024_coco17_tpu-8.tar.gz'

    elif model_sel == model_list[1]:
        model_url = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz'

    elif model_sel == model_list[2]:
        model_url = 'http://download.tensorflow.org/models/object_detection/tf2/20200713/centernet_hg104_1024x1024_coco17_tpu-32.tar.gz'

    elif model_sel == model_list[-1]:
        model_url = st.text_input()


    st.sidebar.markdown('#### 정밀도 필터')
    pred_pcnt = st.sidebar.slider('예측 확률 (%)', min_value = 30, max_value = 100, value= 60, help='인공지능이 "사진의 이 부분은 어떤 물체일 것"이라고 예측한 확률입니다. 낮게 설정하면, 인공지능이 강한 확신을 갖지 않은 결과도 모두 표시합니다.')


    # 본 화면 #####
    if image_type != image_list[-1]:
        st.title('컴퓨터 비전 프로젝트')

        # 파일 업로드
        temp_dir = 'temp' # 파일 경로

        st.markdown('## 업로드 방식 선택')
        upload_type = ['컴퓨터에서 업로드', '링크에서 업로드']
        upload_sel = st.selectbox ('', upload_type)
        st.markdown ('---')
        
        if image_type == image_type_list[0]: #이미지 업로드

            if upload_sel == upload_type[0]: #로컬 이미지 업로드
                image_uploader()

            elif upload_sel == upload_type[1]: #링크 이미지 업로드
                st.markdown('##### 이미지 링크 입력')
                st.error ('현재 이용중인 서비스는 외부 이미지나 영상의 권리를 보장하거나 이용상 책임을 지지 않습니다.')
                st.error ('다른 사람의 이미지나 영상을 이용하는 경우 신중하게 이용해주세요.')

                image_url = st.text_input('')
                if image_url != '' :
                    st.image (image_url)

                else:
                    st.write ('현재 이미지 없음')

                if st.button ('이 이미지 사용'):
                    image_downloader(image_url, temp_dir)
                    

        elif image_type == image_type_list[1]: #동영상 업로드

            if upload_sel == upload_type[0]: #로컬 동영상 업로드
                video = video_uploader()
                
            elif upload_sel == upload_type[1]: #링크 동영상 업로드
                st.error ('현재 이용중인 서비스는 외부 이미지나 영상의 권리를 보장하거나 이용상 책임을 지지 않습니다.')
                st.error ('다른 사람의 이미지나 영상을 이용하는 경우 신중하게 이용해주세요.')

                st.markdown('##### 동영상 링크 입력 (현재 You Tube만 지원)')
                video_url = st.text_input('')
                if video_url != '':
                    st.video(video_url)
                
                if st.button ('이 영상 사용'):
                    video_downloader(video_url, temp_dir)
            
                
        # TFOD
        file_list = os.listdir(temp_dir)
        if len(file_list) > 0:
            if image_type == image_type_list[1]:
                st.warning ('동영상 파일의 사물 탐지는 크기, 길이, 모델에 따라 매우 긴 시간이 걸릴 수 있습니다.')
            
            if st.button ('사물 탐지 시작!'):
                if image_type == image_type_list[0]:
                    TFOD_img = TFOD_image (model_url, pred_pcnt)
                    st.image(TFOD_img, use_column_width=True, channels='BGR')

                else:
                    TFOD_video (model_url, pred_pcnt, temp_dir)

                    vid_dir = temp_dir + '/out.avi'
                    video = open(str(vid_dir), 'rb')
                    st.video(video)

        
        # 다운로드

                    
    else:
        about_show()
if __name__ == '__main__':
    main()