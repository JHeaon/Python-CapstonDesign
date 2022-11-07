import re
import matching_braille as mb


def main(text="⠁⠝⠀⠈⠎⠈⠕⠀⠑⠅⠣⠬⠦"):
    text = re.sub("\n|\r", "", text)  # 줄바꿈 처리
    text = pre_assemble(text)
    string = analyze(text).replace("", '\n')
    print(assemble(string))


def analyze(text):
    text = list(text)
    answer = ""

    for i in range(len(text)):
        for j in range(len(mb.key["kr"])):
            if mb.key["kr"][j][1] == 2:
                if text[i] == mb.key["kr"][j][1][0] and text[i] == mb.key["kr"][j][1][1]:
                    text[i] == mb.key["kr"][j][0]
                    text[i + 1] = ""
                    break
            elif text[i] == mb.key["kr"][j][1]:
                text[i] = mb.key["kr"][j][0]

    return "".join(text)


def pre_assemble(text):
    # ㅅㅆㅈㅉㅊ 뒤에 ㅕㅇ, ㅓㅇ 변환
    text = re.sub("([⠠⠨⠰])⠻", "\1ᅥᆼ", text)

    # 한글 문장부호 변환 먼저
    text = text.replace("⠐⠂", ":").replace(
        "⠦⠄", "(").replace("⠠⠴", ")").replace("⠼", "")
    text = re.sub("⠸([⠭⠴]+)⠇", "\1", text)
    return text


def assemble(text):

    # 문장부호
    text = re.sub("⠀", " ", text)

    text = re.sub("ᇁ\s", ". ", text)
    text = re.sub("ᇁ$", ". ", text)
    text = re.sub("ᄅ\s", ", ", text)
    text = re.sub("ᄅ$", ", ", text)
    text = re.sub("ᇂᆺ", "\'", text)
    text = re.sub("ᇀ\s", "?", text)
    text = re.sub("ᇀ$", "?", text)
    text = re.sub("ᆿ\s", "!", text)
    text = re.sub("ᆿ$", "!", text)

    # 모음 뒤에 '예'가 올 때는 붙임표
    text = re.sub("([ᅡ-ᅵ])\(붙임\)ᆻ", "\1예", text)

    # ㅑ, ㅘ, ㅜ, ㅝ 뒤에 '애'가 올 때는 붙임표
    text = re.sub("([ᅣᅪᅮᅯ])\(붙임\)ᅢ", "\1애", text)
    text = re.sub("([ᄀ-ᄒ])\(붙임\)", "\1ᅡ", text)

    # 팠 폐
    text = re.sub("ᄑᆻ", "폐", text)

    # 이중모음
    text = re.sub("ᅮᅢ", "ᅱ", text)
    text = re.sub("ᅣᅢ", "ᅤ", text)
    text = re.sub("ᅯᅢ", "ᅰ", text)
    text = re.sub("ᅪᅢ", "ᅫ", text)

    # 쌍시웃 받침 약자
    text = re.sub("([ᅡ-ᅵ])ᅨ", "\1ᆻ", text)

    # ㅏ 생략된거 복원 [ᄀ-ᄒ](?!\w)
    text = re.sub("([ᄀ-ᄒ])((?=[^ᅡ-ᅵ])|$)", "\1ᅡ", text)

    # 초성 없는거에 ㅇ 붙임 // .replace(/(?<=[^ᄀ-ᄒ])([ᅡ-ᅵ])/g, "ᄋ$1")
    text = re.sub("([^ᄀ-ᄒ])(?=[ᅡ-ᅵ])", "\1ᄋ", text)

    # 중성 먼저 시작하면 ㅇ 붙임
    text = re.sub("(^[ᅡ-ᅵ])", "ᄋ\1", text)  # 문장부호

    return text


