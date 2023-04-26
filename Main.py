import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.customize_running import center_running

st.title("占位")
st.text("中文字符文件不支持启动，我们将为您自动跳转至主页")

center_running()

from time import sleep

sleep(1)

switch_page("主页")

