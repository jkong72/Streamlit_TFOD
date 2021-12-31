import streamlit as st
from PIL import Image
import pandas as pd
import os

from TFOD_image import TFOD_image
from image_uploader import image_uploader
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
        about_show()
    
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
    st.title('컴퓨터 비전 프로젝트')

    # 파일 업로드
    st.markdown('## 업로드 방식 선택')
    upload_type = ['컴퓨터에서 업로드', '링크에서 업로드']
    upload_sel = st.selectbox ('', upload_type)
    
    if upload_sel == upload_type[0]:
        image_uploader()
    elif upload_sel == upload_type[1]:



    # TFOD

    temp_dir = 'D:\\TFOD example\\Streamlit_TFOD\\temp'
    file_list = os.listdir(temp_dir)
    if len(file_list) > 0:
        if st.button ('찾아줘!'):
            if image_type == image_type_list[0]:
                TFOD_img = TFOD_image (image, model_url, thought)
                st.image(TFOD_img, use_column_width=True, channels='BGR')

            else:
                pass
                


if __name__ == '__main__':
    main()