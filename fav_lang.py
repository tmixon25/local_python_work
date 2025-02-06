fav_lang = {
    'jen':'python',
    'sarah':'c',
    'ed':'rust',
    'phil':'python',
    }

friends = ['phil','sarah']
for name in fav_lang.keys():
    print(f"Hi {name.title()}.") 
    if name in friends:
        language = fav_lang[name].title()
        print(f"\t{name.title()}, I see you love {language}!") 

for language in set(fav_lang.values()):
    print(language.title())
# language = fav_lang['sarah'].title()
# print(f"Sarah's fav lang is {language}.")

# for name, language in fav_lang.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")
