# symptom_database.py - COMPLETE UPDATED VERSION WITH ALL CONDITIONS

SYMPTOM_SOLUTIONS = {
    # EXISTING CONDITIONS
    "common_cold": {
        "symptoms": ["Runny Nose", "Sneezing", "Cough", "Sore Throat", "Congestion"],
        "condition": "Common Cold",
        "advice": "Rest, drink plenty of fluids, and use over-the-counter cold remedies. Most colds resolve within 7-10 days.",
        "urgency": "Low - Self-care recommended",
        "immediate_remedy": "💊 Take OTC cold medicine • 💧 Stay hydrated • 🛌 Get plenty of rest • 🍯 Honey for cough"
    },
    
    "flu": {
        "symptoms": ["Fever", "Body Aches", "Chills", "Fatigue", "Cough", "Headache"],
        "condition": "Influenza (Flu)",
        "advice": "Rest, hydrate, and consider antiviral medications if seen early. Stay home to avoid spreading. Seek care if breathing difficulties occur.",
        "urgency": "Moderate - See doctor if severe",
        "immediate_remedy": "🛌 Rest • 💧 Hydrate • 💊 Take fever reducers • 🌡️ Monitor temperature"
    },
    
    "covid": {
        "symptoms": ["Fever", "Cough", "Loss of Smell/Taste", "Shortness of Breath"],
        "condition": "COVID-19",
        "advice": "Isolate immediately, get tested, and monitor symptoms. Seek emergency care for breathing difficulties. Follow local health guidelines.",
        "urgency": "Moderate - Test and isolate",
        "immediate_remedy": "🏠 Isolate immediately • 🧪 Get tested • 🌡️ Monitor symptoms • 🚑 Seek ER for breathing issues"
    },
    
    "migraine": {
        "symptoms": ["Headache", "Sensitivity to Light", "Nausea", "Visual Disturbances"],
        "condition": "Migraine",
        "advice": "Rest in a dark, quiet room. Use prescribed migraine medications. Avoid triggers like bright lights and strong smells.",
        "urgency": "Moderate - See doctor if frequent",
        "immediate_remedy": "🌑 Rest in dark room • 💊 Take pain medication • 🧊 Cold compress on forehead • 🚫 Avoid triggers"
    },
    
    "anxiety": {
        "symptoms": ["Nervousness", "Rapid Heartbeat", "Sweating", "Trembling"],
        "condition": "Anxiety Attack",
        "advice": "Practice deep breathing, mindfulness, and grounding techniques. Reduce caffeine intake. Seek therapy if persistent.",
        "urgency": "Low - Emergency if severe",
        "immediate_remedy": "🌬️ Deep breathing • 👣 Grounding techniques • 💧 Drink water • 📞 Call support person"
    },
    
    "stomach_flu": {
        "symptoms": ["Nausea", "Vomiting", "Diarrhea", "Stomach Cramps"],
        "condition": "Gastroenteritis (Stomach Flu)",
        "advice": "Stay hydrated with clear fluids, follow BRAT diet (bananas, rice, applesauce, toast). Avoid dairy and fatty foods.",
        "urgency": "Low - ER if severe dehydration",
        "immediate_remedy": "💧 Sip clear fluids • 🍌 BRAT diet • 🛌 Rest • 🚫 Avoid dairy/fatty foods"
    },
    
    "uti": {
        "symptoms": ["Frequent Urination", "Burning Sensation", "Pelvic Pain"],
        "condition": "Urinary Tract Infection",
        "advice": "Drink plenty of water, avoid irritants like caffeine. See doctor for antibiotics if symptoms persist.",
        "urgency": "Moderate - See doctor within 24-48 hours",
        "immediate_remedy": "💧 Drink water • 🚫 Avoid caffeine • 💊 Use OTC UTI pain relief • 🏥 Schedule doctor visit"
    },
    
    "allergies": {
        "symptoms": ["Sneezing", "Itchy Eyes", "Runny Nose", "Congestion"],
        "condition": "Seasonal Allergies",
        "advice": "Use antihistamines, nasal sprays, and avoid allergen exposure. Keep windows closed during high pollen days.",
        "urgency": "Low - Self-care recommended",
        "immediate_remedy": "💊 Take antihistamine • 🚪 Keep windows closed • 🕶️ Wear sunglasses outside • 🧼 Shower after being outdoors"
    },
    
    # SKIN PROBLEMS
    "acne": {
        "symptoms": ["Pimples", "Oily Skin", "Skin Inflammation"],
        "condition": "Acne or Skin Breakout",
        "advice": "Gently cleanse twice daily, avoid picking or squeezing pimples. Use non-comedogenic products and consider over-the-counter treatments with benzoyl peroxide or salicylic acid.",
        "urgency": "Low - Self-care recommended",
        "immediate_remedy": "🧼 Gentle cleansing twice daily • 🚫 Avoid picking pimples • 💊 Use benzoyl peroxide spot treatment • 🧴 Non-comedogenic moisturizer"
    },
    
    "sunburn": {
        "symptoms": ["Redness", "Skin Pain", "Swelling", "Blisters"],
        "condition": "Sunburn",
        "advice": "Apply cool compresses, use aloe vera gel, stay hydrated, and take over-the-counter pain relievers if needed. Avoid further sun exposure and see doctor for severe burns with blisters.",
        "urgency": "Low - Self-care unless severe",
        "immediate_remedy": "🌿 Apply aloe vera gel • 🧊 Cool compresses • 💧 Stay hydrated • 💊 Take ibuprofen for pain"
    },
    
    "fungal_infection": {
        "symptoms": ["Itching", "Redness", "Flaking"],
        "condition": "Fungal Skin Infection",
        "advice": "Keep area clean and dry, use over-the-counter antifungal cream, and wear breathable clothing. See doctor if no improvement after 2 weeks.",
        "urgency": "Low - Try OTC antifungal first",
        "immediate_remedy": "💊 Apply antifungal cream • 🧼 Keep area clean and dry • 👕 Wear breathable clothing • 🚫 Don't share towels"
    },
    
    # NEW CONDITIONS ADDED:
    "asthma_attack": {
        "symptoms": ["Shortness of Breath", "Wheezing", "Chest Tightness", "Cough"],
        "condition": "Asthma Attack",
        "advice": "Use rescue inhaler immediately. Sit upright and try to stay calm. Seek emergency care if breathing doesn't improve.",
        "urgency": "High - Emergency if severe",
        "immediate_remedy": "💨 Use rescue inhaler • 🪑 Sit upright • 🌬️ Practice slow breathing • 🚑 Call emergency if worsening"
    },
    
    "tension_headache": {
        "symptoms": ["Headache", "Neck Pain", "Stress", "Muscle Tension"],
        "condition": "Tension Headache",
        "advice": "Practice stress management, improve posture, apply heat to neck and shoulders. Over-the-counter pain relievers may help.",
        "urgency": "Low - Self-care recommended",
        "immediate_remedy": "💊 Take OTC pain reliever • 🔥 Apply heat to neck • 🧘 Practice relaxation • 💆 Gentle massage"
    },
    
    "bronchitis": {
        "symptoms": ["Cough", "Shortness of Breath", "Fatigue", "Chest Discomfort"],
        "condition": "Acute Bronchitis",
        "advice": "Rest, stay hydrated, use cough suppressants if needed. Most cases resolve in 1-3 weeks. See doctor if symptoms worsen.",
        "urgency": "Low - See doctor if persistent",
        "immediate_remedy": "🛌 Rest • 💧 Drink warm fluids • 💊 Use cough medicine • 🌬️ Use humidifier"
    },
    
    "conjunctivitis": {
        "symptoms": ["Eye Problems", "Redness", "Itching", "Discharge"],
        "condition": "Pink Eye (Conjunctivitis)",
        "advice": "Practice good hygiene, avoid touching eyes, use warm compresses. See doctor for antibiotic drops if bacterial.",
        "urgency": "Low - See doctor for diagnosis",
        "immediate_remedy": "👁️ Avoid touching eyes • 🧼 Wash hands frequently • 🧻 Use clean towels • 🔥 Warm compresses"
    },
    
    "sinusitis": {
        "symptoms": ["Headache", "Congestion", "Facial Pain", "Runny Nose"],
        "condition": "Sinus Infection",
        "advice": "Use saline nasal spray, apply warm compresses, stay hydrated. See doctor if symptoms last more than 10 days.",
        "urgency": "Low - Self-care recommended",
        "immediate_remedy": "💧 Saline nasal spray • 🔥 Warm facial compresses • 💧 Stay hydrated • 💊 Decongestants if needed"
    },
    
    # NEW CONDITIONS FOR BETTER MATCHING:
    "anxiety_disorder": {
        "symptoms": ["Anxiety", "Nervousness", "Rapid Heartbeat", "Sweating", "Trembling", "Headache", "Dizziness"],
        "condition": "Anxiety Disorder",
        "advice": "Practice relaxation techniques like deep breathing, meditation, and mindfulness. Reduce caffeine intake, get regular exercise, and maintain a consistent sleep schedule. Consider speaking with a mental health professional for therapy or counseling.",
        "urgency": "Moderate - Consult doctor if persistent",
        "immediate_remedy": "🌬️ Practice deep breathing • 🧘 Try mindfulness meditation • 💧 Drink water • 📞 Call support person • 🚫 Reduce caffeine"
    },
    
    "migraine_with_aura": {
        "symptoms": ["Headache", "Visual Disturbances", "Dizziness", "Nausea", "Sensitivity to Light"],
        "condition": "Migraine with Aura",
        "advice": "Rest in a dark, quiet room. Use prescribed migraine medications if available. Avoid triggers like bright lights, strong smells, and certain foods. Stay hydrated.",
        "urgency": "Moderate - See doctor if frequent",
        "immediate_remedy": "🌑 Rest in dark room • 💊 Take migraine medication • 🧊 Cold compress • 💧 Sip water • 🚫 Avoid triggers"
    },
    
    "vertigo": {
        "symptoms": ["Dizziness", "Balance Problems", "Nausea", "Headache"],
        "condition": "Vertigo or Balance Disorder",
        "advice": "Move slowly and avoid sudden head movements. Sit or lie down when dizzy. Stay hydrated and consider vestibular exercises. See doctor if symptoms persist.",
        "urgency": "Moderate - See doctor if severe",
        "immediate_remedy": "🪑 Sit or lie down immediately • 🚶 Move slowly • 💧 Sip water • 👀 Focus on stationary object • 🚫 Avoid sudden movements"
    },
    
    "stress_related": {
        "symptoms": ["Anxiety", "Headache", "Fatigue/Tiredness", "Sleep Issues", "Muscle Tension"],
        "condition": "Stress-Related Symptoms",
        "advice": "Practice stress management techniques like meditation, exercise, and proper sleep hygiene. Take regular breaks, maintain social connections, and consider counseling if stress becomes overwhelming.",
        "urgency": "Low - Self-care recommended",
        "immediate_remedy": "🧘 Practice deep breathing • 🏃 Light exercise • 💤 Improve sleep routine • 📝 Journal feelings • 👥 Talk to friends/family"
    },
    
    "dehydration": {
        "symptoms": ["Dizziness", "Headache", "Fatigue/Tiredness", "Dry Skin"],
        "condition": "Dehydration",
        "advice": "Drink plenty of water and electrolyte-rich fluids. Avoid caffeine and alcohol. Rest in a cool environment and consume water-rich foods like fruits and vegetables.",
        "urgency": "Low - Self-care recommended",
        "immediate_remedy": "💧 Drink water immediately • 🍉 Eat water-rich fruits • 🚫 Avoid caffeine/alcohol • 🌡️ Rest in cool place • 🧂 Consider electrolyte drink"
    }
}

