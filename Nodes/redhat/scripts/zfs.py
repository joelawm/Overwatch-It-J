'''
Script: ZFS

Script created by: Joe Meyer

Fucntion: This script will monitor your ZFS System and alert you by notification and email, if a system has lost functions.
'''
import subprocess

p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print "Today is", output
