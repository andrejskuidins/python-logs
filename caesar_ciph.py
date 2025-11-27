import string

MSG = """xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"""

MSG_2_ENCODE = """hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"""

MSG1 = """jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."""

MSG2 = (
    """bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"""
)

MSG3 = """vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."""

MSG4 = """txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"""  # friends
MSG4_t = "you were able to decode this? nice work! you are becoming quite the expert at cryptography!"  # friends


def vignere_decode(message, keyword):
    alphabet = list(string.ascii_lowercase)
    keyword_phrase = []
    counter = 0
    decoded = ""
    for l in message:
        if l == "." or l == "?" or l == "!" or l == " ":
            keyword_phrase.append(l)
            decoded += l
            continue
        if counter > len(keyword) - 1:
            counter = 0
            keyword_phrase.append(keyword[counter])
        else:
            keyword_phrase.append(keyword[counter])
        position = alphabet.index(l) + 1
        position2 = alphabet.index(keyword[counter]) + 1
        position_final = position + position2
        if position_final > 26:
            position_final -= 26
        new_letter = alphabet[position_final - 2]
        decoded += new_letter
        counter += 1
    return decoded


def vignere_encode(message, keyword):
    alphabet = list(string.ascii_lowercase)
    keyword_phrase = []
    counter = 0
    decoded = ""
    for l in message:
        if l == "." or l == "?" or l == "!" or l == " ":
            keyword_phrase.append(l)
            decoded += l
            continue
        if counter > len(keyword) - 1:
            counter = 0
            keyword_phrase.append(keyword[counter])
        else:
            keyword_phrase.append(keyword[counter])
        position = alphabet.index(l) + 1
        position2 = alphabet.index(keyword[counter]) + 1
        position_final = position - position2
        new_letter = alphabet[position_final]
        decoded += new_letter
        counter += 1
    return decoded


print(vignere_decode(MSG4, "friends"))
print(vignere_encode(MSG4_t, "friends"))


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
    if "computers" in caesar_decode(MSG3, i):
        print(caesar_decode(MSG3, i))
