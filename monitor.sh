#!/bin/bash
# Server Monitor v1

echo "===== Server Status ====="
echo "Hostname : $(hostname)"
echo "IP       : $(hostname -I)"
echo "Time     : $(date '+%Y-%m-%d %H:%M:%S')"
echo "Uptime   : $(uptime -p)"
echo
echo "----- Disk -----"
df -h /
echo
echo "----- Memory -----"
free -h

echo
echo "----- CPU -----"
top -bn1 | grep "Cpu(s)"
echo
echo "----- Logged-in Users -----"
who
