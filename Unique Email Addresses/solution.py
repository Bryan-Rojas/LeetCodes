def numUniqueEmails(emails):
    s = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0].replace('.', '')
        s.add((local, domain))

    return len(s)

list_of_emails = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com', 'testemail+david@lee.tcode.com']

print('Total unique emails:', numUniqueEmails(list_of_emails))
