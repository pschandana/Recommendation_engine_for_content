# import streamlit as st
# from db import add_user, get_user
# from utils import hash_password, verify_password

# def auth_app():
#     background_image_url = "https://hitfigure.com/wp-content/uploads/2012/03/login-background.jpg"
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("{background_image_url}");
#             background-size: cover;
#             background-position: center;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#         }}

#         .block-container {{
#             background-color: rgba(0, 0, 0, 0);
#             padding: 2rem;
#         }}

#         /* Hide the main title from main.py */
#         .animated-title {{
#             display: none !important;
#         }}

#         /* Hide the top-right buttons from main.py */
#         .top-right-button {{
#             display: none !important;
#         }}

#         /* Hide the background div from main.py */
#         .background {{
#             display: none !important;
#         }}

#         /* Input Styling */
#         .stTextInput > div > div > input,
#         .stTextArea textarea {{
#             background-color: white !important;
#             color: black !important;
#             border-radius: 8px;
#             font-weight: normal;
#         }}

#         /* Tabs Styling */
#         .stTabs [data-baseweb="tab-list"] button {{
#             background-color: transparent !important;
#             border: none !important;
#             box-shadow: none !important;
#             color: white;
#             font-weight: bold;
#             padding: 0.5rem 1rem;
#         }}

#         .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
#             background-color: rgba(0, 123, 255, 0.6);
#             color: white;
#         }}

#         .stTabs [data-baseweb="tab-highlight"] {{
#             background-color: transparent !important;
#         }}

#         /* Light Blue Buttons */
#         .stButton > button {{
#             background-color: #3399ff !important;
#             color: white !important;
#             font-weight: bold;
#             border: none !important;
#             border-radius: 8px !important;
#             padding: 0.5rem 1rem !important;
#             transition: background-color 0.3s ease;
#         }}

#         .stButton > button:hover {{
#             background-color: #007acc !important;
#             cursor: pointer;
#         }}

#         /* Center and style the auth section */
#         .user-auth-section {{
#             margin-top: 100px;
#             background-color: rgba(255, 255, 255, 0.1);
#             padding: 30px;
#             border-radius: 15px;
#             backdrop-filter: blur(10px);
#             max-width: 500px;
#             margin-left: auto;
#             margin-right: auto;
#         }}

#         /* Style the auth title */
#         .auth-title {{
#             color: white;
#             text-align: center;
#             font-size: 2.5rem;
#             margin-bottom: 2rem;
#             font-weight: bold;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # Wrap auth section with custom styling
#     with st.container():
#         st.markdown('<div class="user-auth-section">', unsafe_allow_html=True)
        
#         st.markdown('<h1 class="auth-title">User Authentication</h1>', unsafe_allow_html=True)
        
#         tab_login, tab_signup = st.tabs(["Login", "Signup"])

#         with tab_login:
#             with st.form("login"):
#                 u = st.text_input("Username")
#                 p = st.text_input("Password", type="password")
#                 if st.form_submit_button("Login"):
#                     user = get_user(u)
#                     if user and verify_password(p, user["password"]):
#                         st.session_state.logged_in = True
#                         st.session_state.username = u
#                         st.session_state.page = "app_full"
#                         st.rerun()
#                     else:
#                         st.error("Invalid credentials")

#         with tab_signup:
#             with st.form("signup"):
#                 u = st.text_input("Choose a username")
#                 p = st.text_input("Choose a password", type="password")
#                 if st.form_submit_button("Create Account"):
#                     if add_user(u, hash_password(p)):
#                         st.success("Account created — log in now")
#                     else:
#                         st.error("Username already exists")

#         st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st
from db import add_user, get_user
from utils import hash_password, verify_password

