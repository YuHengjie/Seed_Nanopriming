# %%
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt

# %%
plt.style.use('default')

st.set_page_config(
    page_title = 'Hello',
    page_icon = '💫',
    layout = 'wide'
)

# %%
st.sidebar.success("Select a module above.")

# %%
st.write("# Welcome to interpretable machine learning-aided interactive platform for seed nanopriming! 👋")

st.markdown(
    """
    This is online interactive web app for interpretable machine learning-aided seed nanopriming research🌱

    **👈 Select a module from the sidebar** 

    ### Background 👨🏼‍🌾
    - Agriculture is facing the challenges of climate change, soil degradation, environmental pollution, and limited resources.
    - Existing food growth trends are insufficient to feed the population in 2050. 
    - Seed nanopriming is a cost-effective and environmentally-friendly solution for food sustainability.
    - There is a knowledge gap regarding the nanoparticle uptake and the underlying physiological mechanism due to the diversity of nanomaterials and the complexity of nano-plant/seed-environment interactions. 
    - interpretable machine learning holds great potential to understand the complex problems.

    ### See more interpretable machine learning-aided research 🔍
    - Integrating machine learning interpretation methods for investigating [nanoparticle uptake during seed priming and its biological effects](https://pubs.rsc.org/en/content/articlelanding/2022/NR/D2NR01904C)
    - Interpretable machine learning for investigating [complex nanomaterial-plant-soil interactions](https://pubs.rsc.org/en/content/articlelanding/2022/en/d2en00181k)
    - Predicting and investigating [cytotoxicity of nanoparticles by translucent machine learning](https://www.sciencedirect.com/science/article/pii/S0045653521006330?via%3Dihub)
    
    ### Contact ✈️
    - The web app is still under construction. If you have any ideas, please contact Hengjie Yu (hengjieyu@yeah.net,hengjieyu@zju.edu.cn)

"""
)

# %%