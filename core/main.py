import asyncio
import pathlib
import os

import pandas as pd
import numpy as np
import pickle

from constants import COMMUNITIES
from get_chats import get_communities_chats
from preprocess_chats import preprocess_subgroup2
from openai_api import get_embedding
from infrences import handle_votes

path = str(os.getcwd())
MODEL_PATH =os.path.join(path,"core", "models", "stock_nlp_model_v1.pickle")
print("\n", path)


# asyncio.run(main())
# stocks = pd.read_csv("../")
# global COMMUNITIES
def run():
    # raw_chats = asyncio.run(get_communities_chats())
    preprocessed_chats = pd.DataFrame()

    # for community_name, chat_list in raw_chats.items():
    #     df = pd.DataFrame(preprocess_subgroup2(chat_list)["messages"])
    #     df["channel_name"] = community_name
    #     preprocessed_chats = pd.concat([preprocessed_chats, df])
    # preprocessed_chats.to_csv("./preprocessed_chats.csv", index=False)
    preprocessed_chats = pd.read_csv("./preprocessed_chats.csv")

    preprocessed_chats = preprocessed_chats[preprocessed_chats["text"] != ""]
    preprocessed_chats.dropna(inplace=True)
    # preprocessed_chats = preprocessed_chats.reindex()
    preprocessed_chats.reset_index(inplace=True, drop=True)

    # embeded_chats = get_embedding(preprocessed_chats) # add embeded columns to the chats dataframe
    # embeded_chats.to_csv("./embeded_chats.csv", index=False)
    embeded_chats = pd.read_csv("./embeded_chats.csv")

    loaded_model = pickle.load(open(MODEL_PATH, "rb"))
    embeded_chats["embedding"] = embeded_chats.embedding.apply(eval).apply(np.array,dtype=object)
    # embeded_chats["embedding"] = embeded_chats.embedding.apply(eval).apply

    # y_predicted = loaded_model.predict(list(embeded_chats["embedding"]))
    # embeded_chats["pred"]=y_predicted
    # embeded_chats.to_csv("./pred_chats.csv", index=False)
    embeded_chats = pd.read_csv("./pred_chats.csv")
    print("embeded_chats.columns.values__> ",embeded_chats.columns.values)
    print(handle_votes(embeded_chats))

    # dataset.dropna(axis=0, inplace=True)


# you can use loaded model to compute predictions


if __name__ == "__main__":
    run()
    pass