def auth_app():
    background_image_url = "https://images.unsplash.com/photo-1557804506-669a67965ba0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{background_image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            min-height: 100vh;
        }}

        .block-container {{
            background-color: rgba(0, 0, 0, 0);
            padding: 0rem !important;
            max-width: 100% !important;
            width: 100% !important;
        }}

        /* Hide the main title from main.py */
        .animated-title {{
            display: none !important;
        }}

        /* Hide the top-right buttons from main.py */
        .top-right-button {{
            display: none !important;
        }}

        /* Hide the background div from main.py */
        .background {{
            display: none !important;
        }}

        /* Enhanced Home Button Styling */
        .home-button-container {{
            position: fixed;
            top: 15px;
            left: 15px;
            z-index: 9999;
        }}

        .stButton.home-btn > button {{
            background: rgba(255, 255, 255, 0.95) !important;
            color: #2c3e50 !important;
            border: 2px solid rgba(102, 126, 234, 0.3) !important;
            border-radius: 30px !important;
            padding: 10px 24px !important;
            font-weight: 700 !important;
            font-size: 15px !important;
            box-shadow: 0 6px 25px rgba(0, 0, 0, 0.15) !important;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
            height: 44px !important;
            min-width: 100px !important;
            backdrop-filter: blur(10px) !important;
        }}

        .stButton.home-btn > button:hover {{
            transform: translateY(-3px) scale(1.05) !important;
            box-shadow: 0 10px 35px rgba(102, 126, 234, 0.4) !important;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border-color: transparent !important;
        }}

        .stButton.home-btn > button:active {{
            transform: translateY(-1px) scale(1.02) !important;
        }}

        /* Main Auth Container - Immediate visibility and reduced width */
        .auth-container {{
            display: flex !important;
            justify-content: center !important;
            align-items: flex-start !important;
            min-height: 100vh !important;
            padding: 20px 10px !important;
            margin: 0 !important;
            padding-top: 80px !important;
        }}

        .auth-card {{
            background: rgba(255, 255, 255, 0.95) !important;
            backdrop-filter: blur(20px) !important;
            border-radius: 20px !important;
            padding: 25px !important;
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2) !important;
            max-width: 350px !important;
            width: 100% !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
            animation: slideUp 0.8s ease-out !important;
            margin: 0 auto !important;
            position: relative !important;
        }}

        @keyframes slideUp {{
            0% {{
                opacity: 0;
                transform: translateY(30px);
            }}
            100% {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        /* Title Styling */
        .auth-title {{
            color: #2c3e50 !important;
            text-align: center !important;
            font-size: 1.8rem !important;
            margin-bottom: 0.5rem !important;
            font-weight: 700 !important;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
        }}

        .auth-subtitle {{
            color: #6c757d !important;
            text-align: center !important;
            margin-bottom: 1rem !important;
            font-size: 0.9rem !important;
            font-weight: 400 !important;
        }}

        /* Input Styling - Reduced width and height */
        .stTextInput > div > div > input {{
            background-color: #f8f9fa !important;
            color: #2c3e50 !important;
            border: 2px solid #e9ecef !important;
            border-radius: 8px !important;
            padding: 8px 12px !important;
            font-size: 13px !important;
            transition: all 0.3s ease !important;
            height: 35px !important;
            min-height: 35px !important;
            line-height: 1.2 !important;
            width: 100% !important;
        }}

        .stTextInput > div > div > input:focus {{
            border-color: #667eea !important;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
        }}

        .stTextInput > label {{
            color: #495057 !important;
            font-weight: 600 !important;
            font-size: 12px !important;
            margin-bottom: 3px !important;
        }}

        .stTextInput {{
            margin-bottom: 10px !important;
        }}

        /* Tabs Styling - Ensure immediate visibility */
        .stTabs {{
            margin-top: 0 !important;
            margin-bottom: 0 !important;
        }}

        .stTabs [data-baseweb="tab-list"] {{
            gap: 4px !important;
            background-color: #f1f3f4 !important;
            border-radius: 10px !important;
            padding: 3px !important;
            margin-bottom: 1rem !important;
            justify-content: center !important;
            width: 100% !important;
        }}

        .stTabs [data-baseweb="tab-list"] button {{
            background-color: transparent !important;
            border: none !important;
            border-radius: 7px !important;
            color: #6c757d !important;
            font-weight: 600 !important;
            padding: 8px 16px !important;
            transition: all 0.3s ease !important;
            font-size: 13px !important;
            flex: 1 !important;
        }}

        .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3) !important;
        }}

        .stTabs [data-baseweb="tab-highlight"] {{
            background-color: transparent !important;
        }}

        .stTabs [data-baseweb="tab-panel"] {{
            padding-top: 0px !important;
            margin-top: 0 !important;
        }}

        /* Form Buttons - Reduced size */
        .stButton > button {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            font-weight: 600 !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            font-size: 14px !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
            height: 40px !important;
            margin-top: 8px !important;
        }}

        .stButton > button:hover {{
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4) !important;
        }}

        /* Success/Error Messages */
        .stSuccess {{
            background-color: rgba(40, 167, 69, 0.1) !important;
            color: #28a745 !important;
            border-left: 4px solid #28a745 !important;
            border-radius: 6px !important;
            padding: 8px !important;
            margin: 8px 0 !important;
            font-size: 13px !important;
        }}

        .stError {{
            background-color: rgba(220, 53, 69, 0.1) !important;
            color: #dc3545 !important;
            border-left: 4px solid #dc3545 !important;
            border-radius: 6px !important;
            padding: 8px !important;
            margin: 8px 0 !important;
            font-size: 13px !important;
        }}

        /* Form spacing - Ensure immediate visibility */
        .stForm {{
            padding: 0 !important;
            margin: 0 !important;
        }}

        /* Remove extra margins and ensure immediate visibility */
        .element-container {{
            margin-bottom: 0.2rem !important;
        }}

        /* Remove top spacing and ensure content is visible immediately */
        .main .block-container {{
            padding-top: 0rem !important;
            margin-top: 0rem !important;
        }}

        /* Force immediate visibility of tabs */
        .stTabs > div {{
            margin-top: 0 !important;
            padding-top: 0 !important;
        }}

        /* Ensure the entire app content is visible from the start */
        .stApp > div {{
            margin-top: 0 !important;
            padding-top: 0 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Enhanced Home Button - Fixed positioning
    st.markdown('<div style="position: fixed; top: 15px; left: 15px; z-index: 9999;">', unsafe_allow_html=True)
    if st.button("🏠 Home", key="home_btn", help="Return to main page"):
        st.session_state.page = "main"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Main Auth Container - Immediate visibility with reduced width
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    
    # Title Section
    st.markdown('<h1 class="auth-title">Authentication</h1>', unsafe_allow_html=True)
    st.markdown('<p class="auth-subtitle">Sign in to your account or create a new one</p>', unsafe_allow_html=True)
    
    # Tabs for Login/Signup - Force immediate visibility
    tab_login, tab_signup = st.tabs(["Sign In", "Sign Up"])

    with tab_login:
        with st.form("login", clear_on_submit=False):
            u = st.text_input("Username", placeholder="Enter your username")
            p = st.text_input("Password", type="password", placeholder="Enter your password")
            
            login_button = st.form_submit_button("Sign In")
            
            if login_button:
                if u and p:
                    user = get_user(u)
                    if user and verify_password(p, user["password"]):
                        st.session_state.logged_in = True
                        st.session_state.username = u
                        st.session_state.page = "app_full"
                        st.success("Login successful! Redirecting...")
                        st.rerun()
                    else:
                        st.error("Invalid credentials. Please try again.")
                else:
                    st.error("Please fill in all fields.")

    with tab_signup:
        with st.form("signup", clear_on_submit=True):
            u = st.text_input("Username", placeholder="Create a unique username")
            p = st.text_input("Password", type="password", placeholder="Create a strong password")
            confirm_p = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
            
            signup_button = st.form_submit_button("Create Account")
            
            if signup_button:
                if u and p and confirm_p:
                    if p == confirm_p:
                        if len(p) >= 6:
                            if add_user(u, hash_password(p)):
                                st.success("Account created successfully! Please sign in now.")
                            else:
                                st.error("Username already exists. Please choose another.")
                        else:
                            st.error("Password must be at least 6 characters long.")
                    else:
                        st.error("Passwords don't match. Please try again.")
                else:
                    st.error("Please fill in all fields.")

    st.markdown('</div>', unsafe_allow_html=True)  # Close auth-card
    st.markdown('</div>', unsafe_allow_html=True)  # Close auth-container

