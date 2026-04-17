import streamlit as st
from PIL import Image
from api_calling import error_explanation,correct_code


st.title(":green[Code Debugger]")
st.markdown("Upload the image of your code error")
st.divider()

with st.sidebar:
    st.header("Controls")

    images=st.file_uploader("Upload the photos of your code",
    type=['jpg','jpeg','png'],accept_multiple_files=True
    )
    
    pil_images=[]
    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)
    if images:  
     if len(images)>1 :
       col=st.columns(len(images))
     
       for i,img in enumerate(images):
         with col[i]:
            st.image(img)

    selected_option=st.selectbox("How you want to solve the problem",
  ('Hints','Solution with code'),index=None
  )
    pressed= st.button("Debug Code",type='primary')
if pressed:
    if not images:
        st.error("You must upload at least an image!")
    if not selected_option:
        st.error("You must choose an option!")        


    if images and selected_option:

        #error_explanation   
        with st.container(border=True):
            st.subheader("The Issues :")
            
            with st.spinner("AI is analyzing your code..."):
              explanation=error_explanation(pil_images,selected_option)     
              st.markdown(explanation)
         

        st.divider()   
        #correct code    
        with st.container(border=True):
            st.subheader("The Solution")
            with st.spinner("AI is analyzing your code..."):
               solution=correct_code(pil_images,selected_option) 
               st.markdown(solution)           