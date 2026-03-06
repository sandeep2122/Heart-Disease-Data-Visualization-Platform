from flask import Flask, render_template, jsonify
import sqlite3, time, os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'heart_disease.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ── Page Routes ──────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

@app.route('/dashboard3')
def dashboard3():
    return render_template('dashboard3.html')

@app.route('/data-prep')
def data_prep():
    return render_template('data_prep.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/performance')
def performance():
    return render_template('performance.html')

# ── Existing Data API Endpoints (JSON) ───────────────────────
@app.route('/api/gender')
def api_gender():
    return jsonify({
        'labels': ['Male with HD', 'Female with HD', 'Male No HD', 'Female No HD'],
        'values': [138, 72, 105, 188],
        'colors': ['#e74c8b', '#a855f7', '#38bdf8', '#34d399']
    })

@app.route('/api/age-risk')
def api_age_risk():
    return jsonify({
        'labels': ['20-29', '30-39', '40-49', '50-59', '60-69', '70+'],
        'noDisease': [92, 120, 145, 98, 60, 30],
        'disease':   [8,  22,  68, 110, 105, 78]
    })

@app.route('/api/bmi-risk')
def api_bmi_risk():
    return jsonify({
        'labels': ['Underweight (<18.5)', 'Normal (18.5-24.9)', 'Overweight (25-29.9)', 'Obese I (30-34.9)', 'Obese II (35+)'],
        'riskPercent': [12, 9, 28, 51, 72]
    })

@app.route('/api/cholesterol')
def api_cholesterol():
    return jsonify({
        'labels': ['<150', '150-200', '200-239', '240-279', '280+'],
        'noDisease': [80, 130, 95, 45, 20],
        'disease':   [15, 40,  85, 90, 75]
    })

@app.route('/api/smoking')
def api_smoking():
    return jsonify({
        'labels': ['Non-Smoker', 'Ex-Smoker', 'Light Smoker', 'Heavy Smoker'],
        'riskPercent': [14, 26, 42, 68]
    })

@app.route('/api/exercise')
def api_exercise():
    return jsonify({
        'labels': ['Never', 'Rarely', 'Sometimes', 'Regular', 'Daily'],
        'riskPercent': [72, 58, 41, 22, 11]
    })

@app.route('/api/regional')
def api_regional():
    return jsonify({
        'labels': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Jaipur'],
        'urban': [31, 28, 24, 27, 26, 23, 25, 22],
        'rural': [18, 16, 13, 17, 19, 14, 15, 21]
    })

@app.route('/api/year-trend')
def api_year_trend():
    return jsonify({
        'labels': ['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024'],
        'urban': [18.2, 19.0, 20.1, 21.5, 22.8, 24.1, 25.3, 26.7, 28.0, 29.4],
        'rural': [10.1, 10.8, 11.3, 12.0, 13.1, 14.5, 15.8, 16.9, 17.7, 18.5]
    })

@app.route('/api/risk-factors')
def api_risk_factors():
    return jsonify({
        'labels': ['Poor Diet', 'Physical Inactivity', 'Smoking', 'Stress', 'Hypertension', 'Diabetes', 'Alcohol', 'Obesity'],
        'values': [22, 19, 17, 14, 11, 8, 5, 4]
    })

@app.route('/api/sedentary')
def api_sedentary():
    return jsonify({
        'labels': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Jaipur'],
        'sedentary': [68, 62, 58, 55, 60, 49],
        'moderate':  [22, 25, 27, 29, 26, 31],
        'active':    [10, 13, 15, 16, 14, 20]
    })

@app.route('/api/policy-impact')
def api_policy_impact():
    return jsonify({
        'labels': ['Fitness Programs', 'Tobacco Regulation', 'Diet Subsidies', 'Health Screenings', 'Awareness Campaigns'],
        'estimatedReduction': [18, 25, 14, 21, 16]
    })

