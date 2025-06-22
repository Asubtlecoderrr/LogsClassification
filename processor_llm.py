import ollama

def classify_with_llm(log_text, model='llama3'):
    
    prompt = f"""Classify the following log entry into categories -  Workflow Error, Deprecation Warning. 
    If you cant figure out the category return Unclassiffied.
    Return only the category. no premable or postamble.
    \n\nLog: {log_text}"""
    
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content'].strip()
