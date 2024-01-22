#!/usr/bin/python3
import sys
import re

def line_elements(line: str) -> bool:
    parts = line.split()
    if len(parts) != 9:
        return False
    
    line_info = {
        "file_size": 0,
        "status_code": 0,
        "line_validtion": False
    }

    # Validate IP address
    ip_address = parts[0]
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if not re.match(ip_pattern, ip_address):
        return line_info
    
    # Validate dash
    dash = parts[1]
    if dash != "-":
        return line_info
    
    # Validate date
    date = "".join(parts[2:4])
    date_pattern = r"\[\d{4}-\d{2}-\d{4}:\d{2}:\d{2}.\d{6}\]"
    if not re.match(date_pattern, date):
        return line_info
    
    # Validate request
    request = " ".join(parts[4:7])
    request_pattern = r"\"GET\W\/projects\/260\WHTTP\/1.1\""
    if not re.match(request_pattern, request):
        return line_info
    
    # Validate status code and file size
    status_code = parts[7]
    file_size = parts[8]
    if not status_code.isdigit() or not file_size.isdigit():
        return line_info
    
    line_info["status_code"] = status_code
    line_info["file_size"] = file_size
    line_info["line_validtion"] = True

    return line_info

def print_result(total_size, status_count):
    print(f"File size: {total_size}")
    for status_code in sorted(status_count):
        print(f"{status_code}: {status_count[status_code]}")


try:
    line_count = 0
    total_size = 0
    status_count = {}

    while True:
        line = sys.stdin.readline()
        
        if not line:
            break

        line_values = line_elements(line)
        
        if not line_values["line_validtion"]:
            continue
        line_count += 1
        total_size += int(line_values["file_size"])
        
        if line_values["status_code"] in status_count:
            status_count[line_values["status_code"]] += 1
        else:
            status_count[line_values["status_code"]] = 1
        
        if line_count % 10 == 0:
            print_result(total_size, status_count)

except KeyboardInterrupt:
    print_result(total_size, status_count)

