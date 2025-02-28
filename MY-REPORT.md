![GenI-banner](https://github.com/genilab-fau/genilab-fau.github.io/blob/8d6ab41403b853a273983e4c06a7e52229f43df5/images/genilab-banner.png?raw=true)

# Optimizing Prompt Engineering Techniques for Automated Requirements Analysis in Italian Culinary Science
A comparaison of various prompt engineering techniques in LLMs for a requirements analysis in Italian Culinary Science, and more broadly, the software development lifecycle (SDLC). 


* Authors: [Ruben Nelson]
* Academic Supervisor: [Dr. Fernando Koch](http://www.fernandokoch.me)


# Research Question 

How can different prompt engineering techniques and LLMs optimize the quality, completeness, and efficiency of automated requirements analysis to address Italian cuisine queries?


## Arguments

#### What is already known about this topic

* Every day example of Gen-AI appplications: input a prompt into a generative transformer utilizing LLMs for a desired result, from an answer to a question to large blocks of code.
* Specifically, Large Language Models (LLMs) can be leveraged to generate requirements documentation, saving significant time in the software development process.
* The quality of LLM outputs is highly dependent on the prompt engineering techniques employed.
* Few-shot learning with carefully selected examples can guide models toward more accurate and domain-specific outputs, compared to zero-shot learning that has no guidance.
* Chain-of-thought prompting can improve reasoning capabilities in complex technical domains.
* Some challenges include maintaining consistency in prompt development and the requirements generated through Generative A.I. systems.
*The possibility of using multi-step prompting techniques to refine and enhance initial requirements offers a solution to automating requirements analysis geared toward solution development, or more broadly, software development.

#### What this research is exploring

* We employ zero-shot, few-shot, chain-of-thought, and meta-prompting to generate requirements for Italian cuisine design. 
* We are building a comparative framework to evaluate the effectiveness of each technique in terms of result relevancy, quality, completeness, and processing time.
* We are exploring how the different LLMs affect the requirements generation process. The other parameters (temperature, context window, prediction length) will also generally be considered in the analysis generally, but not directly modified due to the excessive number of possible combinations.
· Overall, we investigate how prompt structure and complexity influence the comprehensiveness of generated requirements.

#### Implications for practice

* It will be easier to automate requirements needed for prompts addressing specialized queries or projects.
* It will optimize the software development lifecycle by reducing time spent on preliminary requirement drafting.
* We will better understand understand how to construct prompts that extract domain-specific technical requirements with higher accuracy and less human effort.

# Research Method

The research methodology comprisies of a comparison of four different prompt engineering techniques applied to the same use case of Italian cuisines.

1. Zero-shot learning: Providing no prior example or information in the prompt. The model relies on its pre-trained knowledge of Italian cuisines to infer what is needed, in this case, to name an ingridient in an Italian dish.

2. Few-shot learning: Providing concise examples of requirements for other Italian cuisines (such as pizza and lasanga) to guide the model toward generating structured outputs.

3. Chain-of-thought Prompting: Step-by-step reasoning before arriving at the requirement specification, encouraging the model to use knowledge of ingredients of known Italian dishes.

4. Meta-prompting: An abstract prompt explicitly structuring categories of requirements to direct the model's output organization.

For each technique, four different models are used (llama3.2, qwen, phi3.5, and smollm) while keeping consisten the varying parameters such as temperature, context window size, and prediction length determine model performance. Qualitative aspects are inspected for completeness, relevance, organization and quantitative metrics are measured in processing time.

# Results

## Zero-Shot Prompt

#### llama3.2

The response time was 27.612s. It provided a good answer (basil), but within a large amount of time. This may be remedied by modifying the prediction parameters as a point of future work.

#### qwen

The respone time was 46.528s. It provide a popular answer (tomatoes), but within the largest amount of time of all the models. A point of future work would be to investigate which parameters could reduce decision time.

#### phi3.5

The response time was 31.117s. It provided a good answer (olive oil), but within a large amount of time. This may be remedied by modifying the prediction parameters as a point of future work. 

#### smollm

The response time was 6.459s. Of all the models, this had the fastest performance, but arguably the worst accuracy. The question asked for one ingredient and it gave two. But this model gave additional details of what the ingredients it chose does for Italian cooking, showing extra answer quality.

## Few-Shots Prompt

#### llama3.2

The response time was 23.603s. In the few-shots prompt, two dishes and two ingredients were provided, but the answer that was provided (olives) was not something associated with the examples given, demonstrating answer quality being low, despite the answer being an accurate answer.

#### qwen

The response time was 28.422s, which was the longest of all the models. The answer provided (tomatoes) was an answer suggested and encouraged by the prompt itself, demonstrating good answer quality and accuracy.

#### phi3.5

The response time was 25.92s. The answer provided was the same as the qwen model (tomatoes), demonstrating good answer quality and accuracy.

#### smollm

The response time was 4.19s the fastest of all the models.  However, the answer quality was low due to following the prompt instructions after an initial misinterpretation of the prompt, despite high answer accuracy (chose olives).

## Chain of Thought Prompt

#### llama3.2

The response time was 47.342s. It is highly possible the prompt was written poorly, but the answer received was not a self-generated prompt. However, it provided a list of ingredients and discussed why it chose what it chose, as the prompt required. Unfortunately, the terminal cut off the full answer.

#### qwen

The response time was 41.823s. Again, due to a poorly written prompt, the model did not self-generate a prompt.  However, the answer was concise (parmesan cheese) and the considerations taken to arrive at that answer were given. It was a high quality and accurate answer in that respect.

#### phi3.5

The response time was 40.41s. The response clearly intended to follow chain-of-thought, but it misinterpreted the prompt, explaining rather than using chain-of-thought. The answer also was cut off by the terminal so it is not possible to determine answer quality or accuracy with the given payload parameters.

#### smollm

The response time was 8.289s, the fastest response time. However, as with the phi3.5 model, the sollm model misinterpreted the prompt, and the answer was cut off by the terminal.  A commentary on the answer quality or accuracy cannot be given with the given payload parameters.

## Meta-Prompt

#### llama3.2

The response time was 29.067s. This model accurately understood the prompt to self-generate a prompt and respond to that prompt. The only issue was that the answer was lengthy, so the answer was cut off by the terminal. Meta-prompt structuring performs well in this model.

#### qwen

The response time was 45.174s. This model somewhat understood the prompt to self-generate a prompt and respond to that prompt, however, the relevancy was off. It made a prompt about natural language processing (a better topic to explore than food) The answer to the prompt was not provided, however. Meta-prompt could perform well, but with a better meta-prompt structure.

#### phi3.5

The response time was 50.152s the longest response time of the four models. This model accurately understood the prompt to self-generate a prompt and respond to that prompt. The only issue was that the answer was more lengthy than the llama3.2 model, so the answer was cut off by the terminal. Meta-prompt structuring performs well in this model.

#### smollm

The response time was 4.891s, the quickest time of four models.  The response itself, however, was not relevant to the prompt request.  Instead it was an explnantion on steps to constructing a generic prompt rather than address Italian cuisine. Also, the terminal cut off the response.  

## Overall

In all prompt structures, the smollm model performed the fastest, but was also the worst performing model.  The answers were based on a prompt misinterpretation, illustrating the importance of model selection. The other models had similar response times, so the additional vetting criteria, answer quality and relevancy, would be the next determining performance factor. This was dependent on the prompt structure. Simple prompts, such as zero-shot and few-shot prompts, resulted in accurate and relevant, but also short, answers.  When the prompt becomes complex, then the prompt structure dictates which model gives relevant answers. The qwen model veers off when given a meta-prompt, while the phi model veers off when given a chain-of-thought prompt. In all cases, the llama3.2 model performed more consistently with regards to accuracy and relevancy, regardless of prompt structure.

# Further research

There are many more opportunities to expand this work, partiularly in different domains, as opposed to cooking.  Also, the payload parameters particularly have a direct effect on the response size and quality.  for example, increasing the temperature or the context window would likely provide more lengthy and creative answers, but what is the threshold for potential diminshing returns? And what transformer model can objectively and quantitatively evaluate response quality.