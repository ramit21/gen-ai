import os
from langchain_anthropic import ChatAnthropic
from langchain.tools import tool
# --- AGENTCORE SPECIFIC IMPORTS ---
from aws_agentcore import AgentCoreApp, Agent, Memory, trace
from aws_agentcore.memory import EpisodicMemory # For cross-session memory

# 1. Define a tool (Standard LangChain style)
@tool
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculates BMI given weight in kg and height in meters."""
    return round(weight_kg / (height_m ** 2), 2)

# 2. Define the Agent Class with AgentCore Annotations
@Agent(
    name="HealthAnalyst",
    description="Analyzes health metrics and remembers user history.",
    # --- AGENTCORE ADDITION: Managed Memory ---
    # EpisodicMemory allows the agent to remember facts from sessions days ago.
    memory=EpisodicMemory(ttl_days=30) 
)
class HealthAgent:
    def __init__(self):
        self.llm = ChatAnthropic(model="claude-3-5-sonnet")

    # --- AGENTCORE ADDITION: The @trace annotation ---
    # This sends detailed logic "steps" to the AgentCore Trace UI
    @trace(name="OrchestrationStep")
    def call_llm(self, prompt, memory_context):
        # The 'memory_context' is automatically injected by AgentCore
        full_prompt = f"User History: {memory_context}\n\nUser Question: {prompt}"
        return self.llm.invoke(full_prompt)

# 3. Entry point for AgentCore Runtime
# This replaces the standard "app.run()" with the AgentCore provider
app = AgentCoreApp(agents=[HealthAgent])

if __name__ == "__main__":
    # Local testing mode
    app.run_local()