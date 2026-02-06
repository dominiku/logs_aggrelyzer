def error_handler(func):
    def wrapper(filepath, *args, **kwargs):
        try:
            return func(filepath, *args, **kwargs)
        except FileNotFoundError:
            return {"status": "error", "error": "file_not_found", "filepath": filepath}
        except PermissionError:
            return {"status": "error", "error": "permission_error", "filepath": filepath}
    return wrapper


web_server_log = {}


@error_handler
def detect_log_format(line: str) -> str:
    """Detect if line is web_server, database, api_call, or unknown format."""
    if line.startswith("{"):
        return "api_json"
    elif line.startswith("["):
        return "database"
    elif line.endswith("ms"):
        return "web_server"
    else:
        return "unknown"

@error_handler
def parse_web_server_log(line: str) -> dict:
    """Parse web server format, return structured dict."""
    line = line.strip('{}')
    value = line.split(' ')
    key = ["timestamp", "also part of time stamp although without regexp I can't tokenize :)", "log_level", "request_method", "endpoint", "status_code", "duration"]
    web_server_log = {key: value for key, value in zip(key, value)}
    return web_server_log


# 2026-01-26 10:23:49 WARN GET /api/slow 200 5023ms

"""
Now write the next function: parse_web_server_log().
Use the same approach:

Simple string methods
.split() to break the line into parts
Extract what you need
Return a dict
"""




@error_handler
def parse_database_log(line: str) -> dict:
    """Parse database format, return structured dict."""

@error_handler
def parse_api_log(line: str) -> dict:
    """Parse JSON API log format."""

@error_handler
def parse_log_line(line: str) -> dict:
    """Universal parser - detects format and calls appropriate parser."""

@error_handler
def categorize_severity(log_entry: dict) -> str:
    """Return 'error', 'warning', 'info' based on entry."""

test_line = '2026-01-26 10:23:45 INFO GET /api/users 200 45ms'
print(detect_log_format(test_line))
print(parse_web_server_log(test_line))




"""
{"timestamp": "2026-01-26T10:23:47Z", "endpoint": "/login", "status": 200, "duration_ms": 45}
{"timestamp": "2026-01-26T10:23:48Z", "endpoint": "/checkout", "status": 500, "duration_ms": 1203}
{"timestamp": "2026-01-26T10:23:49Z", "endpoint": "/profile", "status": 200, "duration_ms": 23}

[2026-01-26 10:23:46] ERROR Connection timeout host=db1
[2026-01-26 10:23:47] INFO Query executed in 45ms
[2026-01-26 10:23:48] ERROR Deadlock detected table=orders
[2026-01-26 10:23:49] WARN Slow query detected 2.3s

2026-01-26 10:23:45 INFO GET /api/users 200 45ms
2026-01-26 10:23:46 ERROR POST /api/login 500 1203ms
2026-01-26 10:23:47 INFO GET /api/products 200 23ms
2026-01-26 10:23:48 ERROR GET /api/orders 404 12ms


"""