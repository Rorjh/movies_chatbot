import pandas as pd

def prepare_dataset():
    df = pd.read_csv("data/wiki_movie_plots_deduped.csv")
    # df['text'] = df.apply(lambda row: f"Title: {row['Title']}\nReleased in: {row['Release Year']}\nPlot: {row['Plot']}\nOrigin: {row["Origin/Ethnicity"]}\nDirected by: {row["Director"]}\nCast: {row["Cast"]}\nGenre: {row["Genre"]}", axis=1)
    df['text'] = df.apply(lambda row: "Title: {}\nReleased in: {}\nPlot: {}\nOrigin: {}\nDirected by: {}\nCast: {}\nGenre: {}".format(row['Title'], row['Release Year'], row['Plot'], row["Origin/Ethnicity"], row["Director"], row["Cast"], row["Genre"]), axis=1)

    return {"text": df["text"].to_list(), "metadata": [{"id": text_id} for text_id in df.index]}
