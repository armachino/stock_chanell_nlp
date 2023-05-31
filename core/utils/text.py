import re
from parsivar import Normalizer
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

def clean_text(txt):
    replacement_patterns = {
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+": "",  # website
        r"[\w\.-]+@[\w\.-]+": "",  # email
        r"@[A-Za-z0-9]*": "",  # @ID
        r"#": "",
        r"\n{2,}": "\n",
    }
    for pattern, replacement in replacement_patterns.items():
        txt = re.sub(pattern, replacement, txt)
    return txt


def norm(txt):
    return Normalizer().normalize(txt)


def compute_token_count(txt):
    return len(enc.encode(txt))
