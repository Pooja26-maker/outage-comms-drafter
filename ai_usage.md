# AI Usage Note

## What AI Helped With
- Writing 70% of boilerplate code (Streamlit UI, agent loop)
- Debugging errors quickly (quota errors, import errors)
- Writing prompt templates for tone-controlled generation
- Suggesting MCP tool structure
- Writing test cases

## What AI Got Wrong
- Suggested deprecated Gemini library (google.generativeai)
- Initial model name gemini-1.5-flash was outdated
- Some prompt suggestions were too verbose

## Best Prompts Used

### Severity Detection
"Read this technical outage description and reply with 
only one word: low, medium, or high based on severity."

### Message Generation
"You are a customer communication expert. Write a 
customer-facing status update. Do NOT use technical 
terms. Keep it under 3 sentences. Match the tone exactly."

### Quality Check
"Does this message match a {tone} tone? 
Reply with only YES or NO."

## Tools Used
- Cursor AI — code generation
- Claude AI — architecture planning
- Groq API — LLM inference
- GitHub Copilot — code suggestions
