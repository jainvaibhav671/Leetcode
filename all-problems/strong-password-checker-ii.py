class Solution:

    def strongPasswordCheckerII(self, password: str) -> bool:
        
        if len(password) < 8:
            return False

        special_chars: str = "!@#$%^&*()-+"
        flags: List[bool] = [False] * 4
        for i in range(len(password)):
            ch: str = password[i]
            key: int = ord(ch)

            if i > 0 and password[i] == password[i-1]:
                return False

            if key >= 97 and key <= 122:
                # mark lower case to True
                flags[0] = True
            
            elif key >= 65 and key <= 90:
                # mark upper case to True
                flags[1] = True
            
            elif key >= 48 and key <= 57:
                # mark digit to True
                flags[2] = True
            elif ch in special_chars:
                # mark special char to True
                flags[3] = True


        return all(flags)
