##
## FEW SHOTS PROMPTING
##

from _pipeline import create_payload, model_req

#### (1) Adjust the inbounding  Prompt, simulating inbounding requests from users or other systems
MESSAGE = "Name one and only one single popular ingredient in Italian cuisines."

#### (2) Adjust the Prompt Engineering Technique to be applied, simulating Workflow Templates
FEW_SHOT = "I am looking for a home recipe for an Italian dinner for a family. Pizza is an Italian cuisine that has tomatoes as an ingredient. Lasanga is an Italian cuisine that has pasta. Italian cuisines normally have several ingredients.  Provide the result only: "
PROMPT = FEW_SHOT + '\n' + MESSAGE 

#### (3) Configure the Model request, simulating Workflow Orchestration
# Documentation: https://github.com/ollama/ollama/blob/main/docs/api.md
payload = create_payload(target="ollama",
                         model="qwen:latest", 
                         prompt=PROMPT, 
                         temperature=1.0, 
                         num_ctx=100, 
                         num_predict=100)

### YOU DONT NEED TO CONFIGURE ANYTHING ELSE FROM THIS POINT
# Send out to the model
time, response = model_req(payload=payload)
print(response)
if time: print(f'Time taken: {time}s')