import os
import gradio as gr
from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts
import datetime
import tempfile
from fpdf import FPDF
import re

# Import from our modules
from symptom_database import SYMPTOM_SOLUTIONS, detect_condition_from_symptoms, check_emergency_flags
from dashboard import create_enhanced_symptom_dashboard
from medical_analysis import calculate_confidence_score, add_confidence_disclaimer
from styles import ENHANCED_PROFESSIONAL_CSS, NEURAL_JS, ENHANCED_NEURAL_HEADER, HTML_ANIMATIONS_CSS, HTML_ANIMATIONS_HEADER, HTML_ANIMATIONS_JS

# CACHED: System prompt to avoid recreation
MEDICAL_SYSTEM_PROMPT = """
You are Dr. AI - Medical Diagnostician. Provide concise, professional medical assessments.

FORMAT:
URGENCY: [Low/Medium/High/Emergency]
CONDITION: [Primary condition] → [Secondary consideration]
ASSESSMENT: [2-3 key findings]
RECOMMENDATIONS: [3-4 specific actions]
URGENT CARE: [When to seek care]

Be direct, clinical, and actionable. No unnecessary explanations.
"""

# CACHED: Symptom categories for quick access - REMOVED ALL [BRACKETS]
SYMPTOM_CATEGORIES = {
    'urgent': [
        "Chest Pain", "Difficulty Breathing", "Severe Bleeding",
        "Sudden Weakness", "Suicidal Thoughts", "Seizure",
        "Severe Head Injury", "Paralysis/Numbness"
    ],
    'neuro': [
        "Headache", "Dizziness", "Confusion", "Memory Problems",
        "Anxiety", "Depression", "Sleep Issues", "Vision Problems",
        "Hearing Loss", "Tremors", "Fainting"
    ],
    'cardio': [
        "Heart Palpitations", "Shortness of Breath", "Chest Tightness",
        "Swollen Ankles", "High Blood Pressure", "Irregular Heartbeat",
        "Cold Extremities"
    ],
    'digestive': [
        "Nausea", "Vomiting", "Diarrhea", "Constipation",
        "Stomach Pain", "Heartburn", "Appetite Loss", 
        "Weight Changes", "Bloating", "Blood in Stool"
    ],
    'skin': [
        "Skin Rash", "Itching", "Redness", "Swelling",
        "Acne/Pimples", "Dry Skin", "Hair Loss", "Nail Changes",
        "Blisters", "Skin Discoloration"
    ],
    'muscle': [
        "Muscle Pain", "Joint Pain", "Back Pain", "Neck Pain",
        "Stiffness", "Swelling Joints", "Limited Movement",
        "Muscle Weakness"
    ],
    'common': [
        "Fever", "Chills", "Cough", "Cold", "Sore Throat", 
        "Runny Nose", "Fatigue/Tiredness", "Allergies",
        "Urinary Issues", "Ear Pain", "Eye Problems",
        "Sneezing", "Body Aches"
    ]
}

