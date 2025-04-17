#!/usr/bin/env python
# coding: utf-8

# In[2]:


def test_even_nums(answer):
    truth = np.arange(2,1001, 2)
    try:
        assert(np.array_equal(answer, truth))
        print("Good job!")
    except AssertionError:
        print(f"Hmm it looks like this isn't quite right. Try again!")


# In[ ]:


def test_random_stats(array, mean, std):
    mean_t = array.mean()
    sd_t = array.std()
    try:
        assert(mean_t == mean and std == sd_t)
        print("Good job!")
    except AssertionError:
        print(f"Hmm it looks like this isn't quite right. Try again!")


# In[ ]:


def generate_random_test_scores(count):
    return np.random.randint(0, 100, count)


# In[ ]:


def test_score_filter(scores, answer):
    fm = scores > 59
    truth = scores[fm]
    try:
        assert(np.array_equal(answer, truth))
        print("Good job!")
    except AssertionError:
        print(f"Hmm it looks like this isn't quite right. Try again!")


# In[ ]:


def test_gaga_row(df, answer):
    truth = df[df['Name'] == 'Lady Gaga'].iloc[0]
    if isinstance(answer, pd.DataFrame):
        answer = answer.iloc[0]
    try:
        assert(np.array_equal(answer, truth))
        print("Good job!")
    except AssertionError:
        print(f"Hmm it looks like this isn't quite right. Try again!")


# In[ ]:


def test_groupby_fun(df):
    return df.groupby(['Genre'], as_index=False).agg({'Age': 'mean', 'Grammys': 'sum'})