FOLLOW_UP_QUESTIONS = {
    "fever": [
        "How high is your temperature?",
        "How long have you had the fever?",
        "Do you have any other symptoms with the fever?"
    ],
    "headache": [
        "Where is the pain located?",
        "Is the pain constant or comes and goes?",
        "Does light or sound make it worse?"
    ],
    "cough": [
        "Is it a dry cough or productive?",
        "What color is the mucus?",
        "Does it get worse at night?"
    ],
    "pain": [
        "On a scale of 1-10, how severe is the pain?",
        "What makes the pain better or worse?",
        "When did the pain start?"
    ],
    "fatigue": [
        "How many hours are you sleeping?",
        "Does rest make you feel better?",
        "Has your appetite changed?"
    ],
    "nausea": [
        "Are you actually vomiting?",
        "What foods make it worse?",
        "Can you keep fluids down?"
    ]
}

PROFESSIONAL_TEMPLATES = {
    "greeting": "Thank you for sharing your symptoms with me today.",
    "empathy": "I understand that {symptoms} can be concerning.",
    "assessment": "Based on the symptoms you've described, this appears to be {condition}.",
    "advice": "Here is what I recommend: {advice}",
    "urgency": "Urgency Level: {urgency}",
    "followup": "Please monitor your symptoms and seek in-person medical care if they worsen.",
    "closing": "Take care of yourself and don't hesitate to seek additional medical attention."
}

