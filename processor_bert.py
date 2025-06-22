from sentence_transformers import SentenceTransformer
import joblib 

transformers_model = SentenceTransformer('all-MiniLM-L6-v2')

def load_model():
    model = joblib.load("models/log_classifier.joblib")
    return model

def classify_with_bert(log_message):
    
    classifier_model = load_model()
    embeddings = transformers_model.encode(log_message)
    predicted_label = classifier_model.predict([embeddings])[0]
    probabilities = classifier_model.predict_proba([embeddings])[0]
    if probabilities.max() < 0.5:
        predicted_label = "Unclassified"
    else:
        predicted_label = predicted_label
    
    return predicted_label
    
    