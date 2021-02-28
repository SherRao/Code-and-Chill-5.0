def letterCasePermutation(S):
    if S is None:
        return []
    output = []

    def ul(s, snew):
        if s[0].isalpha():
            if len(s) == 1:
                output.append(snew+s[0].lower())
                output.append(snew+s[0].upper())
            else:
                ul(s[1:], snew+s[0].lower())
                ul(s[1:], snew+s[0].upper())
        else:
            if len(s) == 1:
                output.append(snew+s[0])
            else:
                ul(s[1:], snew+s[0])
    ul(S, '')
    return list(set(output))
