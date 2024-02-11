import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def process_data():
    # Load jobs and candidates data
    jobs = pd.read_csv('data/jobs.csv')
    candidates = pd.read_csv('data/candidates.csv')

    # Display matplotlib plots inline
    plt.show()
    print("Original 'candidates' dataframe:")
    print(candidates.head())

    # Handle missing values in the "Experience" column
    candidates["Experience"].fillna("None", inplace=True)
    candidates.fillna("N/A", inplace=True)

    # Create the "StudyProgram" column by concatenating "StudyMode" and "StudyPattern"
    candidates['StudyProgram'] = candidates[["StudyMode", "StudyPattern"]].agg('-'.join, axis=1)

    # Your clean function
    def clean(program):
        program = program.split("-")
        study_mode, study_pattern = program[0], program[1]
        
        if study_mode == "N/A" and study_pattern == "N/A":
            # assume student is campus, fulltime
            return "Campus-FT"
        
        if study_mode == "N/A":
            # assume student in on-campus
            return f"Campus-{study_pattern}"
        
        if study_pattern == "N/A":
            # assume student is fulltime
            return f"{study_mode.capitalize()}-FT"
        
        # both entries are specified
        return f"{study_mode.capitalize()}-{study_pattern}"

    # Drop the unified columns
    candidates.drop(["StudyMode", "StudyPattern"], axis=1, inplace=True)

    # Handle null-values in the StudyProgram column
    candidates["CleanedStudyProgram"] = candidates["StudyProgram"].apply(clean)

    print("\n'candidates' dataframe after cleaning:")
    print(candidates.head())

    # Your round_to_closest function
    def round_to_closest(x):
        # extract the unitary digit
        unitary = int(x) % 10
            
        # extract the decimal digit
        decimal = int(x)//10
            
        # round up or down based on the unitary digit
        if unitary < 5: return decimal * 10
        if unitary == 5: return x
        else: return (decimal + 1) * 10

    # Round the values in the MinScore column to the nearest 5%
    jobs['MinScore'] = jobs['MinScore'].apply(round_to_closest)
    print(jobs.head())

    # Save the processed dataframes to CSV files
    jobs.to_csv('processed_jobs.csv', index=False)
    candidates.to_csv('processed_candidates.csv', index=False)

    print("Processed data saved to 'processed_jobs.csv' and 'processed_candidates.csv'")

    # Return the processed dataframes
    return jobs, candidates
