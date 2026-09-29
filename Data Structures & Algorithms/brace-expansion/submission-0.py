class Solution:
    def expand(self, s: str) -> List[str]:
        out = []
        string_so_far = ""
        for idx, c in enumerate(s):
            if c == "{":
                options = []
                for R in range(idx+1, len(s)):
                    curr = s[R]
                    if curr == "}":
                        break
                    if curr == ",":
                        continue
                    options.append(curr)
            
                for option in options:
                    ret = self.expand(option + s[R+1:])
                    out.extend(string_so_far + ret[i] for i in range(len(ret)))
                return out
            else:
                string_so_far += c
        out.append(string_so_far)
        return out
        