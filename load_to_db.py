import sqlite3
import pandas as pd
import os

db_path = 'tableau_data.db'
csv_path = 'heart_disease_tableau_final.csv'

def main():
    print(f"Connecting to database: {db_path}...")
    conn = sqlite3.connect(db_path)
    
    # 1. Load Data
    print(f"Loading data from {csv_path} into pandas...")
    df = pd.read_csv(csv_path)
    
    print("Writing data to SQLite table 'RawHeartData'...")
    df.to_sql('RawHeartData', conn, if_exists='replace', index=False)
    print("Raw data loaded successfully.")
    
    # 2. SQL Transformations
    print("Executing SQL transformations to create 'CleanedHeartDataView'...")
    
    create_view_sql = """
    DROP VIEW IF EXISTS CleanedHeartDataView;
    CREATE VIEW CleanedHeartDataView AS
    SELECT 
        -- Original fields with new names
        HeartDisease AS Has_HeartDisease,
        BMI AS Body_Mass_Index,
        Smoking,
        AlcoholDrinking,
        Stroke,
        PhysicalHealth AS PhysicalHealth_Bad_Days,
        MentalHealth AS MentalHealth_Bad_Days,
        DiffWalking AS Difficulty_Walking,
        Sex,
        AgeCategory,
        Race,
        Diabetic,
        PhysicalActivity,
        GenHealth AS General_Health_Rating,
        SleepTime AS Sleep_Hours_Per_Night,
        Asthma,
        KidneyDisease,
        SkinCancer,

        -- Categorize BMI
        CASE 
            WHEN BMI < 18.5 THEN 'Underweight'
            WHEN BMI >= 18.5 AND BMI < 25 THEN 'Normal Weight'
            WHEN BMI >= 25 AND BMI < 30 THEN 'Overweight'
            ELSE 'Obese'
        END AS BMICategory,
        
        -- Boolean Encoding for easier Tableau math (1/0)
        CASE WHEN HeartDisease = 'Yes' THEN 1 ELSE 0 END AS HeartDisease_Num,
        CASE WHEN Smoking = 'Yes' THEN 1 ELSE 0 END AS Smoking_Num,
        CASE WHEN Stroke = 'Yes' THEN 1 ELSE 0 END AS Stroke_Num,
        CASE WHEN DiffWalking = 'Yes' THEN 1 ELSE 0 END AS DiffWalking_Num,
        CASE WHEN Diabetic = 'Yes' OR Diabetic = 'Yes (during pregnancy)' THEN 1 ELSE 0 END AS Diabetic_Num,
        CASE WHEN Asthma = 'Yes' THEN 1 ELSE 0 END AS Asthma_Num,
        CASE WHEN KidneyDisease = 'Yes' THEN 1 ELSE 0 END AS KidneyDisease_Num,
        CASE WHEN SkinCancer = 'Yes' THEN 1 ELSE 0 END AS SkinCancer_Num,
        CASE WHEN PhysicalActivity = 'Yes' THEN 1 ELSE 0 END AS PhysicalActivity_Num,
        
        -- Age Ordering Constraint (extracting lowest number from '18-24', '80 or older')
        CAST(SUBSTR(AgeCategory, 1, 2) AS INTEGER) AS AgeOrderInt,

        -- Calculated Fields: Health Risk Score
        (CASE WHEN Smoking = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN Stroke = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN Diabetic = 'Yes' OR Diabetic = 'Yes (during pregnancy)' THEN 1 ELSE 0 END) +
        (CASE WHEN Asthma = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN KidneyDisease = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN BMI >= 30 THEN 1 ELSE 0 END) +
        (CASE WHEN CAST(SUBSTR(AgeCategory, 1, 2) AS INTEGER) >= 60 THEN 1 ELSE 0 END) AS Health_Risk_Score,
        
        -- Derived Boolean for High Risk
        CASE WHEN ((CASE WHEN Smoking = 'Yes' THEN 1 ELSE 0 END) +
                   (CASE WHEN Stroke = 'Yes' THEN 1 ELSE 0 END) +
                   (CASE WHEN Diabetic = 'Yes' OR Diabetic = 'Yes (during pregnancy)' THEN 1 ELSE 0 END) +
                   (CASE WHEN Asthma = 'Yes' THEN 1 ELSE 0 END) +
                   (CASE WHEN KidneyDisease = 'Yes' THEN 1 ELSE 0 END) +
                   (CASE WHEN BMI >= 30 THEN 1 ELSE 0 END) +
                   (CASE WHEN CAST(SUBSTR(AgeCategory, 1, 2) AS INTEGER) >= 60 THEN 1 ELSE 0 END)) >= 3 
             THEN 1 ELSE 0 END AS Is_High_Risk

    FROM RawHeartData
    -- Filtering constraint: Exclude nonsensical BMI or extreme outliers if any exist
    WHERE BMI > 10 AND BMI < 100;
    """
    
    conn.executescript(create_view_sql)
    print("SQL View created successfully.")
    
    # Verify the view
    print("\n--- Verifying View Output ---")
    verify_df = pd.read_sql_query("SELECT * FROM CleanedHeartDataView LIMIT 3", conn)
    print(verify_df[['Has_HeartDisease', 'HeartDisease_Num', 'Body_Mass_Index', 'BMICategory', 'Health_Risk_Score', 'Is_High_Risk']])
    
    print("\n--- Validating Health Risk Score vs Heart Disease ---")
    val_df = pd.read_sql_query("SELECT Has_HeartDisease, AVG(Health_Risk_Score) as Avg_Risk_Score FROM CleanedHeartDataView GROUP BY Has_HeartDisease", conn)
    print(val_df)
    
    # Export final structured dataset to CSV to simulate connected DB view
    final_output_path = 'tableau_ready_heart_data.csv'
    print(f"\nExporting transformed view to {final_output_path} for direct Tableau testing...")
    final_df = pd.read_sql_query("SELECT * FROM CleanedHeartDataView", conn)
    final_df.to_csv(final_output_path, index=False)
    print("Export complete.")
    
    conn.close()
    print("Database integration and SQL operations complete.")

if __name__ == '__main__':
    main()
