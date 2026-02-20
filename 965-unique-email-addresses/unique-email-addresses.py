class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            # Drop everything after '+'
            local = local.split('+')[0]
            # Remove all dots
            local = local.replace('.', '')
            # Add normalized email to set
            unique.add(local + '@' + domain)
        return len(unique)