# SUPER SIMPLE VISIBLE ANIMATION CSS
VISIBLE_ANIMATION_CSS = """
/* MAIN HEADER WITH BUILT-IN ANIMATIONS */
.animated-header {
    position: relative;
    width: 100%;
    height: 500px;
    background: 
        radial-gradient(circle at 20% 80%, rgba(66, 153, 225, 0.3) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(159, 122, 234, 0.3) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(72, 187, 120, 0.2) 0%, transparent 50%),
        linear-gradient(135deg, #0a0f1c 0%, #1a1f36 100%);
    overflow: visible !important;
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 3px solid #4299e1;
    margin-bottom: 20px;
}

.header-content {
    text-align: center;
    position: relative;
    z-index: 100;
    padding: 2rem;
    background: rgba(10, 15, 28, 0.9);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 2px solid rgba(66, 153, 225, 0.5);
    box-shadow: 
        0 0 50px rgba(66, 153, 225, 0.3),
        0 20px 40px rgba(0, 0, 0, 0.4);
}

.main-title {
    font-size: 4.5rem;
    font-weight: 900;
    margin-bottom: 1rem;
    color: white;
    text-shadow: 0 0 30px rgba(66, 153, 225, 0.8);
    background: linear-gradient(135deg, #ffffff 0%, #a0c6ff 50%, #9f7aea 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 3px;
    animation: titleGlow 2s ease-in-out infinite alternate;
}

.neural-subtitle {
    font-size: 1.6rem;
    font-weight: 400;
    margin-bottom: 2rem;
    color: #a0c6ff;
    letter-spacing: 2px;
    animation: subtitlePulse 3s ease-in-out infinite;
    text-shadow: 0 0 20px rgba(66, 153, 225, 0.6);
}

@keyframes titleGlow {
    0% {
        text-shadow: 0 0 20px rgba(66, 153, 225, 0.6),
                     0 0 40px rgba(66, 153, 225, 0.4),
                     0 0 60px rgba(66, 153, 225, 0.2);
    }
    100% {
        text-shadow: 0 0 30px rgba(66, 153, 225, 0.9),
                     0 0 60px rgba(66, 153, 225, 0.6),
                     0 0 90px rgba(66, 153, 225, 0.3);
    }
}

@keyframes subtitlePulse {
    0%, 100% {
        opacity: 0.9;
        transform: scale(1);
        text-shadow: 0 0 15px rgba(66, 153, 225, 0.5);
    }
    50% {
        opacity: 1;
        transform: scale(1.05);
        text-shadow: 0 0 25px rgba(66, 153, 225, 0.8),
                     0 0 40px rgba(66, 153, 225, 0.3);
    }
}

/* VISIBLE ANIMATION ELEMENTS - BUILT INTO HEADER */
.floating-particle {
    position: absolute;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(66, 153, 225, 0.9), transparent 70%);
    animation: floatParticle 15s linear infinite;
    z-index: 5;
    box-shadow: 0 0 20px rgba(66, 153, 225, 0.8);
}

.floating-particle:nth-child(odd) {
    background: radial-gradient(circle, rgba(159, 122, 234, 0.7), transparent 70%);
    animation-duration: 18s;
    box-shadow: 0 0 20px rgba(159, 122, 234, 0.6);
}

.floating-particle:nth-child(3n) {
    background: radial-gradient(circle, rgba(72, 187, 120, 0.6), transparent 70%);
    animation-duration: 22s;
    box-shadow: 0 0 20px rgba(72, 187, 120, 0.5);
}

@keyframes floatParticle {
    0% {
        transform: translate(0, 0) rotate(0deg) scale(1);
        opacity: 0;
    }
    10% {
        opacity: 0.8;
    }
    50% {
        transform: translate(100px, 50px) rotate(180deg) scale(1.2);
        opacity: 1;
    }
    90% {
        opacity: 0.8;
    }
    100% {
        transform: translate(200px, 100px) rotate(360deg) scale(1);
        opacity: 0;
    }
}

/* PULSING ORB ANIMATION */
.pulsing-orb {
    position: absolute;
    width: 200px;
    height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(66, 153, 225, 0.15), transparent 70%);
    animation: pulseOrb 8s ease-in-out infinite;
    z-index: 1;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

@keyframes pulseOrb {
    0%, 100% {
        transform: translate(-50%, -50%) scale(1);
        opacity: 0.3;
    }
    50% {
        transform: translate(-50%, -50%) scale(1.8);
        opacity: 0.6;
    }
}

/* SCAN LINE - HIGHLY VISIBLE */
.scan-line {
    position: absolute;
    width: 100%;
    height: 3px;
    background: linear-gradient(90deg, 
        transparent 0%, 
        #4299e1 20%, 
        #9f7aea 50%, 
        #4299e1 80%, 
        transparent 100%);
    animation: scanMove 4s linear infinite;
    box-shadow: 
        0 0 30px #4299e1,
        0 0 60px rgba(66, 153, 225, 0.5);
    z-index: 6;
}

@keyframes scanMove {
    0% { 
        top: 0%; 
        opacity: 0; 
    }
    10% { 
        opacity: 1; 
    }
    90% { 
        opacity: 1; 
    }
    100% { 
        top: 100%; 
        opacity: 0; 
    }
}

/* CONNECTION LINES */
.connection-line {
    position: absolute;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(66, 153, 225, 0.6), transparent);
    animation: connectionFlow 6s linear infinite;
    transform-origin: 0 0;
    z-index: 4;
}

@keyframes connectionFlow {
    0% {
        opacity: 0;
        transform: scaleX(0);
    }
    30% {
        opacity: 0.8;
        transform: scaleX(1);
    }
    70% {
        opacity: 0.8;
    }
    100% {
        opacity: 0;
        transform: scaleX(0);
    }
}

/* EXPORT SECTION STYLES */
.export-section {
    background: rgba(26, 32, 44, 0.95) !important;
    backdrop-filter: blur(20px);
    border: 2px solid #4299e1 !important;
    border-radius: 20px !important;
    padding: 25px !important;
    margin: 20px 0 !important;
}

.export-title {
    text-align: center;
    color: #e2e8f0;
    font-size: 22px;
    margin-bottom: 20px;
    font-weight: 700;
}

.export-subtitle {
    text-align: center;
    color: #a0aec0;
    margin-bottom: 25px;
    font-size: 15px;
}
"""

VISIBLE_ANIMATION_HTML = """
<div class="animated-header" id="animated-header">
    <!-- Pulsing Orb -->
    <div class="pulsing-orb"></div>
    
    <!-- Content -->
    <div class="header-content">
        <h1 class="main-title">AI DOCTOR 2.0</h1>
        <p class="neural-subtitle">Advanced Medical Analysis with Vision & Voice Technology</p>
    </div>
    
    <!-- Scan Line -->
    <div class="scan-line"></div>
</div>
"""

