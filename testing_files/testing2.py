#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np
from collections import Counter


# In[2]:


def find_max_index_sol(l1, l2):
    l3 = [x + y for x, y in zip(l1, l2)]
    
    return np.argmax(l3)


# In[3]:


def test_max_index(answer, l1, l2):
    truth = find_max_index_sol(l1, l2)
    try:
        assert(answer == truth)
        print("Good job!")
    except AssertionError:
        print(f"Hmm it looks like this isn't quite right. Try again! The answer should be {truth}")


# In[4]:


def pick_random_names(count):
    common_names = [
    "Alex", "Taylor", "Jamie", "Jordan", "Morgan",
    "Chris", "Casey", "Drew", "Avery", "Riley",
    "Cameron", "Reese", "Blake", "Harper", "Skyler",
    "Logan", "Peyton", "Rowan", "Emerson", "Quinn",
    "Dakota", "Elliot", "Charlie", "Finley", "Jesse",
    "Sage", "Phoenix", "Spencer", "Tatum", "Shiloh",
    "Devin", "Hayden", "River", "Justice", "Remy",
    "Sasha", "Parker", "Micah", "Noel", "Frankie",
    "Rory", "Arden", "Lennon", "Oakley", "Ellis",
    "Hunter", "Indigo", "Marley", "Blair", "Greer",
    "Sky", "Taylor", "Reagan", "Quincy", "Angel",
    "Jaden", "Kennedy", "Kendall", "Alexis", "Bailey", "Neha", "Pragya"
    ]
    return [random.choice(common_names) for _ in range(count)]


# In[5]:


def names_counter(names):
    return dict(Counter(names))


# In[6]:


def test_count_swifties(answer, swifties):
    truth = names_counter(swifties)
    try:
        assert(answer == truth)
        print("Good job!")
    except AssertionError:
        print("Hmm it looks like this isn't quite right. Try again!")


# In[7]:


import math

class Tribute:
    def __init__(self, name, height, weight, district):
        self.name = name
        self.height = height  # in in
        self.weight = weight  # in lb
        self.district = district

    def __repr__(self):
        return (f"Tribute(name='{self.name}', height={self.height} in, "
                f"weight={self.weight} lb, district={self.district})")

def generate_random_tribute():
    first_names = [
        "Katniss", "Peeta", "Rue", "Cato", "Clove", "Finnick", "Annie", "Gale",
        "Alex", "Jordan", "Taylor", "Casey", "Morgan", "Skyler", "Drew", "Avery",
        "Ash", "Flint", "Nova", "Zane", "Lyra", "Vega", "Onyx", "Rex", "Sable"
    ]

    last_names = [
        "Everdeen", "Mellark", "Hawthorne", "Odair", "Crest", "Thorne", "Ashfall",
        "Stone", "Blight", "Vire", "Ember", "Storm", "Blackwell", "Rowe", "Vale",
        "Nyx", "Rook", "Frost", "Hollow", "Shade", "Winter", "Stroud", "Crane",
        "Locke", "Cross", "Draven", "Wolfe"
    ]

    first = random.choice(first_names)
    last = random.choice(last_names)
    full_name = f"{first} {last}"
    height = random.randint(46, 79)   # in
    weight = random.randint(75, 250)    # lb
    district = random.randint(1, 12)
    
    return Tribute(full_name, height, weight, district)

def generate_random_tributes(number):
    return [generate_random_tribute() for _ in range(number)]

def pick_winning_tribute(tributes):
    max_vf = -float('inf')
    winning_tribute = None
    
    for tribute in tributes:
        tribute.vf = tribute.height**(3/2) * math.sqrt(tribute.weight) / math.sqrt(tribute.district)
        
        if tribute.vf > max_vf:
            max_vf = tribute.vf
            winning_tribute = tribute
    
    return winning_tribute


# In[8]:


def test_hunger_games(answer, tributes):
    truth = pick_winning_tribute(tributes)
    try:
        assert(answer == truth)
        print("Good job!")
    except AssertionError:
        print(f"Hmm it looks like this isn't quite right. Try again! The top tribute should be named {truth.name}.")


# In[9]:


def generate_att_usage_data(count):
    names = set(pick_random_names(count))
    usage_data = {}

    for name in names:
        shape = np.random.uniform(2, 2.5)
        scale = np.random.uniform(28, 32)
        months = random.randint(5, 25)

        will_spike = np.random.rand() < 0.01
        spike_month = random.randint(0, months - 1) if will_spike else -1

        monthly_usage = []

        for i in range(months):
            base = np.random.weibull(shape) * scale
            if i == spike_month:
                base *= np.random.uniform(0.01, 0.05)
            monthly_usage.append(round(base, 2))

        usage_data[name] = monthly_usage

    return usage_data


# In[10]:


def get_data_outliers(usage_dict):
    bad_users = []
    
    for item in usage_dict.items():
        itemu = np.mean(item[1])
        for itemv in item[1]:
            if itemv < itemu/10:
                bad_users.append(item[0])
                break
    
    return bad_users


# In[11]:


def test_att_outliers(answer, usage_dict):
    truth = get_data_outliers(usage_dict)
    try:
        assert(answer == truth)
        print("Good job!")
    except AssertionError:
        print(f"Hmm it looks like this isn't quite right. Try again! The answer should be {truth}.")


# In[12]:


