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


def TFOD(image):
    st.write('TFOD 기능이 들어갈 곳입니다.')