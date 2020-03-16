#!/usr/bin/env python3

import re
import operator
import csv


error = {}
info = {}

with open("syslog.log", "r") as logs:
    for log in logs:
        parser = r"ticky: ([\w]*) ([\w ']*\w|[\w '\[#]*\]) \(([\w\.]*)\)"
        data = re.search(parser, log)
        if data!=None:
          status = data.group(1)
          msg = data.group(2)
          user = data.group(3)
          if not user in info:
              info[user] = {"info": 0, "error": 0}
          if status == "ERROR":
              if not msg in error:
                  error[msg] = 0
              error[msg] += 1
          info[user][status.lower()] += 1
    logs.close()

error_sorted = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
info_sorted = sorted(info.items(), key=operator.itemgetter(0))

with open('error_message.csv', 'w') as file:
    fieldnames = ["Error", "Count"]
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    for err in error_sorted:
        writer.writerow({'Error': err[0], 'Count': err[1]})
    file.close()

with open('user_statistics.csv', 'w') as file:
    fieldnames = ["Username", "INFO", "ERROR"]
    writer = csv.DictWriter(file, fieldnames = fieldnames)
    writer.writeheader()
    for name in info_sorted:
        writer.writerow({'Username': name[0], 'INFO': name[1]['info'], 'ERROR': name[1]['error']})
    file.close()



