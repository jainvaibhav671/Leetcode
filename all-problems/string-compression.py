class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt: int = 0
        res = []

        for i in range(len(chars)):
            if i == 0:
                cnt += 1
                continue
            
            if chars[i] != chars[i-1]:
                if cnt == 1:
                    res.append(chars[i-1])
                elif cnt > 1:
                    res.append(chars[i-1])
                    res.extend(list(str(cnt)))
                cnt = 1
            else:
                cnt += 1
        
        if cnt == 1:
            res.append(chars[-1])
        else:
            res.append(chars[-1])
            res.extend(list(str(cnt)))

        chars.clear()
        chars.extend(res)
        return len(chars)
