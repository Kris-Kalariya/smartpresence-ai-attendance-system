import streamlit as st

def main():
    st.header("This is title")
    name = st.text_input("Enter your name : ")

    if st.button("Hi", type='primary', key='btn1', width='stretch'):
        print('Hiiii', name)
    if st.button("Byy", type='primary', key='btn1', width='stretch'):
        print('Byyy', name)


if __name__ == "__main__":
    main()