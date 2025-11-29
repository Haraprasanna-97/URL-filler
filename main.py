import streamlit as st

from urlHandler import urlHandler

def createBasicPageLayout(title: str) -> tuple:
    """
    Defines the basic layout of the streamlit application
    
    :param title: Defines the titke of the streamlit application
    :type title: str
    :return: A tuple containing the URL entered by the user, the sections (info and placeHolder) and a flag for showing or hiding the filled URL
    :rtype: tuple
    """

    st.title(title)
    url = st.text_input("Enter the url", key="urlInput")
    infoSec, placeHolderSec = st.columns([1, 3])
    showFilledURL = st.checkbox("Show filled URL")
    return url, infoSec, placeHolderSec, showFilledURL

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

def fillPlaceHolders(fields: list | None, urlHandlerObject: urlHandler):
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
        urlHandlerObject.definePlaceHolders(placeHolderNames=placeHolderNames)
    else:
        st.write("Their are no Query paramitters in the given URL")

if __name__ == "__main__":
    url, infoSec, placeHolderSec, showFilledURL = createBasicPageLayout(title="URL filler")
    urlHandlerObj = urlHandler(url)
    if url:
        with infoSec:
            fillInfoSection(urlHandlerObject=urlHandlerObj)
        
        with placeHolderSec:
            fillPlaceHolders(fields=urlHandlerObj.fields, urlHandlerObject=urlHandlerObj)
    
        if showFilledURL:
            st.code(urlHandlerObj.placeHolderUrl, language=None)