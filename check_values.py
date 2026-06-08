import pandas as pd

df = pd.read_csv("Student_performance_data _.csv")

columns = [
    'Gender',
    'Ethnicity',
    'ParentalEducation',
    'Tutoring',
    'ParentalSupport',
    'Extracurricular',
    'Sports',
    'Music',
    'Volunteering'
]

for col in columns:
    print(f"\n{col}")
    print(sorted(df[col].unique()))

print(f"\n Grade class :{sorted(df['GradeClass'].unique())}")