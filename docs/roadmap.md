# JARVIS – Personal Agent Roadmap (Private)

## Purpose:
- Keep technical skills warm (Python, AWS, GenAI systems). The gap between "using a chatbot" and "building an agentic system" is where the real engineering—and the learning—happens.

## Guiding principle
- Deterministic skills first; LLM is optional and never the source of truth.
- Build small, low-frequency agents with clear value.
- Security by default: secrets and personal data never committed.

## Candidate agents
- Birthday & anniversary reminders
- AI Travel planner
- Personal notes capture (optional, low priority)
- Weather / daily briefing (already done)
- Helping my wife with Youtube tihngs (High ROI)
- Stock tracking / summaries
- CR reviewer based on Google coding standards

## Engineering goals
- Deterministic skills first (no AI where facts matter)
- Agent layer for routing & planning
- Tool-based design (skills are callable units)
- Clear separation: data → logic → phrasing

## Cloud & GenAI goals:
- Secrets/config: .env → AWS Parameter Store
- Runtime: local → AWS Lambda (maybe Fargate later)
- Observability: logging, metrics, basic tracing
- Agentic workflows: tool calling, planning, retries
- RAG when local data grows
- MCP-style tool interfaces (later)

## Non-goals:
- No daily automation pressure
- No financial transactions
- No public sharing of personal data
