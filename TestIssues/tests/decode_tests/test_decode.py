from src.morse import decode
import pytest


@pytest.mark.parametrize(
    "morse_message, decoded_message",
    [
        ('.- ...- .. - ---', 'AVITO'),
        ('.- -. .- .-.. -.-- - .. -.-. ...', 'ANALYTICS'),
        ('.- -.-. .- -.. . -- -.--', 'ACADEMY'),
        ('.--. -.-- - .... --- -.', 'PYTHON')
    ]
)
def test_decode_with_pytest_param(morse_message, decoded_message):
    assert decode(morse_message) == decoded_message
