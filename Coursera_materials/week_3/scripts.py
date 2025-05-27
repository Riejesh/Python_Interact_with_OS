"""Objective of the Code
The primary objective of this code is to update email addresses in a CSV file by replacing an old email domain with a new one. 
1. Read a list of user data, including email addresses, from a CSV file.
2. Identify email addresses that belong to a predefined old_domain (e.g., abc.edu).
3. For those identified emails, replace the old_domain with a new_domain (e.g., xyz.edu).
4. Write the entire updated user data (including the modified email addresses) to a new CSV file.

re.match(pattern, string): This function attempts to match the pattern only at the beginning of the string.
re.search(pattern, string): This function scans through the entire string to find the first location where the pattern produces a match. 

domain = r'[\w\.-]+@'+domain+'$' in contains_domain:

r'...': This denotes a "raw string" in Python. It means that backslashes (\) are treated as literal characters and not as escape sequences. This is crucial for regular expressions to avoid conflicts with Python's own string escape sequences (e.g., \n for newline).
[\w\.-]+: This is a character set definition:
[ and ]: Define a character set. Any single character within this set will match.
\w: Matches any "word" character. This includes alphanumeric characters (a-z, A-Z, 0-9) and the underscore (_). It's equivalent to [a-zA-Z0-9_].
\.: Matches a literal dot (.). The dot has special meaning in regex (matches any character except newline), so it must be escaped with a backslash to match a literal dot.
-: Matches a literal hyphen (-). Inside a character set, if it's not defining a range (like a-z), it matches itself.
+: This is a quantifier meaning "one or more" of the preceding character or group. So, [\w\.-]+ means "match one or more word characters, literal dots, or hyphens." This part typically matches the username/local part of the email address (e.g., john.doe, my-email).

"""

#!/usr/bin/env python3

import re  #The re module provides regular expression operations. Regular expressions (regex) are powerful patterns used to match character combinations in strings. They are extremely useful for pattern matching, searching, and replacing text based on complex rules.
import csv


def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain = r'[\w\.-]+@'+domain+'$'
  if re.match(domain,address):  #Attempts to match a pattern only at the beginning of the string
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address) #re.sub(pattern, replacement, string): Replaces occurrences of a pattern in a string with a specified replacement.
  return address

def main():
  """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = '/home/student-00-9857f50afeb0/data/user_emails.csv'
  report_file = '/home/student-00-9857f50afeb0/data' + '/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))  # [CSV reader]  Reads a CSV file row by row, returning each row as a list of strings.
    user_email_list = [data[1].strip() for data in user_data_list[1:]]

    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)

    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()

  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)  
    writer.writerows(user_data_list)  #Writes multiple rows (provided as a list of lists) to the CSV file.
    output_file.close()

main()

