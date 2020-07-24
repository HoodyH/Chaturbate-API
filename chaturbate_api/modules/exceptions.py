

class NoResults(Exception):
    def __init__(self, url, query):
        """
        :param url:
        :param query:
        """
        self.url = url
        self.query = query

    def __str__(self):
        return self.url, self.query
