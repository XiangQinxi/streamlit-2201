# encoding=utf-8

import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.customize_running import center_running

st.set_page_config(
    page_title="湖南省邵阳市第七中学 2201班",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "QQ：`137977353` E-Mail：`XiangQinxi@outlook.com`"
    }
)

with st.sidebar:
    from streamlit_extras.colored_header import colored_header

    rain(
        emoji="🍭",
        font_size=32,
        falling_speed=8,
    )

    colored_header(
        label="湖南省邵阳市第七中学 2201班",
        description="创建者：向秦希",
        color_name="red-70",
    )

st.balloons()

st.title("主页")

st.caption('此文档为七中2201班所编辑', help="目的在于记录2201班所发生过的事，以留做纪念")

st.caption("此文档源于旧文档", help="为了使网站更加现代化，从Sphinx转到Streamlit")

with st.expander("其他", expanded=True):
    st.text("如需要加入其他文档，请联系我并带上文本，我会进行整理上传。")

st.divider()

if st.button("博客 2023.4.25"):
    center_running()
    from time import sleep
    sleep(1)
    switch_page("博客 2023.4.25")
