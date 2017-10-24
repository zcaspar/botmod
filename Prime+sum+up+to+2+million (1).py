
# coding: utf-8

# In[1]:

def is_prime(input):
    counter = 3
    if input%2 == 0:
        return 0
    while counter < (input/2):
        if input%counter == 0:
            return 0
        counter += 2
    return 1


# In[2]:

def next_prime(current_prime):
    counter = 0
    test_subject = current_prime + 2
    while counter < current_prime/2:
        if is_prime(test_subject) == 1:
            return test_subject
        else:
            counter += 1
            test_subject +=2


# In[3]:

def list_generator(upper_limit):
    potential_primes = [i for i in range(0,upper_limit)]
    return potential_primes


# In[4]:

def prime_list(upper_limit):
    prime_list = [2,3]
    while prime_list[-1] < upper_limit:
        if len(prime_list) % 10000 == 0:
            print ("The number of primes found is " + str(len(prime_list)))
        prime_list.append(next_prime(prime_list[-1]))
    return prime_list[0:-1]


# In[5]:

# Put in the prime used as sieve and list of possible primes, return: sieved list
def sieve_of_eratosthenes(upper_limit):
    prime_list1 = prime_list(upper_limit**(0.5))
    potential_primes = list_generator(upper_limit)
    for i in prime_list1:
        remove_multiples(i,potential_primes)
    counter1 = 0
    list_length = len(potential_primes)
    potential_primes = potential_primes[::-1]
    for i in potential_primes:
        if is_prime(i) == 0 and i != 0:
            potential_primes[counter1] = 0
        counter1 += 1
        if counter1 % 1000 == 0:
            print(str(round((counter1/list_length*100),2)) + "% complete")
    list_of_primes = set(potential_primes)
    my_list = []
    for i in list_of_primes:
        my_list.append(i)
    my_list = sorted(my_list)
    return my_list


# In[6]:

def remove_multiples(factor,possible_primes):
    factor_position = possible_primes.index(factor)
    counter = 1
    # possible_primes[(counter * factor_position)] = 0
    while len(possible_primes) >= ((counter+1) * factor_position)-1:
        if counter > 1:
            possible_primes[counter * factor_position] = 0
        counter += 1
    return possible_primes


# In[7]:

fiftyfivegrand = sieve_of_eratosthenes(100000)


# In[9]:

bbbb = str(sum(fiftyfivegrand))
# %save my_useful_session 1
get_ipython().magic('save final_answer_1 bbbb')


# In[ ]:



