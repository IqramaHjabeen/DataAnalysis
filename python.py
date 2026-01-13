#Task01------------Distribution of Job Postings for Different Analyst Roles----------------
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Data Analyst Job Roles in Canada.csv')

# Display the first few rows to understand the data structure
print(df.head())

# Count the number of unique job titles
unique_job_titles_count = df['Job Title'].nunique()

print(f'Number of unique job titles: {unique_job_titles_count}')

# To visualize the frequency of job titles (if you want to see the most common ones)
job_title_counts = df['Job Title'].value_counts()
print(job_title_counts)
# Plotting the data
plt.figure(figsize=(12, 8))
job_title_counts.plot(kind='bar', color='purple')
plt.title('Frequency of Job Titles')
plt.xlabel('Job Title')
plt.ylabel('Count')
plt.xticks(rotation=90)  # Rotate x labels for better readability
plt.tight_layout()  # Adjust layout to make sure everything fits
plt.show()
'''

#Task02----Number of job position associates with each job title---
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Data Analyst Job Roles in Canada.csv')

# Display the first few rows to understand the data structure
print(df.head())

# Create a mapping of job titles to job positions
# Assuming columns 'Position' (job title) and 'Job Title' (job position)
job_title_position_mapping = df.groupby('Position')['Job Title'].unique().reset_index()
job_title_position_mapping.columns = ['Job Title', 'Associated Job Positions']

# Count the number of associated job positions for each job title
job_title_position_mapping['Number of Associated Positions'] = job_title_position_mapping['Associated Job Positions'].apply(len)

# Sort the job titles by the number of associated job positions in descending order
sorted_job_titles = job_title_position_mapping.sort_values(by='Number of Associated Positions', ascending=False)

# Print the sorted job titles and their associated job positions
print('Job Titles and Their Associated Job Positions:')
print(sorted_job_titles)

# Plotting the data
plt.figure(figsize=(12, 8))
bars = plt.barh(sorted_job_titles['Job Title'], sorted_job_titles['Number of Associated Positions'], color='skyblue')

# Add labels on the bars
for bar in bars:
    plt.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
             f'{int(bar.get_width())}', ha='left', va='center')

# Set labels and title
plt.xlabel('Number of Associated Job Positions')
plt.ylabel('Job Title')
plt.title('Number of Job Positions Associated with Each Job Title')
plt.tight_layout()  # Adjust layout to make sure everything fits

# Display the plot
plt.show()
'''

#Task03-------------------Work Mode Distribution:---------------------
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('Data Analyst Job Roles in Canada.csv')

# Display the first few rows to understand the data structure
print(df.head())

# Count the number of remote vs. on-site jobs
work_mode_counts = df['Work Type'].value_counts()

# Print the counts
print('Work Mode Distribution:')
print(work_mode_counts)

# Plotting the data
plt.figure(figsize=(8, 6))
colors = ['lightblue', 'darkblue']  # Define the colors for the bars
work_mode_counts.plot(kind='bar', color=colors)
plt.title('Distribution of Remote vs. On-Site Work')
plt.xlabel('Work Mode')
plt.ylabel('Count')
plt.xticks(rotation=0)  # Keep x labels horizontal
plt.tight_layout()  # Adjust layout to make sure everything fits
plt.show()
'''

#Task04---------------Top Skills for Position-------------------
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Data Analyst Job Roles in Canada.csv')

# Check the structure of the dataset (adjust column names based on your actual dataset)
print(data.head())

# Ensure relevant columns exist
assert 'Position' in data.columns, "Column 'Position' is missing in the dataset"
assert 'Skill' in data.columns, "Column 'Skills' is missing in the dataset"

# Split the skills into individual skills and create a DataFrame where each row is a skill for a position
data['Skill'] = data['Skill'].astype(str)
skills_df = data[['Position', 'Skill']].copy()
skills_df['Skill'] = skills_df['Skill'].str.split(',')  # Adjust delimiter if necessary

# Explode the list of skills into separate rows
skills_df = skills_df.explode('Skill')

# Strip whitespace from skills
skills_df['Skill'] = skills_df['Skill'].str.strip()

# Count occurrences of each skill for each position
skill_counts = skills_df.groupby(['Position', 'Skill']).size().unstack(fill_value=0)

# Print the skill counts for verification
print(skill_counts)

# Plot the top skills for each position
for position in skill_counts.index:
    plt.figure(figsize=(12, 8))

    # Get the skills and their counts for the current position
    skills_for_position = skill_counts.loc[position]

    # Sort by frequency and select the top 10 skills
    top_skills = skills_for_position.sort_values(ascending=False).head(10)

    # Plot the top skills
    bars = plt.bar(top_skills.index, top_skills.values, color='skyblue')

    # Add labels on top of the bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, int(yval), ha='center', va='bottom')

    # Set labels and title
    plt.xlabel('Skill')
    plt.ylabel('Frequency')
    plt.title(f'Top Skills for Position: {position}')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    # Display the plot
    plt.tight_layout()
    plt.show()
'''
#Task05------------------- salary---------------------
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Data Analyst Job Roles in Canada.csv')

# Check the structure of the dataset (adjust column names based on your actual dataset)
print(data.head())

# Ensure relevant columns exist
assert 'Seniority' in data.columns, "Column 'Seniority' is missing in the dataset"
assert 'Max_Salary' in data.columns, "Column 'Max_Salary' is missing in the dataset"

# Check data types of relevant columns
print(data[['Seniority', 'Max_Salary']].dtypes)