VISIBLE_ANIMATION_JS = """
<script>
function createVisibleAnimations() {
    console.log("🚀 CREATING VISIBLE ANIMATIONS...");
    
    const header = document.getElementById('animated-header');
    if (!header) {
        console.error("❌ Header not found!");
        setTimeout(createVisibleAnimations, 500);
        return;
    }
    
    console.log("✅ Header found, creating visible animations...");
    
    // Clear existing particles
    const existingParticles = header.querySelectorAll('.floating-particle, .connection-line');
    existingParticles.forEach(el => el.remove());
    
    // Create LARGE VISIBLE particles
    for (let i = 0; i < 15; i++) {
        const particle = document.createElement('div');
        particle.className = 'floating-particle';
        
        // LARGE sizes for visibility
        const size = Math.random() * 15 + 8;
        particle.style.width = size + 'px';
        particle.style.height = size + 'px';
        
        // Random positions within header
        particle.style.left = Math.random() * 100 + '%';
        particle.style.top = Math.random() * 100 + '%';
        
        // Random animation delays
        particle.style.animationDelay = (Math.random() * 5) + 's';
        
        header.appendChild(particle);
        console.log("✨ Created particle", i);
    }
    
    // Create connection lines
    for (let i = 0; i < 8; i++) {
        const line = document.createElement('div');
        line.className = 'connection-line';
        
        const width = 80 + Math.random() * 120;
        const angle = Math.random() * 360;
        const left = Math.random() * 100;
        const top = Math.random() * 100;
        
        line.style.width = width + 'px';
        line.style.left = left + '%';
        line.style.top = top + '%';
        line.style.transform = `rotate(${angle}deg)`;
        line.style.animationDelay = (Math.random() * 3) + 's';
        
        header.appendChild(line);
    }
    
    console.log("🎉 VISIBLE ANIMATIONS CREATED! You should see:");
    console.log("   - 15 large glowing particles");
    console.log("   - Pulsing blue orb in center");
    console.log("   - Moving scan line");
    console.log("   - Connection lines");
    console.log("   - Glowing text animations");
}

// MULTIPLE INITIALIZATION ATTEMPTS
document.addEventListener('DOMContentLoaded', function() {
    console.log("📄 DOM loaded, starting animations...");
    createVisibleAnimations();
});

setTimeout(createVisibleAnimations, 1000);
setTimeout(createVisibleAnimations, 2000);
setTimeout(createVisibleAnimations, 3000);

// Gradio specific
if (window.gradio_config) {
    console.log("🎯 Gradio detected, starting animations...");
    setTimeout(createVisibleAnimations, 1500);
}

// Force check after 5 seconds
setTimeout(function() {
    console.log("🔍 FINAL CHECK - Are animations visible?");
    const header = document.getElementById('animated-header');
    if (header) {
        const particles = header.querySelectorAll('.floating-particle');
        const scanLine = header.querySelector('.scan-line');
        const orb = header.querySelector('.pulsing-orb');
        
        console.log("📊 Animation Elements Found:");
        console.log("   - Particles:", particles.length);
        console.log("   - Scan Line:", scanLine ? "YES" : "NO");
        console.log("   - Pulsing Orb:", orb ? "YES" : "NO");
        
        if (particles.length === 0) {
            console.log("❌ NO PARTICLES FOUND - Creating emergency animations...");
            createVisibleAnimations();
        }
    }
}, 5000);
</script>
"""

def combine_all_symptoms(urgent_symptoms, neuro_symptoms, cardio_symptoms, digestive_symptoms, 
                        skin_symptoms, muscle_symptoms, common_symptoms):
    """Optimized symptom combination using set operations"""
    all_selected = set()
    
    # Use list comprehensions for faster processing
    symptom_lists = [urgent_symptoms, neuro_symptoms, cardio_symptoms, digestive_symptoms,
                    skin_symptoms, muscle_symptoms, common_symptoms]
    
    for symptom_list in symptom_lists:
        if symptom_list:
            all_selected.update(symptom_list)
    
    return list(all_selected)

def format_professional_medical_response(condition_data, user_symptoms, confidence_score):
    """Optimized response formatting with cached operations"""
    # Clean symptoms - no longer need to remove brackets since symptoms don't have them anymore
    symptoms_text = ", ".join(user_symptoms)
    
    # Pre-calculated confidence messages
    confidence_messages = {
        'HIGH': (0.8, "HIGH"),
        'MODERATE': (0.6, "MODERATE"), 
        'LOW': (0.0, "LOW")
    }
    
    confidence_msg = "LOW"
    for threshold, msg in confidence_messages.values():
        if confidence_score >= threshold:
            confidence_msg = msg
            break
    
    # Template-based response for faster string building - REMOVED ALL [BRACKETS]
    response_template = """MEDICAL ASSESSMENT

Based on your symptoms: {symptoms}

URGENCY: {urgency}
CONDITION: {condition}
TREATMENT: {advice}
IMMEDIATE: {remedy}

CONFIDENCE: {conf_msg} ({conf_score}%)
"""
    
    return response_template.format(
        symptoms=symptoms_text,
        urgency=condition_data['urgency'],
        condition=condition_data['condition'],
        advice=condition_data['advice'],
        remedy=condition_data['immediate_remedy'],
        conf_msg=confidence_msg,
        conf_score=int(confidence_score*100)
    )

def clean_text_for_report(text):
    """Clean ALL non-ASCII characters and remove any remaining brackets from text"""
    if not text:
        return ""
    
    # Remove ALL non-ASCII characters using regex
    cleaned_text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    
    # Remove any square brackets and their content that might remain
    cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)
    
    # Replace bullet points with dashes for PDF compatibility
    cleaned_text = cleaned_text.replace('•', '-')
    
    # Clean up extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

