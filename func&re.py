import re

# Function email_check
def email_check(email):
    pattern = r'^(?=^((?!-).)*$)(?=[^0-9])((?=^((?!\.\d).)*$)|(?=.*_))'
	# Update pattern here
    if re.match(pattern, email):
        return "Pass"
    else:
        return "Not Pass"

# Masukkan data email ke dalam list
emails = ['my-name@someemail.com', 'myname@someemail.com', 'my.name@someemail.com', 'my.name2019@someemail.com',
          'my.name.2019@someemail.com', 'somename.201903@someemail.com', 'my_name.201903@someemail.com',
          '201903myname@someemail.com', '201903.myname@someemail.com']

# Looping untuk pengecekan Pass atau Not Pass, gunakan variabel email untuk mengiterasi emails
for email in emails:
  result = email_check(email)
  print("Email: {}, Result: {}".format(email, result))