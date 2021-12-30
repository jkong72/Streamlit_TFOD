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
    model_list = ['모델 리스트가 들어갈 자리입니다.']
    st.sidebar.selectbox('메뉴', model_list)

    # 본 화면
    st.title('제목')

    # 파일 업로드
    image = file_uploader()

    # TFOD
    TFOD(image)


if __name__ == '__main__':
    main()