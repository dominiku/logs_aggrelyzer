# Log Analyzer

A Python tool for parsing and aggregating multi-format log files.

## Why I Built This

Learning exercise to master:
- Regular expressions for pattern matching
- Generators for memory-efficient file processing  
- Decorators for reusable error handling
- Multi-format data parsing

## Features

- Parses 3 log formats (web server, database, JSON API)
- Memory-efficient processing using generators
- Error aggregation and statistics
- Clean terminal output

## What I Learned

- Regex pattern matching and capture groups
- Python decorators for cross-cutting concerns
- Generator functions with `yield`
- Structured error handling

## Usage
```bash
python analyze_logs.py
```

## Project Structure
```
log-analyzer/
├── log_parser.py      # Parsing engine
├── analyze_logs.py    # Orchestrator
└── logs/              # Sample log files
```

## Next Steps

Built as part of my transition into AI Safety Engineering. 
Next: Applying these patterns to LLM output analysis.