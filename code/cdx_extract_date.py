from __future__ import print_function
import fileinput
from datetime import datetime


for line in fileinput.input():
    line = line.rstrip()

    # This condition removes CDX header lines
    if line[0] is ' ':
        continue

    # Extract just the timestamp from line
    timestamp = line.split(' ', 2)[1]

    # Datetiem format in CDX is  20121125005312
    date_object = datetime.strptime(timestamp, '%Y%m%d%H%M%S')

    # print(date_object.strftime('%Y-%m-%d'))
    print(date_object.strftime('%Y-%m-%d %H:%M:%S'))
