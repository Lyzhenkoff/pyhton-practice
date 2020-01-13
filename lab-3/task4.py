class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        d = {}
        for idx, s in enumerate(transactions):
            name, time, amount, city = s.split(',')
            if name not in d: d[name] = []
            d[name].append((idx, int(time), int(amount), city))
        for name in d:
            d[name].sort(key=lambda s: s[1])

        added = set()
        res = []
        for name in d:
            for i in range(len(d[name])):
                flag = False
                idx, t, a, c = d[name][i]
                for j in range(i + 1, len(d[name])):
                    idx2, t2, a2, c2 = d[name][j]
                    if t2 - t > 60: continue
                    if c2 != c:
                        res.append(transactions[idx2])
                        added.add(idx2)
                        flag = True
                if flag or a > 1000:
                    res.append(transactions[idx])
                    added.add(idx)
        return list(set(res))