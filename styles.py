# styles.py - UPDATED WITH PARTICLE NETWORK BRAIN ANIMATION

ENHANCED_NEURAL_CSS = """
.neural-container {
    position: relative;
    width: 100%;
    height: 500px;
    background: 
        radial-gradient(circle at 20% 80%, rgba(66, 153, 225, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(159, 122, 234, 0.08) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(72, 187, 120, 0.04) 0%, transparent 50%),
        linear-gradient(135deg, #0a0f1c 0%, #1a1f36 100%);
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 3px solid #4299e1;
    margin-bottom: 20px;
}

.neural-content {
    text-align: center;
    position: relative;
    z-index: 100;
    padding: 2rem;
    background: rgba(10, 15, 28, 0.7);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    border: 1px solid rgba(66, 153, 225, 0.4);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.main-title {
    font-size: 4.5rem;
    font-weight: 900;
    margin-bottom: 1rem;
    color: white;
    text-shadow: 0 0 30px rgba(66, 153, 225, 0.7);
    background: linear-gradient(135deg, #ffffff 0%, #a0c6ff 50%, #9f7aea 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 3px;
    animation: titlePowerUp 3s ease-out, titleFloat 8s ease-in-out infinite 3s;
}

.neural-subtitle {
    font-size: 1.6rem;
    font-weight: 400;
    margin-bottom: 2rem;
    color: #a0c6ff;
    letter-spacing: 2px;
    animation: subtitleGlide 6s ease-in-out infinite;
    text-shadow: 0 0 15px rgba(66, 153, 225, 0.4);
}

/* Canvas for particle network */
.particle-canvas {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 2;
}

/* Brain outline glow effect */
.brain-outline {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 400px;
    height: 400px;
    opacity: 0.1;
    background: radial-gradient(circle, rgba(66, 153, 225, 0.3), transparent 70%);
    border-radius: 50%;
    filter: blur(20px);
    animation: brainPulse 8s ease-in-out infinite;
}

@keyframes brainPulse {
    0%, 100% { opacity: 0.1; transform: translate(-50%, -50%) scale(1); }
    50% { opacity: 0.2; transform: translate(-50%, -50%) scale(1.1); }
}

@keyframes titlePowerUp {
    0% { 
        opacity: 0;
        transform: scale(0.9) translateY(30px);
        filter: blur(5px);
    }
    70% {
        transform: scale(1.02) translateY(-5px);
        text-shadow: 0 0 50px rgba(66, 153, 225, 0.9),
                     0 0 80px rgba(66, 153, 225, 0.5);
    }
    100% { 
        opacity: 1;
        transform: scale(1) translateY(0);
        filter: blur(0);
    }
}

@keyframes titleFloat {
    0%, 100% { 
        transform: translateY(0) rotate(0deg);
        text-shadow: 0 0 25px rgba(66, 153, 225, 0.6),
                     0 0 50px rgba(66, 153, 225, 0.3);
    }
    50% { 
        transform: translateY(-8px) rotate(0.3deg);
        text-shadow: 0 0 35px rgba(66, 153, 225, 0.8),
                     0 0 70px rgba(66, 153, 225, 0.4),
                     0 0 100px rgba(66, 153, 225, 0.2);
    }
}

@keyframes subtitleGlide {
    0%, 100% { 
        opacity: 0.8;
        transform: translateY(0) scale(1);
        letter-spacing: 2px;
    }
    50% { 
        opacity: 1;
        transform: translateY(-3px) scale(1.01);
        letter-spacing: 2.5px;
        text-shadow: 0 0 25px rgba(66, 153, 225, 0.6);
    }
}
"""

