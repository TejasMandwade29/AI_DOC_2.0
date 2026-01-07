# dashboard.py - OPTIMIZED BODY SYSTEM IMPACT SECTION

def create_enhanced_symptom_dashboard(selected_symptoms, matched_condition=None):
    """Create advanced visual analysis with AI insights and recovery tracking"""
    if not selected_symptoms:
        return """
        <div style='
            background: linear-gradient(135deg, #1a1f36 0%, #2d3748 100%);
            color: #e2e8f0;
            padding: 40px;
            border-radius: 16px;
            margin: 15px 0;
            text-align: center;
            border: 1px solid #4a5568;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        '>
            <div style='font-size: 48px; margin-bottom: 20px;'>📊</div>
            <h3 style='color: #e2e8f0; margin-bottom: 10px;'>Medical Analysis Dashboard</h3>
            <p style='color: #a0aec0;'>Select symptoms to begin analysis and see immediate remedies</p>
        </div>
        """
    
    # Severity scale function
    def get_severity_label(percentage):
        if percentage <= 30:
            return "🟢 Mild", "#48bb78", "Minor impact"
        elif percentage <= 60:
            return "🟡 Moderate", "#ed8936", "Noticeable but manageable"
        elif percentage <= 80:
            return "🟠 Significant", "#dd6b20", "Substantial impact"
        else:
            return "🔴 Severe", "#e53e3e", "Major health concern"
    
    # Symptom severity mapping
    def get_symptom_severity(symptom):
        """Determine severity level based on symptom type"""
        symptom_lower = symptom.lower()
        
        # Critical symptoms (red)
        critical_keywords = ["chest pain", "difficulty breathing", "severe bleeding", 
                           "sudden weakness", "suicidal thoughts", "seizure", 
                           "severe head injury", "paralysis", "numbness"]
        if any(keyword in symptom_lower for keyword in critical_keywords):
            return {"level": "critical", "percentage": 90, "color": "#e53e3e", "emoji": "🔴"}
        
        # Moderate symptoms (orange)
        moderate_keywords = ["fever", "high pain", "head injury", "vision problems", 
                           "heart palpitations", "shortness of breath", "fainting",
                           "vomiting", "severe headache", "burning sensation"]
        if any(keyword in symptom_lower for keyword in moderate_keywords):
            return {"level": "moderate", "percentage": 60, "color": "#ed8936", "emoji": "🟡"}
        
        # Mild symptoms (green)
        mild_keywords = ["cough", "runny nose", "sneezing", "mild headache", "fatigue",
                        "allergies", "itching", "dry skin", "congestion"]
        if any(keyword in symptom_lower for keyword in mild_keywords):
            return {"level": "mild", "percentage": 30, "color": "#48bb78", "emoji": "🟢"}
        
        # Default to moderate
        return {"level": "moderate", "percentage": 50, "color": "#ed8936", "emoji": "🟡"}
    
    def create_progress_bar(percentage, color, width=200):
        filled_width = (percentage / 100) * width
        return f"""
        <div style="
            width: {width}px; 
            height: 12px; 
            background: #4a5568; 
            border-radius: 10px; 
            overflow: hidden;
            display: inline-block;
            margin: 0 10px;
            vertical-align: middle;
        ">
            <div style="
                width: {filled_width}px;
                height: 100%;
                background: {color};
                border-radius: 10px;
                transition: all 0.3s ease;
                box-shadow: 0 0 10px {color}80;
            "></div>
        </div>
        """
    
    def create_compact_progress_bar(percentage, color, width=120):
        filled_width = (percentage / 100) * width
        return f"""
        <div style="
            width: {width}px; 
            height: 8px; 
            background: #4a5568; 
            border-radius: 4px; 
            overflow: hidden;
            display: inline-block;
            margin: 0 6px;
            vertical-align: middle;
        ">
            <div style="
                width: {filled_width}px;
                height: 100%;
                background: {color};
                border-radius: 4px;
            "></div>
        </div>
        """
    
    # Symptom Priority Analysis
    def analyze_symptom_priority(symptom_data):
        """Analyze and prioritize symptoms by severity and urgency"""
        priority_list = []
        
        for data in symptom_data:
            symptom = data["clean"]
            severity = data["severity"]
            
            # Assign priority level based on severity
            if severity["level"] == "critical":
                priority_level = 1
                priority_color = "#e53e3e"
                priority_emoji = "🔴"
                action_guide = "Address immediately"
                details = "This symptom requires urgent attention and may indicate serious health risks"
            elif severity["level"] == "moderate":
                priority_level = 2
                priority_color = "#ed8936"
                priority_emoji = "🟡"
                action_guide = "Monitor closely"
                details = "This symptom needs proper management to prevent complications"
            else:  # mild
                priority_level = 3
                priority_color = "#48bb78"
                priority_emoji = "🟢"
                action_guide = "Self-care"
                details = "This symptom can be managed with self-care and should improve naturally"
            
            priority_list.append({
                "symptom": symptom,
                "priority_level": priority_level,
                "priority_color": priority_color,
                "priority_emoji": priority_emoji,
                "action_guide": action_guide,
                "details": details,
                "severity_percentage": severity["percentage"]
            })
        
        # Sort by priority level (1 = highest priority)
        priority_list.sort(key=lambda x: x["priority_level"])
        return priority_list
    
    # AI Insights Generator
    def generate_ai_insights(symptom_data, matched_condition):
        """Generate intelligent insights based on symptom patterns"""
        insights = []
        
        # Get clean symptom names for analysis
        clean_symptoms = [data["clean"].lower() for data in symptom_data]
        symptom_text = " ".join(clean_symptoms)
        
        # Pattern 1: Respiratory symptoms
        respiratory_keywords = ["cough", "cold", "runny nose", "congestion", "sneezing", "sore throat"]
        respiratory_count = sum(1 for keyword in respiratory_keywords if keyword in symptom_text)
        
        if respiratory_count >= 2:
            insights.append({
                "emoji": "🫁",
                "title": "Upper Respiratory Pattern Detected",
                "description": "Your symptoms suggest a common cold or viral URI. Focus on respiratory care.",
                "tip": "Steam inhalation can reduce congestion by 60%"
            })
        
        # Pattern 2: Fever + Body aches
        if "fever" in symptom_text and any(symptom in symptom_text for symptom in ["body aches", "fatigue", "chills"]):
            insights.append({
                "emoji": "🌡️",
                "title": "Systemic Infection Pattern",
                "description": "Fever with body aches suggests your immune system is actively fighting infection.",
                "tip": "Rest is crucial - your body needs energy to fight the infection"
            })
        
        # Pattern 3: Headache patterns
        headache_keywords = ["headache", "migraine", "sensitivity to light"]
        if any(keyword in symptom_text for keyword in headache_keywords):
            insights.append({
                "emoji": "🧠",
                "title": "Neurological Symptom Pattern",
                "description": "Headache symptoms respond well to hydration and rest in a quiet environment.",
                "tip": "Avoid screen time and bright lights to reduce headache intensity"
            })
        
        # Pattern 4: Digestive issues
        digestive_keywords = ["nausea", "vomiting", "diarrhea", "stomach pain"]
        if any(keyword in symptom_text for keyword in digestive_keywords):
            insights.append({
                "emoji": "🍽️",
                "title": "Gastrointestinal Pattern",
                "description": "Digestive symptoms require careful hydration and bland diet management.",
                "tip": "Sip clear fluids slowly rather than drinking large amounts at once"
            })
        
        # Default insight if no specific patterns
        if not insights:
            insights.append({
                "emoji": "🔍",
                "title": "General Symptom Management",
                "description": "Your symptoms are being monitored. Consistent self-care will support recovery.",
                "tip": "Track symptom changes daily to identify improvement patterns"
            })
        
        return insights
    
    # Recovery Timeline Generator
    def generate_recovery_timeline(symptom_data, matched_condition):
        """Generate visual recovery timeline based on symptoms"""
        
        # Calculate overall severity score
        total_severity = sum(data["severity"]["percentage"] for data in symptom_data)
        avg_severity = total_severity / len(symptom_data)
        
        # Determine recovery days based on severity
        if avg_severity >= 70:  # High severity
            recovery_days = 7
            timeline = [
                {"day": "Today", "status": "Peak Symptoms", "percentage": 100, "description": "Maximum symptom intensity"},
                {"day": "Day 2-3", "status": "Gradual Improvement", "percentage": 70, "description": "Symptoms begin to decrease"},
                {"day": "Day 4-5", "status": "Significant Relief", "percentage": 40, "description": "Major improvement visible"},
                {"day": "Day 6-7", "status": "Near Recovery", "percentage": 10, "description": "Minimal symptoms remain"}
            ]
        elif avg_severity >= 40:  # Medium severity
            recovery_days = 5
            timeline = [
                {"day": "Today", "status": "Active Symptoms", "percentage": 80, "description": "Symptoms are prominent"},
                {"day": "Day 2-3", "status": "Steady Improvement", "percentage": 50, "description": "Noticeable reduction in symptoms"},
                {"day": "Day 4-5", "status": "Mostly Recovered", "percentage": 15, "description": "Symptoms largely resolved"}
            ]
        else:  # Low severity
            recovery_days = 3
            timeline = [
                {"day": "Today", "status": "Mild Symptoms", "percentage": 60, "description": "Manageable symptom level"},
                {"day": "Day 2", "status": "Rapid Improvement", "percentage": 25, "description": "Quick recovery progression"},
                {"day": "Day 3", "status": "Full Recovery", "percentage": 5, "description": "Back to normal health"}
            ]
        
        return {
            "recovery_days": recovery_days,
            "timeline": timeline,
            "avg_severity": avg_severity
        }
    
    # Process symptoms with severity data
    symptom_data = []
    for symptom in selected_symptoms:
        # Clean symptom name (remove emoji)
        if ' ' in symptom and any(symptom.startswith(emoji) for emoji in ["🔴", "🟡", "🟢"]):
            clean_name = symptom.split(' ', 1)[1]
        else:
            clean_name = symptom
        
        severity_info = get_symptom_severity(clean_name)
        symptom_data.append({
            "original": symptom,
            "clean": clean_name,
            "severity": severity_info
        })
    
    # Generate AI Insights
    ai_insights = generate_ai_insights(symptom_data, matched_condition)
    
    # Generate Recovery Timeline
    recovery_data = generate_recovery_timeline(symptom_data, matched_condition)
    
    # Generate Symptom Priority
    symptom_priority = analyze_symptom_priority(symptom_data)
    
    # 🆕 UPDATED: Horizontal Bar Chart for Symptom Severity
    symptom_chart_html = ""
    for data in symptom_data:
        bar_width = data["severity"]["percentage"]
        symptom_chart_html += f"""
        <div style="display: flex; align-items: center; margin: 15px 0; gap: 15px;">
            <div style="min-width: 140px; display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 18px;">{data["severity"]["emoji"]}</span>
                <span style="color: #e2e8f0; font-weight: 600; font-size: 14px;">{data["clean"]}</span>
            </div>
            <div style="flex: 1; display: flex; align-items: center; gap: 15px;">
                <div style="width: 100%; height: 24px; background: #2d3748; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid #4a5568;">
                    <div style="width: {bar_width}%; height: 100%; background: linear-gradient(90deg, {data["severity"]["color"]}, {data["severity"]["color"]}cc); border-radius: 12px; transition: all 0.3s ease; box-shadow: 0 2px 8px {data["severity"]["color"]}40;"></div>
                    <div style="position: absolute; right: 10px; top: 50%; transform: translateY(-50%); color: white; font-weight: 700; font-size: 12px; text-shadow: 0 1px 2px rgba(0,0,0,0.5);">{data["severity"]["percentage"]}%</div>
                </div>
            </div>
        </div>
        """
    
    # 🆕 NEW: Color Disclaimer for Symptom Severity
    severity_disclaimer = """
    <div style="
        background: rgba(45, 55, 72, 0.6);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        border: 1px solid #4a5568;
    ">
        <div style="color: #e2e8f0; font-weight: 600; font-size: 14px; margin-bottom: 12px; text-align: center;">
            🎨 SEVERITY COLOR GUIDE
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; font-size: 12px;">
            <div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 10px; background: rgba(72, 187, 120, 0.1); border-radius: 8px; border: 1px solid #48bb7840;">
                <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 5px;">
                    <span style="color: #48bb78; font-size: 16px;">🟢</span>
                    <span style="color: #e2e8f0; font-weight: 600;">Mild</span>
                </div>
                <div style="color: #a0aec0; font-size: 11px; line-height: 1.3;">0-30% • Minor impact</div>
            </div>
            
            <div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 10px; background: rgba(237, 137, 54, 0.1); border-radius: 8px; border: 1px solid #ed893640;">
                <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 5px;">
                    <span style="color: #ed8936; font-size: 16px;">🟡</span>
                    <span style="color: #e2e8f0; font-weight: 600;">Moderate</span>
                </div>
                <div style="color: #a0aec0; font-size: 11px; line-height: 1.3;">31-60% • Noticeable impact</div>
            </div>
            
            <div style="display: flex; flex-direction: column; align-items: center; text-align: center; padding: 10px; background: rgba(229, 62, 62, 0.1); border-radius: 8px; border: 1px solid #e53e3e40;">
                <div style="display: flex; align-items: center; gap: 6px; margin-bottom: 5px;">
                    <span style="color: #e53e3e; font-size: 16px;">🔴</span>
                    <span style="color: #e2e8f0; font-weight: 600;">Critical</span>
                </div>
                <div style="color: #a0aec0; font-size: 11px; line-height: 1.3;">61-100% • Major concern</div>
            </div>
        </div>
        <div style="text-align: center; color: #718096; font-size: 11px; margin-top: 10px; font-style: italic;">
            Based on general medical guidelines and symptom characteristics
        </div>
    </div>
    """
    
    # Body system impact analysis WITH SEVERITY LABELS
    body_systems = {
        "🧠 Neurological": 0,
        "🫀 Cardiovascular": 0, 
        "🍽️ Digestive": 0,
        "🧴 Skin": 0,
        "🦴 Musculoskeletal": 0,
        "🤒 General": 0
    }
    
    # Map symptoms to body systems
    for data in symptom_data:
        symptom_lower = data["clean"].lower()
        
        if any(keyword in symptom_lower for keyword in ["headache", "dizziness", "confusion", "memory", "anxiety", "depression", "vision", "hearing"]):
            body_systems["🧠 Neurological"] += data["severity"]["percentage"]
        elif any(keyword in symptom_lower for keyword in ["chest", "heart", "breathing", "palpitations", "blood pressure", "irregular heartbeat"]):
            body_systems["🫀 Cardiovascular"] += data["severity"]["percentage"]
        elif any(keyword in symptom_lower for keyword in ["nausea", "vomiting", "diarrhea", "constipation", "stomach", "appetite", "bloating"]):
            body_systems["🍽️ Digestive"] += data["severity"]["percentage"]
        elif any(keyword in symptom_lower for keyword in ["rash", "itching", "redness", "swelling", "acne", "dry skin", "hair loss"]):
            body_systems["🧴 Skin"] += data["severity"]["percentage"]
        elif any(keyword in symptom_lower for keyword in ["muscle", "joint", "back", "neck", "stiffness", "swelling", "movement"]):
            body_systems["🦴 Musculoskeletal"] += data["severity"]["percentage"]
        else:
            body_systems["🤒 General"] += data["severity"]["percentage"]
    
    # 🆕 OPTIMIZED: Create body system impact visualization with consistent styling
    body_system_html = ""
    for system, score in body_systems.items():
        if score > 0:
            # Normalize score to percentage (max 300% possible across all systems)
            normalized_score = min(100, (score / 300) * 100)
            severity_label, severity_color, severity_description = get_severity_label(normalized_score)
            
            body_system_html += f"""
            <div style="
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 15px;
                margin: 10px 0;
                background: rgba(45, 55, 72, 0.6);
                border-radius: 10px;
                border-left: 4px solid {severity_color};
            ">
                <div style="display: flex; align-items: center; gap: 12px; min-width: 140px;">
                    <span style="color: #e2e8f0; font-weight: 600; font-size: 14px;">{system}</span>
                </div>
                
                <div style="display: flex; align-items: center; gap: 15px; flex: 1;">
                    <div style="width: 100%; height: 20px; background: #2d3748; border-radius: 10px; overflow: hidden; position: relative; border: 1px solid #4a5568;">
                        <div style="width: {normalized_score}%; height: 100%; background: linear-gradient(90deg, {severity_color}, {severity_color}cc); border-radius: 10px; transition: all 0.3s ease; box-shadow: 0 2px 6px {severity_color}40;"></div>
                        <div style="position: absolute; right: 10px; top: 50%; transform: translateY(-50%); color: white; font-weight: 700; font-size: 11px; text-shadow: 0 1px 2px rgba(0,0,0,0.5);">{int(normalized_score)}%</div>
                    </div>
                </div>
                
                <div style="
                    background: {severity_color}15;
                    color: {severity_color};
                    padding: 6px 12px;
                    border-radius: 12px;
                    font-size: 12px;
                    font-weight: 600;
                    border: 1px solid {severity_color}30;
                    min-width: 100px;
                    text-align: center;
                ">
                    {severity_label}
                </div>
            </div>
            """
    
    # Handle empty body system HTML
    body_system_display = body_system_html
    if not body_system_display.strip():
        body_system_display = """
            <div style="text-align: center; color: #a0aec0; padding: 30px; font-size: 14px;">
                No specific body system impact detected
            </div>
        """
    
    # 🆕 OPTIMIZED: Severity Scale Legend with consistent styling
    severity_legend = """
    <div style="
        background: rgba(45, 55, 72, 0.6);
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
        border: 1px solid #4a5568;
    ">
        <div style="color: #e2e8f0; font-weight: 600; font-size: 14px; margin-bottom: 15px; text-align: center;">
            📊 SEVERITY SCALE GUIDE
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; font-size: 13px;">
            <div style="display: flex; align-items: center; gap: 10px; padding: 8px; background: rgba(72, 187, 120, 0.1); border-radius: 8px;">
                <span style="color: #48bb78; font-size: 18px;">🟢</span>
                <div>
                    <div style="color: #e2e8f0; font-weight: 600;">Mild (0-30%)</div>
                    <div style="color: #a0aec0; font-size: 12px;">Minor impact</div>
                </div>
            </div>
            
            <div style="display: flex; align-items: center; gap: 10px; padding: 8px; background: rgba(237, 137, 54, 0.1); border-radius: 8px;">
                <span style="color: #ed8936; font-size: 18px;">🟡</span>
                <div>
                    <div style="color: #e2e8f0; font-weight: 600;">Moderate (31-60%)</div>
                    <div style="color: #a0aec0; font-size: 12px;">Noticeable but manageable</div>
                </div>
            </div>
            
            <div style="display: flex; align-items: center; gap: 10px; padding: 8px; background: rgba(221, 107, 32, 0.1); border-radius: 8px;">
                <span style="color: #dd6b20; font-size: 18px;">🟠</span>
                <div>
                    <div style="color: #e2e8f0; font-weight: 600;">Significant (61-80%)</div>
                    <div style="color: #a0aec0; font-size: 12px;">Substantial impact</div>
                </div>
            </div>
            
            <div style="display: flex; align-items: center; gap: 10px; padding: 8px; background: rgba(229, 62, 62, 0.1); border-radius: 8px;">
                <span style="color: #e53e3e; font-size: 18px;">🔴</span>
                <div>
                    <div style="color: #e2e8f0; font-weight: 600;">Severe (81-100%)</div>
                    <div style="color: #a0aec0; font-size: 12px;">Major health concern</div>
                </div>
            </div>
        </div>
    </div>
    """

    # Create AI Insights HTML
    ai_insights_html = ""
    for insight in ai_insights:
        ai_insights_html += f"""
        <div style="
            background: rgba(66, 153, 225, 0.1);
            padding: 18px;
            border-radius: 12px;
            margin-bottom: 15px;
            border: 1px solid #4299e1;
            border-left: 5px solid #4299e1;
        ">
            <div style="display: flex; align-items: flex-start; gap: 15px;">
                <div style="font-size: 22px; margin-top: 2px;">{insight['emoji']}</div>
                <div style="flex: 1;">
                    <div style="font-weight: 700; color: #90cdf4; font-size: 16px; margin-bottom: 8px;">
                        {insight['title']}
                    </div>
                    <div style="color: #cbd5e0; font-size: 14px; line-height: 1.5; margin-bottom: 10px;">
                        {insight['description']}
                    </div>
                    <div style="
                        background: rgba(66, 153, 225, 0.2);
                        padding: 8px 12px;
                        border-radius: 8px;
                        font-size: 13px;
                        color: #90cdf4;
                        border-left: 3px solid #90cdf4;
                    ">
                        💡 {insight['tip']}
                    </div>
                </div>
            </div>
        </div>
        """
    
    # Create Recovery Timeline HTML
    recovery_timeline_html = ""
    for phase in recovery_data["timeline"]:
        recovery_timeline_html += f"""
        <div style="display: flex; align-items: center; margin: 15px 0; gap: 15px;">
            <div style="
                background: rgba(72, 187, 120, 0.2);
                padding: 8px 12px;
                border-radius: 8px;
                min-width: 70px;
                text-align: center;
                border: 1px solid #48bb78;
                color: #68d391;
                font-weight: 600;
                font-size: 13px;
            ">{phase['day']}</div>
            <div style="flex: 1;">
                <div style="color: #e2e8f0; font-weight: 600; font-size: 14px; margin-bottom: 5px;">
                    {phase['status']}
                </div>
                <div style="color: #a0aec0; font-size: 13px;">
                    {phase['description']}
                </div>
            </div>
            <div style="
                background: rgba(66, 153, 225, 0.2);
                padding: 6px 12px;
                border-radius: 20px;
                font-size: 12px;
                color: #90cdf4;
                border: 1px solid #4299e1;
                min-width: 50px;
                text-align: center;
            ">{phase['percentage']}%</div>
        </div>
        """
    
    # COMPACT Symptom Priority HTML
    symptom_priority_html = ""
    if symptom_priority:
        for i, item in enumerate(symptom_priority, 1):
            progress_bar = create_compact_progress_bar(item['severity_percentage'], item['priority_color'], 100)
            
            symptom_priority_html += f"""
            <div style="
                background: rgba(45, 55, 72, 0.6);
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 10px;
                border-left: 4px solid {item['priority_color']};
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 10px;
            ">
                <div style="display: flex; align-items: center; gap: 8px; min-width: 120px;">
                    <div style="
                        background: {item['priority_color']}20;
                        color: {item['priority_color']};
                        padding: 4px 8px;
                        border-radius: 6px;
                        font-weight: 700;
                        font-size: 12px;
                        border: 1px solid {item['priority_color']}40;
                    ">{i}</div>
                    <div style="display: flex; align-items: center; gap: 6px;">
                        <span style="font-size: 16px;">{item['priority_emoji']}</span>
                        <span style="color: #e2e8f0; font-weight: 600; font-size: 14px;">{item['symptom']}</span>
                    </div>
                </div>
                
                <div style="display: flex; align-items: center; gap: 10px; flex: 1;">
                    {progress_bar}
                    <span style="color: #a0aec0; font-size: 12px; min-width: 30px; text-align: center;">
                        {item['severity_percentage']}%
                    </span>
                </div>
                
                <div style="
                    background: {item['priority_color']}15;
                    color: {item['priority_color']};
                    padding: 4px 8px;
                    border-radius: 12px;
                    font-size: 11px;
                    font-weight: 600;
                    border: 1px solid {item['priority_color']}30;
                    min-width: 100px;
                    text-align: center;
                ">
                    {item['action_guide']}
                </div>
            </div>
            """
    else:
        symptom_priority_html = """
            <div style="text-align: center; color: #a0aec0; padding: 30px; font-size: 14px;">
                No symptoms to prioritize
            </div>
        """

    # Risk assessment logic
    critical_symptoms = ["chest pain", "difficulty breathing", "severe bleeding", "sudden weakness", "suicidal thoughts", "seizure", "severe head injury", "paralysis/numbness"]
    moderate_symptoms = ["fever", "high pain", "head injury", "vision problems", "heart palpitations", "shortness of breath", "fainting"]
    
    clean_selected_symptoms = []
    for symptom in selected_symptoms:
        if ' ' in symptom and any(symptom.startswith(emoji) for emoji in ["🔴", "🟡", "🟢"]):
            clean_selected_symptoms.append(symptom.split(' ', 1)[1].lower())
        else:
            clean_selected_symptoms.append(symptom.lower())
    
    symptom_text = " ".join(clean_selected_symptoms)
    
    critical_count = sum(1 for symptom in critical_symptoms if symptom in symptom_text)
    moderate_count = sum(1 for symptom in moderate_symptoms if symptom in symptom_text)
    mild_count = len(selected_symptoms) - critical_count - moderate_count
    
    # Determine risk level
    if critical_count > 0:
        risk_level = "HIGH"
        risk_description = "Potential emergency - seek immediate care"
        risk_color = "#e53e3e"
        risk_emoji = "🚨"
        risk_icon = "⚠️"
        risk_gradient = "linear-gradient(135deg, #742a2a 0%, #c53030 100%)"
    elif moderate_count >= 2:
        risk_level = "MODERATE" 
        risk_description = "Consult healthcare provider soon"
        risk_color = "#dd6b20"
        risk_emoji = "🟡"
        risk_icon = "📋"
        risk_gradient = "linear-gradient(135deg, #744210 0%, #ed8936 100%)"
    else:
        risk_level = "LOW"
        risk_description = "Self-care may be appropriate"
        risk_color = "#38a169"
        risk_emoji = "🟢"
        risk_icon = "💚"
        risk_gradient = "linear-gradient(135deg, #22543d 0%, #48bb78 100%)"
    
    # Get immediate remedy
    immediate_remedy = ""
    if matched_condition:
        from symptom_database import SYMPTOM_SOLUTIONS
        if matched_condition in SYMPTOM_SOLUTIONS:
            immediate_remedy = SYMPTOM_SOLUTIONS[matched_condition].get("immediate_remedy", "")
    
    if not immediate_remedy and selected_symptoms:
        immediate_remedy = "💧 Stay hydrated • 🛌 Get plenty of rest • 🌡️ Monitor your symptoms • 📞 Contact doctor if symptoms worsen"

    # 🆕 STANDARDIZED SECTION STYLES
    section_style = """
        background: rgba(45, 55, 72, 0.8);
        padding: 25px;
        border-radius: 16px;
        margin-bottom: 25px;
        border: 1px solid #4a5568;
        backdrop-filter: blur(10px);
    """

    heading_style = """
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 20px;
    """

    heading_text_style = """
        font-weight: 700;
        color: #e2e8f0;
        font-size: 18px;
    """

    # COMPLETE ENHANCED DASHBOARD HTML WITH OPTIMIZED BODY SYSTEM SECTION
    dashboard_html = f"""
    <div style="
        background: linear-gradient(135deg, #1a1f36 0%, #2d3748 100%);
        color: white;
        padding: 30px;
        border-radius: 20px;
        margin: 20px 0;
        border: 1px solid #4a5568;
        box-shadow: 0 12px 40px rgba(0,0,0,0.4);
        font-family: 'Inter', sans-serif;
    ">
        <!-- Header -->
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 25px; padding-bottom: 20px; border-bottom: 1px solid #4a5568;">
            <div style="display: flex; align-items: center; gap: 15px;">
                <div style="
                    background: linear-gradient(135deg, #4299e1, #3182ce);
                    padding: 12px;
                    border-radius: 12px;
                    font-size: 24px;
                ">🤖</div>
                <div>
                    <h2 style="margin: 0; font-size: 22px; font-weight: 700; color: #e2e8f0;">AI-POWERED MEDICAL DASHBOARD</h2>
                    <p style="margin: 5px 0 0 0; color: #a0aec0; font-size: 14px;">Intelligent symptom analysis with predictive recovery insights</p>
                </div>
            </div>
            <div style="
                background: rgba(66, 153, 225, 0.2);
                padding: 8px 16px;
                border-radius: 20px;
                font-size: 14px;
                border: 1px solid #4299e1;
                color: #90cdf4;
            ">
                {len(selected_symptoms)} Symptoms Analyzed
            </div>
        </div>
        
        <!-- 1. RISK LEVEL CARD (Urgency First) -->
        <div style="
            background: {risk_gradient};
            padding: 25px;
            border-radius: 16px;
            margin-bottom: 25px;
            border: 1px solid {risk_color};
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        ">
            <div style="display: flex; align-items: center; gap: 20px;">
                <div style="font-size: 42px; filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));">{risk_icon}</div>
                <div style="flex: 1;">
                    <div style="font-size: 24px; font-weight: 800; margin-bottom: 8px; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                        {risk_emoji} {risk_level} RISK LEVEL
                    </div>
                    <div style="font-size: 16px; opacity: 0.95; font-weight: 500;">{risk_description}</div>
                </div>
            </div>
        </div>

        <!-- 2. SYMPTOM SEVERITY GRAPH (See Data First) -->
        <div style="{section_style}">
            <div style="{heading_style}">
                <div style="font-size: 20px;">📊</div>
                <div style="{heading_text_style}">SYMPTOM SEVERITY GRAPH</div>
            </div>
            {symptom_chart_html}
            {severity_disclaimer}
        </div>

        <!-- 3. SYMPTOM PRIORITY (Know What to Address) -->
        <div style="{section_style}">
            <div style="{heading_style}">
                <div style="font-size: 20px;">🎯</div>
                <div style="{heading_text_style}">SYMPTOM PRIORITY</div>
            </div>
            <div style="color: #a0aec0; font-size: 14px; margin-bottom: 20px; line-height: 1.5;">
                Symptoms are prioritized by severity and urgency. Address higher priority items first for optimal recovery.
            </div>
            {symptom_priority_html}
        </div>

        <!-- 4. AI PATTERN INSIGHTS (Intelligent Analysis) -->
        <div style="{section_style}">
            <div style="{heading_style}">
                <div style="font-size: 20px;">🔍</div>
                <div style="{heading_text_style}">AI PATTERN INSIGHTS</div>
            </div>
            {ai_insights_html}
        </div>

        <!-- 5. 🆕 OPTIMIZED BODY SYSTEM IMPACT (System-wide View) -->
        <div style="{section_style}">
            <div style="{heading_style}">
                <div style="font-size: 20px;">👤</div>
                <div style="{heading_text_style}">BODY SYSTEM IMPACT</div>
            </div>
            {body_system_display}
            {severity_legend}
        </div>

        <!-- 6. SYMPTOMS BREAKDOWN (Quantitative Summary) -->
        <div style="{section_style}">
            <div style="{heading_style}">
                <div style="font-size: 20px;">📈</div>
                <div style="{heading_text_style}">SYMPTOMS BREAKDOWN</div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 15px;">
                <div style="
                    background: rgba(72, 187, 120, 0.15);
                    padding: 25px;
                    border-radius: 14px;
                    text-align: center;
                    border: 1px solid #48bb78;
                    backdrop-filter: blur(10px);
                ">
                    <div style="font-size: 32px; font-weight: 800; color: #68d391; margin-bottom: 8px;">{mild_count}</div>
                    <div style="font-size: 14px; color: #a0aec0; font-weight: 600;">MILD SYMPTOMS</div>
                </div>
                <div style="
                    background: rgba(237, 137, 54, 0.15);
                    padding: 25px;
                    border-radius: 14px;
                    text-align: center;
                    border: 1px solid #ed8936;
                    backdrop-filter: blur(10px);
                ">
                    <div style="font-size: 32px; font-weight: 800; color: #fbd38d; margin-bottom: 8px;">{moderate_count}</div>
                    <div style="font-size: 14px; color: #a0aec0; font-weight: 600;">MODERATE SYMPTOMS</div>
                </div>
                <div style="
                    background: rgba(229, 62, 62, 0.15);
                    padding: 25px;
                    border-radius: 14px;
                    text-align: center;
                    border: 1px solid #e53e3e;
                    backdrop-filter: blur(10px);
                ">
                    <div style="font-size: 32px; font-weight: 800; color: #fc8181; margin-bottom: 8px;">{critical_count}</div>
                    <div style="font-size: 14px; color: #a0aec0; font-weight: 600;">CRITICAL SYMPTOMS</div>
                </div>
            </div>
        </div>

        <!-- 7. RECOVERY TIMELINE (Future Outlook) -->
        <div style="{section_style}">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
                <div style="{heading_style}">
                    <div style="font-size: 20px;">🔄</div>
                    <div style="{heading_text_style}">RECOVERY TIMELINE</div>
                </div>
                <div style="
                    background: rgba(72, 187, 120, 0.2);
                    padding: 6px 12px;
                    border-radius: 20px;
                    font-size: 13px;
                    color: #68d391;
                    border: 1px solid #48bb78;
                ">
                    {recovery_data["recovery_days"]} days expected
                </div>
            </div>
            {recovery_timeline_html}
        </div>

        <!-- 8. IMMEDIATE ACTIONS (Action Plan) -->
        <div style="{section_style}">
            <div style="{heading_style}">
                <div style="
                    background: linear-gradient(135deg, #4299e1, #3182ce);
                    padding: 10px;
                    border-radius: 10px;
                    font-size: 20px;
                ">🚑</div>
                <div style="{heading_text_style}">IMMEDIATE CARE RECOMMENDATIONS</div>
            </div>
            
            <div style="
                background: rgba(66, 153, 225, 0.1);
                padding: 20px;
                border-radius: 12px;
                margin-bottom: 15px;
                border: 1px solid #4299e1;
            ">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                    <div style="font-size: 18px; color: #90cdf4;">💊</div>
                    <div style="font-weight: 700; color: #90cdf4; font-size: 16px;">IMMEDIATE SELF-CARE</div>
                </div>
                <div style="color: #cbd5e0; font-size: 14px; line-height: 1.6; padding-left: 30px;">
                    {immediate_remedy}
                </div>
            </div>
            
            <div style="
                font-size: 13px;
                color: #718096;
                margin-top: 15px;
                display: flex;
                align-items: center;
                gap: 8px;
                justify-content: center;
            ">
                <span>🤖</span> AI-powered medical insights for better health decisions
            </div>
        </div>
    </div>
    """
    return dashboard_html
