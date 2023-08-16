import smtplib
import random
import time
def auth(user_id):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('group1@apsjorhat.org', 'apsj#12345678')
    otp = random.randint(111111, 999999)
    message = str(otp)
    s.sendmail("group1@apsjorhat.org",user_id, message)
    s.quit()
    a = ("Enter the OTP: ")
    val = int(input(a))
    if val == otp:
        print("Verifing the OTP....")
        time.sleep(1)
        return 1

    elif val != otp:
        print("Incorrect OTP !!!")
        print("Sending OTP again...")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('group1@apsjorhat.org', 'apsj#12345678')
        otp = random.randint(111111, 999999)
        message = str(otp)
        s.sendmail("group1@apsjorhat.org", user_id, message)
        s.quit()
        print("Enter the OTP: ")
        val = int(input())
        if val == otp:
            print("Verifing the OTP....")
            time.sleep(1)
            print("Login Successfully !!!")
            print("*" * 46)

    elif val != otp:
        print("Incorrect OTP !!!")
        print("Sending OTP again...")
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('group1@apsjorhat.org', 'apsj#12345678')
        otp = random.randint(111111, 999999)
        message = str(otp)
        s.sendmail("group1@apsjorhat.org", user_id, message)
        s.quit()
        print("Enter the OTP: ")
        val = int(input())
        if val == otp:
            print("Verifing the OTP....")
            time.sleep(1)
            print("Login Successfully !!!")
            print("*" * 46)