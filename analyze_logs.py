# 1. Load all `.log` files from a directory
# 2. Parse each line using `log_parser.py`
# 3. Collect statistics:
#     - Total entries per log file
#     - Total errors/warnings/info per file
#     - Most common error messages (top 10)
#     - Time range covered (earliest to latest timestamp)
#     - Files with highest error rate
# 4. Generate report: `reports/LOG-ANALYSIS-YYYYMMDD-HHMMSS.json`
# 5. Print summary to terminals

from log_parser import detect_log_format, parse_log_line, parse_api_log, parse_database_log, parse_web_server_log
from pathlib import Path
import json

def read_logs(directory: str):
    try:
        for filepath in Path(directory).glob("*.log"):
            with open(filepath) as f:
                yield from f

    except FileNotFoundError:
        print(f"Error: file not found in {filepath}")

logs_dir = "logs"
read_dir = read_logs(logs_dir)

def main():
    print("🚀 Starting log analysis")
    file_count = sum(1 for p in Path(logs_dir).rglob('*.log') if p.is_file())
    print(f"📁 Log files found: {file_count}")

    api_json_count = 0
    database_count = 0
    web_server_count = 0

    for line in read_dir:
        log_line = parse_log_line(line)
    
        if log_line == "api_json":
            api_json_count += 1
            print(parse_api_log(line))
        elif log_line == "database":
            database_count +=1
            print(parse_database_log(line))
        else:
            web_server_count +=1
            print(parse_web_server_log(line))
            
    print(api_json_count, database_count, web_server_count)

if __name__ == "__main__":
    main()