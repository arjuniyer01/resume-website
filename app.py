import streamlit as st
from constant_values import *

from streamlit_timeline import timeline
import streamlit.components.v1 as components
from streamlit_echarts import st_echarts

st.set_page_config(page_title="Arjun Iyer's Resume", layout="wide", page_icon=":smile:")

# div.stDownloadButton > button:hover {{background-color: #00ff00;color:#ff0000;}}
# div.stDownloadButton > button:hover {{border-color: white;}}
st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 25rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 25rem;}}
        div.stDownloadButton > button:first-child {{background-color: #000000; color:#FFFFFF; border-radius: 10px; padding: 10px; font-weight: bold;}}  
        div.stDownloadButton > button:hover {{border-width: thick;}}
    </style>
''',unsafe_allow_html=True)

with st.sidebar:
    components.html(embed_component["linkedin"], height=300)
    components.html(embed_component["github"], height=500)

# col7, col8 = st.sidebar.columns([1,5])
# with col7:
#     pass
# with col8:
#     pdfFileObj = open("pdf_files/iyer_resume.pdf", "rb")
#     st.download_button("Download PDF Resume", pdfFileObj, file_name="iyer_resume.pdf", mime="pdf")

col1, col2, col3 = st.columns([4, 4, 3])

with col1:
    st.markdown("## :email: iyer9@wisc.edu")
with col2:
    st.markdown("## :phone: 608-622-4320")
with col3 :
    pdfFileObj = open("pdf_files/iyer_resume.pdf", "rb")
    st.download_button("Download PDF Resume", pdfFileObj, file_name="iyer_resume.pdf", mime="pdf")

# st.markdown("## :email: iyer9@wisc.edu &emsp;&emsp; :phone: 608-622-4320")


with st.spinner(text="Building line"):
    with open("timeline.json", "r") as f:
        data = f.read()
        timeline(data, height=500,)


st.markdown("# Interactive Project Viewer :computer:")
st.markdown("#### Click on the chart to view my work in a language!")

option = {
    "click": "function(params) { console.log(params.name) }",
    "toolbox": {
        "show": True,
        "feature": {
            "mark": {"show": True},
        },
    },
    "series": [
        {
            "type": "pie",
            "radius": [50, 250],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 8},
            "data": [
                {"value": 10, "name": "Python"},
                {"value": 9, "name": "C"},
                {"value": 8, "name": "Java"},
                {"value": 7, "name": "TypeScript"},
                {"value": 8, "name": "SQL"},
                {"value": 8, "name": "R"},
                {"value": 7, "name": "Bash"},
            ],
        }
    ],
}
clicked_label = st_echarts(
    options=option, 
    height="600px",
    events={"click": "function(params) { return params.name }"},
)

if clicked_label:
    with st.spinner(text="Loading Repositories"):
        if clicked_label == "Python":
            st.markdown(repository_md_strings['Pneumonia_Detector'])
            st.markdown(repository_md_strings['resume-website'])
        if clicked_label == "C":
            st.markdown(repository_md_strings['neural-network-from-scratch'])
            st.markdown(repository_md_strings['Memory_Allocator'])
        if clicked_label == "Java":
            st.markdown(repository_md_strings['WikipediaTermSearch'])
            st.markdown(repository_md_strings['BestFlight'])
        if clicked_label == "R":
            st.markdown(repository_md_strings['Instant_Body_Fat'])