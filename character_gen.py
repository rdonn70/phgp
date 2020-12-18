import random

def town_gen(climate='plains'):    
    name_based_on_climate = random.randint(0, 2)
    if name_based_on_climate <= 1:
        name = ''
        syllables = ['mor', 'del', 'gol', 'bel', 'com', 'ere', 'gon', 'an', 'bar', 'es']
        x = 0
        while x < 2:
            name += syllables[random.randint(0, (len(syllables) - 1))]
            x += 1
        name = name.capitalize()
        return name
    else:
        gen_adjectives = ['placeholder']
        if climate == 'plains':
            adjectives = ['placeholder']
        elif climate == 'mountains':
            adjectives = ['placeholder']
        elif climate == 'hills':
            adjectives = ['placeholder']
        elif climate == 'coast':
            adjectives = ['placeholder']
        name = gen_adjectives[random.randint(0, (len(gen_adjectives) - 1))]
        name += ' ' + adjectives[random.randint(0, (len(adjectives) - 1))]
        name = name.capitalize()
        return name

def firstname():
    name = ''
    syllables = ['mor', 'sha', 'an', 'ann', 'rash', 'izen', 'alo', 'var', 'oros', 'golo', 'ale']
    num = random.randint(2, 3)
    x = 0
    while x < num:
        name += syllables[random.randint(0, (len(syllables) - 1))]
        x += 1
    if random.randint(0, 1) == 1 and name[len(name) - 1] != 'a' and name[len(name) - 1] != 'e' and name[len(name) - 1] != 'i' and name[len(name) - 1] != 'o' and name[len(name) - 1] != 'u':
        letter = random.randint(0, 4)
        if letter == 0:
            name += 'a'
        elif letter == 1:
            name += 'e'
        elif letter == 2:
            name += 'i'
        elif letter == 3:
            name += 'o'
        else:
            name += 'u'
    name = name.capitalize()
    return name
#wip
def lastname():
    name = ''
    syllables = []
    num = random.randint(1, 2)
    x = 0
    while x < num:
        name += syllables[random.randint(0, (len(syllables) - 1))]
        x += 1
    name = name.capitalize()
    return name
    
def char_gen():
    personality_traits = ['imaginative', 'creative', 'original', 'curious', 'conscientious', 'hard-working', 'organized', 'punctual', 'conformist', 'talkative', 'active', 'affectionate', 'trusting', 'lenient', 'soft-hearted', 'good-natured', 'worried', 'temperamental', 'self-conscious', 'emotional']
    age = random.randint(0, 100)
    name = firstname()
    last_char = name[-1]
    gender_roll = random.randint(0, 99)
    if(last_char == 'e' or last_char == 'a' or last_char == 'i' or last_char == 'u' or last_char == 'y'):
        gender = 'Female'
    else:
        gender = 'Male'
    if gender == 'Female' and gender_roll == 1:
        gender = 'Male'
    elif gender == 'Male' and gender_roll == 1:
        gender = 'Female'
    d100 = random.randint(0, 100)
    if(d100 <= 1):
        if(gender == 'Male'):
            rank = 'King'
        else:
            rank = 'Queen'
    if(1 < d100 <= 81):
        rank = 'Peasant'
    if(81 < d100 <= 100 and age >= 20):
        if(gender == 'Male'):
            rank = 'Noble Sir'
        else:
            rank = 'Noble Dame'
    else:
        rank = 'Peasant'
            
    for x in range(20):
        personality_traits[x] = random.randint(0, 1)
        
    if(personality_traits[1] >= personality_traits[2]):
        personality_traits[2] = personality_traits[1]
    else:
        personality_traits[1] = personality_traits[2]
    if(personality_traits[6] >= personality_traits[7]):
        personality_traits[7] = personality_traits[6]
    else:
        personality_traits[6] = personality_traits[7]
    if(personality_traits[19] == 1):
        personality_traits[18] = 1
        personality_traits[17] = 1
        personality_traits[16] = 1
    else:
        personality_traits[18] = 0
        personality_traits[17] = 0
        personality_traits[16] = 0

    return [name, age, gender, rank, personality_traits, 'location']

if __name__ == "__main__":
    people = []
    amount_of_characters = int(input("Amount of Characters: "))
    for x in range(amount_of_characters):
        people.append(char_gen())
    
    with open('character_data.json', 'w') as f:
        for s in people:
            f.write(str(s) + '\n')
    with open('character_data.json', 'r') as f:
        people = [line.rstrip('\n').rstrip('"') for line in f]
    
    print(people)