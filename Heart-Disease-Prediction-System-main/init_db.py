"""
init_db.py — Initialize SQLite database with synthetic heart disease data
Run once: python init_db.py
"""
import sqlite3
import random

DB_PATH = 'heart_disease.db'

def create_tables(conn):
    conn.executescript("""
        DROP TABLE IF EXISTS patients;
        CREATE TABLE patients (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            age         INTEGER,
            gender      TEXT,
            bmi         REAL,
            cholesterol INTEGER,
            blood_pressure INTEGER,
            smoking     TEXT,
            exercise    TEXT,
            diabetes    INTEGER,
            family_history INTEGER,
            heart_disease  INTEGER,
            region      TEXT,
            year        INTEGER
        );

        DROP TABLE IF EXISTS risk_factors;
        CREATE TABLE risk_factors (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            factor  TEXT,
            pct     REAL
        );

        DROP TABLE IF EXISTS regional_stats;
        CREATE TABLE regional_stats (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            city    TEXT,
            urban   REAL,
            rural   REAL
        );
    """)

def populate(conn):
    random.seed(42)
    genders  = ['Male', 'Female']
    smokes   = ['Non-Smoker', 'Ex-Smoker', 'Light Smoker', 'Heavy Smoker']
    exercise = ['Never', 'Rarely', 'Sometimes', 'Regular', 'Daily']
    regions  = ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Jaipur']

    patients = []
    for _ in range(503):
        age    = random.randint(25, 80)
        gender = random.choice(genders)
        bmi    = round(random.uniform(16.0, 42.0), 1)
        chol   = random.randint(120, 320)
        bp     = random.randint(80, 180)
        smoke  = random.choice(smokes)
        ex     = random.choice(exercise)
        diab   = random.randint(0, 1)
        fam    = random.randint(0, 1)
        region = random.choice(regions)
        year   = random.randint(2015, 2024)

        # Synthetic risk computation
        risk = 0
        if age > 55: risk += 2
        if bmi > 30: risk += 2
        if chol > 240: risk += 2
        if smoke == 'Heavy Smoker': risk += 3
        elif smoke == 'Light Smoker': risk += 2
        elif smoke == 'Ex-Smoker': risk += 1
        if ex == 'Never': risk += 2
        elif ex == 'Rarely': risk += 1
        if diab: risk += 2
        if fam:  risk += 1
        hd = 1 if (risk + random.randint(-2, 2)) >= 5 else 0
        patients.append((age, gender, bmi, chol, bp, smoke, ex, diab, fam, hd, region, year))

    conn.executemany("""INSERT INTO patients
        (age,gender,bmi,cholesterol,blood_pressure,smoking,exercise,
         diabetes,family_history,heart_disease,region,year)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", patients)

    # Risk factors
    factors = [
        ('Poor Diet', 22), ('Physical Inactivity', 19), ('Smoking', 17),
        ('Stress', 14), ('Hypertension', 11), ('Diabetes', 8),
        ('Alcohol', 5), ('Obesity', 4)
    ]
    conn.executemany("INSERT INTO risk_factors (factor,pct) VALUES (?,?)", factors)

    # Regional stats
    cities = [
        ('Delhi', 31, 18), ('Mumbai', 28, 16), ('Bangalore', 24, 13),
        ('Chennai', 27, 17), ('Kolkata', 26, 19), ('Hyderabad', 23, 14),
        ('Pune', 25, 15), ('Jaipur', 22, 21)
    ]
    conn.executemany("INSERT INTO regional_stats (city,urban,rural) VALUES (?,?,?)", cities)

    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect(DB_PATH)
    create_tables(conn)
    populate(conn)
    conn.close()
    print(f"✅ Database created: {DB_PATH}  (503 patients)")
