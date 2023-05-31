import re
import pandas as pd
import numpy as np


def handle_votes(labeled_chats):
    votes = {}
    communities = labeled_chats["channel_name"].unique()  ##Telegram groups and channels
    for com in communities:
        com_chats = labeled_chats[labeled_chats["channel_name"] == com]
        votes[com] = {}
        # com_votes = pd.DataFrame()
        print("****", com)
        for _, row in com_chats.iterrows():
            included_stocks = re.findall(r"<([ا-ی]*)>", row["text"])
            print("*_ORG_>", list(set(included_stocks)))
            # if row["text"].str.contains('بررسی|تحلیل|?|؟', regex=True)
            if row["reply_to_message_id"]:
                # com_chats[]
                replied_from_filter = labeled_chats["reply_to_message_id"].isin(
                    [row["reply_to_message_id"]]
                )
                print(
                    'row["reply_to_message_id"],',
                    len(labeled_chats[replied_from_filter]),
                    labeled_chats[replied_from_filter]["text"],
                )
                replied_from_stocks = re.findall(
                    r"<([ا-ی]*)>", str(labeled_chats[replied_from_filter]["text"])
                )
                included_stocks.extend(replied_from_stocks)
                print("*_EXTEND_ORG_>", included_stocks)
                # print("reply_to_message_id", row["reply_to_message_id"])

            for stock in list(set(included_stocks)):
                votes[com][stock] = (
                    # votes[com][stock] if (stock in votes[com]) else stock_interface
                    votes[com][stock]
                    if (stock in votes[com])
                    else {}
                )
                # pd.concat([])
                print("\stock ------", stock)
                print("\row[pred ------", row["pred"])
                # repeated_stock_count = len(included_stocks)
                # stock_filter =
                if row["pred"] in votes[com][stock]:
                    # votes[com][stock][row["pred"]]={}
                    votes[com][stock][row["pred"]]["chat_id_list"].add(row["chat_id"])
                    votes[com][stock][row["pred"]]["pers_id_list"].add(row["person_id"])
                    votes[com][stock][row["pred"]]["chat_id_count"] = len(
                        votes[com][stock][row["pred"]]["chat_id_list"]
                    )
                    votes[com][stock][row["pred"]]["pers_id_count"] = len(
                        votes[com][stock][row["pred"]]["pers_id_list"]
                    )
                else:
                    votes[com][stock][row["pred"]] = {
                        "chat_id_list": {row["chat_id"]},
                        "pers_id_list": {row["person_id"]},
                        "chat_id_count": 1,
                        "pers_id_count": 1,
                    }
                    # votes[com][stock][row["pred"]]={"chat_id_list":{row["chat_id"]} , "pers_id_list":set((row["person_id"])),"chat_id_count":1,"pers_id_count": 1 }

    return votes
    # print(com_chats["channel_name"].unique())