def detect_condition_from_symptoms(selected_symptoms):
    """Symptom matching with weights and logic"""
    if not selected_symptoms:
        return None
    
    SYMPTOM_WEIGHTS = {
        # CRITICAL SYMPTOMS
        "chest pain": 3.0, "difficulty breathing": 3.0, "severe bleeding": 3.0,
        "sudden weakness": 3.0, "suicidal thoughts": 3.0, "seizure": 3.0,
        "severe head injury": 3.0, "paralysis/numbness": 3.0,
        
        # NEUROLOGICAL
        "headache": 1.5, "dizziness": 1.5, "confusion": 2.0, "memory problems": 1.5,
        "anxiety": 1.5, "nervousness": 1.5, "depression": 1.0, "sleep issues": 0.5, 
        "vision problems": 2.0, "visual disturbances": 2.0, "hearing loss": 1.5, 
        "tremors": 2.0, "fainting": 2.5, "balance problems": 1.5,
        
        # CARDIOVASCULAR
        "heart palpitations": 2.0, "rapid heartbeat": 2.0, "shortness of breath": 2.5, 
        "chest tightness": 2.5, "swollen ankles": 1.0, "high blood pressure": 1.5, 
        "irregular heartbeat": 2.0, "cold extremities": 1.0,
        
        # DIGESTIVE
        "nausea": 1.0, "vomiting": 1.5, "diarrhea": 1.0, "constipation": 0.5,
        "stomach pain": 1.5, "heartburn": 0.5, "appetite loss": 0.5, "weight changes": 1.0,
        "bloating": 0.5, "blood in stool": 2.5, "stomach cramps": 1.0,
        
        # DERMATOLOGICAL
        "skin rash": 1.0, "itching": 0.5, "redness": 0.5, "swelling": 1.0,
        "acne/pimples": 0.5, "dry skin": 0.5, "hair loss": 0.5, "nail changes": 0.5,
        "blisters": 1.0, "skin discoloration": 1.0, "skin inflammation": 1.0,
        "skin pain": 1.0, "flaking": 0.5,
        
        # MUSCULOSKELETAL
        "muscle pain": 1.0, "joint pain": 1.0, "back pain": 1.0, "neck pain": 1.0,
        "stiffness": 0.5, "swelling joints": 1.0, "limited movement": 1.0, 
        "muscle weakness": 1.5, "muscle tension": 1.0,
        
        # GENERAL
        "fever": 2.0, "chills": 1.0, "cough": 1.0, "cold": 0.5, "sore throat": 1.0,
        "runny nose": 0.5, "fatigue/tiredness": 0.5, "allergies": 0.5, "urinary issues": 1.0,
        "ear pain": 1.0, "eye problems": 1.5, "sneezing": 0.5, "body aches": 1.0,
        "sweating": 1.0, "trembling": 1.0, "frequent urination": 1.0, "burning sensation": 1.5,
        "pelvic pain": 1.5, "itchy eyes": 0.5, "congestion": 0.5, "stress": 1.0,
        
        # EXISTING SYMPTOMS
        "loss of smell/taste": 2.0, "sensitivity to light": 1.0
    }
    
    # Clean symptoms
    clean_symptoms = []
    for symptom in selected_symptoms:
        if ' ' in symptom and any(symptom.startswith(emoji) for emoji in ["🔴", "🟡", "🟢"]):
            clean_symptoms.append(symptom.split(' ', 1)[1].lower())
        else:
            clean_symptoms.append(symptom.lower())
    
    best_match = None
    highest_score = 0
    
    for condition_id, condition_data in SYMPTOM_SOLUTIONS.items():
        score = 0
        condition_symptoms = [s.lower() for s in condition_data["symptoms"]]
        
        for symptom in clean_symptoms:
            if symptom in condition_symptoms:
                score += SYMPTOM_WEIGHTS.get(symptom, 1.0)
        
        if score > highest_score and score >= 2.0:
            highest_score = score
            best_match = condition_id
    
    return best_match

