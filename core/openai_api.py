import pandas as pd
import numpy as np 
import openai  # for OpenAI API calls
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

from utils.text import compute_token_count

openai.api_key = "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"

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(7))
def embedding_with_backoff(input_data: list):
    # input_data.
    return openai.Embedding.create(model="text-embedding-ada-002", input=input_data)

def get_embedding(chats:pd.DataFrame):
    i = 0
    token_count = 0
    prev_index = 0
    # chats_limit_bound = []
    # chats = chats[chats["text"] != ""]
    chats["embedding"] = np.nan
    embed_index = chats.columns.get_loc("embedding")

    data_len = len(chats)
    text_index = chats.columns.get_loc("text")
    while i < data_len:
        chat = chats.iloc[i]
        print(chat["text"])
        chat_tokens_count = compute_token_count(chat["text"])

        # print(i,chat_tokens_count,token_count,token_count + chat_tokens_count > 4096,i + 1 == len(chanell),)
        if token_count + chat_tokens_count > 8192:
            # slice_embed=chats.iloc[(prev_index) : i , text_index]
            # chats.iloc[(0 if i == 0 else i + 1) : i, embed_index] = embedding_with_backoff(
            #     slice_embed
            # )
            prev_index = 0 if prev_index == 0 else prev_index + 1

            print("s1")
            print(f"i: {i}, prev_index: {prev_index}")
            slice_embed = list(chats.iloc[prev_index:i, text_index])
            embeddings = embedding_with_backoff(slice_embed)
            embed_str_list = [str(embed["embedding"]) for embed in embeddings["data"]]
            chats.iloc[prev_index:i, embed_index] = embed_str_list
            print("s2")
            # chats_limit_bound.append(i - 1)
            prev_index = i - 1
            token_count = 0
        elif i + 1 == data_len:
            prev_index = 0 if prev_index == 0 else prev_index + 1
            print("f1")
            print(f"i: {i}, prev_index: {prev_index}")
            slice_embed = list(chats.iloc[prev_index : i + 1, text_index])
            embeddings = embedding_with_backoff(slice_embed)
            embed_str_list = [str(embed["embedding"]) for embed in embeddings["data"]]
            chats.iloc[prev_index : i + 1, embed_index] = embed_str_list
            print("f2")
            # chats.iloc[prev_index : i + 1, embed_index] = embedding_with_backoff(slice_embed)
            # chats_limit_bound.append(i)
            prev_index = i
            token_count = 0
            i += 1
        else:
            token_count += chat_tokens_count
            i += 1
    return chats