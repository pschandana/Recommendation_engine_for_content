
# import streamlit as st
# from db import add_user, get_user
# from utils import hash_password, verify_password

# def auth_app():
#     st.markdown("""
#     <style>
#     /* Overall app background */
#     .stApp {
#         background-color: #f4f6f8; /* light grey */
#         font-family: 'Segoe UI', Tahoma, sans-serif;
#         min-height: 100vh;
#         padding-top: 10px;
#     }

#     /* Headings */
#     h2 {
#         margin-bottom: 20px;
#         font-weight: 700;
#         font-size: 22px;
#         color: #333;
#         text-align: center;
#     }

#     /* LOGIN button specific styling */
#     .login-button-container .stButton > button {
#         background-color: #4a90e2 !important;
#         color: white !important;
#         border-radius: 6px !important;
#         font-size: 15px !important;
#         font-weight: 600 !important;
#         padding: 8px 20px !important;
#         border: none !important;
#         width: 5% !important;
#         transition: background-color 0.2s ease !important;
#         margin-bottom: 10px !important;
#     }
#     .login-button-container .stButton > button:hover {
#         background-color: #3b78c2 !important;
#     }
    
#     /* SIGN UP button specific styling */
#     .signup-button-container .stButton > button {
#         background-color: #4a90e2 !important;
#         color: white !important;
#         border-radius: 6px !important;
#         font-size: 15px !important;
#         font-weight: 600 !important;
#         padding: 8px 10px !important;
#         border: none !important;
#         width: 5% !important;
#         transition: background-color 0.2s ease !important;
#         margin-bottom: 10px !important;
#     }
#     .signup-button-container .stButton > button:hover {
#         background-color: #3b78c2 !important;
#     }

#     /* Form submit buttons - Login and Create Account buttons */
#     button[kind="formSubmit"] {
#         background-color: #4a90e2 !important;
#         color: white !important;
#         border-radius: 6px !important;
#         font-size: 15px !important;
#         font-weight: 600 !important;
#         padding: 10px 20px !important;
#         border: none !important;
#         width: 100% !important;
#         margin-top: 15px !important;
#         transition: background-color 0.2s ease !important;
#     }
#     button[kind="formSubmit"]:hover {
#         background-color: #3b78c2 !important;
#     }
    
#     /* Alternative selector for form submit buttons */
#     div[data-testid="stForm"] button[type="submit"] {
#         background-color: #4a90e2 !important;
#         color: white !important;
#         border-radius: 6px !important;
#         font-size: 15px !important;
#         font-weight: 600 !important;
#         padding: 10px 20px !important;
#         border: none !important;
#         width: 100% !important;
#         margin-top: 15px !important;
#         transition: background-color 0.2s ease !important;
#     }
#     div[data-testid="stForm"] button[type="submit"]:hover {
#         background-color: #3b78c2 !important;
#     }

#     /* Input fields - Fixed width and styling */
#     .stTextInput > div > div > input,
#     .stPassword > div > div > input {
#         background-color: #f9f9f9 !important;
#         border: 1px solid #ccc !important;
#         border-radius: 6px !important;
#         padding: 10px 12px !important;
#         font-size: 14px !important;
#         color: #333 !important;
#         width: 100% !important;
#         max-width: 320px !important;
#         box-sizing: border-box !important;
#     }
#     .stTextInput > div > div > input:focus,
#     .stPassword > div > div > input:focus {
#         border-color: #4a90e2 !important;
#         outline: none !important;
#         box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2) !important;
#     }

#     /* Input containers */
#     .stTextInput > div,
#     .stPassword > div {
#         max-width: 320px !important;
#         width: 100% !important;
#     }

#     .stTextInput,
#     .stPassword {
#         max-width: 320px !important;
#         width: 100% !important;
#         margin: 0 auto !important;
#     }

#     /* Labels */
#     label {
#         font-weight: 500 !important;
#         color: #555 !important;
#         font-size: 13px !important;
#         margin-bottom: 5px !important;
#     }

