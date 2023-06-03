from telethon.sync import TelegramClient, connection
import datetime
import pandas as pd

print("telgeraaaaaaaaaaaaaaaaaam")

from constants import COMMUNITIES, SUBGROUPS

# Remember to use your own values from my.telegram.org!
api_id = 23316483
api_hash = "41e58d027579ade30d3e505a48fe3679"
client = TelegramClient("stock", api_id, api_hash)

# chats = ['smartboursegroup', 'close_trades','smartbourse_com','hezartahlil_g','saahmii','amir_ramzali','fundamental_View','MajidSoltany','Goldenn_Bourse']
# chats = ["smartboursegroup"]
# import datetime
# client =  TelegramClient('test', api_id, api_hash)

all_chat_list = {
    # community["name_id"]: {
    key: {
        "id": None,
        "community_name": None,
        "messages": [],
    }
    for key, community in COMMUNITIES.items()
}
proxy = (
    "2020haghll.co.apple.com.co.uk.do_yo.want_to.clash_with.this.microsoft.com.there_is_no.place_nano.localhost.bing.com.count_with_me.cyou.com.now_sudo.rm_rf.ddns.net.we_are_here.again_to_fight.with_everyone.i_am.the_internet.special_waya.api-botads23.co.uk",
    443,
    "0xee1603010200010001fc030386e24c3add686167682e7374617469632e666172616b61762e636f6d",
)


async def get_communities_chats(offsetdate: datetime.date = datetime.date.today()):
    # df = pd.DataFrame()
    async with TelegramClient(
        "stock_prog",
        api_id,
        api_hash,
        # connection=connection.ConnectionTcpMTProxyAbridged,
        # proxy=proxy,
    ) as client:
        for community_name, value in COMMUNITIES.items():
            # community_name = value["name_id"]
            all_chat_list[community_name]["community_name"] = community_name
            all_chat_list[community_name]["type"] = value["type"]
            client
            chats = client.iter_messages(
                community_name, offset_date=datetime.date.today(), reverse=True
            )

            async for message in chats:
                if not message.action:
                    print(message)
                    data = {
                        # "group": community,
                        "chat_id": message.id,  ###
                        "person_id": message.sender_id,  ###
                        "org_text": message.text,  #
                        "date": message.edit_date
                        if message.edit_date
                        else message.date,  #
                        # "action": message.action if message.action else None,  #
                        "reply_to_message_id": message.reply_to.reply_to_msg_id
                        if message.reply_to
                        else None,  ##
                    }

                    all_chat_list[community_name]["id"] = message.peer_id.channel_id
                    all_chat_list[community_name]["messages"].append(data)
        return all_chat_list


# df.to_excel("telegrammmm.xlsx".format(datetime.date.today()), index=False)

#  {community: {"id": None, "messages": []}} for community in communities}

# import datetime
# client =  TelegramClient('test', api_id, api_hash)
# df = pd.DataFrame()
# all_chat_list = []


# temp_df = pd.DataFrame(data, index=[1])
# df = df.append(temp_df)

# df['date'] = df['date'].dt.tz_localize(None)

# df.to_excel("telegrammmm.xlsx".format(datetime.date.today()), index=False)
all_chat_list
