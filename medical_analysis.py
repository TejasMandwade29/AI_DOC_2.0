# medical_analysis.py - FIXED VERSION

def calculate_confidence_score(selected_symptoms, has_image, has_audio, image_quality="unknown"):
    """Calculate confidence level for the diagnosis"""
    score = 0.5
    
    # FIX: Initialize clean_symptoms at the start
    clean_symptoms = []
    
    if selected_symptoms:
        score += min(len(selected_symptoms) * 0.1, 0.3)
        
        # Enhanced symptom pattern recognition
        specific_combinations = [
            ["fever", "cough", "fatigue", "body aches"],
            ["headache", "nausea", "vision problems", "sensitivity to light"],
            ["joint pain", "muscle pain", "fatigue"],
            ["nausea", "appetite loss", "fatigue", "stomach pain"],
            ["anxiety", "headache", "dizziness", "rapid heartbeat"],
            ["dizziness", "headache", "nausea", "balance problems"],
            ["chest pain", "shortness of breath", "palpitations"],
            ["skin rash", "itching", "redness", "swelling"]
        ]
        
        # FIX: Properly define clean_symptoms
        for s in selected_symptoms:
            if ' ' in s and any(s.startswith(emoji) for emoji in ["🔴", "🟡", "🟢"]):
                clean_symptoms.append(s.split(' ', 1)[1].lower())
            else:
                clean_symptoms.append(s.lower())
        
        # Better pattern matching
        matched_patterns = 0
        for combo in specific_combinations:
            matched_symptoms = sum(1 for symptom in combo if symptom in " ".join(clean_symptoms))
            if matched_symptoms >= 2:
                matched_patterns += 1
                score += 0.15
        
        # Bonus for multiple pattern matches
        if matched_patterns >= 2:
            score += 0.1
    
    # Enhanced data quality scoring
    if has_image:
        if image_quality == "good":
            score += 0.3
        else:
            score += 0.2
    
    if has_audio:
        score += 0.15
    
    # FIX: Only check specific symptoms if clean_symptoms has content
    if clean_symptoms:  # Added this check
        specific_symptoms = ["chest pain", "difficulty breathing", "loss of smell", "visual disturbances"]
        if any(symptom in " ".join(clean_symptoms) for symptom in specific_symptoms):
            score += 0.1
    
    # Ensure we return a float, not None
    return min(float(score), 0.95)

def add_confidence_disclaimer(analysis, confidence_score, selected_symptoms):
    """Add appropriate disclaimers based on confidence"""
    
    # Make sure confidence_score is a number
    if confidence_score is None:
        confidence_score = 0.5
    
    # Remove any existing markdown formatting
    analysis = analysis.replace("**", "").replace("*", "")
    
    # Enhanced disclaimer based on confidence level
    if confidence_score < 0.4:
        disclaimer = "\n\n⚠️ NOTE: Low confidence assessment. Multiple conditions possible. Professional evaluation strongly recommended."
    elif confidence_score < 0.7:
        disclaimer = "\n\nℹ️ NOTE: Moderate confidence. Consider professional confirmation if symptoms persist."
    else:
        disclaimer = "\n\n✅ NOTE: High confidence assessment based on clear symptom patterns."
    
    return analysis + disclaimer

# Emergency scoring function
def calculate_emergency_score(selected_symptoms):
    """Calculate emergency level for immediate triage"""
    critical_symptoms = ["chest pain", "difficulty breathing", "severe bleeding", 
                        "sudden weakness", "suicidal thoughts", "seizure", 
                        "severe head injury", "paralysis/numbness"]
    
    moderate_symptoms = ["fever", "high pain", "head injury", "vision problems", 
                        "heart palpitations", "shortness of breath", "fainting"]
    
    clean_symptoms = []
    for s in selected_symptoms:
        if ' ' in s and any(s.startswith(emoji) for emoji in ["🔴", "🟡", "🟢"]):
            clean_symptoms.append(s.split(' ', 1)[1].lower())
        else:
            clean_symptoms.append(s.lower())
    
    symptom_text = " ".join(clean_symptoms)
    
    critical_count = sum(1 for symptom in critical_symptoms if symptom in symptom_text)
    moderate_count = sum(1 for symptom in moderate_symptoms if symptom in symptom_text)
    
    if critical_count > 0:
        return "HIGH"
    elif moderate_count >= 2:
        return "MODERATE"
    else:
        return "LOW"