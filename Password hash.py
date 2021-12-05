import werkzeug

pwd="ُShahroozSafari"
pwd_hash=werkzeug.security.generate_password_hash(pwd)
check_password=werkzeug.security.check_password_hash(pwd_hash,pwd)

print(pwd_hash , '\n' ,check_password)
