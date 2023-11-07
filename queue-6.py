def movesToStamp(stamp, target):
    def can_stamp(s, t, idx):
        changed = False
        for i in range(len(s)):
            if t[idx + i] == '?':
                continue
            if t[idx + i] != s[i]:
                return False, changed
            changed = True
        return changed, changed

    def do_stamp(s, t, idx):
        changed = False
        for i in range(len(s)):
            if t[idx + i] == '?':
                continue
            if t[idx + i] != s[i]:
                t = t[:idx + i] + '?' + t[idx + i + 1:]
                changed = True
        return t, changed

    m, n = len(stamp), len(target)
    res = []
    changed = True

    while changed:
        changed = False
        for i in range(n - m + 1):
            change, current_changed = can_stamp(stamp, target, i)
            if change:
                target, changed = do_stamp(stamp, target, i)
                res.append(i)

        if not changed and target != '?' * n:
            return []

    return res[::-1] if target == '?' * n else []

print(movesToStamp("abc", "ababc")) 
print(movesToStamp("abca", "aabcaca")) 
