import pandas as pd

def calculate():
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. Number of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    # 4. Advanced education and >50K
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_education]['salary'] == '>50K').sum() / advanced_education.sum() * 100, 1)

    # 5. Without advanced education and >50K
    lower_education = ~advanced_education
    lower_education_rich = round((df[lower_education]['salary'] == '>50K').sum() / lower_education.sum() * 100, 1)

    # 6. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. % of people working min hours and earning >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100, 1)

    # 8. Country with highest percentage of >50K earners
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_by_country = df['native-country'].value_counts()
    country_percentages = rich_by_country / total_by_country * 100
    highest_earning_country = country_percentages.idxmax()
    highest_earning_country_percentage = round(country_percentages.max(), 1)

    # 9. Top occupation in India for >50K earners
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

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