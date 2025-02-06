fav_langs = {
    'jen':['python','rust'],
    'sarah':['c'],
    'ed':['rust''go'],
    'phil':['python','haskell'],
    }
for name, langs in fav_langs.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in langs:
        print(f"\t{language.title()}")