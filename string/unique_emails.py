def numUniqueEmails(emails):
    '''
    For each email, apply the following rules:
    remove periods from the first half of string
    remove all words on and after the +

    Push the updated word into a set
    Return the length of the set
    '''
    def edit_email(email):
        first, last = email.split('@')
        first = first.replace('.', '')
        if '+' in first:
            end = first.index('+')
            first = first[:end]
        return first + '@' + last

    s = set()
    for email in emails:
        s.add(edit_email(email))
    return len(s)


emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
res = numUniqueEmails(emails)
print(f'\nres: {res}')
