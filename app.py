from PIL import Image
import requests     
import streamlit as st  
from streamlit_lottie import st_lottie  

st.set_page_config(page_title="My Webpage",page_icon=":tada:", layout="wide")

def load_lottieurl(url):
	r = requests.get(url)
	if r.status_code !=200:
		return None
	return r.json()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")            

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json") 
img_contact_form = Image.open("images/CODING_IS_FUNS.png")
img_lottie_animation = Image.open("images/CODING_IS_FUN.png")

with st.container():

    st.subheader("Hi, I am Unnat :wave:")

    st.title("A Data Analyst from Nepal")   

    st.write("I am passionate on finding new ways to use python and using various programming language")

    st.write("[Learn More >](https://www.youtube.com/watch?v=VqgUkExPvLY&t=70s)")

    with st.container():

        st.write("---")
        left_column, right_column = st.columns(2)   
        with left_column:
            st.header("What Can I DO")
            st.write("##")
            st.write(
                """"
                This channel creates tutorials for people who:
                •are looking for a way to leverage the power of Python in their day-to-day work. 
                •are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
                •want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
                •are working with Excel and found themselves thinking - "there has to be a better way."

                If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
                """
            )
            st.write("[Youtube Channel >](https://www.youtube.com/@CodingIsFun)")

            with right_column:
                 st_lottie(lottie_coding, height=300, key="coding")

                 with st.container():
                     st.write("---")
                     st.header("My Projects")
                     st.write("##")
                     image_column, text_column = st.columns((1, 2))
                     
                     with image_column:

                      st.image(img_lottie_animation)
                     with text_column:
                        st.subheader("Integrate Lottie Animations Inside Your Streamlit APP")
                        st.write(
	                        """
	                        Learn how to use Lottie Files in Stremlit!
	                        Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do so.
	                        In this tuitorial,I will show you exactly how it is done.
                            """
                        )
                        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=YClmpnpszq8)")
                 with st.container():
                    image_column, text_column = st.columns((1, 2))
                    with image_column:
                        st.image(img_contact_form)
                    with text_column:
                        st.subheader("How TO Add A contact Form To Your Streamlit APP")
                        st.write(
                            """
                        Want to add a contact form to your streamlit website?
                        In this video, I am going to show how to implement a contact from in your Streamlit app using
                        """
                        )
                        st.markdown("[Watch My Video...](https://www.youtube.com/watch?v=Jkct0NXMuFQ&list=PLLHKPd6Uie-rtIhfD8jgkhjIbWy6wA2kl&index=3)")
                 with st.container():
                  st.write("---")
                  st.header("Get In Touch With Me!")
                  st.write("##")  

                  contact_form = """
                  <form action="https://formsubmit.co/bluesrock076@gmail.com" method="POST">
                      <input type="hidden" name="_captcha" value="false">
                      <input type="text" name="name" placeholder="Your Name" required>
                      <input type="email" name="email" placeholder="Your Email Address" required>
                      <textarea name="message" placeholder="Your Message Here" required></textarea>
                      <button type="submit">Send</button>
                 </form>
                 """
            left_column, right_column = st.columns(2)           
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()
