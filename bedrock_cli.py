import boto3
import typer
import json
from rich import print

app = typer.Typer()

# ✅ Initialize Bedrock client
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")


# ✅ Exposed for testing
def call_claude(prompt: str) -> str:
    request_body = {
        "prompt": f"Human: {prompt}\nAssistant:",
        "max_tokens_to_sample": 300
    }

    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2",
        contentType="application/json",
        accept="application/json",
        body=bytes(json.dumps(request_body), "utf-8")
    )

    # 🔽 Clean response
    raw = response['body'].read().decode("utf-8")
    data = json.loads(raw)
    return data.get("completion", "[No response from Claude]")


@app.command()
def ask(prompt: str):
    """
    Ask Claude a question using Amazon Bedrock.
    """
    print("[bold cyan]🧠 Claude's Response:[/bold cyan]")
    try:
        response = call_claude(prompt)
        print(response)
    except Exception as e:
        print(f"[red]❌ Error:[/red] {e}")


@app.command()
def help():
    """
    Show help on how to use the CLI.
    """
    print("[bold yellow]Usage:[/bold yellow]")
    print("  python bedrock_cli.py ask 'your question here'")


if __name__ == "__main__":
    app()
