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
#             top: 65px;
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
#             transition: all 0.3s ease;
#         }}

#         .top-right-button a:hover {{
#             background-color: #135a96;
#             transform: translateY(-2px);
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
#             width: 100%;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             margin-top: 150px;
#         }}

#         .custom-button-container > div {{
#             display: flex;
#             justify-content: center;
#             width: 100%;
#         }}

#         .stButton {{
#             display: flex;
#             justify-content: center;
#             width: 100%;
#         }}

#         .stButton > button {{
#             background: linear-gradient(135deg, #4A90E2 0%, #357ABD 100%) !important;
#             color: white !important;
#             padding: 18px 60px !important;
#             font-size: 28px !important;
#             font-weight: 900 !important;
#             font-family: 'Arial Black', Arial, sans-serif !important;
#             letter-spacing: 2px !important;
#             text-transform: uppercase !important;
#             border: none !important;
#             border-radius: 50px !important;
#             box-shadow: 0 8px 25px rgba(74, 144, 226, 0.4) !important;
#             transition: all 0.3s ease !important;
#             margin: 0 auto !important;
#             cursor: pointer !important;
#             min-width: 280px !important;
#             height: 70px !important;
#         }}

#         .stButton > button:hover {{
#             background: linear-gradient(135deg, #357ABD 0%, #2E6BA8 100%) !important;
#             transform: translateY(-3px) !important;
#             box-shadow: 0 12px 35px rgba(74, 144, 226, 0.6) !important;
#         }}

#         .stButton > button:active {{
#             transform: translateY(-1px) !important;
#             box-shadow: 0 6px 20px rgba(74, 144, 226, 0.3) !important;
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
#             font-size: 20px;
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

#         /* Responsive design */
#         @media (max-width: 768px) {{
#             .animated-title {{
#                 font-size: 40px;
#                 margin-left: 20px;
#                 text-align: center;
#             }}
            
#             .custom-button-container {{
#                 margin-left: 20px;
#                 justify-content: center;
#             }}
            
#             .top-right-button {{
#                 right: 20px;
#                 gap: 20px;
#             }}
            
#             #about-section {{
#                 margin: 400px 20px 0 20px;
#                 padding: 40px;
#             }}
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # Session state init
# if "page" not in st.session_state:
#     st.session_state.page = "main"
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
# if "title_animated" not in st.session_state:
#     st.session_state.title_animated = False

# # Main Page
# if st.session_state.page == "main":
#     # Set background and add navigation buttons only for main page
#     set_background_web("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCd5zNSfuI189Eghdfq-1NTfQ1GDQd7WFacg&s")
    
#     # Add the background div and top-right buttons only for main page
#     st.markdown("""
#         <div class="background"></div>
#         <div class="top-right-button">
#             <a href="mailto:your-email@example.com" target="_blank">Contact Us</a>
#             <a href="#about-section">About</a>
#         </div>
#     """, unsafe_allow_html=True)
    
#     # Title animation only for main page
#     title_text = "📘 Welcome to Recommendation Engine For Curating Learning Content"
#     if not st.session_state.title_animated:
#         title_container = st.empty()
#         for i in range(1, len(title_text) + 1):
#             title_container.markdown(
#                 f"<div class='animated-title'>{title_text[:i]}</div>",
#                 unsafe_allow_html=True
#             )
#             time.sleep(0.02)
#         st.session_state.title_animated = True
#     else:
#         st.markdown(
#             f"<div class='animated-title'>{title_text}</div>",
#             unsafe_allow_html=True
#         )

#     # Put the Get Started button immediately below the animated title, centered
#     st.markdown('<div class="custom-button-container">', unsafe_allow_html=True)
#     col1, col2, col3 = st.columns([1, 2, 1])
#     with col2:
#         if st.button("Get Started"):
#             st.session_state.page = "app_full"
#             st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)

#     # About Section only for main page
#     # About Section only for main page
#     st.markdown("""
#         <div id="about-section">
#             <h2>ℹ️ About</h2>
#             <h3>
#                 Our platform is designed to make learning and discovery effortless. Whether you want to grow your skills or find your next favorite book, we’ve got you covered.
#             </h3>
#             <br>
#             <p>
#                 We offer two kinds of personalized recommendations: learning paths to guide your skill growth, and book suggestions to match your reading tastes.
#             </p>
#             <ol>
#                 <li>
#                     <strong>Learning Path Generator</strong><br>
#                     Create a customized roadmap based on your goals, interests, and skills.<br>
#                     Follow a clear, step-by-step process to achieve mastery in your chosen field.<br>
#                     Ideal for students, professionals, and lifelong learners.
#                 </li>
#                 <br>
#                 <li>
#                     <strong>Book Store</strong><br>
#                     Enter a book you love, and we’ll suggest similar titles you might enjoy.<br>
#                     Perfect for exploring new authors, genres, or topics while staying close to your taste.<br>
#                     From career growth to leisure reading, we make your next step easy and exciting.
#                 </li>
#             </ol>
#             <p>
#                 Click “Get Started” and begin your journey today!
#             </p>
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