def check_emergency_flags(selected_symptoms):
    """Detect emergency symptoms immediately"""
    EMERGENCY_RED_FLAGS = {
        "chest pain": "CHEST PAIN - Could indicate heart issues. Seek emergency care immediately.",
        "difficulty breathing": "BREATHING DIFFICULTY - Requires immediate medical attention.", 
        "severe bleeding": "SEVERE BLEEDING - Apply pressure and seek emergency care.",
        "sudden weakness": "SUDDEN WEAKNESS - Could be stroke. Call emergency services.",
        "suicidal thoughts": "MENTAL HEALTH EMERGENCY - Contact crisis helpline immediately.",
        "shortness of breath": "BREATHING DIFFICULTY - Requires immediate medical attention.",
        "seizure": "SEIZURE - This is a medical emergency. Call emergency services.",
        "severe head injury": "SEVERE HEAD INJURY - Requires immediate medical attention.",
        "paralysis/numbness": "PARALYSIS/NUMBNESS - Could be stroke. Call emergency services immediately."
    }
    
    emergencies = []
    if selected_symptoms:
        for symptom in selected_symptoms:
            if ' ' in symptom and any(symptom.startswith(emoji) for emoji in ["🔴", "🟡", "🟢"]):
                clean_symptom = symptom.split(' ', 1)[1].lower()
            else:
                clean_symptom = symptom.lower()
                
            if clean_symptom in EMERGENCY_RED_FLAGS:
                emergencies.append(EMERGENCY_RED_FLAGS[clean_symptom])
    
    return emergencies

