#!/usr/bin/python
#################################################################################
# To use this script, copy this script to the folder                            #
# configured for storing your cgi scripts and then using                        #
# your web browser access the URL                                               #
#                                                                               #    
# 127.0.0.1/scripts/FileManager.py?filename="Path of folder you want to access" #
#################################################################################

print ("Content-Type: text/html\n\n")
print ("<!DOCTYPE html>")

import os
import cgi,cgitb

cgitb.enable()
path = cgi.FormContent()["filename"][0]
if path[len(path)-1]!='/':
    path=path+'/'
listDir = os.listdir(path)

print '''<html>
    <head>
        <title>File Manager</title>
            <script type="text/javascript">
                function fileClicked(clickedId)
                {
                window.location.assign("FileManager.py?filename="+clickedId)
                /*
                    var xhttp = new XMLHttpRequest();
                    xhttp.onreadystatechange = fucntion() {
                        if(this.readyState == 4 && this.status == 200)
                        {
                            document.getElementById("demo").innerHTML = this.responeText;
                        }
                    };
                    xhttp.open("POST","/scripts/FileManager.py",true);
                    xhttp.send("filename="+clickedId);
                    */
                }
                function dirClicked(clickedId)
                {
                    window.location.assign("FileManager.py?filename="+clickedId)
                /*
                    var xhttp = new XMLHttpRequest();
                    xhttp.onreadystatechange = fucntion() {
                        if(this.readyState == 4 && this.status == 200)
                        {
                            document.getElementById("p1").innerHTML = this.responeText;
                        }
                    };
                    xhttp.open("GET","FileManager.py?filename="+clickedId,true);
                    xhttp.send();
                    alert(clickedId);
                */
                }
            </script>
            <style>
                .Button
                {
                        border: none;
                        color: white;
                        padding: 15px 32px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin: 4px 2px;
                        cursor: pointer;
                }
                .fileButton
                {
                    background-color: #008CBA; /*Blue*/
                }
                .dirButton
                {
                    background-color: #f44336; /*Red*/
                }
            </style>
    </head>
<body>
    <div id="div1">
'''

dirName=""
fileName=""
for x in listDir:
    filePath = path+x
    if os.path.isfile(filePath):
        fileName=fileName+(("<button id='%s' onclick='fileClicked(this.id)' class = 'Button fileButton'>File : %s </button><br>")%(filePath,x))
    elif os.path.isdir(filePath):
        dirName=dirName+(("<button id='%s' onclick='dirClicked(this.id)' class = 'Button dirButton'>Dir : %s </button><br>")%(filePath,x))

print dirName+"<br><br>"
print fileName
print '''
        </div>
        <p id="p1"></p>
    </body>
</html>
'''