# Sidebar style override
st.markdown("""
<style>
/* Style sidebar page links */
section[data-testid="stSidebar"] .css-1v3fvcr, 
section[data-testid="stSidebar"] .css-1d391kg {
    font-size: 50px !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg, #4A90E2, #357ABD);
    color: white !important;
    padding: 14px 20px;
    border-radius: 20px;
    margin-bottom: 15px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    transition: all 0.3s ease;
}

/* Hover effect */
section[data-testid="stSidebar"] .css-1v3fvcr:hover, 
section[data-testid="stSidebar"] .css-1d391kg:hover {
    background: linear-gradient(135deg, #357ABD, #2E6BA8);
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.25);
}
</style>
""", unsafe_allow_html=True)

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
            top: 65px;
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
            transition: all 0.3s ease;
        }}

        .top-right-button a:hover {{
            background-color: #135a96;
            transform: translateY(-2px);
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
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 150px;
        }}

        .custom-button-container > div {{
            display: flex;
            justify-content: center;
            width: 100%;
        }}

        .stButton {{
            display: flex;
            justify-content: center;
            width: 100%;
        }}

        .stButton > button {{
            background: linear-gradient(135deg, #4A90E2 0%, #357ABD 100%) !important;
            color: white !important;
            padding: 18px 60px !important;
            font-size: 28px !important;
            font-weight: 900 !important;
            font-family: 'Arial Black', Arial, sans-serif !important;
            letter-spacing: 2px !important;
            text-transform: uppercase !important;
            border: none !important;
            border-radius: 50px !important;
            box-shadow: 0 8px 25px rgba(74, 144, 226, 0.4) !important;
            transition: all 0.3s ease !important;
            margin: 0 auto !important;
            cursor: pointer !important;
            min-width: 280px !important;
            height: 70px !important;
        }}

        .stButton > button:hover {{
            background: linear-gradient(135deg, #357ABD 0%, #2E6BA8 100%) !important;
            transform: translateY(-3px) !important;
            box-shadow: 0 12px 35px rgba(74, 144, 226, 0.6) !important;
        }}

        .stButton > button:active {{
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 20px rgba(74, 144, 226, 0.3) !important;
        }}

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
            font-size: 20px;
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

        @media (max-width: 768px) {{
            .animated-title {{
                font-size: 40px;
                margin-left: 20px;
                text-align: center;
            }}
            
            .custom-button-container {{
                margin-left: 20px;
                justify-content: center;
            }}
            
            .top-right-button {{
                right: 20px;
                gap: 20px;
            }}
            
            #about-section {{
                margin: 400px 20px 0 20px;
                padding: 40px;
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
    set_background_web("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCd5zNSfuI189Eghdfq-1NTfQ1GDQd7WFacg&s")
    
    st.markdown("""
        <div class="background"></div>
        <div class="top-right-button">
            <a href="mailto:recommendationengine2025@gmail.com" target="_blank">Contact Us</a>
            <a href="#about-section">About</a>
        </div>
    """, unsafe_allow_html=True)
    
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

    st.markdown('<div class="custom-button-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Get Started"):
            st.session_state.page = "app_full"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div id="about-section">
            <h2>ℹ️ About</h2>
            <h3>
                Our platform is designed to make learning and discovery effortless. Whether you want to grow your skills or find your next favorite book, we’ve got you covered.
            </h3>
            <br>
            <p>
                We offer two kinds of personalized recommendations: learning paths to guide your skill growth, and book suggestions to match your reading tastes.
            </p>
            <ol>
                <li>
                    <strong>Learning Path Generator</strong><br>
                    Create a customized roadmap based on your goals, interests, and skills.<br>
                    Follow a clear, step-by-step process to achieve mastery in your chosen field.<br>
                    Ideal for students, professionals, and lifelong learners.
                </li>
                <br>
                <li>
                    <strong>Book Store</strong><br>
                    Enter a book you love, and we’ll suggest similar titles you might enjoy.<br>
                    Perfect for exploring new authors, genres, or topics while staying close to your taste.<br>
                    From career growth to leisure reading, we make your next step easy and exciting.
                </li>
            </ol>
            <p>
                Click “Get Started” and begin your journey today!
            </p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "auth":
    from auth import auth_app
    auth_app()

elif st.session_state.page == "app_full":
    from app_full import run_app
    run_app()
