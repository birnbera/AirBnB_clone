#!/usr/bin/python3
from datetime import datetime
from unittest import mock

with mock.patch.object(test.datetime, 'now', return_value="woo") as mockdt:
    a = datetime.now()
print(a)
