#!/usr/bin/env python3
# Server Monitor v2 (Python)

import socket
import shutil
import datetime
import yaml


def load_config(path="config.yaml"):
    with open(path) as f:
       return yaml.safe_load(f)


def get_memory_percent():
    info = {}
    with open("/proc/meminfo") as f:
        for line in f:
            key, value = line.split(":")
            info[key] = int(value.split()[0])
    used = info["MemTotal"] - info["MemAvailable"]
    return round(used / info["MemTotal"] * 100, 1)


def main():
    config = load_config()
    
    print("==== Server Status (Python) ====")
    print(f"Hostname : {socket.gethostname()}")
    print(f"Time     : {datetime.datetime.now():%Y-%m-%d %H:%M:%S}")

    disk = shutil.disk_usage(config["disk"]["path"])
    disk_percent = round(disk.used / disk.total * 100, 1)
    print(f"Disk     : {disk_percent}%")

    mem_percent = get_memory_percent()
    print(f"Memory   : {mem_percent}%")


    print("----- Check -----")
    if disk_percent >= config["disk"]["warning_percent"]:
       print(f"[WARNING] Disk usage {disk_percent}%")
    else:
       print(f"[OK] Disk usage {disk_percent}%")
    if mem_percent >= config["memory"]["warning_percent"]:
       print(f"[WARNING] Memory usage {mem_percent}%")
    else:
       print(f"[OK] Memory usage {mem_percent}%")
if __name__ == "__main__":
    main()
