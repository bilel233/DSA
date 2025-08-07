# dans cet exercice, nous allons voir la concatenation de deux
#chaines de caracteres


def concatenate(s1,s2):
    """renvoie la concatenation de s1 et s2"""

    return s1 + s2

if __name__ == "__main__":
    assert concatenate("Bilel","yoh") == "Bilelyoh"
    assert concatenate("lelbi", " et la force") == "lelbi et la force"