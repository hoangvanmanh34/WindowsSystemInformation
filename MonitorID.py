import subprocess

#Hoang Van Manh
#Danny TE-NPI
#hoangvanmanhpc@gmail.com
#https://www.youtube.com/c/StevenHCode
#https://github.com/hoangvanmanh34

#gwmi WmiMonitorID -Namespace root\wmi | ForEach-Object {($_.UserFriendlyName | foreach {[char]$_}) -join ""; ($_.SerialNumberID | foreach {[char]$_}) -join ""}
cmd = 'gwmi WmiMonitorID -Namespace root\wmi | ForEach-Object {($_.SerialNumberID | foreach {[char]$_}) -join ""}'

process = subprocess.run(['powershell.exe', cmd], stdout=subprocess.PIPE, shell=True)

mylist = str(process.stdout, 'utf-8').replace('\x00', '').replace('\r\n', '')

print(mylist)
