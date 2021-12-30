import streamlit as st
from datetime import datetime as dt
from PIL import Image
import os

def file_uploader():
    st.write ('파일 업로드 기능이 들어갈 곳입니다.')

    def save_uploaded_file(directory, file) :
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(os.path.join(directory, file.name), 'wb') as f:
            f.write(file.getbuffer())
        return st.success (f'{file.name} 파일을 {directory} 경로에 저장하는데 성공했습니다.')

    image_file = st.file_uploader('이미지 업로드', type = ['png', 'jpg', 'jpeg'])
    if image_file is not None :
        current_time = dt.now()
        current_time = current_time.isoformat().replace(':', '-')

        save_uploaded_file ('temp/', image_file)

        img = Image.open(image_file)
        st.image(img, use_column_width=True)
        
        return img
    pass