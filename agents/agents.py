from crewai import Agent

architect = Agent(
    role="Software Architect",
    goal="design proxy platform architecture",
)

frontend = Agent(
    role="Frontend Engineer",
    goal="build UI pages"
)

backend = Agent(
    role="Backend Engineer",
    goal="build backend APIs"
)

proxy_engineer = Agent(
    role="Proxy Infrastructure Engineer",
    goal="implement proxy rotation engine"
)

billing = Agent(
    role="Billing Engineer",
    goal="implement billing system"
)

decodo = Agent(
    role="Decodo Integration Engineer",
    goal="integrate Decodo API"
)

debugger = Agent(
    role="Debug Engineer",
    goal="find bugs"
)

refactor = Agent(
    role="Refactor Engineer",
    goal="rewrite code"
)