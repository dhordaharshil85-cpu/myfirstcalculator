import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

st.title("🧮 Calculator App")

# Initialize session state for expression
if "expr" not in st.session_state:
    st.session_state.expr = ""

# Display screen
st.text_input("Display", value=st.session_state.expr, key="display", disabled=True)

# Function to handle button presses
def add_val(val):
    if st.session_state.expr == "Error":
        st.session_state.expr = ""
    st.session_state.expr += str(val)

def clear_display():
    st.session_state.expr = ""

def calculate_result():
    try:
        st.session_state.expr = str(eval(st.session_state.expr))
    except Exception:
        st.session_state.expr = "Error"

# Calculator layout
grid = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in grid:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        if btn == "C":
            cols[i].button(btn, use_container_width=True, on_click=clear_display)
        elif btn == "=":
            cols[i].button(btn, use_container_width=True, on_click=calculate_result)
        else:
            cols[i].button(btn, use_container_width=True, on_click=add_val, args=(btn,))