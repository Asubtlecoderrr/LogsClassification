# Classifying the logs of system 

We will use a combination of methods for log classification:

- **Regex pattern matching**: For log types that can be reliably identified with regular expressions.
- **BERT-based model**: For log types with enough training data, we will train a BERT model to classify them.
- **LLM-based classification**: For log types with fewer than 10 training samples, we use an LLM (Ollama) to classify them. The target labels with insufficient data are included in the prompt to the LLM for better context.

This hybrid approach leverages the strengths of each method depending on the available data for each log type.