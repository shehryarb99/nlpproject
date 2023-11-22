import streamlit as st
from textblob import TextBlob
from pattern.en import pluralize, singularize, comparative, superlative
import streamlit.components.v1 as components

def main():
    st.title("Spell Correction")

    # html_temp6 = """
    # <div style="background-color:#16A085;"><p style="color:white;font-size:60px;">Spell Correction</p></div>
    # """
    # components.html(html_temp6)
    
    text_data = st.text_area("Enter Text Here")
    a = TextBlob(text_data)
    
    if st.button("Correct"):
        st.success(a.correct())

    # html_temp7 = """
    # <div style="background-color:tomato;"><p style="color:white;font-size:60px;,text-align:center;">pluralize & singularize</p></div>
    # """
    # components.html(html_temp7)
    
    text_data1 = st.text_input("Enter a word For pluralize / singularize")
    
    if st.checkbox("pluralize"):
        st.warning(pluralize(text_data1))
    
    if st.checkbox("singularize"):
        st.warning(singularize(text_data1))

    # html_temp8 = """
    # <div style="background-color:#16A085;"><p style="color:white;font-size=60px;,text-align:center;">comparative & superlative</p></div>
    # """
    # components.html(html_temp8)
    
    text2 = st.text_input("Enter Text For comparative & superlative")
    
    if st.checkbox("comparative"):
        st.success(comparative(text2))
    
    if st.checkbox("superlative"):
        st.success(superlative(text2))

if __name__ == '__main__':
    main()
