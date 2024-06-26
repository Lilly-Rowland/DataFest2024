import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def graph_expectancy(students="all", title_suf="All Students"):
    # Read the data
    df = pd.read_csv('full_03_04/checkpoints_pulse.csv')

    if students != "all":
        df = df[df["student_id"].isin(students)]

    # Filter the data
    subset_df = df[(df["construct"] == "Expectancy") & df["response"].notnull()]
    data_top = subset_df[["chapter_number", "response"]]

    # Calculate average responses per chapter
    expectancy_counts = data_top.groupby("chapter_number")["response"].mean().to_dict()

    # Prepare data for plotting
    chpts, averages = zip(*expectancy_counts.items())

    # Set custom colors
    custom_colors = ['#046C9A', '#B17729', '#ABDDDE']

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(chpts, averages, color=custom_colors)
    plt.xlabel('Chapter Number')
    plt.ylabel('Response Average')
    plt.title('Average Confidence per Chapter for ' + title_suf)
    plt.gca().set_facecolor('#F6EBDB')
    plt.show()

if __name__ == "__main__":
    graph_expectancy()
