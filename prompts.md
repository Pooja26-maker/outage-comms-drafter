# Prompts Used in Development

## 1. Severity Detection Prompt
Used to auto-detect severity from technical text.
Input: technical description
Output: low / medium / high

## 2. Message Generation Prompt
Used to generate customer-facing messages.
Variables: technical_text, tone, severity, stage

## 3. Quality Check Prompt
Used in agent loop to verify tone matches.
Input: message + expected tone
Output: YES / NO

## Best Prompts
- Being specific about tone definitions helped a lot
- Telling AI to reply with only the message avoided extra text
- Quality check loop improved tone accuracy significantly
