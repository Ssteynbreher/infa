emails = {
    'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
    'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
    'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
    'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
    'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']
}
def format_emails(emails_dict):
    formatted_emails = []
    for domain, usernames in emails_dict.items():
        for username in usernames:
            formatted_emails.append(f"{username}@{domain}")
    return formatted_emails
formatted_emails = format_emails(emails)
for email in formatted_emails:
    print(email)