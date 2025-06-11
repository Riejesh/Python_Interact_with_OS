'''This Python script is designed to search for specific errors within a given log file and then write any matching log entries to a new file.

Here's a more detailed breakdown of its purpose:
Error Searching: It takes a log file as input and prompts the user to enter an "error" string. It then searches for log entries that contain both the literal string "error" and all the individual words from the user-provided error string (case-insensitively).
Log File Processing: It reads the specified log file line by line to perform the search.
Output to File: If any log entries match the search criteria, they are written to a new file named errors_found.log located in a data subdirectory within the user's home directory.
'''

#!/usr/bin/env python3
import sys         #Provides access to system-specific parameters and functions
import os          #Provides a way of using operating system dependent functionality
import re          #Provides regular expression operations.


def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:         #Opens the specified log_file in read mode ('r'). encoding='UTF-8' specifies the character encoding to handle a wider range of characters.
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))    #For each word, it converts it to lowercase and appends it to the error_patterns list. The r"{}" creates a raw string, which is good practice for regular expressions (though not strictly necessary here since the words are simple). This ensures that every individual word from the user's input must also be present in the log entry.
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):  # This built-in function returns True if all the elements in the iterable are true
        returned_errors.append(log)
    file.close()
  return returned_errors


def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
      file.close()
      
if __name__ == "__main__":
  log_file = sys.argv[1]    #sys.argv is a list of command-line arguments. sys.argv[0] is the script name itself, and sys.argv[1] is the first argument provided after the script name. This line expects the user to provide the log file path as a command-line argument when running the script.
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)      #exits the script with a status code of 0, which typically indicates successful execution.
