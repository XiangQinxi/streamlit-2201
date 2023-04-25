import streamlit as st
import streamlit as st

from streamlit_jupyter import StreamlitPatcher, tqdm

StreamlitPatcher().jupyter()  # register streamlit with jupyter-compatible wrappers

st.title("湖南省邵阳市第七中学 2201班")

st.caption('此文档为七中2201班所编辑', help="目的在于记录2201班所发生过的事，以留做纪念")
