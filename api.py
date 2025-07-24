#Tools our api will be able to use 

from livekit.agents import llm 

class AssistantFnc(llm.FunctionContext): 
    def __init__(self): 
        super().__init__()

