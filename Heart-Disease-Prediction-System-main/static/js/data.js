// ========================================================
// HEART DISEASE VISUALIZATION — Synthetic Dataset
// ========================================================

const HDData = {

    // ---------- DASHBOARD 1: Dr. Sharma (Lifestyle Risk Factors) ----------
    genderDistribution: {
        labels: ['Male with HD', 'Female with HD', 'Male No HD', 'Female No HD'],
        values: [138, 72, 105, 188],
        colors: ['#e74c8b', '#a855f7', '#38bdf8', '#34d399']
    },

    ageRisk: {
        labels: ['20-29', '30-39', '40-49', '50-59', '60-69', '70+'],
        noDisease: [92, 120, 145, 98, 60, 30],
        disease: [8, 22, 68, 110, 105, 78]
    },

    bmiRisk: {
        labels: ['Underweight\n(<18.5)', 'Normal\n(18.5-24.9)', 'Overweight\n(25-29.9)', 'Obese I\n(30-34.9)', 'Obese II\n(35+)'],
        riskPercent: [12, 9, 28, 51, 72]
    },

    cholesterol: {
        labels: ['<150', '150-200', '200-239', '240-279', '280+'],
        noDisease: [80, 130, 95, 45, 20],
        disease: [15, 40, 85, 90, 75]
    },

    smokingRisk: {
        labels: ['Non-Smoker', 'Ex-Smoker', 'Light Smoker\n(<10/day)', 'Heavy Smoker\n(10+/day)'],
        riskPercent: [14, 26, 42, 68]
    },

    exerciseImpact: {
        labels: ['Never', 'Rarely\n(1-2x/month)', 'Sometimes\n(1-2x/week)', 'Regular\n(3-4x/week)', 'Daily'],
        riskPercent: [72, 58, 41, 22, 11]
    },

    // ---------- DASHBOARD 2: Ramesh (Regional & Policy Analysis) ----------
    regionalPrevalence: {
        labels: ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune', 'Jaipur'],
        urban: [31, 28, 24, 27, 26, 23, 25, 22],
        rural: [18, 16, 13, 17, 19, 14, 15, 21]
    },

    yearTrend: {
        labels: ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        urban: [18.2, 19.0, 20.1, 21.5, 22.8, 24.1, 25.3, 26.7, 28.0, 29.4],
        rural: [10.1, 10.8, 11.3, 12.0, 13.1, 14.5, 15.8, 16.9, 17.7, 18.5]
    },

    riskFactorBreakdown: {
        labels: ['Poor Diet', 'Physical\nInactivity', 'Smoking', 'Stress', 'Hypertension', 'Diabetes', 'Alcohol', 'Obesity'],
        values: [22, 19, 17, 14, 11, 8, 5, 4]
    },

    sedentaryByRegion: {
        labels: ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata', 'Jaipur'],
        sedentary: [68, 62, 58, 55, 60, 49],
        moderate: [22, 25, 27, 29, 26, 31],
        active: [10, 13, 15, 16, 14, 20]
    },

    policyImpact: {
        labels: ['Fitness\nPrograms', 'Tobacco\nRegulation', 'Diet\nSubsidies', 'Health\nScreenings', 'Awareness\nCampaigns'],
        estimatedReduction: [18, 25, 14, 21, 16]
    },

    // ---------- DASHBOARD 3: Anita (Personal Risk Monitor) ----------
    anita: {
        age: 45,
        gender: 'Female',
        overallRiskScore: 62,  // out of 100

        metrics: [
            { name: 'Total Cholesterol', value: 238, unit: 'mg/dL', benchmark: 200, max: 300, status: 'warning', lower_is_better: true },
            { name: 'Blood Pressure', value: 132, unit: 'mmHg', benchmark: 120, max: 180, status: 'warning', lower_is_better: true },
            { name: 'BMI', value: 27.4, unit: 'kg/m²', benchmark: 24.9, max: 40, status: 'warning', lower_is_better: true },
            { name: 'Fasting Blood Sugar', value: 95, unit: 'mg/dL', benchmark: 100, max: 200, status: 'good', lower_is_better: true },
            { name: 'Resting Heart Rate', value: 78, unit: 'bpm', benchmark: 70, max: 120, status: 'good', lower_is_better: true },
            { name: 'Physical Activity', value: 2, unit: 'days/wk', benchmark: 5, max: 7, status: 'danger', lower_is_better: false }
        ],

        radarData: {
            labels: ['Diet', 'Exercise', 'Stress Mgmt', 'Sleep', 'No Smoking', 'Alcohol Control'],
            anita: [55, 30, 50, 65, 90, 80],
            ideal: [85, 85, 85, 85, 100, 95]
        },

        actionSteps: [
            { priority: 'high', icon: '🏃', title: 'Increase Physical Activity', desc: 'Aim for at least 30 min of brisk walking 5 days/week. Even moderate exercise reduces heart disease risk by up to 35%.' },
            { priority: 'high', icon: '🥗', title: 'Reduce Saturated Fat Intake', desc: 'Replace red meat with fish and legumes. Limit fried foods. A Mediterranean diet lowers cholesterol by 10-15%.' },
            { priority: 'medium', icon: '💊', title: 'Monitor Cholesterol Monthly', desc: 'Your LDL is borderline high. Track monthly and consult your doctor about medication if lifestyle changes are insufficient.' },
            { priority: 'medium', icon: '🧘', title: 'Stress Reduction Techniques', desc: 'Practice mindfulness or yoga for 20 min daily. Chronic stress raises cortisol, which increases blood pressure.' },
            { priority: 'low', icon: '😴', title: 'Improve Sleep Quality', desc: 'Target 7-8 hours nightly. Poor sleep is linked to higher blood pressure and inflammation markers.' }
        ]
    }
};
