import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def graph_eoc(students="all", title_suf="All Students"):
    # Read the data
    df = pd.read_csv('full_03_04/checkpoints_eoc.csv')

    # Filter the data for specified students
    if students != "all":
        df = df[df["student_id"].isin(students)]

    # Filter the data for non-null EOC values
    subset_df = df[df["EOC"].notnull()]
    data_top = subset_df.loc[:, ["chapter_number", "EOC"]]

    # Calculate average responses per chapter
    expectancy_counts = data_top.groupby("chapter_number")["EOC"].mean().mul(100).to_dict()

    # Prepare data for plotting
    chpts = list(expectancy_counts.keys())
    averages = list(expectancy_counts.values())

    # Set custom colors
    custom_colors = ['#046C9A', '#B17729', '#ABDDDE']

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.bar(chpts, averages, color=custom_colors)
    plt.xlabel('Chapter Number')
    plt.ylabel('End of Chapter Score (%)')
    plt.title(f'Average End of Chapter Scores for {title_suf}')
    plt.gca().set_facecolor('#F6EBDB')
    plt.show()

if __name__ == "__main__":
    graph_eoc()