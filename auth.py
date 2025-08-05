# import streamlit as st
# from db import add_user, get_user
# from utils import hash_password, verify_password

# def auth_app():
#     background_image_url = "https://images.unsplash.com/photo-1557804506-669a67965ba0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80"
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background: url("{background_image_url}");
#             background-size: cover;
#             background-position: center;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#             min-height: 100vh;
#         }}

#         .block-container {{
#             background-color: rgba(0, 0, 0, 0);
#             padding: 0rem !important;
#             max-width: 100% !important;
#             width: 100% !important;
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

#         /* Enhanced Home Button Styling */
#         .home-button-container {{
#             position: fixed;
#             top: 15px;
#             left: 15px;
#             z-index: 9999;
#         }}

#         .stButton.home-btn > button {{
#             background: rgba(255, 255, 255, 0.95) !important;
#             color: #2c3e50 !important;
#             border: 2px solid rgba(102, 126, 234, 0.3) !important;
#             border-radius: 30px !important;
#             padding: 10px 24px !important;
#             font-weight: 700 !important;
#             font-size: 15px !important;
#             box-shadow: 0 6px 25px rgba(0, 0, 0, 0.15) !important;
#             transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
#             height: 44px !important;
#             min-width: 100px !important;
#             backdrop-filter: blur(10px) !important;
#         }}

#         .stButton.home-btn > button:hover {{
#             transform: translateY(-3px) scale(1.05) !important;
#             box-shadow: 0 10px 35px rgba(102, 126, 234, 0.4) !important;
#             background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
#             color: white !important;
#             border-color: transparent !important;
#         }}

#         .stButton.home-btn > button:active {{
#             transform: translateY(-1px) scale(1.02) !important;
#         }}

#         /* Main Auth Container - Immediate visibility and reduced width */
#         .auth-container {{
#             display: flex !important;
#             justify-content: center !important;
#             align-items: flex-start !important;
#             min-height: 100vh !important;
#             padding: 20px 10px !important;
#             margin: 0 !important;
#             padding-top: 80px !important;
#         }}

#         .auth-card {{
#             background: rgba(255, 255, 255, 0.95) !important;
#             backdrop-filter: blur(20px) !important;
#             border-radius: 20px !important;
#             padding: 25px !important;
#             box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2) !important;
#             max-width: 350px !important;
#             width: 100% !important;
#             border: 1px solid rgba(255,255,255,0.3) !important;
#             animation: slideUp 0.8s ease-out !important;
#             margin: 0 auto !important;
#             position: relative !important;
#         }}

#         @keyframes slideUp {{
#             0% {{
#                 opacity: 0;
#                 transform: translateY(30px);
#             }}
#             100% {{
#                 opacity: 1;
#                 transform: translateY(0);
#             }}
#         }}

#         /* Title Styling */
#         .auth-title {{
#             color: #2c3e50 !important;
#             text-align: center !important;
#             font-size: 1.8rem !important;
#             margin-bottom: 0.5rem !important;
#             font-weight: 700 !important;
#             background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
#             -webkit-background-clip: text !important;
#             -webkit-text-fill-color: transparent !important;
#             background-clip: text !important;
#         }}

#         .auth-subtitle {{
#             color: #6c757d !important;
#             text-align: center !important;
#             margin-bottom: 1rem !important;
#             font-size: 0.9rem !important;
#             font-weight: 400 !important;
#         }}

#         /* Input Styling - Reduced width and height */
#         .stTextInput > div > div > input {{
#             background-color: #f8f9fa !important;
#             color: #2c3e50 !important;
#             border: 2px solid #e9ecef !important;
#             border-radius: 8px !important;
#             padding: 8px 12px !important;
#             font-size: 13px !important;
#             transition: all 0.3s ease !important;
#             height: 35px !important;
#             min-height: 35px !important;
#             line-height: 1.2 !important;
#             width: 100% !important;
#         }}

#         .stTextInput > div > div > input:focus {{
#             border-color: #667eea !important;
#             box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
#         }}

#         .stTextInput > label {{
#             color: #495057 !important;
#             font-weight: 600 !important;
#             font-size: 12px !important;
#             margin-bottom: 3px !important;
#         }}

#         .stTextInput {{
#             margin-bottom: 10px !important;
#         }}

#         /* Tabs Styling - Ensure immediate visibility */
#         .stTabs {{
#             margin-top: 0 !important;
#             margin-bottom: 0 !important;
#         }}

#         .stTabs [data-baseweb="tab-list"] {{
#             gap: 4px !important;
#             background-color: #f1f3f4 !important;
#             border-radius: 10px !important;
#             padding: 3px !important;
#             margin-bottom: 1rem !important;
#             justify-content: center !important;
#             width: 100% !important;
#         }}