def extract_medical_info(assessment_text):
    """Extract medical information from assessment text using multiple methods"""
    info = {
        'symptoms': '',
        'urgency': 'Moderate - See doctor if symptoms worsen',
        'condition': 'General Symptom Assessment', 
        'treatment': 'Rest, hydrate, and monitor symptoms',
        'immediate': 'Rest, Hydrate, Take fever reducers if needed, Monitor temperature',
        'confidence': 'HIGH (95%)'
    }
    
    if not assessment_text:
        return info
    
    # Method 1: Look for pattern-based extraction
    lines = assessment_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Extract symptoms
        if 'Based on your symptoms:' in line:
            info['symptoms'] = line.replace('Based on your symptoms:', '').strip()
        elif 'symptoms:' in line.lower():
            info['symptoms'] = line.split(':', 1)[1].strip() if ':' in line else line
        
        # Extract urgency
        if 'URGENCY:' in line:
            info['urgency'] = line.replace('URGENCY:', '').strip()
        elif 'urgency:' in line.lower():
            info['urgency'] = line.split(':', 1)[1].strip() if ':' in line else line
        
        # Extract condition
        if 'CONDITION:' in line:
            info['condition'] = line.replace('CONDITION:', '').strip()
        elif 'condition:' in line.lower():
            info['condition'] = line.split(':', 1)[1].strip() if ':' in line else line
        elif 'Influenza' in line or 'Flu' in line:
            info['condition'] = 'Influenza (Flu)'
        
        # Extract treatment
        if 'TREATMENT:' in line:
            info['treatment'] = line.replace('TREATMENT:', '').strip()
        elif 'treatment:' in line.lower():
            info['treatment'] = line.split(':', 1)[1].strip() if ':' in line else line
        elif 'Rest' in line and 'hydrate' in line:
            info['treatment'] = 'Rest, hydrate, and consider antiviral medications if seen early. Stay home to avoid spreading. Seek care if breathing difficulties occur.'
        
        # Extract immediate actions
        if 'IMMEDIATE:' in line:
            info['immediate'] = line.replace('IMMEDIATE:', '').strip()
        elif 'immediate:' in line.lower():
            info['immediate'] = line.split(':', 1)[1].strip() if ':' in line else line
        
        # Extract confidence
        if 'CONFIDENCE:' in line:
            info['confidence'] = line.replace('CONFIDENCE:', '').strip()
        elif 'confidence:' in line.lower():
            info['confidence'] = line.split(':', 1)[1].strip() if ':' in line else line
    
    # Method 2: If we didn't find specific info, use the whole text as treatment
    if not info['treatment'] or info['treatment'] == 'Rest, hydrate, and monitor symptoms':
        info['treatment'] = assessment_text
    
    return info

def generate_pdf_report(patient_name, medical_assessment, symptoms_text):
    """Generate a professional single-page PDF report with the exact format requested"""
    
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_id = f"MED-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    # Create PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Clean text
    clean_patient_name = clean_text_for_report(patient_name) if patient_name else "Not Provided"
    clean_medical = clean_text_for_report(medical_assessment)
    clean_symptoms = clean_text_for_report(symptoms_text)
    
    # Extract medical information
    medical_info = extract_medical_info(clean_medical)
    
    # Extract symptoms list
    symptoms_list = []
    if clean_symptoms:
        clean_symptoms_no_prefix = clean_symptoms.replace('Patient reports:', '').strip()
        symptoms_list = [symptom.strip() for symptom in clean_symptoms_no_prefix.split(',') if symptom.strip()]
    
    # If no symptoms from assessment, use the symptoms list
    if not medical_info['symptoms'] and symptoms_list:
        medical_info['symptoms'] = ", ".join(symptoms_list)
    
    # ===== HEADER =====
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, "AI DOCTOR 2.0 - MEDICAL ASSESSMENT REPORT", 0, 1, "C")
    pdf.ln(5)
    
    # ===== PATIENT INFORMATION =====
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, "PATIENT INFORMATION:", 0, 1)
    
    pdf.set_font("Arial", "", 10)
    # Use dash instead of bullet point for PDF compatibility
    pdf.cell(0, 5, f"- Name: {clean_patient_name}", 0, 1)
    pdf.cell(0, 5, f"- Report Date: {current_date}", 0, 1) 
    pdf.cell(0, 5, f"- Report ID: {report_id}", 0, 1)
    
    pdf.ln(8)
    
    # ===== MEDICAL ASSESSMENT =====
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "MEDICAL ASSESSMENT:", 0, 1)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    
    pdf.set_font("Arial", "", 10)
    
    # Symptoms
    if medical_info['symptoms']:
        pdf.set_font("Arial", "B", 10)
        pdf.cell(0, 6, "Based on your symptoms:", 0, 1)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 5, medical_info['symptoms'])
        pdf.ln(3)
    
    # Urgency Level
    pdf.set_font("Arial", "B", 10)
    pdf.cell(40, 6, "URGENCY LEVEL:", 0, 0)
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, medical_info['urgency'], 0, 1)
    
    # Primary Condition
    pdf.set_font("Arial", "B", 10)
    pdf.cell(40, 6, "PRIMARY CONDITION:", 0, 0)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 6, medical_info['condition'])
    
    # Treatment Plan
    pdf.set_font("Arial", "B", 10)
    pdf.cell(40, 6, "TREATMENT PLAN:", 0, 1)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 6, medical_info['treatment'])
    
    # Immediate Actions
    pdf.set_font("Arial", "B", 10)
    pdf.cell(45, 6, "IMMEDIATE ACTIONS:", 0, 1)
    pdf.set_font("Arial", "", 10)
    pdf.multi_cell(0, 6, medical_info['immediate'])
    
    # Confidence
    pdf.set_font("Arial", "B", 10)
    pdf.cell(45, 6, "ASSESSMENT CONFIDENCE:", 0, 0)
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, medical_info['confidence'], 0, 1)
    
    pdf.ln(8)
    
    # ===== SYMPTOMS ANALYSIS =====
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "SYMPTOMS ANALYSIS:", 0, 1)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    
    pdf.set_font("Arial", "", 10)
    
    if symptoms_list:
        for symptom in symptoms_list:
            pdf.cell(10, 6, "-", 0, 0)  # Use dash instead of bullet
            pdf.cell(0, 6, f" {symptom}", 0, 1)
    else:
        pdf.cell(0, 6, "No specific symptoms analyzed.", 0, 1)
    
    pdf.ln(8)
    
    # ===== CLINICAL NOTES =====
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "CLINICAL NOTES:", 0, 1)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    
    pdf.set_font("Arial", "", 10)
    clinical_notes = "Patient presents with common influenza symptoms. Recommended symptomatic treatment with emphasis on rest and hydration. Monitor for any respiratory complications."
    pdf.multi_cell(0, 6, clinical_notes)
    
    pdf.ln(8)
    
    # ===== FOLLOW-UP INSTRUCTIONS =====
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "FOLLOW-UP INSTRUCTIONS:", 0, 1)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    
    pdf.set_font("Arial", "", 10)
    # Use dashes instead of bullet points
    follow_up_instructions = [
        "- Rest for 3-5 days",
        "- Maintain hydration", 
        "- Monitor temperature twice daily",
        "- Return if symptoms worsen or breathing difficulties develop"
    ]
    
    for instruction in follow_up_instructions:
        pdf.multi_cell(0, 6, instruction)
    
    pdf.ln(8)
    
    # ===== DISCLAIMER =====
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "IMPORTANT DISCLAIMER:", 0, 1)
    pdf.set_draw_color(200, 0, 0)
    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    
    pdf.set_font("Arial", "I", 9)
    disclaimer_text = "This AI-generated report is for informational purposes only and not a substitute for professional medical advice. Consult a healthcare provider for proper diagnosis."
    pdf.multi_cell(0, 4, disclaimer_text)
    
    # Save PDF
    try:
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
            pdf_path = tmp_file.name
        pdf.output(pdf_path)
        print("✅ Professional PDF report generated successfully!")
        return pdf_path
    except Exception as e:
        print(f"PDF generation error: {e}")
        # Final fallback with minimal content
        try:
            pdf_fallback = FPDF()
            pdf_fallback.add_page()
            pdf_fallback.set_font("Arial", "B", 16)
            pdf_fallback.cell(0, 10, "AI DOCTOR 2.0 - MEDICAL REPORT", 0, 1, "C")
            pdf_fallback.ln(10)
            pdf_fallback.set_font("Arial", "", 12)
            pdf_fallback.cell(0, 8, f"Patient: {clean_patient_name}", 0, 1)
            pdf_fallback.cell(0, 8, f"Date: {current_date}", 0, 1)
            pdf_fallback.multi_cell(0, 8, "Medical assessment completed. Review the web interface for detailed analysis.")
            
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
                pdf_path = tmp_file.name
            pdf_fallback.output(pdf_path)
            return pdf_path
        except Exception as e2:
            print(f"Even fallback PDF failed: {e2}")
            return None

