import re

def check_copy_paste(text):
    """
    Detect repeated sentences or phrases.
    """
    sentences = [s.strip() for s in re.split(r'[.!?]', text) if s.strip()]
    seen = set()
    for s in sentences:
        if s in seen:
            return True, "copy_paste"
        seen.add(s)
    return False, ""

def check_excessive_links(text, max_links=3):
    """
    Detect if text contains too many links.
    """
    links = re.findall(r'http[s]?://\S+', text)
    if len(links) > max_links:
        return True, "excessive_links"
    return False, ""

def check_duplicate_text(text, past_texts):
    """
    Detect if text was previously seen.
    """
    if text in past_texts:
        return True, "duplicate_text"
    return False, ""
