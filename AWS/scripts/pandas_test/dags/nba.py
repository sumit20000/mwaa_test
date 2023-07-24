import pandas as pd

def read_nba_data(file_path):
    df = pd.read_csv(file_path)
    return df

def modify_nba_data(df,salary):
    df['Full Name'] = df['Name'] + " (" + df['Team'] + ")"

    df_filtered = df[(df['Age'] < 30) & (df['Salary'] > salary)]

    df_sorted = df_filtered.sort_values(by='Salary', ascending=False)

    return df_sorted['Full Name'].head(5)


if __name__ == "__main__":
    import sys  
    salary=eval(sys.argv[1])    
    
    file_path = "AWS/scripts/pandas_test/dags/nba.csv"

    nba_data = read_nba_data(file_path)

    modified_nba_data = modify_nba_data(nba_data,salary)

    print(modified_nba_data)
