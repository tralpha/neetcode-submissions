class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # NODE: AI
        adj = {c: set() for w in words for c in w}
        indeg = {c: 0 for c in adj}
        # EDGES ZZCCU
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if y not in adj[x]:
                        adj[x].add(y); indeg[y] += 1
                    break
            else:
                if len(a) > len(b):
                    return ""
        # KAHN - SDPD
        # SEED
        q = deque(c for c in indeg if indeg[c] == 0)
        out = []
        while q:
            # POP
            c = q.popleft(); out.append(c)
            for nb in adj[c]:
                # DROP
                indeg[nb] -= 1
                if indeg[nb] == 0:
                    # PUSH
                    q.append(nb)
        # CYCLE-CHECK
        return "".join(out) if len(out) == len(indeg) else ""
        