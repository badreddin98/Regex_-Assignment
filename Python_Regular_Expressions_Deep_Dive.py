import re
# Task: Email Extraction Enhancement:
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
# (?!exclude\.com) - Negative lookahead to ensure the domain is not 'exclude.com'
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)