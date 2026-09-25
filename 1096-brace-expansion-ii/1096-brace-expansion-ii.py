class Solution:
    def braceExpansionII(self, expression):
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    sub, i = parse(i + 1)
                    current = {a + b for a in current for b in sub}

                else:
                    ch = expression[i]
                    current = {a + ch for a in current}
                    i += 1

            result |= current
            return result, i + 1

        result, _ = parse(0)
        return sorted(result)