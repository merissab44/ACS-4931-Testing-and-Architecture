# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def toxin_alert():
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
def toxin_free_alert():
    print('***')
    print('Toxin Free')
    print('***')

ingredients = ['sodium benzoate']
harmful_ingredients = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']

for ingredient in ingredients:
    if ingredient in harmful_ingredients:
        toxin_alert()
    # make_alert_sound()
    else:
        toxin_free_alert()
