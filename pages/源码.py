import streamlit as st
from streamlit_extras.let_it_rain import rain


with st.sidebar:
    from streamlit_extras.colored_header import colored_header

    rain(
        emoji="🍭",
        font_size=45,
        falling_speed=8,
    )

    colored_header(
        label="湖南省邵阳市第七中学 2201班 源码",
        description="查看此应用程序的源码（不可以查看源码页面的源码，你在想什么呢）",
        color_name="red-70",
    )

rain(
    emoji="🍭",
    font_size=45,
    falling_speed=8,
)


st.balloons()


st.title("源码")

with st.expander("主页.py", expanded=True):
    st.code(open("主页.py", "r", encoding="utf-8").read())

with st.expander("博客 2023.4.25.py", expanded=True):
    st.code(open("pages/博客 2023.4.25.py", "r", encoding="utf-8").read())