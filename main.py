from urllib.parse import urlparse, urlunparse, urlencode, quote, unquote

class urlHandler():
    def __init__(self, url):
        self.url = url
    
    @property
    def fields(self):
        # Parsing a URL
        parsed_url = urlparse(url)
        query = parsed_url.query
        encodedQuery = unquote(query)
        QueryParts = encodedQuery.split("&")
        fields = [part.split("=")[0] for part in QueryParts]
        return fields
    
    def __str__(self):
        return f"URL : {self.url}\n" + "Fields : "+ ", ".join(self.fields)

if __name__ == "__main__":
    url = "https://www.example.com/path/to/resource?name=John%20Doe&age=30#section1"
    Obj = urlHandler(url)
    print(Obj)
    print(Obj.fields)