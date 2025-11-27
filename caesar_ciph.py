import string

MSG = """xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"""

MSG_2_ENCODE = """hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"""

MSG1 = """jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."""

MSG2 = (
    """bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"""
)

MSG3 = """vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."""


def caesar_decode(message, offset):
    alphabet = list(string.ascii_lowercase)
    decoded = ""
    for l in message:
        if l == " ":
            decoded += " "
            continue
        elif l == "." or l == "?" or l == "!" or l == "'":
            decoded += l
            continue
        position = alphabet.index(l) + 1
        position += offset
        if position > 26:
            position -= 26
        new_letter = alphabet[position - 1]
        decoded += new_letter
    return decoded


def caesar_encode(message, offset):
    alphabet = list(string.ascii_lowercase)
    encode = ""
    for l in message:
        if l == " ":
            encode += " "
            continue
        elif l == "." or l == "?" or l == "!" or l == "'":
            encode += l
            continue
        position = alphabet.index(l) + 1
        position -= 10
        new_letter = alphabet[position - 1]
        encode += new_letter
    return encode


print(caesar_decode(MSG, 10))
print(caesar_encode(MSG_2_ENCODE, 10))
print(caesar_decode(MSG1, 10))
print(caesar_decode(MSG2, 14))
for i in range(1, len(list(string.ascii_lowercase))):
    print(caesar_decode(MSG3, i))
print(caesar_decode(MSG3, 7))
