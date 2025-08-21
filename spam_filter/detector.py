import json
from .rules import check_copy_paste, check_excessive_links, check_duplicate_text

class SpamDetector:
    def __init__(self, config):
        self.config = config
        self.past_texts = set()

    def analyze_bid(self, bid):
        text = bid['bid_text']
        spam = False
        triggered = []

        if self.config['rules'].get('copy_paste', True):
            cp, rule = check_copy_paste(text)
            if cp:
                spam = True
                triggered.append(rule)

        if self.config['rules'].get('excessive_links', True):
            el, rule = check_excessive_links(text)
            if el:
                spam = True
                triggered.append(rule)

        if self.config['rules'].get('duplicate_text', True):
            dt, rule = check_duplicate_text(text, self.past_texts)
            if dt:
                spam = True
                triggered.append(rule)

        self.past_texts.add(text)
        confidence = min(1.0, 0.7 + 0.1 * len(triggered))

        return {
            "id": bid["id"],
            "bidder_name": bid["bidder_name"],
            "bid_text": text,
            "spam": spam,
            "triggered_rules": triggered,
            "confidence": confidence
        }


