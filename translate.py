# formcharcode => ord


# 한글 자음, 모음, 받침 자름
class hangulToJaso():
    def translate(self, text):
        chars = []
        v = []

        for i in range(len(text)):
            chars.append(ord(text[i]))
            if chars[i] >= int("0xAC00", 16) and chars[i] <= int("0xD743", 16):
                v.append(self.iSound(chars[i]))
                v.append(self.mSound(chars[i]))
                if self.tSound(chars[i] != ""):
                    v.append(self.tSound(chars[i]))
                else:
                    v.append(chr(chars[i]))

        return v

    # 자음 처리
    def iSound(self, a):
        r = int(((a - int('0xac00', 16)) / 28) / 21)
        t = chr(r + int('0x1100', 16))
        print(t)
        return t

    # 모음 처리
    def mSound(self, a):
        r = int(((a - int('0xac00', 16)) / 28) % 21)
        t = chr(r + int('0x1161', 16))
        print(t)
        return t

    # 받침 처리
    def tSound(self, a):
        r = int((a - int('0xac00', 16)) % 28)
        t = ""
        if r == 0:
            return ""
        else:
            return chr(r + int('0x11A8', 16) - 1)


def translate_braille(text):
    case = hangulToJaso()
    text = case.translate(text)
    print(text)
    # text = re.sub(r"\d+", '⠼$1', text)
    # text = re.sub(r"[×○]+", '⠸$1⠇', text)
    print(text)

    # for i in range(len(text)):
    #     if ord(text[i]) >= int("0xFF01", 16) and ord(text[i]) <= int("0xFF5E", 16):
    #         text[i] = e
    #     elif ord(text[i]) >= int("0x0041", 16) and ord(text[i]) <= int("0x005D", 16):
    #         pass
    #     elif ord(text[i]) >= int("0x3041", 16) and ord(text[i]) <= int("0x3096", 16):
    #         pass
