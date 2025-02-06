def describe_pet (pet_name, animnal_type='dog'):
    """Disply inifo about a pet."""
    print(f"\nI have a {animnal_type}.")
    print(f"My {animnal_type}'s name is {pet_name.title()}.")

#Positional arguments
# describe_pet('hamster','harry')
# describe_pet('dog','willie')

# Keyword arguments
# describe_pet(animnal_type='hamster', pet_name='harry')

#defaul values
describe_pet(pet_name='willie')
describe_pet(animnal_type='hamster', pet_name='harry')