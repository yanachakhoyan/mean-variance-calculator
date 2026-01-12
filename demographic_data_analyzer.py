import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    race_count = df["race"].value_counts()

    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    advanced = df["education"].isin(["Bachelors", "Masters", "Doctorate"])

    higher_education_rich = round(
        (df[advanced]["salary"] == ">50K").mean() * 100, 1
    )

    lower_education_rich = round(
        (df[~advanced]["salary"] == ">50K").mean() * 100, 1
    )

    min_work_hours = df["hours-per-week"].min()

    rich_percentage = round(
        (df[df["hours-per-week"] == min_work_hours]["salary"] == ">50K").mean() * 100, 1
    )

    country_stats = (
        df[df["salary"] == ">50K"]["native-country"]
        .value_counts()
        / df["native-country"].value_counts()
        * 100
    )

    highest_earning_country = country_stats.idxmax()
    highest_earning_country_percentage = round(country_stats.max(), 1)

    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]
        ["occupation"]
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors:", percentage_bachelors)
        print("Percentage with higher education earning >50K:", higher_education_rich)
        print("Percentage without higher education earning >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage earning >50K at min work hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
