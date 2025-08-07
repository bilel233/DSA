# dans cet exercice, nous allons voir la concatenation de deux
#chaines de caracteres


def concatenate(s1,s2):
    """renvoie la concatenation de s1 et s2"""

    return s1 + s2

def my_methode_concatenate(s1,s2):
    """renvoie la concatenation de deux chaines de caracteres s1 et s2"""

    res = ''

    for k in s1:
        res = res + k
    for k in s2:
        res = res + k
    return res

if __name__ == "__main__":
    assert concatenate("Bilel","yoh") == "Bilelyoh"
    assert concatenate("lelbi", " et la force") == "lelbi et la force"

    assert my_methode_concatenate("Hello","World") == "HelloWorld"
