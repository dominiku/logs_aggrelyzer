import re
import json

def detect_log_format(line: str) -> str:
    """Detect if line is web_server, database, api_call, or unknown format."""
    if line.startswith("{"):
        return "api_json"
    elif line.startswith("["):
        return "database"
    elif re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line):
        return "web_server"
    else:
        return "unknown"

def parse_web_server_log(line: str) -> dict:
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w+) (/\S+) (\d+) (\d+)ms"
    match = re.match(pattern, line)

    if match:
        return {
            "status": "ok",
            "timestamp": match.group(1),
            "log_level": match.group(2),
            "request_method": match.group(3),
            "endpoint": match.group(4),
            "status_code": int(match.group(5)),
            "duration_ms": int(match.group(6))
        }
    else:
        return {"status": "parse_error", "raw": line}

def parse_database_log(line: str) -> dict:
    pattern = r"^\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]\s+(ERROR|INFO|WARN)\s+(.*)$"
    match = re.match(pattern, line)

    if match:
        return {
            "timestamp": match.group(1),
            "log_level": match.group(2),
            "message": match.group(3)
        }
    else:
        return {"status": "parse_error", "raw": line}

def parse_api_log(line: str) -> dict:
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return {"status": "parse_error", "raw": line}

def parse_log_line(line: str) -> dict:
    """Universal parser - detects format and calls appropriate parser."""
    log_type = detect_log_format(line)

    if log_type == "api_json":
        log_raw_data = parse_api_log(line)
        return { "log_type": log_type, "line_data": log_raw_data }
    elif log_type == "database":
        log_raw_data = parse_database_log(line)
        return { "log_type": log_type, "line_data": log_raw_data }
    elif log_type == "web_server":
        log_raw_data = parse_web_server_log(line)
        return { "log_type": log_type, "line_data": log_raw_data }
    else:
        print("No line has been detected — IDK what would be the best message here?")
