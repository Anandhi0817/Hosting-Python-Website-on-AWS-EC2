import streamlit as st 

# Streamlit part
st.markdown("<h1 style='text-align: center; color: Brown; font-size: 25px; font-family: Arial, sans-serif;'> Hosting Python Website on AWS EC2 instance </h1>", unsafe_allow_html=True)

with st.sidebar:
    selected = st.sidebar.selectbox("Navigation", ["Home", "Questions"])

if selected == "Home":
    st.markdown("                            ")
    st.markdown("                            ")
    st.markdown("LEARNER TO LEADER IN CLOUD !")
    st.write("With our platform, you can gain valuable insights and make informed decisions about cloud computing. Whether you're a beginner, an experienced developer, or a business owner, our comprehensive resources provide you with the information you need. Explore tutorials, case studies, best practices, and more with ease. Let us empower you in the world of cloud computing!")
    st.write("Name : Anandhi")
    st.write("Batch : DT20DT21")
    
    # Footer with image
    st.markdown('<div class="icon-container"><img src="/content/5.png" width="60"></div>', unsafe_allow_html=True)
    st.markdown("---")
    st.write("© 2024 Cloud. All rights reserved.")

if selected == "Questions":
    st.markdown("AWS Concepts Explained")
    Questions = st.selectbox('SELECT QUESTION', ('1. What is the difference between server and serverless?',
                                                '2. What is AWS EC2?',
                                                '3. What are security groups?'))
    
    if Questions == "1. What is the difference between server and serverless?":
        st.markdown("Server and Serverless")
        st.write("""
        A server is a physical or virtual machine that runs applications, stores data, and serves requests from clients over a network.
        On the other hand, serverless computing abstracts away the infrastructure management entirely. Developers can focus solely on writing code without worrying about provisioning or managing servers.
        """)

    elif Questions == "2. What is AWS EC2?":
        st.markdown("AWS EC2")
        st.write("""
        Amazon Elastic Compute Cloud (EC2) is a web service provided by Amazon Web Services (AWS) that offers resizable compute capacity in the cloud.
        EC2 allows users to rent virtual servers, known as instances, on which they can run their applications.
        With EC2, users have full control over their instances, including the choice of operating system, configuration, and security settings.
        """)

    elif Questions == "3. What are security groups?":
        st.markdown("Security Groups")
        st.write("""
        In the context of AWS EC2, Security Groups act as virtual firewalls that control the traffic allowed to reach your EC2 instances.
        They act at the instance level and can be thought of as a set of inbound and outbound rules.
        Security Groups operate at the instance level, meaning each instance can have its own set of rules.
        """)
