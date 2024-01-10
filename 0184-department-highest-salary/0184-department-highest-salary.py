import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner').drop(columns=["id_y"])

    max_salary_per_department = merged_df.groupby('departmentId')['salary'].transform('max')
    
    df = merged_df[merged_df['salary'] == max_salary_per_department]
    return pd.DataFrame({
        "Department": df["name_y"],
        "Employee": df['name_x'],
        "Salary": df['salary']
    })