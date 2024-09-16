"""
Code verifiant si une chaine de caractere est un palindrome
"""

#### Fonction secondaire

def ispalindrome(p):
    "fonction verifiant si il s'agit d'un palindome"
    table = p.maketrans('êéèëàùôç','eeeeauoc',"-?!,': ")
    p=p.lower()
    p=p.translate(table)
    print(p)
    if p[::-1] == p:
        return True
    return False


#### Fonction principale

def main():
    "fonction principale qui appelle la secondaire et effectue le test"
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
