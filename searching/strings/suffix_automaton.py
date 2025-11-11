class SuffixAutomaton:
    def __init__(self):
        self.len = [0]
        self.link = [-1]
        self.next = [{}]
        self.last = 0  # the state representing the entire prefix processed so far

    def extend(self, c):
        p = self.last
        cur = len(self.len)
        self.len.append(self.len[p] + 1)
        self.link.append(0)
        self.next.append({})
        while p != -1 and c not in self.next[p]:
            self.next[p][c] = cur
            p = self.link[p]
        if p == -1:
            self.link[cur] = 0
        else:
            q = self.next[p][c]
            if self.len[p] + 1 == self.len[q]:
                self.link[cur] = q
            else:
                clone = len(self.len)
                self.len.append(self.len[p] + 1)
                self.next.append(self.next[q].copy())
                self.link.append(self.link[q])
                while p != -1 and self.next[p].get(c) == q:
                    self.next[p][c] = clone
                    p = self.link[p]
                self.link[q] = self.link[cur] = clone
        self.last = cur
