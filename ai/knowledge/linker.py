from rapidfuzz import fuzz


class KnowledgeLinker:

    def __init__(self, threshold: int = 90):
        self.threshold = threshold

    def find_matches(self, nodes):

        linked = {}

        used = set()

        for i, node in enumerate(nodes):

            if i in used:
                continue

            group = [node]
            used.add(i)

            for j in range(i + 1, len(nodes)):

                if j in used:
                    continue

                score = fuzz.ratio(
                    node.id.lower(),
                    nodes[j].id.lower()
                )

                if score >= self.threshold:
                    group.append(nodes[j])
                    used.add(j)

            linked[node.id] = group

        return linked