Collecting workspace information```markdown
# Log Extractor for Windows

This project provides Python scripts to extract and process log data from various log files. The scripts are designed to parse specific patterns in the logs and generate structured output files.

## Features

- **`printuser.py`**: Extracts user, client, and printer information from log files.
- **`applocker.py`**: Extracts user, client, policy name, and file path information from AppLocker logs.
- Outputs are saved in a structured format in the `output` directory.

## Prerequisites

- Python 3.x
- Required permissions to read the log files.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Zer0-AT/logextractor-windows.git
   ```
2. Navigate to the project directory:
   ```bash
   cd logextractor-windows
   ```

## Usage

### `printuser.py`

1. Place the log file (e.g., `avex_250417.log`) in the project directory.
2. Run the script:
   ```bash
   python printuser.py
   ```
3. The output will be saved in the `output` directory with a timestamped filename.

### `applocker.py`

1. Place the AppLocker log file (e.g., `wcex_250429.log`) in the project directory.
2. Run the script:
   ```bash
   python applocker.py
   ```
3. The output will be saved in the `output` directory with a timestamped filename.

## Output Format

### `printuser.py`

The output file contains the following columns:
- `User`: The user who owns the resource.
- `Client`: The client machine.
- `Printer`: The printer used.

### `applocker.py`

The output file contains the following columns:
- `User`: The user associated with the policy.
- `Client`: The client machine.
- `PolicyName`: The name of the policy.
- `Path\Software`: The file path or software associated with the policy.

## Directory Structure

```
.
├── applocker.py
├── printuser.py
├── output/
│   ├── output-<script>-<timestamp>.txt
├── README.MD
├── .gitignore
└── log files (e.g., avex_250417.log, wcex_250429.log)
```

## Contributing

Contributions are welcome! Please ensure your code adheres to the existing style and includes appropriate comments.

## License

This project is licensed under the MIT License.
```