import pandas as pd

def calculate_demographic_data(print_data=True):
    # 1. Read data from the source URL directly into a pandas DataFrame
    url = "https://raw.githubusercontent.com/freeCodeCamp/boilerplate-demographic-data-analyzer/main/adult.data.csv"
    df = pd.read_csv(url)

    # 2. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 3. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 4. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 5. Define conditions for higher education and lower education groups
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # 6. Percentage of people with advanced education who earn >50K
    higher_education_rich = round((df[higher_education]['salary'] == '>50K').sum() / df[higher_education].shape[0] * 100, 1)

    # 7. Percentage of people without advanced education who earn >50K
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').sum() / df[lower_education].shape[0] * 100, 1)

    # 8. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 9. Percentage of people who work the minimum hours and earn >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100, 1)

    # 10. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack() * 100
    highest_earning_country = country_salary['>50K'].idxmax()
    highest_earning_country_percentage = round(country_salary['>50K'].max(), 1)

    # 11. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # Print results to the console if print_data flag is set to True
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Highest earning country:", highest_earning_country)
        print(f"Highest earning country percentage: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
