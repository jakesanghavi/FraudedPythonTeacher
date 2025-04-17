#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def test_groceries(groceries):
    try:
        assert(sorted(groceries) == ['apples', 'eggs', 'milk'])
        print('Good job!')
    except AssertionError:
        print("Hmm it looks like this isn't quite right. Try again!")


# In[ ]:


def test_groceries2(groceries):
    try:
        assert(len(groceries) == 4 and len(set(groceries)) == 4 and \
               set([groceries[0]] + groceries[2:]).issubset(['apples', 'eggs', 'milk', 'strawberries']))
        assert(groceries[1] == 'flour')
        print('Good job!')
    except AssertionError:
        print("Hmm it looks like this isn't quite right. Try again!")


# In[ ]:


def test_grocery_prices(groceries):
    try:
        assert(milk_price == grocery_prices['milk'])
        assert(grocery_prices.get('strawberries') is not None)
        assert(grocery_prices['eggs'] > 3.79)
        print('Good job!')
    except AssertionError:
        print("Hmm it looks like this isn't quite right. Try again!")


# In[ ]:


def list100(empty):
    try:
        assert(empty == [x for x in range(1,101)])
        print('Good job!')
    except AssertionError:
        print("Hmm it looks like this isn't quite right. Try again!")


# In[ ]:


def good_day(greeting_message, current_time):
    try:
        correct_greeting = 'night' if current_time < 4 or current_time > 6 \
        else ('afternoon' if current_time > 12 else 'morning')
        assert(correct_greeting in greeting_message.lower())
        print('Good job!')
    except AssertionError:
        print("Hmm it looks like this isn't quite right. Try again!")


# In[ ]:


def computer_lab(computer):
    try:
        assert(computer.company and computer.company.lower() == 'apple' and computer.size and (computer.size == 15 \
        or computer.size == '15') and computer.color and computer.color.lower() == 'blue')
        print('Good job!') 
    except AssertionError:
        print("Hmm it looks like this isn't quite right. Try again!")

