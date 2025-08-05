
# import streamlit as st
# import time

# # Set page config
# st.set_page_config(page_title="Learning Path Engine", layout="wide")

# def set_background_web(url):
#     st.markdown(
#         f"""
#         <style>
#         .background {{
#             position: fixed;
#             top: 0;
#             left: 0;
#             width: 100vw;
#             height: 100vh;
#             background-image: url("{url}");
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-position: center;
#             filter: blur(10px);
#             z-index: -1;
#         }}

#         .stApp {{
#             background-color: rgba(0, 0, 0, 0);
#         }}

#         .top-right-button {{
#             position: fixed;
#             top: 20px;
#             right: 300px;
#             z-index: 9999;
#             display: flex;
#             gap: 45px;
#         }}

#         .top-right-button a {{
#             background-color: #1f77b4;
#             color: white;
#             padding: 10px 18px;
#             text-decoration: none;
#             border-radius: 8px;
#             font-weight: bold;
#         }}

#         .top-right-button a:hover {{
#             background-color: #135a96;
#         }}

#         .animated-title {{
#             color: #FFFFFF;
#             font-size: 70px;
#             margin-left: 100px;
#             margin-top: 100px;
#             font-weight: bold;
#             animation: fadeInUp 3.5s ease-out;
#         }}

#         @keyframes fadeInUp {{
#             0% {{
#                 opacity: 0;
#                 transform: translateY(30px);
#             }}
#             100% {{
#                 opacity: 1;
#                 transform: translateY(0);
#             }}
#         }}
         
#         .custom-button-container {{
#             display: flex;
#             justify-content: flex-start;
#             margin-left: 100px;
            
#         }}

#         .stButton > button {{
#             background-color: #007bff !important;
#             color: white !important;
#             padding: 14px 30px !important;
#             font-size: 18px !important;
#             border: none;
#             border-radius: 8px;
#         }}

#         .stButton > button:hover {{
#             background-color: #0056b3 !important;
#         }}

#         /* About Section Styling */
#         #about-section {{
#             margin-top: 600px;
#             background-color: rgba(0, 119, 255, 0.25);
#             padding: 50px;
#             border-radius: 12px;
#             animation: fadeInSlide 1.5s ease-out forwards;
#             opacity: 0;
#         }}

#         #about-section h2, #about-section p {{
#             color: white;
#             font-size:20;
#             text-align: center;
#         }}

#         @keyframes fadeInSlide {{
#             0% {{
#                 opacity: 0;
#                 transform: translateY(40px);
#             }}
#             100% {{
#                 opacity: 1;
#                 transform: translateY(0);
#             }}
#         }}
#         </style>

#         <div class="background"></div>

#         <div class="top-right-button">
#             <a href="mailto:your-email@example.com" target="_blank">Contact Us</a>
#             <a href="#about-section">About</a>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# # Set background
# set_background_web("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCd5zNSfuI189Eghdfq-1NTfQ1GDQd7WFacg&s")

# # Session state init
# if "page" not in st.session_state:
#     st.session_state.page = "main"
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
# if "title_animated" not in st.session_state:
#     st.session_state.title_animated = False

# # Title
# title_text = "📘 Welcome to Recommendation Engine For Curating Learning Content"
# if not st.session_state.title_animated:
#     title_container = st.empty()
#     for i in range(1, len(title_text) + 1):
#         title_container.markdown(
#             f"<div class='animated-title'>{title_text[:i]}</div>",
#             unsafe_allow_html=True
#         )
#         time.sleep(0.02)
#     st.session_state.title_animated = True
# else:
#     st.markdown(
#         f"<div class='animated-title'>{title_text}</div>",
#         unsafe_allow_html=True
#     )


# # Main Page
# if st.session_state.page == "main":
#     st.markdown("<div style='margin-top: 300px;'></div>", unsafe_allow_html=True)
#     st.title("     Ready to get your path?")

#     st.markdown("<div class='custom-button-container'>", unsafe_allow_html=True)
#     if st.button(" Get Started"):
#         st.session_state.page = "auth"
#         st.rerun()
#     st.markdown("</div>", unsafe_allow_html=True)

