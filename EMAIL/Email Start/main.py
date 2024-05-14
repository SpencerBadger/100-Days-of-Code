# import smtplib


# my_email = ""
# password = ""


# with smtplib.SMTP("", port=587) as connection:
#         connection.starttls()
#         connection.login(user = my_email, password = password)
#         connection.sendmail(
#                             from_addr = my_email, 
#                             to_addrs = "", 
#                             msg = "Subject:Hello\n\nThis was sent from code I am typing"
#                             )

import datetime as dt

now = dt.datetime.now()
year = now.year
if year == 2024:
    print(f"It's {year}")

print(year)