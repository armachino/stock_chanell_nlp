# %%time
import pandas as pd
import re
import pathlib

from constants import SUBGROUPS,COMMUNITIES
from utils.text import clean_text, compute_token_count, norm


# print(pathlib.Path().resolve())


stocks = pd.read_csv(str(pathlib.Path().resolve()) + "/core/stocks_tsetmcs.csv")
stocks = stocks[["sym_name", "name", "sym", "gp_name"]]
exlude_list = ["بورس","ما", "تمدن"]
stocks = stocks[~stocks["sym_name"].isin(exlude_list)]


def if_stock_included_replace(txt):
    txt = norm(txt)
    #     txt_list=txt.split()

    for index, row in stocks.iterrows():
        norm_sym = norm(row["sym_name"]).replace("\u200c", " ")
        # txt = re.sub(rf"\b{norm_sym}\b", f"<{row['sym']}>", txt)
        txt = re.sub(rf"\b{norm_sym}\b", f"<{norm_sym}>", txt)
    #     print("replace_stock_with_idـ",norm_sym)
    # if re.findall(r"<[0-9A-Za-z]*>", txt):

    if re.findall(r"<[آا-ی\s]*>", txt):
        return True, txt
    return False, txt


def is_id_in_chatlist(chatlist, ID):
    #     print("CHATLIS__",chat_list)
    for chat in chatlist:
        if ID == chat["chat_id"]:
            return True
    return False


def preprocess_subgroup2(data: object):
    # data_id = str(data["id"])
    com_name = data["community_name"]

    print("__> preprocess_subgroup", data["community_name"])
    # messages = boursgram_data["messages"]
    chat_list = []
    for mess in data["messages"]:
        txt = clean_text(mess["org_text"])
        print("__> chat_id", mess["chat_id"])

        if compute_token_count(txt) > 450:
            continue

        is_stock_included, rep_txt = if_stock_included_replace(txt.strip())
        mess["text"] = rep_txt
        # mess["channel_id"] = data_id
        print("[opics__>",mess["reply_to_message_id"] not in COMMUNITIES[com_name]["topics"])
        if (
            ("reply_to_message_id" in mess)
            and (
                (  ## checks in public_supergroup that have topics,wheter the replied messaged is not replied to the topics ID
                    data["type"] == "public_supergroup"
                    and (com_name in COMMUNITIES)
                    and (mess["reply_to_message_id"] not in COMMUNITIES[com_name]["topics"])
                )
                or (data["type"] != "public_supergroup")
            )
            and (is_id_in_chatlist(chat_list, mess["reply_to_message_id"]))
        ):
            # chat_info["reply_to_message_id"] = mess["reply_to_message_id"]
            #         txt_rep = replace_stock_with_id(txt.strip())
            # chat_info["text"] = txt
            chat_list.append(mess)
            #                 print(cht["id_list"])
            # print("looooool")
        #     is_included,txt = replace_stock_with_id(txt.strip())
        elif is_stock_included:
            # chat_info["text"] = txt
            chat_list.append(mess)

    return {**data, "messages": chat_list}


# print(chat_list_1)
#


# returns just chats included stocks without any description.
def extract_just_stocks_chats(chats: pd.DataFrame): 
    clear_stock_names = (
        chats["text"].str.replace("<([ا-ی]*)>", "", regex=True).str.strip()
    )
    return chats[clear_stock_names == ""]
