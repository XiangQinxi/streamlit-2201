import streamlit as st
from streamlit_extras.let_it_rain import rain


with st.sidebar:
    from streamlit_extras.colored_header import colored_header

    rain(
        emoji="🍭",
        font_size=32,
        falling_speed=8,
    )

    colored_header(
        label="博客 2023年4月25日",
        description="应用程序开始构建",
        color_name="red-70",
    )


st.balloons()


st.title("博客 2023.4.25")
st.text("开始从静态网站转为应用程序")
st.image("Blog.2023.4.25.png", caption="预览图片")
