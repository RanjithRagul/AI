import pandas as pd 

def explore_data(file_path: str) -> None:
    # Step 1: Load Excel file
    data = pd.read_excel(file_path)

    # Step 2: Calculate average hours worked
    avg_hours = data['Hours_Worked'].mean()

    # Step 3: Calculate average tasks completed
    avg_tasks = data['Tasks_Completed'].mean()

    # Step 4: Group by department and calculate average satisfaction score
    dept_satisfaction = data.groupby('Department')['Satisfaction_Score'].mean()

    # Step 5: Find department with highest satisfaction
    best_dept = dept_satisfaction.idxmax()
    
    # Step 6: Print results
    print(f"Average Hours Worked: {avg_hours:.1f}")
    print(f"Average Tasks Completed: {avg_tasks:.1f}")
    print(f"Department with Highest Satisfaction: {best_dept}")


if __name__ == "__main__":
    explore_data(r'C:\AI\Part1\1. Data Exploration\sampledata.xlsx')