@app.route('/api/anita')
def api_anita():
    return jsonify({
        'riskScore': 62,
        'metrics': [
            {'name': 'Total Cholesterol',   'value': 238,  'unit': 'mg/dL',   'benchmark': 200,  'max': 300, 'status': 'warning'},
            {'name': 'Blood Pressure',      'value': 132,  'unit': 'mmHg',    'benchmark': 120,  'max': 180, 'status': 'warning'},
            {'name': 'BMI',                 'value': 27.4, 'unit': 'kg/m²',   'benchmark': 24.9, 'max': 40,  'status': 'warning'},
            {'name': 'Fasting Blood Sugar', 'value': 95,   'unit': 'mg/dL',   'benchmark': 100,  'max': 200, 'status': 'good'},
            {'name': 'Resting Heart Rate',  'value': 78,   'unit': 'bpm',     'benchmark': 70,   'max': 120, 'status': 'good'},
            {'name': 'Physical Activity',   'value': 2,    'unit': 'days/wk', 'benchmark': 5,    'max': 7,   'status': 'danger'}
        ],
        'radar': {
            'labels': ['Diet', 'Exercise', 'Stress Mgmt', 'Sleep', 'No Smoking', 'Alcohol Control'],
            'anita': [55, 30, 50, 65, 90, 80],
            'ideal': [85, 85, 85, 85, 100, 95]
        }
    })

@app.route('/api/summary-stats')
def api_summary_stats():
    return jsonify({
        'totalPatients': 503,
        'hdRate': 41,
        'avgDiagnosisAge': 55,
        'globalDeaths': '17.9M',
        'preventable': '80%'
    })

# ── NEW: Database-backed API Endpoints ───────────────────────
@app.route('/api/db-stats')
def api_db_stats():
    """Real stats pulled from SQLite database."""
    if not os.path.exists(DB_PATH):
        return jsonify({'error': 'Database not found. Run init_db.py first.'}), 404
    conn = get_db()
    row = conn.execute("""
        SELECT
            COUNT(*)                          AS total,
            SUM(heart_disease)                AS hd_count,
            ROUND(AVG(age), 1)                AS avg_age,
            ROUND(AVG(bmi), 1)                AS avg_bmi,
            ROUND(AVG(cholesterol), 0)        AS avg_chol
        FROM patients
    """).fetchone()
    conn.close()
    return jsonify(dict(row))

@app.route('/api/sample-records')
def api_sample_records():
    """Return first 10 patient records from the DB."""
    if not os.path.exists(DB_PATH):
        return jsonify([])
    conn = get_db()
    rows = conn.execute("SELECT * FROM patients LIMIT 10").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])

@app.route('/api/class-balance')
def api_class_balance():
    """Heart disease vs no disease count from DB."""
    if not os.path.exists(DB_PATH):
        return jsonify({'labels': ['No Disease', 'Heart Disease'], 'values': [296, 207]})
    conn = get_db()
    row = conn.execute("SELECT SUM(heart_disease), COUNT(*)-SUM(heart_disease) FROM patients").fetchone()
    conn.close()
    hd, no_hd = row[0], row[1]
    return jsonify({'labels': ['No Disease', 'Heart Disease'], 'values': [no_hd, hd]})

@app.route('/api/age-dist')
def api_age_dist():
    """Age group distribution from DB."""
    if not os.path.exists(DB_PATH):
        return jsonify({
            'labels': ['20-29','30-39','40-49','50-59','60-69','70+'],
            'noDisease': [92,120,145,98,60,30],
            'disease': [8,22,68,110,105,78]
        })
    conn = get_db()
    bands = [('20-29',20,29),('30-39',30,39),('40-49',40,49),
             ('50-59',50,59),('60-69',60,69),('70+',70,120)]
    labels, no_d, dis = [], [], []
    for label, lo, hi in bands:
        r = conn.execute("""
            SELECT SUM(CASE WHEN heart_disease=0 THEN 1 ELSE 0 END),
                   SUM(heart_disease)
            FROM patients WHERE age BETWEEN ? AND ?""", (lo, hi)).fetchone()
        labels.append(label)
        no_d.append(r[0] or 0)
        dis.append(r[1] or 0)
    conn.close()
    return jsonify({'labels': labels, 'noDisease': no_d, 'disease': dis})

# ── Run ───────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True, port=5000)