def get_condition_info(condition_id):
    """Get detailed information about a condition"""
    if condition_id in SYMPTOM_SOLUTIONS:
        return SYMPTOM_SOLUTIONS[condition_id]
    return None

def get_followup_questions(condition_id):
    """Get relevant follow-up questions for a condition"""
    questions = []
    condition_info = get_condition_info(condition_id)
    
    if condition_info:
        for symptom in condition_info["symptoms"]:
            symptom_key = symptom.lower().replace(" ", "_").replace("/", "_")
            if symptom_key in FOLLOW_UP_QUESTIONS:
                questions.extend(FOLLOW_UP_QUESTIONS[symptom_key])
    
    # Remove duplicates while preserving order
    seen = set()
    unique_questions = []
    for q in questions:
        if q not in seen:
            seen.add(q)
            unique_questions.append(q)
    
    return unique_questions[:3]

def format_professional_response(condition_id, user_symptoms):
    """Format a professional medical response"""
    condition_info = get_condition_info(condition_id)
    if not condition_info:
        return "I'm not sure about your symptoms. Please consult a healthcare professional."
    
    symptoms_text = ", ".join(user_symptoms)
    
    response_parts = [
        PROFESSIONAL_TEMPLATES["greeting"],
        PROFESSIONAL_TEMPLATES["empathy"].format(symptoms=symptoms_text),
        PROFESSIONAL_TEMPLATES["assessment"].format(condition=condition_info["condition"]),
        PROFESSIONAL_TEMPLATES["advice"].format(advice=condition_info["advice"]),
        PROFESSIONAL_TEMPLATES["urgency"].format(urgency=condition_info["urgency"]),
        "Immediate Actions: " + condition_info["immediate_remedy"],
        PROFESSIONAL_TEMPLATES["followup"],
        PROFESSIONAL_TEMPLATES["closing"]
    ]
    
    return "\n\n".join(response_parts)

# Simple test function
def test_symptom_matching():
    """Test basic symptom matching"""
    test_cases = [
        ["Fever", "Cough", "Body Aches"],
        ["Headache", "Sensitivity to Light"],
        ["Nausea", "Vomiting"]
    ]
    
    for i, symptoms in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {symptoms}")
        condition = detect_condition_from_symptoms(symptoms)
        
        if condition:
            info = get_condition_info(condition)
            print(f"Matched: {info['condition']}")
        else:
            print("No specific condition matched")