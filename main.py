from urllib.parse import urlparse, urlunparse, urlencode, quote, unquote, parse_qs

class urlHandler():
    def __init__(self, url: str):
        self.url = url
        self.parsed_url = urlparse(url)
        self.placeHolderUrl = None
    
    @property
    def fields(self) -> list | None:
        """
        If their are fields available in the url then return them otherwise returns None
        
        :param self: The object which is calling the function
        :return: A list of fields if present in the query paramiters of the URL otherwise returns None
        :rtype: list | None
        
        """
        query = self.parsed_url.query
        if query:
            keyValuePairs = parse_qs(query)
            return list(keyValuePairs.keys())
        return None
    
    @property
    def parts(self) -> dict:
        """
        Returns all the parts of the given URL as a dictonary. Return None for those parts which are not available
        
        :param self: The object which is calling the function
        :return: A python dictionary containing dufferent parts of the URL such as Scheme, Network location, Path, Query, Fragment
        :rtype: dict
        """
        return {
            "Scheme" : self.parsed_url.scheme,
            "Network location" : self.parsed_url.netloc,
            "Path" : self.parsed_url.path,
            "Query" : self.parsed_url.query,
            "Fragment" : self.parsed_url.fragment
        }
    
    def definePlaceHolders(self, placeHolderNames: list) -> str :
        Scheme, netloc, Path, _, Fragment = self.parts.values()
        fields = self.fields
        queryParams = [fields[i] + "={" + placeHolderNames[i] + "}" for i in range(len(fields))]
        queryParamsstr = "&".join(queryParams)
        components = (Scheme, netloc, Path, '', queryParamsstr, Fragment)
        placeHolderUrl = urlunparse(components)
        self.placeHolderUrl = placeHolderUrl
        return placeHolderUrl
    
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
        URL with placeholders : {self.placeHolderUrl}
""" # Display None if a part in the URL is not preset

if __name__ == "__main__":
    # url = "https://www.example.com/path/to/resource?name=John%20Doe&age=30#section1"
    url = "https://www.google.com/search?q={Query}"
    URL = urlHandler(url)
    URL.definePlaceHolders(["Query","Page"])
    print(URL)
    # print(URL.fields)
    # print(URL.parts)