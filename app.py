import streamlit as st
from constant_values import *
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from streamlit_echarts import st_echarts
import base64

st.set_page_config(page_title="Arjun Iyer's Resume", layout="wide", page_icon=":smile:")

st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 25rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 25rem;}}
        div.stDownloadButton > button:first-child {{background-color: #000000; color:#FFFFFF; border-radius: 10px; padding: 10px; font-weight: bold;}}  
        div.stDownloadButton > button:hover {{border-width: thick;}}
    </style>
''', unsafe_allow_html=True)

with st.sidebar:
    components.html(embed_component["linkedin"], height=300)
    components.html(embed_component["github"], height=500)

col1, col2, col3 = st.columns([4, 4, 3])

with col1:
    st.markdown("## :email: iyer9@wisc.edu")
with col2:
    st.markdown("## :phone: 608-622-4320")
with col3 :
    pdfFileObj = open("pdf_files/iyer_resume.pdf", "rb")
    st.download_button("Download PDF Resume", pdfFileObj, file_name="iyer_resume.pdf", mime="pdf")

with st.spinner(text="Building line"):
    with open("timeline.json", "r") as f:
        data = f.read()
        timeline(data, height=500,)

st.markdown("# Interactive Project Viewer :computer:")

st.markdown('<h4><span style="color:blue">👇 Click</span> on the chart to view my work in a language! </h4>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    clicked_label = st_echarts(
    options=lang_chart, 
    height="400px",
    events={"click": "function(params) { return params.name }"},)

with col2:
    projects_gif = st.image("images/projects.gif")
    if clicked_label:
        if len(repository_embed[clicked_label]) == 0 :
            wip_gif = st.image("images/wip.gif")
            st.markdown("### &emsp;&emsp;&emsp;&emsp; Thinking of ideas! :smile:")
            projects_gif.empty()
        else:
            for item in repository_embed[clicked_label]:
                st.markdown(repository_embed[clicked_label][item])
        
        