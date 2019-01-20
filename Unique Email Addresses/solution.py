def numUniqueEmails(emails):
    seen = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        seen.add((local, domain))

    return len(seen)

list_of_emails = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com']

print('Total unique emails:', numUniqueEmails(list_of_emails))
