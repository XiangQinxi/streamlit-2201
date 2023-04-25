import streamlit as st
from streamlit_extras.let_it_rain import rain

with st.sidebar:
    st.info("创建者：向秦希")

rain(
    emoji="🍭",
    font_size=32,
    falling_speed=7,
)


def Home():
    st.title("湖南省邵阳市第七中学 2201班")

    st.caption('此文档为七中2201班所编辑', help="目的在于记录2201班所发生过的事，以留做纪念")

    st.caption("此文档源于旧文档")

    st.text("如需要加入其他文档，请联系我并带上文本，我会进行整理上传。")

    st.subheader("源代码")

    st.code(open("app.py", "r", encoding="utf-8").read())


def Blog2023425():
    st.title("博客 2023.4.25")
    st.text("开始从静态网站转为应用程序")
    st.image("Blog.2023.4.25.png", caption="预览图片")


page_names_to_funcs = {
    "主页": Home,
    "博客 2023.4.25": Blog2023425
}

demo_name = st.sidebar.selectbox("选择页面", options=page_names_to_funcs.keys(), help="这里就是导航")
page_names_to_funcs[demo_name]()
