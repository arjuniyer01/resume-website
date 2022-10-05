import streamlit as st
from constant_values import *

from PIL import Image
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from streamlit_echarts import st_echarts

st.set_page_config(page_title="Arjun Iyer's Resume", layout="wide", page_icon=":smile:")

st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 25rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 25rem;}}
    </style>
''',unsafe_allow_html=True)

with st.sidebar:
    components.html(embed_component["linkedin"], height=300)
    components.html(embed_component["github"], height=500)

pdfFileObj = open("pdf_files/iyer_resume.pdf", "rb")
st.sidebar.download_button("Download PDF Resume", pdfFileObj, file_name="iyer_resume.pdf", mime="pdf")

st.markdown("## :email: iyer9@wisc.edu &emsp;&emsp; :phone: 608-622-4320")

def hello():
    print("Hello World")

with st.spinner(text="Building line"):
    with open("timeline.json", "r") as f:
        data = f.read()
        timeline(data, height=500,)

option = {
    "title": {"text": "Languages"},
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
st_echarts(
    options=option, height="600px",
)