#     /* Center the form elements */
#     div[data-testid="stForm"] {
#         max-width: 320px;
#         margin: 0 auto;
#     }

#     /* Tab button containers */
#     /* Tab button containers with positioning control */
#     .login-button-container {
#     float: left;
#     width: 50%;
#     text-align: left; /* Change to center or right if needed */
#     }
#     .login-button-container .stButton > button {
#         width: 45% !important; /* Button width */
#         margin-left: px !important; /* Distance from left edge */
#     }
    
#     .signup-button-container {
#     float: right;
#     width: 50%;
#     text-align: right; /* Change to center or left if needed */
#     }
#     .signup-button-container .stButton > button {
#         width: 15% !important; /* Button width */
#         margin-right: 100px !important; /* Distance from right edge */
#     }
#     /* Container for both buttons */
#     .button-row {
#         width: 100%;
#         max-width: 400px;
#         margin: 0 auto 0px auto;
#         overflow: hidden; /* Clear floats */
#     }


#     /* Remove default streamlit padding */
#     .block-container {
#         padding-top: 2rem;
#         padding-bottom: 2rem;
#     }

#     /* Success and error messages */
#     .stSuccess, .stError {
#         max-width: 320px;
#         margin: 10px auto;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # No container needed

#     # Initialize auth_tab
#     if 'auth_tab' not in st.session_state:
#         st.session_state.auth_tab = 'login'

#     # Tab buttons with individual containers - REMOVED use_container_width=True
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown('<div class="login-button-container">', unsafe_allow_html=True)
#         if st.button("LOGIN", key="login_tab"):  # REMOVED use_container_width=True
#             st.session_state.auth_tab = 'login'
#         # No closing container div needed
#     with col2:
#         st.markdown('<div class="signup-button-container">', unsafe_allow_html=True)
#         if st.button("SIGN UP", key="signup_tab"):  # REMOVED use_container_width=True
#             st.session_state.auth_tab = 'signup'
#         st.markdown('</div>', unsafe_allow_html=True)

#     if st.session_state.auth_tab == 'login':
#         st.markdown("<h2>Welcome Back</h2>", unsafe_allow_html=True)
#         with st.form("login_form"):
#             username = st.text_input("Username", placeholder="Enter your username", key="login_username")
#             password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")
#             submitted = st.form_submit_button("Login")

#             if submitted:
#                 if username and password:
#                     user = get_user(username)
#                     if user and verify_password(password, user["password"]):
#                         st.session_state.logged_in = True
#                         st.session_state.username = username
#                         st.session_state.page = "app_full"
#                         st.success("Login successful! Redirecting...")
#                         st.rerun()
#                     else:
#                         st.error("Invalid username or password.")
#                 else:
#                     st.error("Please fill in all fields.")

#     else:
#         st.markdown("<h2>Create Account</h2>", unsafe_allow_html=True)
#         with st.form("signup_form"):
#             username = st.text_input("Username", placeholder="Choose a username", key="signup_username")
#             email = st.text_input("Email", placeholder="Enter your email", key="signup_email")
#             password = st.text_input("Password", type="password", placeholder="Create a password", key="signup_password")
#             confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password", key="confirm_password")
#             submitted = st.form_submit_button("Create Account")

#             if submitted:
#                 if username and email and password and confirm_password:
#                     if password == confirm_password:
#                         if len(password) >= 6:
#                             if "@" in email and "." in email:
#                                 if add_user(username, hash_password(password)):
#                                     st.success("Account created successfully! Please login now.")
#                                     st.session_state.auth_tab = 'login'
#                                     st.rerun()
#                                 else:
#                                     st.error("Username already exists. Please choose another.")
#                             else:
#                                 st.error("Please enter a valid email address.")
#                         else:
#                             st.error("Password must be at least 6 characters long.")
#                     else:
#                         st.error("Passwords do not match.")
#                 else:
#                     st.error("Please fill in all fields.")

#     st.markdown('</div>', unsafe_allow_html=True)

import streamlit as st

