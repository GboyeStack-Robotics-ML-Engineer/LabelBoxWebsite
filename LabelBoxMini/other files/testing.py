
import streamlit as st
from glob import glob
from streamlit_image_annotation import detection
import os
from pynput import keyboard
import time

st.set_page_config(
    page_title="LabelBoxMini",
    page_icon="🧊",
    layout="wide")

label_list = ['deer', 'human', 'dog', 'penguin', 'framingo', 'teddy bear']

root_path=r'D:\PYTHON PROJECTS\FireHaunt\Streamlit-Image-Annotation\image'
image_path_list = os.listdir(root_path)
image_path_list=[os.path.join(root_path,x) for x in image_path_list if x.endswith('.jpg')]

if 'current_image_index' not in st.session_state:
    st.session_state['current_image_index'] = 0

if 'result_dict' not in st.session_state:
    result_dict = {}
    # for img in image_path_list:
    #     result_dict[img] = {'bboxes': [[0,0,0,0],[0,0,0,0]],'labels':[0,3]}
    st.session_state['result_dict'] = result_dict.copy()




def on_key_press(key):
    if key ==key.right:
        print("Right key pressed")
        if st.session_state['current_image_index'] < len(image_path_list)-1:
            st.session_state['current_image_index'] += 1
        else:
            st.alert("You are at the last image")
        
    if key==key.left:
        if st.session_state['current_image_index'] > 0:
            st.session_state['current_image_index'] -= 1
            
        else:
            st.alert("You are at the first image")
    
\
def on_key_release(key):
  pass


keyboard_listener = keyboard.Listener(
    on_press=on_key_press,
    on_release=on_key_release)

# start the listener
keyboard_listener.start()

target_image_path = image_path_list[st.session_state['current_image_index']]
st.session_state['result_dict'][target_image_path]={}
st.session_state['result_dict'][target_image_path]['bboxes']=[[0,0,0,0]]
st.session_state['result_dict'][target_image_path]['labels']=[0]
#num_page = st.slider('page', 0, len(image_path_list)-1, 0, key='slider')
# target_image_path = image_path_list[0]

new_labels = detection(image_path=target_image_path, 
                    bboxes=st.session_state['result_dict'][target_image_path]['bboxes'], 
                    labels=st.session_state['result_dict'][target_image_path]['labels'], 
                    label_list=label_list, use_space=True, key=target_image_path,
                    height=1000,
                    width=5000)

if new_labels is not None:
    st.session_state['result_dict'][target_image_path]['bboxes'] = [v['bbox'] for v in new_labels]
    st.session_state['result_dict'][target_image_path]['labels'] = [v['label_id'] for v in new_labels]
# st.json(st.session_state['result_dict'])
