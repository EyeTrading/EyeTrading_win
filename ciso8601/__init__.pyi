from datetime import datetime

def parse_datetime(datetime_string: str) -> datetime: ...
def parse_rfc3339(datetime_string: str) -> datetime: ...
def parse_datetime_as_naive(datetime_string: str) -> datetime: ...
