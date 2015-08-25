import datetime


class Query(object):

    def __init__(self, content):
        self.content = content.split()
        self.timestamp = datetime.datetime.now()

    def __iter__(self):
        return iter(self.content)

    def __str__(self):
        return str(self.content)


class QueryStream(object):

    def __init__(self):
        self.queries = []

    def add_query(self, query):
        new_query = Query(query)
        self.queries.append(new_query)

    def __iter__(self):
        return iter(self.queries)

    def print_queries(self):
        start = datetime.datetime.now()
        for query in stream:
            print('<NEW QUERY>')
            for word in query:
                print word
            stop = datetime.datetime.now()
            print('Query iter time: {0}'.format(stop - start))
            start = stop


data1 = 'some data is here'
data2 = 'this is another query'
data3 = 'and there goes another one'

stream = QueryStream()
stream.add_query(data1)
stream.add_query(data2)
stream.add_query(data3)

stream.print_queries()
