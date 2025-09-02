# 7. Create a simple rule-based expert system that suggests a diagnosis based on user-entered symptoms.

def expert_system():
    symptom = input("Enter your symptom (fever, cough, headache): ").lower()
    if symptom == "fever":
        print("Diagnosis: You may have the flu.")
    elif symptom == "cough":
        print("Diagnosis: You may have a cold.")
    elif symptom == "headache":
        print("Diagnosis: You may be dehydrated.")
    else:
        print("Diagnosis: Unknown, consult a doctor.")

expert_system()