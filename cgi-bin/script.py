import cgi
import os
import http.cookies

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
counter = cookie.get("counter")

if counter is None:
    print("Set-cookie: counter=1")
else:
    c = int(counter.value) + 1
    print(f"Set-cookie: counter={c}")

form = cgi.FieldStorage()
text1 = form.getfirst("input1", "не задано")
text2 = form.getfirst("input2", "не задано")

checkboxes=form.getlist('cb')
radio_choices=form.getlist('rb')



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Form Handling</title>
        </head>
        <body>""")


print("<h1>Form data</h1>")
print("<p>Input_1: {}</p>".format(text1))
print("<p>Input_2: {}</p>".format(text2))
print("<p>Your checkboxes: {}</p>".format(', '.join(checkboxes)))
print("<p>Your radio: {}</p>".format(', '.join(radio_choices)))
print()
print(cookie.get("counter"))
print('<h1>Cookies log:</h1>')
for key, value in os.environ.items():
    print(f'<p>key = {key} value = {value}</p>')

print("""</body>
        </html>""")