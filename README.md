# CLI-and-Automationg

This is a command-line AI assistant using **Amazon Bedrock (Claude v2)** via the AWS CLI and Python.

## Requirements

- Python 3.8+
- AWS CLI configured (`aws configure`)
- Region: `us-east-1`
- IAM permissions: `bedrock:InvokeModel`

## How to Run

1. Install dependencies:
```bash
pip install boto3 typer rich
```

2. Make sure AWS ClI is configured
```bash
aws configure
```

3. Run the CLI:
```bash
python bedrock_cli.py ask "What is cloud computing?"
```
