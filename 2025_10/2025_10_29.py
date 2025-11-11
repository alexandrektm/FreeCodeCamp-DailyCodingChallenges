def sort(emails):

    new_emails = []
    final_emails = []

    for email in emails:
        user, domain = email.split("@")
        new_email = "@".join([domain, user])
        new_emails.append(new_email)

    sorted_emails = sorted(new_emails, key=str.casefold)

    for email in sorted_emails:
        domain, user = email.split("@")
        final_email = "@".join([user, domain])
        final_emails.append(final_email)

    return final_emails


print(sort(["sam@MAIL.com", "amy@mail.COM", "bob@Mail.com"]))