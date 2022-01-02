import streamlit as st
import tensorflow as tf
import numpy as np
import pathlib
import zipfile
import os

import matplotlib.pyplot as plt
from PIL import Image
import cv2

from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

from TFOD_video_render import TFOD_video_render


#사전 정의 함수
def download_labels(filename):
    base_url = 'https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/data/'
    label_dir = tf.keras.utils.get_file(fname=filename,
                                        origin=base_url + filename,
                                        untar=False)
    label_dir = pathlib.Path(label_dir)
    return str(label_dir)

def download_model(model_name, model_date):
    base_url = 'http://download.tensorflow.org/models/object_detection/tf2/'
    model_file = model_name + '.tar.gz'
    model_dir = tf.keras.utils.get_file(fname=model_name,
                                        origin=base_url + model_date + '/' + model_file,
                                        untar=True)
    return str(model_dir)

def load_model(model_dir):
    model_full_dir = model_dir + "/saved_model"

    detection_model = tf.saved_model.load(model_full_dir)
    return detection_model

def load_image_into_numpy_array(path):
    return cv2.imread(str(path)) # opencv이용.
##########################################################################################
##########################################################################################
##########################################################################################

# 기능 실행 함수
def TFOD_image (model_url, pred_pcnt):
    st.markdown('---')

    LABEL_FILENAME = 'mscoco_label_map.pbtxt'
    PATH_TO_LABELS = download_labels(LABEL_FILENAME)

    url_sep = model_url.split('/')
    model_name = url_sep[-1].split('.')[0]
    model_date = url_sep[-2]

    MODEL_DATE = model_date
    MODEL_NAME = model_name
    PATH_TO_MODEL_DIR = download_model(MODEL_NAME, MODEL_DATE)


    detection_model = load_model(PATH_TO_MODEL_DIR)

    # 로컬 이미지 경로에서 이미지를 가져오는 코드
    PATH_TO_IMAGE_DIR = pathlib.Path('temp') # 가져올 경로 설정
    IMAGE_PATHS = list (PATH_TO_IMAGE_DIR.glob('*.jpg')) # 인자로 주어진 문자열이 포함된 파일들만 가져옴 (*은 모든 문자열을 입력받겠다는 뜻.)


    category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                    use_display_name=True)
    
    
    for image_path in IMAGE_PATHS:

        
        print('Running inference for {}... '.format(image_path), end='')

        image_np = load_image_into_numpy_array(image_path)

        input_tensor = tf.convert_to_tensor(image_np)
        input_tensor = input_tensor[tf.newaxis, ...]

        detections = detection_model(input_tensor)

        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy()
                    for key, value in detections.items()}
        detections['num_detections'] = num_detections

        detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

        image_np_with_detections = image_np.copy()

        viz_utils.visualize_boxes_and_labels_on_image_array(
            image_np_with_detections,
            detections['detection_boxes'],
            detections['detection_classes'],
            detections['detection_scores'],
            category_index,
            use_normalized_coordinates=True,
            max_boxes_to_draw=200,
            min_score_thresh=pred_pcnt/100,
            agnostic_mode=False)
    
    return image_np_with_detections

##########################################################################################
##########################################################################################
##########################################################################################

def TFOD_video (model_url, pred_pcnt, temp_dir):
    LABEL_FILENAME = 'mscoco_label_map.pbtxt'
    PATH_TO_LABELS = download_labels(LABEL_FILENAME)

    url_sep = model_url.split('/')
    model_name = url_sep[-1].split('.')[0]
    model_date = url_sep[-2]

    MODEL_DATE = model_date
    MODEL_NAME = model_name
    PATH_TO_MODEL_DIR = download_model(MODEL_NAME, MODEL_DATE)

    detection_model = load_model(PATH_TO_MODEL_DIR)


    # 비디오를 실행하는 코드
    video_dir = 'temp'
    files = os.listdir(temp_dir)
    file_dir = video_dir +'/'+ files[0]


    cap = cv2.VideoCapture(file_dir) # 비디오가 위치한 경로
    category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                    use_display_name=True)


    if cap.isOpened() == False:
        print('비디오 실행 에러')

    else:
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        
        out = cv2.VideoWriter(video_dir+'/out.avi', # 출력 경로
            cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
            20, # FPS
            (frame_width, frame_height))
        
        while cap.isOpened() :
            ret, frame = cap.read()

            if ret == True:

                
                TFOD_video_render (detection_model, frame, category_index, out, pred_pcnt)   # 프레임별 작업이 끝날 떄마다 동영상 파일로 저장하는 코드
                
                
                
            else:
                break
        cap.release()
        out.release()