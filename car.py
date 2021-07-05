#!/usr/bin/python3

import cgi
import subprocess
import json

print("context-type:text/html")
print()

print('''<style>
body{
       background-image: url('https://www.autoguide.com/blog/wp-content/uploads/2021/06/2022-Hyundai-Elantra-N-Teasers-02.jpg');
       background-repeat: no-repeat;
       background-attachment: fixed;
       background-size: cover;
}

#d1{
    height: 90%;
    width: 40%;
    font-size: 14px;
    font-weight: bold;
    background-color: #ffffff10;
    background-size: cover;
    border-radius: 10px;
    margin-top: 5%;
    margin-left: 10%;
    border-width: 2px;
    overflow : auto;
    overflow-y: auto;
    color:rgb(5, 5, 5);
}

</style>''')
f = cgi.FieldStorage()
cmd = f.getvalue("x")
#out = subprocess.getoutput(cmd)
cm1 = json.dumps(cmd, indent = 1)
if cmd != '':
    print("<body>")
    print(f'''<div id='d1' align='center'>
            <h1  style="color: rgb(243, 23, 23);"><b>Details of car</b></h1>
           <p>{cm1}</p>
        </div>
    ''')
    print("</body>")
