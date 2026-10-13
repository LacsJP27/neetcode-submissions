class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # iterate through all emails
        # for each email
            # split the email at '@' into local and domain
            # create a local that evaluates to the raw name
            # construct a new email with dots and + ignores
            # store the email in a set if not already in the set
        # return the length of the set
        unique = set()
        for email in emails:
            splitEmail = email.split('@')
            # test.jp, neetcode.com
            local, domain = splitEmail[0], splitEmail[1]
            temp = ''

            for c in local:
                if c == '+':
                    break
                if c == '.':
                    continue
                temp += c

            local = temp
            unique.add(local + '@' + domain)

        return len(unique)