def caesar_shift(keyword, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_keyword = ''
    
    for char in keyword.upper():
        if char in alphabet:
            shifted_index = (alphabet.index(char) + shift) % 26
            shifted_keyword += alphabet[shifted_index]
        else:
            shifted_keyword += char  # Non-alphabet characters remain unchanged
    
    return shifted_keyword


# In[13]:


def real_lyrics():
    lyrics = """Fever dream high in the quiet of the night
    You know that I caught it (oh yeah, you're right, I want it)
    Bad, bad boy, shiny toy with a price
    You know that I bought it (oh yeah, you're right, I want it)
    Killing me slow, out the window
    I'm always waiting for you to be waiting below
    Devils roll the dice, angels roll their eyes
    What doesn't kill me makes me want you more
    And it's new, the shape of your body
    It's blue, the feeling I've got
    And it's ooh, whoa-oh
    It's a cruel summer
    "It's cool, " that's what I tell 'em
    No rules in breakable heaven
    But ooh, whoa-oh
    It's a cruel summer with you (yeah, yeah)
    Hang your head low in the glow of the vending machine
    I'm not dying (oh yeah, you're right, I want it)
    You say that we'll just screw it up in these trying times
    We're not trying (oh yeah, you're right, I want it)
    So cut the headlights, summer's a knife
    I'm always waiting for you just to cut to the bone
    Devils roll the dice, angels roll their eyes
    And if I bleed, you'll be the last to know, oh
    It's new, the shape of your body
    It's blue, the feeling I've got
    And it's ooh, whoa-oh
    It's a cruel summer
    "It's cool, " that's what I tell 'em
    No rules in breakable heaven
    But ooh, whoa-oh
    It's a cruel summer with you
    I'm drunk in the back of the car
    And I cried like a baby coming home from the bar (oh)
    Said, "I'm fine, " but it wasn't true
    I don't wanna keep secrets just to keep you
    And I snuck in through the garden gate
    Every night that summer, just to seal my fate (oh)
    And I screamed, "For whatever it's worth
    I love you, ain't that the worst thing you ever heard?"
    He looks up, grinnin' like a devil
    It's new, the shape of your body
    It's blue, the feeling I've got
    And it's ooh, whoa-oh
    It's a cruel summer
    "It's cool, " that's what I tell 'em
    No rules in breakable heaven
    But ooh, whoa-oh
    It's a cruel summer with you
    I'm drunk in the back of the car
    And I cried like a baby coming home from the bar (oh)
    Said, "I'm fine, " but it wasn't true
    I don't wanna keep secrets just to keep you
    And I snuck in through the garden gate
    Every night that summer, just to seal my fate (oh)
    And I screamed, "For whatever it's worth
    I love you, ain't that the worst thing you ever heard?"
    (Yeah, yeah, yeah, yeah)"""
    
    return lyrics


# In[14]:


def encrypt_lyrics():
    lyrics = real_lyrics()
    return caesar_shift(lyrics, 22)


# In[15]:


def keep_letters_and_spaces(s):

    return ''.join(char for char in s if char.isalpha() or char == ' ')


# In[16]:


def test_unencrypted_lyrics(answer):
    truth = keep_letters_and_spaces(real_lyrics()).lower()
    try:
        answer = keep_letters_and_spaces(answer).lower()
        assert(answer == truth)
        print("Good job!")
    except (AssertionError, TypeError):
        print("Hmm it looks like this isn't quite right. Try again!")


# In[17]:


def generate_celebrity_relationship_matrix(n):
    celebrity_names = [
        "Dwayne Johnson", "Ariana Grande", "Taylor Swift", "Kim Kardashian", "Chris Hemsworth",
        "Scarlett Johansson", "Beyonce", "Leonardo DiCaprio", "Rihanna", "Shawn Mendes",
        "Tom Hanks", "Zendaya", "Selena Gomez", "Drake", "Kylie Jenner",
        "Will Smith", "Emma Watson", "Brad Pitt", "Angelina Jolie", "Johnny Depp",
        "Miley Cyrus", "Jennifer Lopez", "Robert Downey Jr.", "Kanye West", "Justin Bieber",
        "Priyanka Chopra", "George Clooney", "Billie Eilish", "Zendaya", "David Beckham",
        "Lady Gaga", "Tom Cruise", "Keanu Reeves", "Eva Mendes", "Matt Damon", "Julia Roberts"
    ]
    
    selected_names = random.sample(celebrity_names, n)

    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            rand = random.random()

            if rand < 0.50:
                matrix[i][j] = matrix[j][i] = 1
            elif rand < 0.85:
                matrix[i][j] = matrix[j][i] = 0
            else:
                matrix[i][j] = matrix[j][i] = -1

    return selected_names, matrix


# In[18]:


def can_invite_group(love_hate_matrix, group):
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            if love_hate_matrix[group[i]][group[j]] == -1 or love_hate_matrix[group[j]][group[i]] == -1:
                return False
    return True


# In[19]:


def max_party_invites_solution(n, love_hate_matrix, names):
    best_group = []
    max_likes = -1
    
    for mask in range(1, 1 << n):
        group = [i for i in range(n) if (mask & (1 << i)) > 0]
        
        if can_invite_group(love_hate_matrix, group):
            likes = sum(love_hate_matrix[i][j] == 1 for i in group for j in group if i != j)
            
            if likes > max_likes:
                best_group = group
                max_likes = likes
    
    return [names[i] for i in best_group]


# In[20]:


def max_party_invites_test(answer, n, love_hate_matrix, names):
    truth = max_party_invites_solution(n, love_hate_matrix, names)
    try:
        assert(answer == truth)
        print("Good job!")
    except (AssertionError, TypeError):
        print(f"Hmm it looks like this isn't quite right. Try again! The answer should be {truth}.")


# In[ ]:




