import streamlit as st
from urlHandler import urlHandler

def createBasicPageLayout(title: str) -> tuple | str:
    """
    Defines the basic layout of the streamlit application. Returns a message stating to enter a valid URL
    
    :param title: Defines the titke of the streamlit application
    :type title: str
    :return: A tuple containing the URL entered by the user, the sections (info and placeHolder) and a flag for showing or hiding the filled URL. Message stating to enter a valid URL
    :rtype: tuple | str
    """

    st.title(title)
    url = st.text_input("Enter the url", key="urlInput")
    if url.startswith("http://") or url.startswith("https://"):
        st.sidebar.title("Settings")
        showInfoSec = st.sidebar.checkbox("Show URL info")
        testFilledURL = st.sidebar.checkbox("Test filled URL")
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

def fillPlaceholders(fields: list | None, urlHandlerObject: urlHandler):
    """
    Defines the placeholder form
    
    :param fields: The fields in the query parameters
    :type fields: list | None
    :param urlHandlerObject: The object containing the definePlaceHolders method
    :type urlHandlerObject: urlHandler
    """

    st.header("Placeholder names")
    if isinstance(fields, list):
        placeHolderNames = [
            st.text_input(
                f"Placrholder name for '{field}' field",
                key=f"placeholder_{key}",
                help="Spaces will be replaced with underscore"
            ).replace(" ", "_")
            for key, field in enumerate(fields, start=1)
        ]
        urlHandlerObject.definePlaceholders(placeHolderNames=placeHolderNames)
        return placeHolderNames
    else:
        st.info("Their are no query paramitters in the given URL")

def fillPlaceholderValues(fields: list | None, urlHandlerObject: urlHandler):
    """
    Defines the placeholder form for acceoting values for the fields
    
    :param fields: The fields in the query parameters
    :type fields: list | None
    :param urlHandlerObject: The object containing the definePlaceHolders method
    :type urlHandlerObject: urlHandler
    """

    st.header("Placeholder values")
    if isinstance(fields, list):
        placeHolderValues = [
            st.text_input(
                f"Value for '{field}' field",
                key=f"value_{key}")
            for key, field in enumerate(fields, start=1)
        ]
        urlHandlerObject.definePlaceholderValues(placeHolderValues=placeHolderValues)
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
            
            placeHolderNames = fillPlaceholders(fields=urlHandlerObj.fields, urlHandlerObject=urlHandlerObj)
            
            if all(placeHolderNames):
                if testFilledURL:
                    fillPlaceholderValues(fields=placeHolderNames, urlHandlerObject=urlHandlerObj)

            if urlHandlerObj.placeHolderUrl:
                st.code(urlHandlerObj.placeHolderUrl, language=None)
            
            if urlHandlerObj.filledUrl:
                st.write(urlHandlerObj.filledUrl)

    elif isinstance(ReturnValue, str):
        st.info(ReturnValue)