#         .stTabs [data-baseweb="tab-list"] button {{
#             background-color: transparent !important;
#             border: none !important;
#             border-radius: 7px !important;
#             color: #6c757d !important;
#             font-weight: 600 !important;
#             padding: 8px 16px !important;
#             transition: all 0.3s ease !important;
#             font-size: 13px !important;
#             flex: 1 !important;
#         }}

#         .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {{
#             background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
#             color: white !important;
#             box-shadow: 0 3px 10px rgba(102, 126, 234, 0.3) !important;
#         }}

#         .stTabs [data-baseweb="tab-highlight"] {{
#             background-color: transparent !important;
#         }}

#         .stTabs [data-baseweb="tab-panel"] {{
#             padding-top: 0px !important;
#             margin-top: 0 !important;
#         }}

#         /* Form Buttons - Reduced size */
#         .stButton > button {{
#             background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
#             color: white !important;
#             font-weight: 600 !important;
#             border: none !important;
#             border-radius: 8px !important;
#             padding: 10px 20px !important;
#             font-size: 14px !important;
#             width: 100% !important;
#             transition: all 0.3s ease !important;
#             box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
#             height: 40px !important;
#             margin-top: 8px !important;
#         }}

#         .stButton > button:hover {{
#             transform: translateY(-1px) !important;
#             box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4) !important;
#         }}

#         /* Success/Error Messages */
#         .stSuccess {{
#             background-color: rgba(40, 167, 69, 0.1) !important;
#             color: #28a745 !important;
#             border-left: 4px solid #28a745 !important;
#             border-radius: 6px !important;
#             padding: 8px !important;
#             margin: 8px 0 !important;
#             font-size: 13px !important;
#         }}

#         .stError {{
#             background-color: rgba(220, 53, 69, 0.1) !important;
#             color: #dc3545 !important;
#             border-left: 4px solid #dc3545 !important;
#             border-radius: 6px !important;
#             padding: 8px !important;
#             margin: 8px 0 !important;
#             font-size: 13px !important;
#         }}

#         /* Form spacing - Ensure immediate visibility */
#         .stForm {{
#             padding: 0 !important;
#             margin: 0 !important;
#         }}

#         /* Remove extra margins and ensure immediate visibility */
#         .element-container {{
#             margin-bottom: 0.2rem !important;
#         }}

#         /* Remove top spacing and ensure content is visible immediately */
#         .main .block-container {{
#             padding-top: 0rem !important;
#             margin-top: 0rem !important;
#         }}

#         /* Force immediate visibility of tabs */
#         .stTabs > div {{
#             margin-top: 0 !important;
#             padding-top: 0 !important;
#         }}

#         /* Ensure the entire app content is visible from the start */
#         .stApp > div {{
#             margin-top: 0 !important;
#             padding-top: 0 !important;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # Enhanced Home Button - Fixed positioning
#     st.markdown('<div style="position: fixed; top: 15px; left: 15px; z-index: 9999;">', unsafe_allow_html=True)
#     if st.button("🏠 Home", key="home_btn", help="Return to main page"):
#         st.session_state.page = "main"
#         st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)

#     # Main Auth Container - Immediate visibility with reduced width
#     st.markdown('<div class="auth-container">', unsafe_allow_html=True)
#     st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    
#     # Title Section
#     st.markdown('<h1 class="auth-title">Authentication</h1>', unsafe_allow_html=True)
#     st.markdown('<p class="auth-subtitle">Sign in to your account or create a new one</p>', unsafe_allow_html=True)
    
#     # Tabs for Login/Signup - Force immediate visibility
#     tab_login, tab_signup = st.tabs(["Sign In", "Sign Up"])

#     with tab_login:
#         with st.form("login", clear_on_submit=False):
#             u = st.text_input("Username", placeholder="Enter your username")
#             p = st.text_input("Password", type="password", placeholder="Enter your password")
            
#             login_button = st.form_submit_button("Sign In")
            
#             if login_button:
#                 if u and p:
#                     user = get_user(u)
#                     if user and verify_password(p, user["password"]):
#                         st.session_state.logged_in = True
#                         st.session_state.username = u
#                         st.session_state.page = "app_full"
#                         st.success("Login successful! Redirecting...")
#                         st.rerun()
#                     else:
#                         st.error("Invalid credentials. Please try again.")
#                 else:
#                     st.error("Please fill in all fields.")

#     with tab_signup:
#         with st.form("signup", clear_on_submit=True):
#             u = st.text_input("Username", placeholder="Create a unique username")
#             p = st.text_input("Password", type="password", placeholder="Create a strong password")
#             confirm_p = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
            