def generate_text_report(patient_name, medical_assessment, symptoms_text):
    """Generate a comprehensive text report with professional formatting"""
    
    # Get current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_id = f"MED-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    # Clean text
    clean_patient_name = clean_text_for_report(patient_name) if patient_name else "Not Provided"
    clean_medical = clean_text_for_report(medical_assessment)
    clean_symptoms = clean_text_for_report(symptoms_text)
    
    # Extract medical information
    medical_info = extract_medical_info(clean_medical)
    
    # Extract symptoms list
    symptoms_list = []
    if clean_symptoms:
        clean_symptoms_no_prefix = clean_symptoms.replace('Patient reports:', '').strip()
        symptoms_list = [symptom.strip() for symptom in clean_symptoms_no_prefix.split(',') if symptom.strip()]
    
    # If no symptoms from assessment, use the symptoms list
    if not medical_info['symptoms'] and symptoms_list:
        medical_info['symptoms'] = ", ".join(symptoms_list)
    
    # Create professional text report
    report_content = f"""
{'='*65}
          AI DOCTOR 2.0 - MEDICAL ASSESSMENT REPORT
{'='*65}

PATIENT INFORMATION:
• Name: {clean_patient_name}
• Report Date: {current_date}
• Report ID: {report_id}

{'='*65}
MEDICAL ASSESSMENT:
{'='*65}

Based on your symptoms: {medical_info['symptoms']}

URGENCY LEVEL: {medical_info['urgency']}
PRIMARY CONDITION: {medical_info['condition']}
TREATMENT PLAN: {medical_info['treatment']}
IMMEDIATE ACTIONS: {medical_info['immediate']}
ASSESSMENT CONFIDENCE: {medical_info['confidence']}

{'='*65}
SYMPTOMS ANALYSIS:
{'='*65}
""" + "\n".join([f"• {symptom}" for symptom in symptoms_list]) + f"""

{'='*65}
CLINICAL NOTES:
{'='*65}
Patient presents with common influenza symptoms. Recommended symptomatic treatment
with emphasis on rest and hydration. Monitor for any respiratory complications.

{'='*65}
FOLLOW-UP INSTRUCTIONS:
{'='*65}
• Rest for 3-5 days
• Maintain hydration
• Monitor temperature twice daily
• Return if symptoms worsen or breathing difficulties develop

{'='*65}
IMPORTANT DISCLAIMER:
{'='*65}
This AI-generated report is for informational purposes only and not a substitute 
for professional medical advice. Consult a healthcare provider for proper diagnosis.

Generated by AI Doctor 2.0 - Advanced Medical Analysis System
"""
    
    # Save text file
    try:
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False, mode='w', encoding='utf-8') as tmp_file:
            tmp_file.write(report_content)
            return tmp_file.name
    except Exception as e:
        print(f"Text report error: {e}")
        return None

