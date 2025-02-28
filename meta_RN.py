##
## META PROMPTING
##

from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "This is a meta-prompt. In this meta-prompt follow the software developer life cycle, where a problem must be defined, solutions must be proposed and requirements must be analyzed to determine the best solution. In defining the problem, consider the perspective of a software developer who needs to create a prompt for a model that addresses a problem related to Italian cuisines. If necessary, rephrase the prompt in order to define the problem clearly. Then propose one or more solutions to that problem. The solutions can be from any known and popular  resources on Italian cuisine. For example, the Italian cuisine could be a recipe from a reciple website. Or the response could be best practices in preparing an Italian cuisine. In the requirements analysis, requirements are detailed and prioritized for the solution to the defined problem. The acceptance criteria of the generated solutions are comparable to typical Italian cuisine and culture. Using the stated parameters in this meta-prompt, provide a prompt that can be used to generate a response from a model and then answer that prompt's problem statement. If necessary rephrase as many times as necessary the prompt to make the problem clear."

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates

# @TODO TO BE COMPLETED
PROMPT = MESSAGE 

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="smollm:135m", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')