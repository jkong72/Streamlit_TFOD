import streamlit as st
from datetime import datetime as dt
from PIL import Image
import os

def image_uploader():
    st.markdown ('#### 이미지를 업로드해주세요')
    temp_dir = 'D:\\TFOD example\\Streamlit_TFOD\\temp'

    file_list = os.listdir(temp_dir) 
    if len(file_list) > 0: # 경로 내부에 파일이 있을 때
        for file in file_list:
            os.remove (temp_dir+'\\'+file)

    def save_uploaded_file(directory, file) :
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(os.path.join(directory, file.name), 'wb') as f:
            f.write(file.getbuffer())
        return st.success (f'{file.name} 파일을 {directory} 경로에 저장하는데 성공했습니다.')

    image_file = st.file_uploader('', type = ['png', 'jpg', 'jpeg'])
    if image_file is not None :
        current_time = dt.now()
        current_time = current_time.isoformat().replace(':', '-')

        save_uploaded_file ('temp/', image_file)

        img = Image.open(image_file)
        st.image(img, use_column_width=True)
        
        return img
    pass