#     # About Section
#     st.markdown("""
#         <div id="about-section">
#             <h2>ℹ️ About</h2>
#             <h3>
#                 This recommendation engine helps users find the best learning paths based on their interests, goals, and skill levels.
#                 We use AI techniques to personalize your experience and guide you through relevant educational content.
#             </h3>
#         </div>
#     """, unsafe_allow_html=True)

# # Auth and App Pages
# elif st.session_state.page == "auth":
#     from auth import auth_app
#     auth_app()

# elif st.session_state.page == "app_full":
#     from app_full import run_app
#     run_app()
import streamlit as st
import time

# Set page config
st.set_page_config(page_title="Learning Path Engine", layout="wide")

def set_background_web(url):
    st.markdown(
        f"""
        <style>
        .background {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-image: url("{url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            filter: blur(10px);
            z-index: -1;
        }}

        .stApp {{
            background-color: rgba(0, 0, 0, 0);
        }}

        .top-right-button {{
            position: fixed;
            top: 20px;
            right: 300px;
            z-index: 9999;
            display: flex;
            gap: 45px;
        }}

        .top-right-button a {{
            background-color: #1f77b4;
            color: white;
            padding: 10px 18px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
        }}

        .top-right-button a:hover {{
            background-color: #135a96;
        }}

        .animated-title {{
            color: #FFFFFF;
            font-size: 70px;
            margin-left: 100px;
            margin-top: 100px;
            font-weight: bold;
            animation: fadeInUp 3.5s ease-out;
        }}

        @keyframes fadeInUp {{
            0% {{
                opacity: 0;
                transform: translateY(30px);
            }}
            100% {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
         
        .custom-button-container {{
            display: flex;
            justify-content: flex-start;
            margin-left: 100px;
            
        }}

        .stButton > button {{
            background-color: #007bff !important;
            color: white !important;
            padding: 14px 30px !important;
            font-size: 18px !important;
            border: none;
            border-radius: 8px;
        }}

        .stButton > button:hover {{
            background-color: #0056b3 !important;
        }}

        /* About Section Styling */
        #about-section {{
            margin-top: 600px;
            background-color: rgba(0, 119, 255, 0.25);
            padding: 50px;
            border-radius: 12px;
            animation: fadeInSlide 1.5s ease-out forwards;
            opacity: 0;
        }}

        #about-section h2, #about-section p {{
            color: white;
            font-size:20;
            text-align: center;
        }}

        @keyframes fadeInSlide {{
            0% {{
                opacity: 0;
                transform: translateY(40px);
            }}
            100% {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Session state init
if "page" not in st.session_state:
    st.session_state.page = "main"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "title_animated" not in st.session_state:
    st.session_state.title_animated = False

# Main Page
if st.session_state.page == "main":
    # Set background and add navigation buttons only for main page
    set_background_web("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCd5zNSfuI189Eghdfq-1NTfQ1GDQd7WFacg&s")
    
    # Add the background div and top-right buttons only for main page
    st.markdown("""
        <div class="background"></div>
        <div class="top-right-button">
            <a href="mailto:your-email@example.com" target="_blank">Contact Us</a>
            <a href="#about-section">About</a>
        </div>
    """, unsafe_allow_html=True)
    
    # Title animation only for main page
    title_text = "📘 Welcome to Recommendation Engine For Curating Learning Content"
    if not st.session_state.title_animated:
        title_container = st.empty()
        for i in range(1, len(title_text) + 1):
            title_container.markdown(
                f"<div class='animated-title'>{title_text[:i]}</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.02)
        st.session_state.title_animated = True
    else:
        st.markdown(
            f"<div class='animated-title'>{title_text}</div>",
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top: 300px;'></div>", unsafe_allow_html=True)
    st.title("     Ready to get your path?")

    st.markdown("<div class='custom-button-container'>", unsafe_allow_html=True)
    if st.button(" Get Started"):
        st.session_state.page = "auth"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # About Section only for main page
    st.markdown("""
        <div id="about-section">
            <h2>ℹ️ About</h2>
            <h3>
                This recommendation engine helps users find the best learning paths based on their interests, goals, and skill levels.
                We use AI techniques to personalize your experience and guide you through relevant educational content.
            </h3>
        </div>
    """, unsafe_allow_html=True)

# Auth and App Pages
elif st.session_state.page == "auth":
    from auth import auth_app
    auth_app()

elif st.session_state.page == "app_full":
    from app_full import run_app
    run_app()