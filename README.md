# Streamlit_TFOD

#### TensorFlow Object Detection TFOD (텐서플로 사물 탐지)기능을 이용해
#### 원하는 정지 영상(그림 및 사진)이나 동영상에 어떤 물체가 있는지
#### 판별 및 시각화하는 웹 대시보드 입니다.

![image](https://user-images.githubusercontent.com/96038721/147878363-9ce6a1fa-f44b-4558-a429-90be6623ecbf.png)

##### 왼쪽 사이드바 메뉴 (날개)에서 메뉴와 인공지능 모델, 시각화할 예측 확률을 설정할 수 있습니다.
---
---
**평균 모델**은 중간정도의 성능과 정확도를 가진 모델입니다.
###### SSD ResNet101 V1 FPN 1024x1024 (RetinaNet101) 모델 사용

![image](https://user-images.githubusercontent.com/96038721/147878732-46ecc509-441a-4449-a477-a3011e75a4ab.png)  

---
**고속 저품질 모델**은 정확도가 낮지만 빠르게 작동합니다.
###### SSD MobileNet v2 320x320 모델 사용   

![image](https://user-images.githubusercontent.com/96038721/147878930-aadbcd8a-678c-4bc1-82d0-8f038a6ceda8.png)

---
**저속 고정밀 모델**은 작업속도가 느린 대신 보다 정확한 결과를 제공합니다.
###### CenterNet HourGlass104 1024x1024 모델 사용

![image](https://user-images.githubusercontent.com/96038721/147878999-b79c73dd-410d-449c-b9a9-30f3dac746b3.png)

---
~~##### 그 외에도 TensorFlow 2 Detection Model Zoo의 다른 모델의 주소를 **직접 입력**할 수 있습니다.
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md

~~**링크 주소 복사**를 통해 **url**을 가져와야 한다는 점을 기억하세요.~~
####현재 해당 기능의 결함이 확인되어 수정중에 있습니다.

---
각 모델은 처음 실행할 때 모델을 다운로드 하는 시간이 추가로 소요되며 경우에 따라 재실행해야 할 수도 있습니다.   
다음 동작부터는 보다 빨라집니다.   
정지 영상(그림 및 사진)과 동영상을 분석할 수 있으며   
컴퓨터에 저장된 파일을 직접 업로드하거나, url주소를 이용할 수 있습니다.   
.png, .jpg, .jpeg 형식의 정지 영상을 업로드 할 수 있습니다.   
.avi, .mp4, .wmv 형식의 동영상을 업로드 할 수 있습니다.   

일부 url은 보안상 반려됩니다. (HTTP 403 Error)
![image](https://user-images.githubusercontent.com/96038721/147879056-6cabf4e9-9a8f-4224-b07f-986a055a4342.png)


동영상 url은 현재 YouTube만 가능합니다.

---
그 외 로드맵
---
버튼 등 위젯 중 일부의 부적절한 표시 수정 (부분적으로 완료됨)   
모델 직접 입력 기능 개선 (진행중)   
Object Detection 과정을 거친 동영상 파일을 바로 확인할 수 있게끔 개선 (진행중)   
Object Detection 과정이 끝난 파일을 다운로드 및 저장하는 기능 추가   
Object Detection 과정을 거친 시간 출력 기능 추가   
Object Detection 작업중임을 알릴 수 있는 진행 상태바 따위를 추가   
Object Detection 과정 전 현재 모델과, 모델의 성능. 이를 바탕으로한 작업 시간 예측   
보다 이용자 친화적인 UI개선   

