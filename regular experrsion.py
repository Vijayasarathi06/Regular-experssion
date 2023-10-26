import re
##Task 1
aadhar_number="^\d{4}\D\d{4}\D\d{4}$"
original=input("enter the my original number")
a=re.match(aadhar_number,original)
if a:
    print("Yes,ther is at least one match")
else:
    print("no match")

##Task 2
import re
pan_number="^[a-zA-Z]{5}\d{5}[a-zA-Z]{1}$"
original=input("enter the my original number")
a=re.match(pan_number,original)
if a:
    print("Yes,ther is at least one match")
else:
    print("no match")


import re
Email_id="^[\w]+@gmail.com$"
original=input("enter the my original number")
a=re.match(Email_id,original)
if a:
    print("Yes,ther is at least one match")
else:
    print("no match")









          
