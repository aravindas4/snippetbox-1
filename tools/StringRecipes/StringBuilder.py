from io import StringIO


class StringBuilder:

    def __init__(self):
        self._string = StringIO()

    def append(self, value):
        self._string.write(value)

    def __str__(self):
        return self._string.getvalue()


