import streamlit as st
from PIL import Image
import pandas as pd
import os

from TFOD_image import TFOD
from file_uploader import file_uploader



# from datetime import datetime as dt


def main() :
    # 레이아웃
    # 사이드바
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


    st.sidebar.markdown('#### 이만큼 확실한 것만 보기')
    thought = st.sidebar.slider('예측 확률 (%)', min_value = 30, max_value = 100, value= 60, help='인공지능이 어떤 물체일 것이라고 생각한 정도입니다. 이 수치보다 더 정확한 값만 보여집니다.')

    # 본 화면
    st.title('컴퓨터 비전 프로젝트')

    # 파일 업로드
    image = file_uploader()


    # TFOD
    temp_dir = 'D:\\TFOD example\\Streamlit_TFOD\\temp'
    file_list = os.listdir(temp_dir)
    if len(file_list) > 0:
        if st.button ('찾아줘!'):
            TFOD_img = TFOD(image, model_url, thought)
            # display(Image.fromarray(TFOD_img))

            st.image(TFOD_img, use_column_width=True, channels='BGR')

if __name__ == '__main__':
    main()