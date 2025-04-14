class KnowledgeBase:
    def __init__(self):
        # Define knowledge base with expanded symptoms and rules
        self.rules = [
            {"symptoms": {"runny nose", "sore throat", "cough", "sneezing"}, 
             "diagnosis": "You might have a common cold. Rest, hydrate, and take over-the-counter medications."},
            {"symptoms": {"fever", "chills", "muscle aches", "fatigue", "dry cough"}, 
             "diagnosis": "You might have influenza. Rest, hydrate, and consult a doctor if symptoms persist."},
            {"symptoms": {"sneezing", "runny nose", "itchy eyes", "nasal congestion"}, 
             "diagnosis": "You might have allergies. Avoid allergens and consider antihistamines."},
            {"symptoms": {"facial pain", "pressure around the eyes", "nasal congestion", "thick nasal discharge"}, 
             "diagnosis": "You might have sinusitis. Stay hydrated, use saline sprays, and consult a doctor if symptoms persist."},
            {"symptoms": {"fever", "dry cough", "loss of taste/smell", "fatigue", "shortness of breath"}, 
             "diagnosis": "You might have COVID-19. Isolate yourself and consult a healthcare provider for testing."}
        ]


class InferenceEngine:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def analyze(self, user_symptoms):
        user_symptoms = set(map(str.strip, user_symptoms))  # Ensure clean input
        for rule in self.knowledge_base.rules:
            if rule["symptoms"].intersection(user_symptoms):  # Check for partial matches
                return rule["diagnosis"]
        return "Your symptoms do not match any known condition in our database. Please consult a healthcare professional."


class UserInterface:
    def __init__(self, inference_engine):
        self.inference_engine = inference_engine

    def run(self, user_input=None):
        print("Welcome to the Health Diagnostic System!")
        print("Please enter your symptoms (comma-separated). For example: fever, dry cough, fatigue")
        
        if user_input is None:
            try:
                user_input = input("Enter symptoms: ").lower()
            except OSError:
                print("Input is not available in this environment. Using a default test case.")
                user_input = "fever, dry cough"
        
        user_symptoms = [symptom.strip() for symptom in user_input.split(",") if symptom.strip()]

        # Get diagnosis from the inference engine
        diagnosis = self.inference_engine.analyze(user_symptoms)
        print(f"\nDiagnosis: {diagnosis}")


# Main function to run the system
if __name__ == "__main__":
    knowledge_base = KnowledgeBase()
    inference_engine = InferenceEngine(knowledge_base)
    user_interface = UserInterface(inference_engine)
    user_interface.run()