def auth_app():
    st.set_page_config(page_title="Auth UI", page_icon="🔐", layout="centered")

    # --- CSS ---
    st.markdown(
        """
        <style>
        /* Full-page gradient and vertical + horizontal centering */
        main {
          background: linear-gradient(135deg,#a1c4fd 0%, #c2e9fb 100%);
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 0;
        }
        /* Force Streamlit container to behave like a centered box */
        .block-container {
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100%;
          padding: 0;
        }
        /* Card styling */
        .card-inner {
          background: #ffffff;
          border-radius: 18px;
          overflow: hidden;
          box-shadow: 0 25px 50px rgba(2,6,23,0.12);
          width: 420px;
          max-width: 94%;
        }
        /* Blue header */
        .card-header {
          background: linear-gradient(90deg,#0052D4,#4364F7,#6FB1FC);
          color: white;
          padding: 18px;
          text-align: center;
          font-size: 22px;
          font-weight: bold;
        }
        /* Tab buttons */
        .tab-buttons {
          display: flex;
          justify-content: space-between;
          margin: 16px 20px 0 20px;
          gap: 10px;
        }
        .tab-btn {
          flex: 1;
          padding: 10px;
          font-weight: bold;
          border: none;
          cursor: pointer;
          border-radius: 10px;
        }
        .active-tab {
          background: linear-gradient(90deg,#0052D4,#4364F7,#6FB1FC);
          color: white;
        }
        .inactive-tab {
          background: white;
          border: 1px solid #ccc;
          color: #333;
        }
        /* Inputs and submit button */
        .stTextInput>div>div>input {
          border-radius: 10px !important;
          padding: 12px !important;
          border: 1px solid #e6e9ef !important;
        }
        .stTextInput > label {
          font-weight: 600;
        }
        .stButton>button {
          border-radius: 12px;
          padding: 12px;
          font-weight: 700;
          background: linear-gradient(90deg,#0052D4,#4364F7,#6FB1FC);
          color: #fff;
          border: none;
          width: 100%;
        }
        .small-link {
          color: #0052D4;
          text-decoration: none;
          cursor: pointer;
        }
        .center-note {
          text-align:center;
          margin-top:12px;
          font-size:14px;
          color:#111827;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Session State ---
    if "users" not in st.session_state:
        st.session_state["users"] = {}
    if "auth_mode" not in st.session_state:
        st.session_state["auth_mode"] = "login"

    # --- Card Start ---
    st.markdown('<div class="card-inner">', unsafe_allow_html=True)
    st.markdown('<div class="card-header">Authentication</div>', unsafe_allow_html=True)

    # Tab Buttons
    st.markdown('<div class="tab-buttons">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login", key="tab_login"):
            st.session_state["auth_mode"] = "login"
    with col2:
        if st.button("Signup", key="tab_signup"):
            st.session_state["auth_mode"] = "signup"
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Login Form ---
    if st.session_state["auth_mode"] == "login":
        email = st.text_input("Email Address", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        st.markdown('<div style="margin-top:8px"><a class="small-link">Forgot password?</a></div>', unsafe_allow_html=True)

        if st.button("Login"):
            if email in st.session_state["users"] and st.session_state["users"][email] == password:
                st.success(f"Welcome back, {email}!")
            else:
                st.error("Invalid username or password")

        st.markdown(
            '<div class="center-note">Create an account <a class="small-link">Signup now</a></div>',
            unsafe_allow_html=True,
        )

    # --- Signup Form ---
    else:
        new_email = st.text_input("Email Address", key="signup_email")
        new_password = st.text_input("Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="signup_confirm")
        if st.button("Sign Up"):
            if new_email in st.session_state["users"]:
                st.error("Username already exists")
            elif new_password != confirm_password:
                st.error("Passwords do not match")
            elif not new_email or not new_password:
                st.error("Please fill all fields")
            else:
                st.session_state["users"][new_email] = new_password
                st.success("Account created successfully! Please login.")
                st.session_state["auth_mode"] = "login"

        st.markdown(
            '<div class="center-note">Already have an account? <a class="small-link">Login</a></div>',
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)  # close card-inner


if __name__ == "__main__":
    auth_app()