# Convert Max_Salary to string to handle non-string values
data['Max_Salary'] = data['Max_Salary'].astype(str)

# Remove non-numeric characters from Max_Salary and convert to numeric
data['Max_Salary'] = pd.to_numeric(data['Max_Salary'].str.replace(',', '').str.replace('$', ''), errors='coerce')

# Drop rows with NaN values in Max_Salary
data = data.dropna(subset=['Max_Salary'])

# Calculate average salary by seniority level
salary_by_seniority = data.groupby('Seniority')['Max_Salary'].mean().reset_index()

# Print the average salary by seniority level for verification
print(salary_by_seniority)

# Plot the average salary by seniority level
plt.figure(figsize=(12, 6))
plt.bar(salary_by_seniority['Seniority'], salary_by_seniority['Max_Salary'], color='teal')

# Add labels on top of the bars
for index, row in salary_by_seniority.iterrows():
    plt.text(row['Seniority'], row['Max_Salary'] + 5000, f'{row["Max_Salary"]:.2f}', ha='center')

# Set labels and title
plt.xlabel('Seniority Level')
plt.ylabel('Average Salary')
plt.title('Average Salary by Seniority Level')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Display the plot
plt.tight_layout()
plt.show()
'''

#Task06----------------------Distributation of job across the provinces------------------------
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Data Analyst Job Roles in Canada.csv')

# Check the structure of the dataset (adjust column names based on your actual dataset)
print(data.head())

# Ensure relevant columns exist
assert 'Province' in data.columns, "Column 'Province' is missing in the dataset"
assert 'Position' in data.columns, "Column 'Position' is missing in the dataset"

# Count the number of job positions for each province
position_distribution_by_province = data.groupby('Province')['Position'].nunique().reset_index()
position_distribution_by_province.columns = ['Province', 'Number of Unique Positions']

# Sort by the number of positions in descending order
position_distribution_by_province = position_distribution_by_province.sort_values(by='Number of Unique Positions', ascending=False)

# Print the distribution for verification
print(position_distribution_by_province)

# Plot the distribution of job positions across provinces
plt.figure(figsize=(14, 8))
bars = plt.bar(position_distribution_by_province['Province'], position_distribution_by_province['Number of Unique Positions'], color='salmon')

# Add labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom')

# Set labels and title
plt.xlabel('Province')
plt.ylabel('Number of Unique Positions')
plt.title('Distribution of Job Positions Across Provinces')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Display the plot
plt.tight_layout()
plt.show()

'''
#Task07-----------distribution of job positions across industries--------------
'''

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Data Analyst Job Roles in Canada.csv')

# Check the structure of the dataset (adjust column names based on your actual dataset)
print(data.head())

# Ensure relevant columns exist
assert 'Industry Type' in data.columns, "Column 'Industry' is missing in the dataset"
assert 'Position' in data.columns, "Column 'Position' is missing in the dataset"

# Count the number of job positions for each industry
position_distribution = data.groupby('Industry Type')['Position'].nunique().reset_index()
position_distribution.columns = ['Industry Type', 'Number of Unique Positions']

# Sort by the number of positions in descending order
position_distribution = position_distribution.sort_values(by='Number of Unique Positions', ascending=False)

# Print the distribution for verification
print(position_distribution)

# Plot the distribution of job positions across industries
plt.figure(figsize=(14, 8))
bars = plt.bar(position_distribution['Industry Type'], position_distribution['Number of Unique Positions'], color='cornflowerblue')

# Add labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval), ha='center', va='bottom')

# Set labels and title
plt.xlabel('Industry')
plt.ylabel('Number of Unique Positions')
plt.title('Distribution of Job Positions Across Industries')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Display the plot
plt.tight_layout()
plt.show()

'''

#Task08----------Average salary by pposition------------
'''
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Data Analyst Job Roles in Canada.csv')

# Check the structure of the dataset (adjust column names based on your actual dataset)
print(data.head())

# Ensure relevant columns exist
assert 'Position' in data.columns, "Column 'Position' is missing in the dataset"
assert 'Employer' in data.columns, "Column 'Employer' is missing in the dataset"
assert 'Max_Salary' in data.columns, "Column 'Max_Salary' is missing in the dataset"

# Convert Max_Salary to string, if it's not already
data['Max_Salary'] = data['Max_Salary'].astype(str)

# Remove non-numeric characters (e.g., commas and dollar signs) and convert to numeric
data['Max_Salary'] = pd.to_numeric(data['Max_Salary'].str.replace(',', '').str.replace('$', ''), errors='coerce')

# Drop rows with NaN values in Max_Salary
data = data.dropna(subset=['Max_Salary'])

# Calculate the average salary for each position within each company
salary_comparison = data.groupby(['Position'])['Max_Salary'].mean().reset_index()

# Sort the positions by average salary in descending order and select the top 25
top_25_positions = salary_comparison.sort_values(by='Max_Salary', ascending=False).head(10)

# Print the top 25 positions for verification
print(top_25_positions)

# Plot the average salaries for the top 25 positions
plt.figure(figsize=(14, 8))
bars = plt.bar(top_25_positions['Position'], top_25_positions['Max_Salary'], color='teal')

# Add labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, f'{yval:.2f}', ha='center', va='bottom')

# Set labels and title
plt.xlabel('Position')
plt.ylabel('Average Salary')
plt.title('Top 10 Positions by Average Salary')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

# Display the plot
plt.tight_layout()
plt.show()
'''
