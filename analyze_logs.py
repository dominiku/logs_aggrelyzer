from log_parser import parse_log_line
from pathlib import Path

def read_logs(directory: str):
    try:
        for filepath in Path(directory).glob("*.log"):
            with open(filepath) as f:
                yield from f

    except FileNotFoundError:
        print(f"Error: file not found in {filepath}")

logs_dir = "logs"

def main():
    print("🚀 Starting log analysis")
    file_count = sum(1 for p in Path(logs_dir).rglob('*.log') if p.is_file())
    print(f"📁 Log files found: {file_count}\n")
    print("Parsing logs...")

    counters = {
        'api_json_count': 0,
        'api_json_errors': 0,
        'database_count': 0,
        'database_errors': 0,
        'web_server_count': 0,
        'web_server_errors': 0
    }

    for line in read_logs(logs_dir):
        log_line = parse_log_line(line)

        if log_line["log_type"] == "web_server":
            counters['web_server_count'] += 1
            if log_line["line_data"]["log_level"] == "ERROR":
                counters["web_server_errors"] += 1
            # print(log_line["line_data"])
        if log_line["log_type"] == "api_json":
            counters['api_json_count'] += 1
            if log_line["line_data"]["status"] == 500:
                counters["api_json_errors"] += 1
            # print(log_line["line_data"])
        if log_line["log_type"] == "database":
            if log_line["line_data"]["log_level"] == "ERROR":
                counters["database_errors"] += 1
            counters['database_count'] += 1
            # print(log_line["line_data"])

    print(f"✓ web_server.log ({counters["web_server_count"]} entries, {counters["web_server_errors"]} errors)")
    print(f"✓ database.log ({counters["database_count"]} entries, {counters["database_errors"]} errors)")
    print(f"✓ api_json.log ({counters["api_json_count"]} entries, {counters["api_json_errors"]} errors)")


if __name__ == "__main__":
    main()

