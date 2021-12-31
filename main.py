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
        model_url = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz'

    elif model_sel == model_list[1]:
        model_url = 'http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_320x320_coco17_tpu-8.tar.gz'

    elif model_sel == model_list[2]:
        model_url = 'http://download.tensorflow.org/models/object_detection/tf2/20200713/centernet_hg104_1024x1024_coco17_tpu-32.tar.gz'

    elif model_sel == model_list[-1]:
        model_url = st.text_input()


    st.sidebar.markdown('#### 정밀도 필터')
    thought = st.sidebar.slider('예측 확률 (%)', min_value = 30, max_value = 100, value= 60, help='인공지능이 "사진의 이 부분은 어떤 물체일 것"이라고 예측한 확률입니다. 낮게 설정하면, 인공지능이 강한 확신을 갖지 않은 결과도 모두 표시합니다.')


    # 본 화면 #####
    if image_type != image_list[-1]:
        st.title('컴퓨터 비전 프로젝트')

        # 파일 업로드
        st.markdown('## 업로드 방식 선택')
        upload_type = ['컴퓨터에서 업로드', '링크에서 업로드']
        upload_sel = st.selectbox ('', upload_type)
        st.markdown ('---')
        
        if image_type == image_type_list[0]: #이미지 업로드

            if upload_sel == upload_type[0]: #로컬 이미지 업로드
                image_uploader()
            elif upload_sel == upload_type[1]: #링크 이미지 업로드
                st.markdown('##### 이미지 링크 입력')
                image_url = st.text_input('')
                if image_url != '' :
                    st.image (image_url)
                else:
                    st.write ('이미지 입력 바람')

                if st.button ('os 다운로드'):
                    file_format = image_url.split('.')[-1]
                    current_time = str(dt.now().isoformat().replace(':', '-').replace('.', '`'))
                    download_name = current_time+'.'+file_format

                    urllib.request.urlretrieve(image_url, download_name)

                image_downloader()

        elif image_type == image_type_list[1]: #동영상 업로드

            if upload_sel == upload_type[0]: #로컬 동영상 업로드
                video = video_uploader()
                
            elif upload_sel == upload_type[1]: #링크 동영상 업로드
                st.markdown('##### 동영상 링크 입력')
                movie_url = st.text_input('')
                if movie_url != '':
                    st.video(movie_url)
                
                video_downloader()
            
                
        # TFOD
        temp_dir = 'D:\\TFOD example\\Streamlit_TFOD\\temp'
        file_list = os.listdir(temp_dir)
        if len(file_list) > 0:
            if image_type == image_type_list[1]:
                st.warning ('동영상 파일의 사물 탐지는 크기, 길이, 모델에 따라 긴 시간이 걸릴 수 있습니다.')
            if st.button ('찾아줘!'):
                if image_type == image_type_list[0]:
                    TFOD_img = TFOD_image (model_url, thought)
                    st.image(TFOD_img, use_column_width=True, channels='BGR')

                else:
                    TFOD_vid = TFOD_video ()
                    st.video(TFOD_vid)
                    
    else:
        about_show()
if __name__ == '__main__':
    main()