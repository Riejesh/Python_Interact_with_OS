#!/usr/bin/env python3
from network import *
import shutil    #High level operations on files.
import psutil    #Process & System Utilities module. 
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100    #Logic to calculate didsk usage
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)     #This gets the current CPU utilization as a percentage. The 1 argument means it will block for 1 second to calculate the percentage over that period.  
    return usage < 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Network checks failed")

