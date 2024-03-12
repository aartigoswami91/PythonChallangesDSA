class LongPressedString:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, t = 0, 0
        n_len, t_len = len(name), len(typed)

        while n < n_len and t < t_len:
            if name[n] == typed[t]:
                n += 1
                t += 1
            elif t > 0 and typed[t] == typed[t - 1]:
                t += 1
            else:
                return False

        while t < t_len and typed[t] == typed[t - 1]:
            t += 1
        return n == n_len and t == t_len
    
bject1 = LongPressedString()
name = "alex"
typed = "aaleex"

print(bject1.isLongPressedName(name,typed))