ENHANCED_PROFESSIONAL_CSS = ENHANCED_NEURAL_CSS + """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

:root {
    --primary-dark: #1a202c;
    --secondary-dark: #2d3748;
    --accent-blue: #4299e1;
    --accent-green: #48bb78;
    --accent-red: #e53e3e;
    --accent-orange: #ed8936;
    --accent-purple: #9f7aea;
    --text-primary: #e2e8f0;
    --text-secondary: #a0aec0;
    --text-muted: #718096;
    --border-color: #4a5568;
    --card-bg: rgba(45, 55, 72, 0.8);
}

.gradio-container {
    font-family: 'Inter', sans-serif !important;
    background: linear-gradient(135deg, #0f1419 0%, #1a202c 100%) !important;
    color: var(--text-primary) !important;
    min-height: 100vh;
    position: relative;
    z-index: 100;
}

/* Medical Card Styles */
.medical-card {
    background: linear-gradient(135deg, rgba(45, 55, 72, 0.95), rgba(30, 41, 59, 0.95)) !important;
    padding: 25px !important;
    border-radius: 20px !important;
    border: 1px solid rgba(100, 116, 139, 0.3) !important;
    margin-bottom: 20px !important;
    box-shadow: 0 12px 40px rgba(0,0,0,0.25) !important;
    position: relative;
    z-index: 100;
    backdrop-filter: blur(12px) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

.medical-card:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 20px 50px rgba(0,0,0,0.35), 0 0 0 1px rgba(66, 153, 225, 0.2) !important;
    border-color: rgba(66, 153, 225, 0.4) !important;
}

.symptom-grid-urgent .gr-checkbox {
    border-left: 5px solid var(--accent-red) !important;
    background: linear-gradient(135deg, rgba(229, 62, 62, 0.12), rgba(229, 62, 62, 0.05)) !important;
    margin: 8px 0 !important;
    padding: 14px 18px !important;
    border-radius: 10px !important;
    transition: all 0.25s ease !important;
    border: 1px solid rgba(229, 62, 62, 0.2) !important;
}

.symptom-grid-urgent .gr-checkbox:hover {
    background: linear-gradient(135deg, rgba(229, 62, 62, 0.18), rgba(229, 62, 62, 0.08)) !important;
    transform: translateX(5px) scale(1.02) !important;
    box-shadow: 0 4px 15px rgba(229, 62, 62, 0.2) !important;
}

.consult-btn {
    background: linear-gradient(135deg, var(--accent-blue), #3182ce, #2c5aa0) !important;
    border: none !important;
    color: white !important;
    padding: 18px 35px !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 6px 20px rgba(66, 153, 225, 0.4) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    position: relative !important;
    overflow: hidden !important;
}

.consult-btn:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0 12px 30px rgba(66, 153, 225, 0.5) !important;
}

.consult-btn::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.6s ease-in-out;
}

.consult-btn:hover::after {
    left: 100%;
}

.secondary-btn {
    background: linear-gradient(135deg, #4a5568, #2d3748) !important;
    border: 1px solid rgba(100, 116, 139, 0.4) !important;
    color: var(--text-primary) !important;
    padding: 15px 25px !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    transition: all 0.3s ease !important;
}

.secondary-btn:hover {
    background: linear-gradient(135deg, #525c70, #344155) !important;
    border-color: rgba(66, 153, 225, 0.4) !important;
    transform: translateY(-2px) !important;
}

.input-section {
    background: linear-gradient(135deg, rgba(45, 55, 72, 0.9), rgba(30, 41, 59, 0.9)) !important;
    border-radius: 16px !important;
    padding: 25px !important;
    border: 1px solid rgba(100, 116, 139, 0.3) !important;
    height: 100% !important;
    position: relative;
    z-index: 100;
    backdrop-filter: blur(10px) !important;
    box-shadow: 0 8px 32px rgba(0,0,0,0.2) !important;
}

.dark-textbox {
    background: rgba(30, 41, 59, 0.9) !important;
    border: 1px solid rgba(100, 116, 139, 0.4) !important;
    border-radius: 12px !important;
    color: var(--text-primary) !important;
    padding: 16px !important;
    font-size: 15px !important;
    transition: all 0.3s ease !important;
    backdrop-filter: blur(8px) !important;
}

.dark-textbox:focus {
    border-color: #4299e1 !important;
    box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.15) !important;
    background: rgba(30, 41, 59, 0.95) !important;
    transform: translateY(-1px) !important;
}

.dark-audio, .dark-image {
    border: 1px solid rgba(100, 116, 139, 0.4) !important;
    border-radius: 12px !important;
    transition: all 0.3s ease !important;
    background: rgba(30, 41, 59, 0.8) !important;
}

.dark-audio:focus, .dark-image:focus {
    border-color: #4299e1 !important;
    box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.1) !important;
}

/* Medical Loading Animation */
.medical-loader {
    text-align: center;
    padding: 30px;
    background: linear-gradient(135deg, rgba(45, 55, 72, 0.9), rgba(30, 41, 59, 0.9));
    border-radius: 16px;
    border: 1px solid rgba(66, 153, 225, 0.3);
    margin: 20px 0;
}

.pulse-dot {
    width: 16px;
    height: 16px;
    background: linear-gradient(135deg, #4299e1, #9f7aea);
    border-radius: 50%;
    margin: 0 auto 20px;
    animation: medicalPulse 2s ease-in-out infinite;
    box-shadow: 0 0 20px rgba(66, 153, 225, 0.5);
}

@keyframes medicalPulse {
    0%, 100% { 
        transform: scale(1); 
        opacity: 1; 
        box-shadow: 0 0 20px rgba(66, 153, 225, 0.5);
    }
    50% { 
        transform: scale(1.3); 
        opacity: 0.8; 
        box-shadow: 0 0 30px rgba(66, 153, 225, 0.8), 0 0 40px rgba(66, 153, 225, 0.3);
    }
}
"""

