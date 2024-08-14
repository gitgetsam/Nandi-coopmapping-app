import streamlit as st


if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "User", "Admin", "Super Admin"]


def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out")
about = st.Page("about.py", title="About")
request_1 = st.Page(
    "User/request_1.py",
    title="Dataframe 1",
    default=(role == "User"),
)
request_2 = st.Page(
    "User/request_2.py",
    title="A Map of All Coops"
)
request_3 = st.Page(
    "User/request_3.py",
    title="Graphs & Charts"
)
request_4 = st.Page(
    "User/request_4.py",
    title="Selection App"
)
respond_1 = st.Page(
    "Admin/respond_1.py",
    title="Dataframe 2",
    default=(role == "Admin"),
)
respond_2 = st.Page(
    "Admin/respond_2.py", title="Respond 2"
)
admin_1 = st.Page(
    "Super Admin/admin_1.py",
    title="Dataframe 3",
    default=(role == "Super Admin"),
)
admin_2 = st.Page("Super Admin/admin_2.py", title="Advanced Graphs & Charts")

account_pages = [logout_page, about]
user_pages = [request_1, request_2, request_3, request_4]
admin_pages = [respond_1, respond_2]
super_admin_pages = [admin_1, admin_2]

st.title("Nandi County Data App")
#st.logo("images/logo2.png", icon_image="images/logo2.png")

page_dict = {}
if st.session_state.role in ["User", "Admin", "Super Admin"]:
    page_dict["User"] = user_pages
if st.session_state.role in ["Admin", "Super Admin"]:
    page_dict["Admin"] = admin_pages
if st.session_state.role == "Super Admin":
    page_dict["Super Admin"] = super_admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()