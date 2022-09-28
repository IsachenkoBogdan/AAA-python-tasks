from src.morse import encode


def test_encode_with_doctest():
    """
    >>> encode('HELLO')
    '.... . .-.. .-.. ---'
    >>> encode('I LOVE YOU') #doctest: +NORMALIZE_WHITESPACE
    '..   .-.. --- ...- .   -.-- --- ..-'
    >>> encode('SOS')
    '... --- ...'
    >>> encode('A LOT OF PY CODE A LOT OF PY CODE A LOT OF PY CODE') #doctest: +ELLIPSIS
    '.-   .-.. --- - ...'
    >>> encode()
    Traceback (most recent call last):
        ...
    TypeError: encode() missing 1 required positional argument: 'message'
    >>> encode('hello')
    Traceback (most recent call last):
        ...
    KeyError: 'h'
    >>> encode(1337)
    Traceback (most recent call last):
    TypeError: 'int' object is not iterable
    """