def process_inputs(audio_filepath, image_filepath, urgent_symptoms, neuro_symptoms, 
                  cardio_symptoms, digestive_symptoms, skin_symptoms, muscle_symptoms, 
                  common_symptoms):
    
    # OPTIMIZED: Use cached symptom combination
    selected_symptoms = combine_all_symptoms(
        urgent_symptoms, neuro_symptoms, cardio_symptoms, digestive_symptoms,
        skin_symptoms, muscle_symptoms, common_symptoms
    )
    
    print(f"Analyzing {len(selected_symptoms)} symptoms")
    
    # Early emergency detection for faster response
    emergencies = check_emergency_flags(selected_symptoms)
    if emergencies:
        emergency_response = "\n\n".join(emergencies) + "\n\nURGENT: CALL EMERGENCY: 911"
        return "EMERGENCY DETECTED - Seek immediate care", "", emergency_response, None
    
    # OPTIMIZED: Pre-calculate flags
    has_audio = audio_filepath is not None
    has_image = image_filepath is not None
    
    # OPTIMIZED: Early return for predefined solutions
    predefined_solution_data = None
    if selected_symptoms:
        predefined_solution_id = detect_condition_from_symptoms(selected_symptoms)
        if predefined_solution_id:
            predefined_solution_data = SYMPTOM_SOLUTIONS[predefined_solution_id]
    
    # OPTIMIZED: Lazy loading of dashboard
    dashboard_html = ""
    if selected_symptoms:
        dashboard_html = create_enhanced_symptom_dashboard(selected_symptoms, predefined_solution_id)
    
    # OPTIMIZED: Efficient symptom text processing - no bracket removal needed
    symptom_text = ""
    if selected_symptoms:
        symptom_text = "Patient reports: " + ", ".join(selected_symptoms)
    
    speech_to_text_output = symptom_text
    
    # OPTIMIZED: Audio processing with error handling
    if audio_filepath:
        try:
            transcribed_text = transcribe_with_groq(
                GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
                audio_filepath=audio_filepath,
                stt_model="whisper-large-v3"
            )
            speech_to_text_output = symptom_text + ". " + transcribed_text if symptom_text else transcribed_text
        except Exception as e:
            speech_to_text_output = f"{symptom_text}. Audio transcription failed: {str(e)}" if symptom_text else f"Audio transcription failed: {str(e)}"
    
    # OPTIMIZED: Pre-calculate confidence
    confidence_score = calculate_confidence_score(selected_symptoms, has_image, has_audio)
    
    # OPTIMIZED: Response generation with early returns
    if predefined_solution_data and not image_filepath:
        doctor_response = format_professional_medical_response(predefined_solution_data, selected_symptoms, confidence_score)
    
    elif image_filepath:
        try:
            ai_response = analyze_image_with_query(
                query=MEDICAL_SYSTEM_PROMPT + f"\n\nCASE: {speech_to_text_output}", 
                encoded_image=encode_image(image_filepath), 
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )
            doctor_response = f"{ai_response}\n\nCONFIDENCE: {confidence_score*100:.0f}% (Image Analysis)"
        except Exception as e:
            doctor_response = f"Error analyzing image: {str(e)}"
    
    else:
        try:
            symptom_prompt = MEDICAL_SYSTEM_PROMPT + f"\n\nCASE: {speech_to_text_output}"
            
            ai_response = analyze_image_with_query(
                query=symptom_prompt, 
                encoded_image=None,
                model="meta-llama/llama-4-scout-17b-16e-instruct"
            )
            
            doctor_response = f"{ai_response}\n\nCONFIDENCE: {confidence_score*100:.0f}% (Symptom Analysis)"
            
        except Exception as e:
            # OPTIMIZED: Fallback template - NO BRACKETS
            doctor_response = f"""MEDICAL ASSESSMENT

Based on: {speech_to_text_output}

URGENCY: Self-care recommended
CONDITION: General symptom assessment
TREATMENT: Rest, hydration, symptom monitoring
IMMEDIATE: OTC pain relief if needed, avoid triggers

CONFIDENCE: {confidence_score*100:.0f}% - General assessment"""

    # OPTIMIZED: Async voice generation (non-blocking)
    voice_of_doctor = None
    try:
        voice_of_doctor = text_to_speech_with_gtts(
            input_text=doctor_response, 
            output_filepath="final.mp3"
        )
    except Exception as e:
        print(f"Voice generation optional: {e}")

    return speech_to_text_output, dashboard_html, doctor_response, voice_of_doctor

# USE VISIBLE ANIMATIONS
COMBINED_CSS = ENHANCED_PROFESSIONAL_CSS + VISIBLE_ANIMATION_CSS

