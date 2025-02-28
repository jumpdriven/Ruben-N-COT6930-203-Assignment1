##
## CHAIN-OF-THOUGHT  PROMPTING
##

from _pipeline import create_payload, model_req


#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "Create a prompt asking what is one popular ingredient in Italian cuisines, and then respond to that prompt with the answer. State only the number of possible solutions you considered before selecting the best solution."

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
CHAIN_OF_THOUGHT = \
f"""
In this Chain-of-Thought exercise as prompt engineer, first begin by identifying the problem. The problem is that I am a chef who needs to make a unique Italian cuisine. Second, identify solutions and weigh the impact and feasibility of those solutions. Your solutions can be from any known and popular Italian cuisine list or resource. For example, Pizza and Lasanga are popular Italian cuisines. Finally perform a requirement analysis, where requirements are detailed and prioritized in the solution to the defined problem. The acceptance criteria of the generated solutions are within the popular or accepted practices by professionals in that industry. 
Using the stated parameters in this Chain-of-Thought, {MESSAGE}. 
"""

PROMPT = CHAIN_OF_THOUGHT 

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="phi3.5:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=1000, 
                         num_predict=1000)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')