#             signup_button = st.form_submit_button("Create Account")
            
#             if signup_button:
#                 if u and p and confirm_p:
#                     if p == confirm_p:
#                         if len(p) >= 6:
#                             if add_user(u, hash_password(p)):
#                                 st.success("Account created successfully! Please sign in now.")
#                             else:
#                                 st.error("Username already exists. Please choose another.")
#                         else:
#                             st.error("Password must be at least 6 characters long.")
#                     else:
#                         st.error("Passwords don't match. Please try again.")
#                 else:
#                     st.error("Please fill in all fields.")

#     st.markdown('</div>', unsafe_allow_html=True)  # Close auth-card
#     st.markdown('</div>', unsafe_allow_html=True)  # Close auth-container

import streamlit as st
from db import add_user, get_user
from utils import hash_password, verify_password

def auth_app():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            min-height: 100vh;
        }

        .block-container {
            background-color: rgba(0, 0, 0, 0);
            padding: 0rem !important;
            max-width: 100% !important;
            width: 100% !important;
        }

        /* Hide default elements from main.py */
        .animated-title,
        .top-right-button,
        .background {
            display: none !important;
        }

        /* Enhanced Home Button */
        .home-button-container {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 9999;
        }

        .stButton.home-btn > button {
            background: rgba(255, 255, 255, 0.15) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
            border-radius: 25px !important;
            padding: 8px 20px !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            backdrop-filter: blur(10px) !important;
            transition: all 0.3s ease !important;
        }

        .stButton.home-btn > button:hover {
            background: rgba(255, 255, 255, 0.25) !important;
            transform: translateY(-2px) !important;
        }

        /* Main Container */
        .auth-main-container {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .auth-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 40px 25px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
            max-width: 320px;
            width: 100%;
            text-align: center;
            backdrop-filter: blur(10px);
        }

        /* User Icon */
        .user-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            border-radius: 50%;
            margin: 0 auto 30px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 8px 20px rgba(30, 60, 114, 0.3);
        }

        .user-icon svg {
            width: 40px;
            height: 40px;
            fill: white;
        }

        /* Input Fields */
        .stTextInput > div > div > input {
            background-color: #f8f9fa !important;
            color: #495057 !important;
            border: 2px solid #e9ecef !important;
            border-radius: 8px !important;
            padding: 15px 45px 15px 15px !important;
            font-size: 14px !important;
            transition: all 0.3s ease !important;
            height: 50px !important;
            width: 100% !important;
        }

        .stTextInput > div > div > input:focus {
            border-color: #2a5298 !important;
            box-shadow: 0 0 0 3px rgba(42, 82, 152, 0.1) !important;
        }

        .stTextInput > label {
            color: #495057 !important;
            font-weight: 600 !important;
            font-size: 13px !important;
            margin-bottom: 5px !important;
            text-align: left !important;
            display: block !important;
        }

        .stTextInput {
            margin-bottom: 15px !important;
            position: relative;
            text-align: left !important;
        }

        /* Input Icons */
        .input-with-icon {
            position: relative;
        }

        .input-icon {
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: #6c757d;
            z-index: 10;
            pointer-events: none;
        }

        /* Tabs - Hide default tabs, use custom buttons */
        .stTabs {
            display: none !important;
        }

        .custom-tabs {
            display: flex;
            margin-bottom: 25px;
            background: #f1f3f4;
            border-radius: 8px;
            padding: 4px;
        }

        .tab-button {
            flex: 1;
            padding: 10px 20px;
            background: transparent;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            font-size: 14px;
            color: #6c757d;
            transition: all 0.3s ease;
        }

        .tab-button.active {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            color: white;
            box-shadow: 0 2px 8px rgba(30, 60, 114, 0.3);
        }

        /* Login Button */
        .stButton > button {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%) !important;
            color: white !important;
            font-weight: 600 !important;
            font-size: 16px !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 15px 20px !important;
            width: 100% !important;
            height: 50px !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 15px rgba(30, 60, 114, 0.3) !important;
            margin-top: 20px !important;
        }

        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(30, 60, 114, 0.4) !important;
        }

        /* Checkbox styling */
        .stCheckbox {
            margin: 15px 0 !important;
        }

        .stCheckbox > label {
            color: #495057 !important;
            font-size: 13px !important;
        }

        /* Links */
        .forgot-password {
            color: #2a5298;
            text-decoration: none;
            font-size: 13px;
            margin-top: 15px;
            display: inline-block;
        }

        .forgot-password:hover {
            text-decoration: underline;
        }

        /* Success/Error Messages */
        .stSuccess {
            background-color: rgba(40, 167, 69, 0.1) !important;
            color: #28a745 !important;
            border-left: 4px solid #28a745 !important;
            border-radius: 6px !important;
            padding: 10px !important;
            margin: 10px 0 !important;
            font-size: 14px !important;
        }

        .stError {
            background-color: rgba(220, 53, 69, 0.1) !important;
            color: #dc3545 !important;
            border-left: 4px solid #dc3545 !important;
            border-radius: 6px !important;
            padding: 10px !important;
            margin: 10px 0 !important;
            font-size: 14px !important;
        }

        /* Form styling */
        .stForm {
            padding: 0 !important;
            margin: 0 !important;
        }

        /* Remove extra spacing */
        .element-container {
            margin-bottom: 0 !important;
        }

        .main .block-container {
            padding-top: 0rem !important;
            margin-top: 0rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Home Button
    st.markdown('<div style="position: fixed; top: 20px; left: 20px; z-index: 9999;">', unsafe_allow_html=True)
    if st.button("🏠 Home", key="home_btn", help="Return to main page"):
        st.session_state.page = "main"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Initialize session state for tab selection
    if 'auth_tab' not in st.session_state:
        st.session_state.auth_tab = 'login'

    # Main Container
    st.markdown('<div class="auth-main-container">', unsafe_allow_html=True)
    st.markdown('<div class="auth-card">', unsafe_allow_html=True)
    
    # User Icon
    st.markdown('''
    <div class="user-icon">
        <svg viewBox="0 0 24 24">
            <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
        </svg>
    </div>
    ''', unsafe_allow_html=True)

    # Custom Tab Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("LOGIN", key="login_tab", use_container_width=True):
            st.session_state.auth_tab = 'login'
    with col2:
        if st.button("SIGN UP", key="signup_tab", use_container_width=True):
            st.session_state.auth_tab = 'signup'

    # Login Form
    if st.session_state.auth_tab == 'login':
        with st.form("login", clear_on_submit=False):
            # Username field with icon
            st.markdown('<div class="input-with-icon">', unsafe_allow_html=True)
            u = st.text_input("Username", placeholder="Enter your username", key="login_username")
            st.markdown('<div class="input-icon">👤</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Password field with icon
            st.markdown('<div class="input-with-icon">', unsafe_allow_html=True)
            p = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")
            st.markdown('<div class="input-icon">🔒</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Remember me checkbox
            remember_me = st.checkbox("Remember me")
            
            # Login button
            login_button = st.form_submit_button("LOGIN")
            
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
        
        # Forgot Password link
        st.markdown('<a href="#" class="forgot-password">Forgot Password?</a>', unsafe_allow_html=True)

    # Signup Form
    else:
        with st.form("signup", clear_on_submit=True):
            # Username field with icon
            st.markdown('<div class="input-with-icon">', unsafe_allow_html=True)
            u = st.text_input("Username", placeholder="Choose a username", key="signup_username")
            st.markdown('<div class="input-icon">👤</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Email field with icon
            st.markdown('<div class="input-with-icon">', unsafe_allow_html=True)
            email = st.text_input("Email", placeholder="Enter your email", key="signup_email")
            st.markdown('<div class="input-icon">📧</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Password field with icon
            st.markdown('<div class="input-with-icon">', unsafe_allow_html=True)
            p = st.text_input("Password", type="password", placeholder="Create a password", key="signup_password")
            st.markdown('<div class="input-icon">🔒</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Confirm Password field with icon
            st.markdown('<div class="input-with-icon">', unsafe_allow_html=True)
            confirm_p = st.text_input("Confirm Password", type="password", placeholder="Confirm your password", key="confirm_password")
            st.markdown('<div class="input-icon">🔒</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Sign up button
            signup_button = st.form_submit_button("CREATE ACCOUNT")
            
            if signup_button:
                if u and email and p and confirm_p:
                    if p == confirm_p:
                        if len(p) >= 6:
                            # Basic email validation
                            if "@" in email and "." in email:
                                if add_user(u, hash_password(p)):
                                    st.success("Account created successfully! Please login now.")
                                    st.session_state.auth_tab = 'login'
                                    st.rerun()
                                else:
                                    st.error("Username already exists. Please choose another.")
                            else:
                                st.error("Please enter a valid email address.")
                        else:
                            st.error("Password must be at least 6 characters long.")
                    else:
                        st.error("Passwords don't match. Please try again.")
                else:
                    st.error("Please fill in all fields.")

    st.markdown('</div>', unsafe_allow_html=True)  # Close auth-card
    st.markdown('</div>', unsafe_allow_html=True)  # Close auth-main-container