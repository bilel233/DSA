# dans cet exercice on va inserer un caractere c dans une chaine s


def insertion(s,c,pos):
    """insere c dans s a pos"""

    return s[0:pos] + c + s[pos:len(s)]

# on teste

if __name__ == '__main__':
    assert insertion('yoh','Y',0) == 'Yyoh'
    assert insertion('lelbi','e',4) == 'lelbei'