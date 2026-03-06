from crewai import Crew

from agents.agents import *
from agents.tasks import *

crew = Crew(

    agents=[
        architect,
        frontend,
        backend,
        proxy_engineer,
        billing,
        decodo,
        debugger,
        refactor
    ],

    tasks=[
        analyze_project,
        design_architecture,
        build_frontend,
        build_backend,
        build_proxy_engine,
        integrate_decodo,
        implement_billing,
        debug_code,
        refactor_code
    ]
)