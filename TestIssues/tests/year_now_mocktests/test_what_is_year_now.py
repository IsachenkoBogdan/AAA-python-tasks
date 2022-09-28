from what_is_year_now import what_is_year_now
import json
import pytest
from unittest.mock import MagicMock


@pytest.mark.parametrize(
    "date_str, year",
    [
        ('2004-06-01', 2004),
        ('29.09.2022', 2022)
    ]
)
def test_year_now(date_str, year):
    json.load = MagicMock(return_value={"currentDateTime": date_str})
    assert what_is_year_now() == year


def test_raises_error():
    json.load = MagicMock(return_value={"currentDateTime": "oops%3error"})
    with pytest.raises(ValueError):
        what_is_year_now()
