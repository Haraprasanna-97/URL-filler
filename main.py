import streamlit as st
from urlHandler import urlHandler

def createBasicPageLayout(title: str) -> tuple | str:
    """
    Defines the basic layout of the streamlit application. Returns a message stating to enter a valid URL
    
    :param title: Defines the titke of the streamlit application
    :type title: str
    :return: A tuple containing the URL entered by the user, the sections (info and placeholder) and a flag for showing or hiding the filled URL. Message stating to enter a valid URL
    :rtype: tuple | str
    """

    st.set_page_config(page_title = title, page_icon="🔗", layout="wide", initial_sidebar_state="auto")
    st.title(title)
    st.sidebar.title(title)
    url = st.text_input("Enter the url", key="urlInput")
    st.sidebar.header("Settings")
    showInfoSec = st.sidebar.checkbox("Show URL details")
    testFilledURL = st.sidebar.checkbox("Test filled URL")
    if url.startswith("http://") or url.startswith("https://"):
        return url, showInfoSec, testFilledURL
    else:
        return "Enter a valid URL to contnue"

def fillInfoSection(urlHandlerObject: urlHandler):
    """
    Deals with filling the info section
    
    :param urlHandlerObject: The object whose information will be displayed
    :type urlHandlerObject: urlHandler
    """

    st.header("URL details")

    with st.expander("Object"):
        st.write(urlHandlerObject.json)
        
    with st.expander("Parts"):
        st.write(urlHandlerObject.parts)
    
    if urlHandlerObj.parts["Query"]:
        with st.expander("Query"):
            st.dataframe(urlHandlerObject.table, hide_index=True)
            if(any([len(val) == 2 for val in urlHandlerObj.values])): # Check if their is any key that has multiple values
                st.write("Multiple values for the same parameters are separated by commas")

def fillPlaceholders(fields: list | None, urlHandlerObject: urlHandler):
    """
    Defines the placeholder form
    
    :param fields: The fields in the query parameters
    :type fields: list | None
    :param urlHandlerObject: The object containing the definePlaceholders method
    :type urlHandlerObject: urlHandler
    """

    st.header("Placeholder names")
    if isinstance(fields, list):
        placeholderNames = [
            st.text_input(
                f"Placeholder name for '{field}' field",
                key=f"placeholder_{key}",
                help="Spaces will be replaced with underscore"
            ).replace(" ", "_")
            for key, field in enumerate(fields, start=1)
        ]
        urlHandlerObject.definePlaceholders(placeholderNames=placeholderNames)
        return placeholderNames
    else:
        st.info("Their are no query paramitters in the given URL")

def fillPlaceholderValues(fields: list | None, urlHandlerObject: urlHandler):
    """
    Defines the placeholder form for acceoting values for the fields
    
    :param fields: The fields in the query parameters
    :type fields: list | None
    :param urlHandlerObject: The object containing the definePlaceholders method
    :type urlHandlerObject: urlHandler
    """

    st.header("Placeholder values")
    if isinstance(fields, list):
        placeholderValues = [
            st.text_input(
                f"Value for '{field}' field",
                key=f"value_{key}")
            for key, field in enumerate(fields, start=1)
        ]
        urlHandlerObject.definePlaceholderValues(placeholderValues=placeholderValues)
    else:
        st.info("Their are no query paramitters in the given URL")

if __name__ == "__main__":
    ReturnValue = createBasicPageLayout(title="URL filler")
    if isinstance(ReturnValue, tuple):
        url, showInfoSec, testFilledURL = ReturnValue
    
        urlHandlerObj = urlHandler(url)
        if url:
            if showInfoSec:
                fillInfoSection(urlHandlerObject=urlHandlerObj)
            
            placeholderNames = fillPlaceholders(fields=urlHandlerObj.fields, urlHandlerObject=urlHandlerObj)
            
            if isinstance(placeholderNames, list):
                if urlHandlerObj.placeholderUrl:
                    st.code(urlHandlerObj.placeholderUrl, language=None)

                if all(placeholderNames):
                    if testFilledURL:
                        fillPlaceholderValues(fields=placeholderNames, urlHandlerObject=urlHandlerObj)
                
                if urlHandlerObj.filledUrl:
                    st.write(urlHandlerObj.filledUrl)

    elif isinstance(ReturnValue, str):
        st.info(ReturnValue)