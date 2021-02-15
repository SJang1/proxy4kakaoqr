#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import requests
import cgi

# Set URL
kakaoqrURL = "http://localhost:3000/"

print("Content-Type: text/html;charset=utf-8")
print()
print("<title>Kakao-QR-Docker Demo site</title>")
print('<meta name="viewport" content="width=device-width, user-scalable=no" />')

form = cgi.FieldStorage() #need something that works like cgi.FieldStorge to TEST IT.
if "email" in form:
    email = form["email"].value
else:
    email = ""
if "password" in form:
    password = form["password"].value
else:
    password = ""



data = {"email": email, "password": password, "secretKey": "secret"}
res = requests.post(kakaoqrURL, data)
res.status_code
res.text

if "02|" not in res.text: 
    print(res.text)
else:
    # print('<script type="text/javascript" src="qrcode.js"></script>')
    # QRcode.js does not work (over limit of size)
    print('''
    <script type="text/javascript" src="jquery.min.js"></script>
            
            <script type="text/javascript">
            window.onload = function generateBarCode()
            {
                var nric = $('#text').val();
                var url = 'https://api.qrserver.com/v1/create-qr-code/?data=''' + res.text + '''&amp;size=427x427';
                $('#barcode').attr('src', url);
            }
        </script>
        <script>setTimeout(function(){location.reload();},16000);</script>
    ''')
    print('''
    <style>

    @media screen and (orientation:portrait) {
    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
    } 
    }
    @media screen and (orientation:landscape) {
    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        height: 95%;
        
    } 
    }  
    body {
        width: 100%;
        height: 100%;
    }
    </style>
    ''')

    print("<body><div id='barcodediv'> <img id='barcode' class='center'> </div>")
    
    print("</body>")