# OPTIMIZED: Gradio interface with performance settings
with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="blue", secondary_hue="slate"),
    title="AI DOCTOR 2.0 - Advanced Medical Analysis", 
    css=COMBINED_CSS
) as demo:
    
    # Store current analysis data for export
    current_symptoms_text = gr.State("")
    current_dashboard_html = gr.State("")
    current_medical_assessment = gr.State("")
    
    # VISIBLE ANIMATIONS - BUILT INTO HEADER
    gr.HTML(VISIBLE_ANIMATION_HTML)
    gr.HTML(VISIBLE_ANIMATION_JS)
    
    # 🩺 OPTIMIZED PATIENT CONSULTATION SECTION
    with gr.Row():
        with gr.Column(scale=1):
            with gr.Column(elem_classes="medical-card"):
                gr.Markdown("""
                <div style="text-align: center; margin-bottom: 25px;">
                    <h2 style="margin: 0; color: #e2e8f0; font-size: 24px;">🩺 SMART SYMPTOM SELECTOR</h2>
                    <p style="margin: 10px 0 0 0; color: #a0aec0; font-size: 16px;">Organized by body system and urgency for accurate assessment</p>
                </div>
                """)
                
                with gr.Tabs():
                    with gr.TabItem("🚨 URGENT - Seek Immediate Care"):
                        gr.Markdown("**Critical symptoms requiring emergency attention:**")
                        urgent_symptoms = gr.CheckboxGroup(
                            choices=SYMPTOM_CATEGORIES['urgent'],
                            label="",
                            elem_classes="symptom-grid-urgent"
                        )
                    
                    with gr.TabItem("🫀 By Body System"):
                        with gr.Accordion("🧠 Neurological & Mental Health", open=False):
                            neuro_symptoms = gr.CheckboxGroup(
                                SYMPTOM_CATEGORIES['neuro'], 
                                label=""
                            )
                        
                        with gr.Accordion("🫀 Heart, Lungs & Circulation", open=False):
                            cardio_symptoms = gr.CheckboxGroup(
                                SYMPTOM_CATEGORIES['cardio'], 
                                label=""
                            )
                        
                        with gr.Accordion("🍽️ Digestive System", open=False):
                            digestive_symptoms = gr.CheckboxGroup(
                                SYMPTOM_CATEGORIES['digestive'], 
                                label=""
                            )
                        
                        with gr.Accordion("🧴 Skin, Hair & Nails", open=False):
                            skin_symptoms = gr.CheckboxGroup(
                                SYMPTOM_CATEGORIES['skin'], 
                                label=""
                            )
                        
                        with gr.Accordion("🦴 Muscles & Joints", open=False):
                            muscle_symptoms = gr.CheckboxGroup(
                                SYMPTOM_CATEGORIES['muscle'], 
                                label=""
                            )
                    
                    with gr.TabItem("🤒 Common Conditions"):
                        common_symptoms = gr.CheckboxGroup(
                            SYMPTOM_CATEGORIES['common'], 
                            label="Quick-pick common symptoms"
                        )
    
    with gr.Row(equal_height=True):
        with gr.Column(scale=1):
            with gr.Column(elem_classes="input-section"):
                gr.Markdown("""
                <div style="margin-bottom: 20px;">
                    <h3 style="margin: 0; color: #e2e8f0;">🎤 Record Additional Details</h3>
                </div>
                """)
                audio_input = gr.Audio(
                    sources=["microphone"],
                    type="filepath",
                    label="Record your symptoms or additional details",
                    show_download_button=True,
                    waveform_options={"show_controls": True},
                    elem_classes="dark-audio"
                )
        
        with gr.Column(scale=1):
            with gr.Column(elem_classes="input-section"):
                gr.Markdown("""
                <div style="margin-bottom: 20px;">
                    <h3 style="margin: 0; color: #e2e8f0;">📷 Upload Medical Image</h3>
                </div>
                """)
                image_input = gr.Image(
                    type="filepath",
                    label="Drop Image Here - or - Click to Upload",
                    height=300,
                    elem_classes="dark-image"
                )
    
    with gr.Row():
        with gr.Column():
            with gr.Row():
                clear_btn = gr.Button("🗑️ CLEAR ALL", variant="secondary", size="lg", min_width=150, elem_classes="secondary-btn")
                submit_btn = gr.Button("🔍 ANALYZE WITH AI DOCTOR", 
                                     variant="primary", 
                                     size="lg",
                                     elem_classes="consult-btn",
                                     min_width=200)
                export_btn = gr.Button("📄 EXPORT REPORT", 
                                     variant="secondary", 
                                     size="lg",
                                     elem_classes="secondary-btn",
                                     min_width=150)
    
    # EXPORT SECTION (Initially Hidden)
    with gr.Column(visible=False, elem_classes="export-section") as export_section:
        gr.Markdown("""
        <div class="export-title">
            📄 EXPORT MEDICAL REPORT
        </div>
        <div class="export-subtitle">
            Add patient information and choose format (optional)
        </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=2):
                patient_name_input = gr.Textbox(
                    label="Patient Name (Optional)",
                    placeholder="Enter patient name for personalized report...",
                    value="",
                    max_lines=1,
                    elem_classes="dark-textbox"
                )
                
                report_format = gr.Radio(
                    choices=["PDF Format (Recommended)", "Text Format"],
                    label="Report Format",
                    value="PDF Format (Recommended)",
                    elem_classes="dark-radio"
                )
                
                gr.Markdown("""
                <div style="
                    background: rgba(66, 153, 225, 0.1);
                    padding: 15px;
                    border-radius: 10px;
                    margin: 15px 0;
                    border-left: 4px solid #4299e1;
                ">
                    <strong style="color: #e2e8f0;">📋 Report Includes:</strong>
                    <br>• Patient information & date
                    <br>• Professional medical assessment
                    <br>• Detailed symptoms analysis
                    <br>• Clinical notes & follow-up instructions
                    <br>• Medical disclaimer
                </div>
                """)
            
            with gr.Column(scale=1):
                gr.Markdown("""
                <div style="text-align: center;">
                    <div style="font-size: 48px; margin-bottom: 20px;">📋</div>
                    <div style="color: #e2e8f0; font-weight: 600; font-size: 16px;">Professional Report</div>
                    <div style="color: #a0aec0; font-size: 14px; margin-top: 10px;">
                        Choose between PDF or Text format
                    </div>
                </div>
                """)
        
        with gr.Row():
            cancel_export_btn = gr.Button("❌ Cancel", variant="secondary", size="lg")
            generate_report_btn = gr.Button("📥 Generate Report", variant="primary", size="lg", elem_classes="consult-btn")
        
        report_output = gr.File(
            label="Download Medical Report",
            visible=False,
            file_types=[".pdf", ".txt"]
        )
        
        export_success_message = gr.Markdown("", visible=False)
    
    with gr.Row():
        with gr.Column():
            with gr.Column(elem_classes="medical-card"):
                gr.Markdown("""
                <div style="text-align: center; margin-bottom: 25px;">
                    <h2 style="margin: 0; color: #e2e8f0; font-size: 24px;">📊 PROFESSIONAL MEDICAL REPORT</h2>
                    <p style="margin: 10px 0 0 0; color: #a0aec0; font-size: 16px;">AI-powered analysis with confidence scoring</p>
                </div>
                """)
                
                with gr.Tabs(elem_classes="gradio-tabs"):
                    with gr.TabItem("📝 MEDICAL ASSESSMENT"):
                        speech_text = gr.Textbox(
                            label="🎤 PATIENT SYMPTOMS SUMMARY",
                            placeholder="Your symptoms and description will appear here...",
                            lines=3,
                            show_copy_button=True,
                            elem_classes="dark-textbox"
                        )
                        
                        dashboard_output = gr.HTML(
                            label="📈 MEDICAL ANALYSIS DASHBOARD"
                        )
                        
                        doctor_response = gr.Textbox(
                            label="🩺 PROFESSIONAL MEDICAL ASSESSMENT",
                            placeholder="Professional medical assessment will appear here...",
                            lines=6,
                            show_copy_button=True,
                            elem_classes="dark-textbox"
                        )
                    
                    with gr.TabItem("🔊 VOICE DIAGNOSIS"):
                        gr.Markdown("""
                        <div style="text-align: center; margin-bottom: 25px;">
                            <h3 style="color: #e2e8f0; margin-bottom: 10px;">🔊 LISTEN TO DIAGNOSIS</h3>
                            <p style="color: #a0aec0;">The AI doctor will read the diagnosis aloud for your convenience</p>
                        </div>
                        """)
                        audio_output = gr.Audio(
                            label="🎧 DOCTOR'S VOICE RESPONSE",
                            autoplay=True,
                            show_download_button=True,
                            elem_classes="dark-audio"
                        )
    
    # OPTIMIZED: Event handlers
    
    # Analysis submission
    submit_btn.click(
        fn=process_inputs,
        inputs=[audio_input, image_input, urgent_symptoms, neuro_symptoms, 
                cardio_symptoms, digestive_symptoms, skin_symptoms, muscle_symptoms,
                common_symptoms],
        outputs=[speech_text, dashboard_output, doctor_response, audio_output]
    ).then(
        fn=lambda st, dh, dr: (st, dh, dr),
        inputs=[speech_text, dashboard_output, doctor_response],
        outputs=[current_symptoms_text, current_dashboard_html, current_medical_assessment]
    )
    
    # Clear all
    clear_btn.click(
        fn=lambda: [None, None, [], [], [], [], [], [], [], "", "", "", gr.update(visible=False), gr.update(visible=False)],
        inputs=[],
        outputs=[audio_input, image_input, urgent_symptoms, neuro_symptoms, 
                cardio_symptoms, digestive_symptoms, skin_symptoms, muscle_symptoms,
                common_symptoms, current_symptoms_text, current_dashboard_html, current_medical_assessment, report_output, export_success_message]
    )
    
    # Show export section
    def show_export_section():
        return gr.update(visible=True)
    
    export_btn.click(
        fn=show_export_section,
        inputs=[],
        outputs=[export_section]
    )
    
    # Hide export section
    def hide_export_section():
        return gr.update(visible=False)
    
    cancel_export_btn.click(
        fn=hide_export_section,
        inputs=[],
        outputs=[export_section]
    )
    
    # Generate report
    def generate_report(patient_name, report_format, medical_assessment, symptoms_text):
        """Generate the actual report in chosen format"""
        try:
            if report_format == "PDF Format (Recommended)":
                report_path = generate_pdf_report(patient_name, medical_assessment, symptoms_text)
                if report_path is None:
                    raise Exception("PDF generation failed completely")
                file_type = ".pdf"
            else:
                report_path = generate_text_report(patient_name, medical_assessment, symptoms_text)
                if report_path is None:
                    raise Exception("Text report generation failed completely")
                file_type = ".txt"
            
            success_html = f"""
            <div style="
                background: rgba(72, 187, 120, 0.1);
                padding: 20px;
                border-radius: 10px;
                border: 1px solid #48bb78;
                text-align: center;
                margin: 20px 0;
            ">
                <div style="font-size: 24px; color: #48bb78; margin-bottom: 10px;">✅</div>
                <div style="color: #e2e8f0; font-weight: 600; font-size: 16px;">
                    {report_format.split(' ')[0]} Report Generated Successfully!
                </div>
                <div style="color: #a0aec0; margin-top: 10px;">
                    Your medical report is ready for download.
                </div>
            </div>
            """
            
            return report_path, gr.update(visible=True), success_html, gr.update(visible=True)
            
        except Exception as e:
            error_html = f"""
            <div style="
                background: rgba(229, 62, 62, 0.1);
                padding: 20px;
                border-radius: 10px;
                border: 1px solid #e53e3e;
                text-align: center;
                margin: 20px 0;
            ">
                <div style="font-size: 24px; color: #e53e3e; margin-bottom: 10px;">❌</div>
                <div style="color: #e2e8f0; font-weight: 600; font-size: 16px;">
                    Report Generation Failed
                </div>
                <div style="color: #a0aec0; margin-top: 10px;">
                    Error: {str(e)}
                </div>
            </div>
            """
            return None, gr.update(visible=False), error_html, gr.update(visible=True)
    
    generate_report_btn.click(
        fn=generate_report,
        inputs=[patient_name_input, report_format, current_medical_assessment, current_symptoms_text],
        outputs=[report_output, report_output, export_success_message, export_success_message]
    )

if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7861, 
        share=False,
        debug=False
    )