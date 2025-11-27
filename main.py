from urllib.parse import urlparse, urlunparse, urlencode, quote, unquote, parse_qs

class urlHandler():
    def __init__(self, url):
        self.url = url
        self.parsed_url = urlparse(url) 
    
    @property
    def fields(self):
        """If their are fields available in the url then return them otherwise returns None"""
        query = self.parsed_url.query
        if query:
            keyValuePairs = parse_qs(query)
            return list(keyValuePairs.keys())
        return None
    
    @property
    def parts(self):
        """Returns all the parts of the given URL as a dictonary. Return None for those parts which are not available"""
        return {
            "Scheme" : self.parsed_url.scheme,
            "Network location" : self.parsed_url.netloc,
            "Path" : self.parsed_url.path or None,
            "Query" : self.parsed_url.query or None,
            "Fragment" : self.parsed_url.fragment or None
        }
    
    def __str__(self):
        return f"""
        URL : {self.url}
        Fields : {", ".join(self.fields) or None}
        Parts :
            Scheme: {self.parsed_url.scheme}
            Netloc: {self.parsed_url.netloc}
            Path: {self.parsed_url.path or None}
            Query: {self.parsed_url.query or None}
            Fragment: {self.parsed_url.fragment or None} 
""" # Display None if a part in the URL is not preset

if __name__ == "__main__":
    url = "https://www.example.com/path/to/resource?name=John%20Doe&age=30#section1"
    URL = urlHandler(url)
    # print(URL)
    print(URL.fields)
    # print(URL.parts)