# ========== DNA HELIX COMPLETELY REMOVED ==========
HTML_ANIMATIONS_CSS = ""

HTML_ANIMATIONS_HEADER = ""

HTML_ANIMATIONS_JS = ""

NEURAL_JS = """
<script>
class ParticleNetwork {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.particles = [];
        this.connections = [];
        this.mouse = { x: 0, y: 0 };
        
        this.init();
        this.animate();
        this.setupEventListeners();
    }

    init() {
        this.resize();
        this.createParticles();
    }

    resize() {
        this.canvas.width = this.canvas.offsetWidth;
        this.canvas.height = this.canvas.offsetHeight;
    }

    createParticles() {
        this.particles = [];
        const particleCount = 150;
        
        // Create brain-shaped particle distribution
        for (let i = 0; i < particleCount; i++) {
            // Brain-like shape using parametric equations
            const angle = (i / particleCount) * Math.PI * 2;
            const variation = 0.3 + Math.random() * 0.4;
            
            // Brain hemisphere shape
            const brainX = Math.sin(angle * 2) * (0.5 + Math.sin(angle) * 0.3);
            const brainY = Math.cos(angle) * (0.6 + Math.cos(angle * 2) * 0.2);
            
            const x = (brainX * 0.3 + 0.5) * this.canvas.width;
            const y = (brainY * 0.3 + 0.5) * this.canvas.height;
            
            this.particles.push({
                x: x + (Math.random() - 0.5) * 100,
                y: y + (Math.random() - 0.5) * 80,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                radius: 1.5 + Math.random() * 2,
                color: this.getParticleColor(i),
                originalX: x,
                originalY: y,
                speed: 0.2 + Math.random() * 0.3
            });
        }
    }

    getParticleColor(index) {
        const colors = [
            'rgba(66, 153, 225, 0.8)',    // Blue
            'rgba(159, 122, 234, 0.8)',   // Purple
            'rgba(72, 187, 120, 0.8)',    // Green
            'rgba(237, 137, 54, 0.8)',    // Orange
            'rgba(229, 62, 62, 0.8)'      // Red
        ];
        return colors[index % colors.length];
    }

    animate() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        this.updateParticles();
        this.drawConnections();
        this.drawParticles();
        
        requestAnimationFrame(() => this.animate());
    }

    updateParticles() {
        this.particles.forEach(particle => {
            // Return to original brain position with smooth movement
            const dx = particle.originalX - particle.x;
            const dy = particle.originalY - particle.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance > 2) {
                particle.vx += (dx / distance) * particle.speed * 0.1;
                particle.vy += (dy / distance) * particle.speed * 0.1;
            }
            
            // Add some organic movement
            particle.vx += (Math.random() - 0.5) * 0.05;
            particle.vy += (Math.random() - 0.5) * 0.05;
            
            // Apply velocity with friction
            particle.vx *= 0.95;
            particle.vy *= 0.95;
            
            // Update position
            particle.x += particle.vx;
            particle.y += particle.vy;
            
            // Mouse interaction
            const mouseDx = particle.x - this.mouse.x;
            const mouseDy = particle.y - this.mouse.y;
            const mouseDistance = Math.sqrt(mouseDx * mouseDx + mouseDy * mouseDy);
            
            if (mouseDistance < 150) {
                const force = (150 - mouseDistance) / 150;
                particle.vx += (mouseDx / mouseDistance) * force * 2;
                particle.vy += (mouseDy / mouseDistance) * force * 2;
            }
        });
    }

    drawParticles() {
        this.particles.forEach(particle => {
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            
            // Glow effect
            const gradient = this.ctx.createRadialGradient(
                particle.x, particle.y, 0,
                particle.x, particle.y, particle.radius * 3
            );
            gradient.addColorStop(0, particle.color);
            gradient.addColorStop(1, 'rgba(255, 255, 255, 0)');
            
            this.ctx.fillStyle = gradient;
            this.ctx.fill();
            
            // Core dot
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, 1, 0, Math.PI * 2);
            this.ctx.fillStyle = 'white';
            this.ctx.fill();
        });
    }

    drawConnections() {
        this.ctx.strokeStyle = 'rgba(66, 153, 225, 0.2)';
        this.ctx.lineWidth = 1;
        
        for (let i = 0; i < this.particles.length; i++) {
            for (let j = i + 1; j < this.particles.length; j++) {
                const p1 = this.particles[i];
                const p2 = this.particles[j];
                
                const dx = p1.x - p2.x;
                const dy = p1.y - p2.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 100) {
                    const opacity = 1 - (distance / 100);
                    this.ctx.globalAlpha = opacity * 0.3;
                    
                    this.ctx.beginPath();
                    this.ctx.moveTo(p1.x, p1.y);
                    this.ctx.lineTo(p2.x, p2.y);
                    this.ctx.stroke();
                }
            }
        }
        this.ctx.globalAlpha = 1;
    }

    setupEventListeners() {
        this.canvas.addEventListener('mousemove', (e) => {
            const rect = this.canvas.getBoundingClientRect();
            this.mouse.x = e.clientX - rect.left;
            this.mouse.y = e.clientY - rect.top;
        });

        window.addEventListener('resize', () => {
            this.resize();
            this.createParticles();
        });
    }
}

// Initialize particle network when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('particleCanvas');
    if (canvas) {
        new ParticleNetwork(canvas);
    }
});

// Also initialize when Gradio is ready
if (window.gradio_config) {
    setTimeout(() => {
        const canvas = document.getElementById('particleCanvas');
        if (canvas) {
            new ParticleNetwork(canvas);
        }
    }, 1000);
}
</script>
"""

ENHANCED_NEURAL_HEADER = """
<div class="neural-container" id="neural-container">
    <div class="neural-content">
        <h1 class="main-title">AI DOCTOR 2.0</h1>
        <p class="neural-subtitle">Advanced Medical Analysis with Vision & Voice Technology</p>
    </div>
</div>
"""
