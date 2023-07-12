import re
import imaplib
import email

# Gmail IMAP configuration
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993
USERNAME = 'Enter Email'
PASSWORD = 'Enter Password'

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

# Login to your Gmail account
mail.login(USERNAME, PASSWORD)

# Select the mailbox (e.g., "inbox")
mail.select("inbox")

# Search for email messages
status, data = mail.search(None, "ALL")

def is_entry_duplicate(entry, file_path):

    # Checks if an entry already exists in the specified file.
    # Returns True if a duplicate is found, False otherwise.

    with open(file_path, "r") as f:
        for line in f:
            if entry == line.strip():
                return True
    return False

# Store the email contents in a file
with open("emails.txt", "w") as f:
    for num in data[0].split():
        # Fetch the email data
        status, data = mail.fetch(num, "(RFC822)")
        raw_email = data[0][1]

        # Parse the raw email data
        msg = email.message_from_bytes(raw_email)

        # Get the email body
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    body = part.get_payload(decode=True)
                    # Decode using utf-8 and ignore errors
                    body = body.decode("utf-8", errors="ignore")
                    # Check if the email body contains the text "-" and doesn't contain "-"
                    if "Specify Data" in body and "Specify Data" not in body:
                        # Extract the "Details" section
                        details_match = re.search(r'"Details":\s*"([^"]+)"', body)
                        if details_match:
                            details = details_match.group(1)
                            # Check if the details line contains "-" and/or "-" (case-insensitive)
                            if not re.search(r'Specify Data' or 'Specify Data', details, re.IGNORECASE):
                                f.write(details + "\n")
        else:
            body = msg.get_payload(decode=True)
            # Decode using utf-8 and ignore errors
            body = body.decode("utf-8", errors="ignore")
            # Check if the email body contains the text "-" and doesn't contain "-"
            if "Specify Data" in body and "Specify Data" not in body:
                # Extract the "Details" section
                details_match = re.search(r'"Details":\s*"([^"]+)"', body)
                if details_match:
                    details = details_match.group(1)
                    # Check if the details line contains "-" and/or "-" (case-insensitive)
                    if not re.search(r'Specify Data' or 'Specify Data', details, re.IGNORECASE):
                        f.write(details + "\n")

# Logout and close the connection
mail.logout()

print("Text labeled 'Details' between curly braces in emails with '----data' text (excluding '----' and '-----') and excluding '...' has been stored in emails.txt")
