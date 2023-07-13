from TeamX.modules.language import gs


def helps(chat):
    return gs(chat, "tools_help")

__help__ = """
  ──「 TOOLS 」──
  
 • /tgm :Get Telegraph Link Of Replied Media
 • /tgt :Get Telegraph Link of Replied Text
*Chatbot* 
_Admins only:_
 • /addchat*:* Enables Chatbot mode in the chat.
 • /rmchat*:* Disables Chatbot mode in the chat.
*Date-time-Weather*
 • /time <country code>*:* Gives information about a timezone.
 • /weather <city>*:* Get weather info in a particular place.
 • /wttr <city>*:* Advanced weather module, usage same as /weather
 • /wttr moon*:* Get the current status of moon
*Converts*
 • /encrypt*:* Encrypts The Given Text
 • /decrypt*:* Decrypts Previously Ecrypted Text
 • /zip*:* reply to a telegram file to compress it in .zip format
 • /unzip*:* reply to a telegram file to decompress it from the .zip format
"""
__mod_name__ = "Tools"
