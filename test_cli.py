# test_cli.py

from bedrock_cli import call_claude

def test_claude_response_not_empty():
    response = call_claude("What is serverless computing?")
    assert isinstance(response, str)
    assert len(response.strip()) > 0
