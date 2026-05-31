"""
EPIDISC Epilepsy Dashboard - Web Interface
==========================================

Comprehensive web-based consultation interface for epilepsy care
with patient records, EEG/MRI integration, medication management,
and literature surveillance visualization.

Based on:
- Flask web framework
- Responsive design principles
- Clinical workflow optimization
- Privacy-first architecture (local-only storage)

Version: 1.0.0
Last Updated: 2026-05-31
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_cors import CORS
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import json
import os


@dataclass
class PatientRecord:
    """Epilepsy patient record structure"""
    patient_id: str
    name: str
    age: int
    gender: str
    epilepsy_type: str
    seizure_frequency: str
    current_medications: List[str]
    eeg_findings: str
    mri_findings: str
    last_consultation: str
    consultation_history: List[Dict[str, Any]]
    notes: List[str]


class EpilepsyDashboard:
    """
    Comprehensive epilepsy consultation dashboard

    Web-based interface for clinical epilepsy care with
    patient management, consultation tools, and information
    resources.
    """

    def __init__(self, port: int = 8790):
        """Initialize epilepsy dashboard"""
        self.port = port
        self.app = Flask(__name__,
                       template_folder='templates',
                       static_folder='static')
        CORS(self.app)

        # Configure Flask for local storage
        self.app.secret_key = 'epidisc_epilepsy_dashboard_local_only'

        # Patient records storage (local-only)
        self.patient_records: Dict[str, PatientRecord] = {}

        # Dashboard statistics
        self.dashboard_stats = {
            "total_consultations": 0,
            "active_patients": 0,
            "literature_updates": 0,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self._setup_routes()
        self._create_templates()
        self._create_static_files()

    def _setup_routes(self):
        """Set up dashboard routes"""

        @self.app.route('/')
        def dashboard_home():
            """Dashboard home page"""
            return render_template('epilepsy_dashboard.html',
                                stats=self.dashboard_stats,
                                patient_count=len(self.patient_records))

        @self.app.route('/consultation')
        def consultation_interface():
            """Consultation interface"""
            return render_template('consultation.html')

        @self.app.route('/api/consult', methods=['POST'])
        def api_consult():
            """API endpoint for epilepsy consultation"""
            from epidisc_core.domains.epilepsy import EpilepsyDomain

            data = request.json
            query = data.get('query', '')
            patient_data = data.get('patient_data', {})
            clinical_context = data.get('clinical_context', {})

            # Create epilepsy domain
            domain = EpilepsyDomain()

            # Process consultation
            result = domain.process_query(query, clinical_context)

            # Update statistics
            self.dashboard_stats['total_consultations'] += 1

            return jsonify({
                'success': True,
                'answer': result.answer,
                'confidence': result.confidence,
                'metadata': result.metadata
            })

        @self.app.route('/api/patient/save', methods=['POST'])
        def api_save_patient():
            """API endpoint to save patient record"""
            data = request.json
            patient_id = data.get('patient_id')

            if not patient_id:
                patient_id = f"PT_{datetime.now().strftime('%Y%m%d%H%M%S')}"

            patient_record = PatientRecord(
                patient_id=patient_id,
                name=data.get('name', ''),
                age=data.get('age', 0),
                gender=data.get('gender', ''),
                epilepsy_type=data.get('epilepsy_type', ''),
                seizure_frequency=data.get('seizure_frequency', ''),
                current_medications=data.get('current_medications', []),
                eeg_findings=data.get('eeg_findings', ''),
                mri_findings=data.get('mri_findings', ''),
                last_consultation=datetime.now().strftime("%Y-%m-%d"),
                consultation_history=[],
                notes=[]
            )

            self.patient_records[patient_id] = patient_record
            self.dashboard_stats['active_patients'] = len(self.patient_records)

            return jsonify({
                'success': True,
                'patient_id': patient_id,
                'message': 'Patient record saved successfully'
            })

        @self.app.route('/api/patient/<patient_id>', methods=['GET'])
        def api_get_patient(patient_id):
            """API endpoint to get patient record"""
            patient = self.patient_records.get(patient_id)

            if patient:
                return jsonify({
                    'success': True,
                    'patient': {
                        'patient_id': patient.patient_id,
                        'name': patient.name,
                        'age': patient.age,
                        'gender': patient.gender,
                        'epilepsy_type': patient.epilepsy_type,
                        'seizure_frequency': patient.seizure_frequency,
                        'current_medications': patient.current_medications,
                        'eeg_findings': patient.eeg_findings,
                        'mri_findings': patient.mri_findings,
                        'last_consultation': patient.last_consultation
                    }
                })
            else:
                return jsonify({
                    'success': False,
                    'message': 'Patient not found'
                }), 404

        @self.app.route('/api/patients', methods=['GET'])
        def api_list_patients():
            """API endpoint to list all patients"""
            patients = [
                {
                    'patient_id': pt.patient_id,
                    'name': pt.name,
                    'age': pt.age,
                    'epilepsy_type': pt.epilepsy_type,
                    'last_consultation': pt.last_consultation
                }
                for pt in self.patient_records.values()
            ]

            return jsonify({
                'success': True,
                'patients': patients,
                'total': len(patients)
            })

        @self.app.route('/knowledge')
        def knowledge_base():
            """Knowledge base interface"""
            return render_template('knowledge_base.html')

        @self.app.route('/literature')
        def literature_updates():
            """Literature updates interface"""
            return render_template('literature.html',
                                literature_count=self.dashboard_stats['literature_updates'])

        @self.app.route('/resources')
        def resources():
            """Resources and references"""
            return render_template('resources.html')

        @self.app.route('/about')
        def about():
            """About page"""
            return render_template('about.html')

    def _create_templates(self):
        """Create HTML templates"""
        templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
        os.makedirs(templates_dir, exist_ok=True)

        # Dashboard home template
        dashboard_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EPIDISC - Epilepsy Consultation Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f5f5; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; }
        .header h1 { margin: 0; font-size: 28px; }
        .header p { margin: 5px 0 0; opacity: 0.9; }
        .nav { background: #fff; padding: 15px 20px; border-bottom: 1px solid #ddd; display: flex; gap: 20px; }
        .nav a { color: #333; text-decoration: none; padding: 8px 16px; border-radius: 4px; }
        .nav a:hover, .nav a.active { background: #667eea; color: white; }
        .container { max-width: 1200px; margin: 30px auto; padding: 0 20px; }
        .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .stat-card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .stat-card h3 { color: #667eea; margin-bottom: 10px; font-size: 16px; }
        .stat-card .number { font-size: 36px; font-weight: bold; color: #333; }
        .main-card { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
        .main-card h2 { color: #333; margin-bottom: 20px; }
        .btn { display: inline-block; padding: 12px 24px; background: #667eea; color: white; text-decoration: none; border-radius: 6px; border: none; cursor: pointer; font-size: 14px; }
        .btn:hover { background: #5568d3; }
        .privacy-notice { background: #e8f5e8; padding: 15px; border-radius: 6px; margin-top: 20px; border-left: 4px solid #4caf50; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🧠 EPIDISC - Epilepsy Consultation Dashboard</h1>
        <p>World-Class Epilepsy Consultation System v2.0.0</p>
    </div>

    <div class="nav">
        <a href="/" class="active">Dashboard</a>
        <a href="/consultation">New Consultation</a>
        <a href="/knowledge">Knowledge Base</a>
        <a href="/literature">Literature Updates</a>
        <a href="/resources">Resources</a>
        <a href="/about">About</a>
    </div>

    <div class="container">
        <div class="stats">
            <div class="stat-card">
                <h3>Total Consultations</h3>
                <div class="number">{{ stats.total_consultations }}</div>
            </div>
            <div class="stat-card">
                <h3>Active Patients</h3>
                <div class="number">{{ patient_count }}</div>
            </div>
            <div class="stat-card">
                <h3>Literature Updates</h3>
                <div class="number">{{ stats.literature_updates }}</div>
            </div>
        </div>

        <div class="main-card">
            <h2>Quick Actions</h2>
            <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                <a href="/consultation" class="btn">🆕 New Consultation</a>
                <a href="/knowledge" class="btn">📚 Knowledge Base</a>
                <a href="/literature" class="btn">📄 Literature Updates</a>
            </div>

            <div class="privacy-notice">
                <strong>🔒 Privacy Notice:</strong> All patient data is stored locally. No external transmission of medical information.
            </div>
        </div>

        <div class="main-card">
            <h2>System Capabilities</h2>
            <ul style="line-height: 1.8;">
                <li>✅ ILAE 2017 seizure classification</li>
                <li>✅ Comprehensive ASM database (15+ medications)</li>
                <li>✅ Advanced differential diagnosis (PNES, syncope, migraine)</li>
                <li>✅ EEG interpretation guidance</li>
                <li>✅ MRI epilepsy protocol interpretation</li>
                <li>✅ Genetic epilepsy consultation</li>
                <li>✅ Status epilepticus protocols</li>
                <li>✅ Women's health & pregnancy guidance</li>
                <li>✅ Sleep medicine integration</li>
                <li>✅ Psychiatry integration (PNES, comorbidities)</li>
                <li>✅ Evidence-based medicine framework</li>
            </ul>
        </div>
    </div>
</body>
</html>'''

        # Write dashboard template
        with open(os.path.join(templates_dir, 'epilepsy_dashboard.html'), 'w') as f:
            f.write(dashboard_html)

        # Consultation interface template
        consultation_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Epilepsy Consultation - EPIDISC</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Segoe UI', sans-serif; background: #f5f5f5; }
        .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; }
        .container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
        .consultation-form { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 20px; }
        .form-group label { display: block; margin-bottom: 8px; font-weight: 500; color: #333; }
        .form-group textarea, .form-group input, .form-group select {
            width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 6px; font-size: 14px;
        }
        .form-group textarea { min-height: 120px; resize: vertical; }
        .btn { display: inline-block; padding: 12px 30px; background: #667eea; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; }
        .btn:hover { background: #5568d3; }
        .result { background: white; padding: 30px; border-radius: 10px; margin-top: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); display: none; }
        .result.show { display: block; }
        .confidence { background: #e8f5e8; padding: 10px 15px; border-radius: 6px; display: inline-block; margin: 15px 0; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🧠 Epilepsy Consultation</h1>
    </div>

    <div class="container">
        <div class="consultation-form">
            <h2 style="margin-bottom: 20px;">Enter Your Consultation Query</h2>

            <form id="consultationForm">
                <div class="form-group">
                    <label for="query">Consultation Query</label>
                    <textarea id="query" name="query" placeholder="Describe the epilepsy case, seizure description, or ask a question about diagnosis/treatment..." required></textarea>
                </div>

                <div class="form-group">
                    <label for="query_type">Query Type (Optional)</label>
                    <select id="query_type" name="query_type">
                        <option value="">General Consultation</option>
                        <option value="classification">Seizure Classification</option>
                        <option value="treatment">Treatment Options</option>
                        <option value="diagnosis">Diagnosis & Workup</option>
                        <option value="eeg">EEG Interpretation</option>
                        <option value="first_aid">Seizure First Aid</option>
                        <option value="pregnancy">Pregnancy Planning</option>
                        <option value="genetics">Genetic Testing</option>
                        <option value="status_epilepticus">Status Epilepticus</option>
                        <option value="pnes">PNES vs Epilepsy</option>
                    </select>
                </div>

                <button type="submit" class="btn">Get Consultation</button>
            </form>
        </div>

        <div id="result" class="result">
            <h2>Consultation Result</h2>
            <div class="confidence">Confidence: <span id="confidenceValue">0%</span></div>
            <div id="consultationAnswer"></div>
        </div>
    </div>

    <script>
        document.getElementById('consultationForm').addEventListener('submit', async (e) => {
            e.preventDefault();

            const query = document.getElementById('query').value;
            const queryType = document.getElementById('query_type').value;

            // Show loading state
            document.getElementById('result').classList.add('show');
            document.getElementById('consultationAnswer').innerHTML = '<p>Processing consultation...</p>';

            try {
                const response = await fetch('/api/consult', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        query: query,
                        query_type: queryType,
                        patient_data: {},
                        clinical_context: {}
                    })
                });

                const data = await response.json();

                if (data.success) {
                    document.getElementById('consultationAnswer').innerHTML = formatAnswer(data.answer);
                    document.getElementById('confidenceValue').textContent = (data.confidence * 100).toFixed(0) + '%';
                } else {
                    document.getElementById('consultationAnswer').innerHTML = '<p>Error processing consultation</p>';
                }
            } catch (error) {
                document.getElementById('consultationAnswer').innerHTML = '<p>Error: ' + error.message + '</p>';
            }
        });

        function formatAnswer(text) {
            // Simple markdown-like formatting
            return text
                .replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>')
                .replace(/\\n\\n/g, '</p><p>')
                .replace(/\\n- /g, '</li><li>')
                .replace(/^(.+)$/gm, '<p>$1</p>');
        }
    </script>
</body>
</html>'''

        # Write consultation template
        with open(os.path.join(templates_dir, 'consultation.html'), 'w') as f:
            f.write(consultation_html)

        # Create other basic templates
        for template_name in ['knowledge_base', 'literature', 'resources', 'about']:
            template_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{template_name.replace('_', ' ').title()} - EPIDISC</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Segoe UI', sans-serif; background: #f5f5f5; }}
        .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; }}
        .nav {{ background: #fff; padding: 15px 20px; border-bottom: 1px solid #ddd; display: flex; gap: 20px; }}
        .nav a {{ color: #333; text-decoration: none; padding: 8px 16px; border-radius: 4px; }}
        .nav a:hover {{ background: #667eea; color: white; }}
        .container {{ max-width: 1000px; margin: 30px auto; padding: 0 20px; }}
        .content {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🧠 EPIDISC - {template_name.replace('_', ' ').title()}</h1>
    </div>
    <div class="nav">
        <a href="/">Dashboard</a>
        <a href="/consultation">New Consultation</a>
        <a href="/knowledge">Knowledge Base</a>
        <a href="/literature">Literature Updates</a>
        <a href="/resources">Resources</a>
        <a href="/about">About</a>
    </div>
    <div class="container">
        <div class="content">
            <h2>{template_name.replace('_', ' ').title()}</h2>
            <p style="margin-top: 20px;">This section is under development. Full implementation coming soon.</p>
        </div>
    </div>
</body>
</html>'''

            with open(os.path.join(templates_dir, f'{template_name}.html'), 'w') as f:
                f.write(template_content)

    def _create_static_files(self):
        """Create static files (CSS, JS)"""
        static_dir = os.path.join(os.path.dirname(__file__), 'static')
        os.makedirs(static_dir, exist_ok=True)

        # Create basic CSS file
        css_content = '''/* EPIDISC Dashboard Styles */
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --text-color: #333;
    --background-color: #f5f5f5;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: var(--background-color);
    color: var(--text-color);
    margin: 0;
    padding: 0;
}

.header {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    padding: 20px;
}

.btn {
    background: var(--primary-color);
    color: white;
    padding: 12px 24px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

.btn:hover {
    background: #5568d3;
}
'''

        with open(os.path.join(static_dir, 'style.css'), 'w') as f:
            f.write(css_content)

    def run(self, debug: bool = False):
        """Run the dashboard server"""
        print(f"🧠 EPIDISC Epilepsy Dashboard starting on port {self.port}")
        print(f"🔒 Privacy Mode: Local-only storage")
        print(f"📍 Access at: http://localhost:{self.port}")
        print(f"📚 Knowledge Base Version: 2.0.0")

        self.app.run(host='127.0.0.1', port=self.port, debug=debug)


def create_epilepsy_dashboard(port: int = 8790) -> EpilepsyDashboard:
    """Factory function to create epilepsy dashboard"""
    return EpilepsyDashboard(port=port)


def start_dashboard(port: int = 8790, debug: bool = False):
    """Start the epilepsy dashboard server"""
    dashboard = create_epilepsy_dashboard(port)
    dashboard.run(debug=debug)


__all__ = [
    'PatientRecord',
    'EpilepsyDashboard',
    'create_epilepsy_dashboard',
    'start_dashboard'
]
