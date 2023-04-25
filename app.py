import streamlit as st
from streamlit_extras.let_it_rain import rain

with st.sidebar:
    st.success("创建者：向秦希")

rain(
    emoji="🍭",
    font_size=32,
    falling_speed=7,
)

st.title("湖南省邵阳市第七中学 2201班")

st.caption('此文档为七中2201班所编辑', help="目的在于记录2201班所发生过的事，以留做纪念")

st.caption("此文档源于旧文档")

st.text("如需要加入其他文档，请联系我并带上文本，我会进行整理上传。")

st.subheader("源代码")

st.code(open("app.py", "r", encoding="utf-8").read())