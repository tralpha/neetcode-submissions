class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # NODES AI
        adj = {c: set() for word in words for c in word}
        indeg = {c: 0 for c in adj}
        # EDGES ZZCCUU
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if y not in adj[x]:
                        adj[x].add(y)
                        indeg[y] += 1
                    break
            else:
                if len(a) > len(b):
                    return ""
        # KHAN SEED --> POP --> DROP --> PUSH
        # SEED
        q = deque([c for c in indeg if indeg[c] == 0])
        out = []
        while q:
            # POP
            c = q.popleft(); out.append(c)
            for nb in adj[c]:
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    # PUSH
                    q.append(nb)
        # CYCLE CHECK
        return "".join(out) if len(indeg) == len(out) else ""