def detect_log_format(line: str) -> str:
    """Detect if line is web_server, database, api_call, or unknown format."""

def parse_web_server_log(line: str) -> dict:
    """Parse web server format, return structured dict."""

def parse_database_log(line: str) -> dict:
    """Parse database format, return structured dict."""

def parse_api_log(line: str) -> dict:
    """Parse JSON API log format."""

def parse_log_line(line: str) -> dict:
    """Universal parser - detects format and calls appropriate parser."""

def categorize_severity(log_entry: dict) -> str:
    """Return 'error', 'warning', 'info' based on entry."""
