from http.cookiejar import join_header_words

time = int(input("Please enter the time from 0 to 8640000: "))

day = time // 86400
hours = (time - day*86400) // 3600
minutes = ((time - day*86400 - hours*3600)) // 60
seconds = ((time - day*86400 - hours*3600)) - minutes * 60

print(str(day).zfill(2),"днів,",str(hours).zfill(2),":",str(minutes).zfill(2), ":", str(seconds).zfill(2))
