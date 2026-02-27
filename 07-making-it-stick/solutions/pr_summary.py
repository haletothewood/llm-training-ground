#!/usr/bin/env python3
"""Generate a PR summary from a git diff."""

import sys
import anthropic


def main():
    diff = sys.stdin.read()
    if not diff.strip():
        print("No diff provided. Usage: git diff | python pr_summary.py")
        sys.exit(1)

    MAX_CHARS = 100_000  # ~25k tokens; avoids hitting API context limits
    if len(diff) > MAX_CHARS:
        print(f"Warning: diff is {len(diff):,} chars — truncating to {MAX_CHARS:,}",
              file=sys.stderr)
        diff = diff[:MAX_CHARS]

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"""Summarise this git diff as a pull request description.

Format:
## Summary
(2-3 bullet points: what changed and why)

## Files changed
(list each file with a one-line description of the change)

Diff:
{diff}"""
            }]
        )
    except anthropic.AuthenticationError:
        print("Error: ANTHROPIC_API_KEY is not set or is invalid.", file=sys.stderr)
        sys.exit(1)
    except anthropic.APIError as e:
        print(f"API error: {e}", file=sys.stderr)
        sys.exit(1)

    print(message.content[0].text)


if __name__ == "__main__":
    main()
