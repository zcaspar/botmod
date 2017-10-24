
# coding: utf-8

# In[5]:

import itertools
from itertools import combinations


# In[6]:

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


# In[7]:

def no_factors(x):
   # This function takes a number and prints the number of its factors
    factor_list = []
    for i in range(1, x + 1):
       if x % i == 0:
           factor_list.append(i)
    return (len(factor_list))


# In[8]:

def find_next_triangle(n):
    # Input a number, ouput a number
    return sum(range(n+1))


# In[9]:

def is_it_tri(n):
    x = (8*n + 1)
    y = (x**0.5 - 1) / 2
    if int(y) == y:
        return 1
    else:
        return 0


# In[10]:

def next_prime(current_prime):
    counter = 0
    test_subject = current_prime + 2
    while counter < current_prime/2:
        if is_prime(test_subject) == 1:
            return test_subject
        else:
            counter += 1
            test_subject +=2


# In[11]:

def prime_list(no_sought):
    # Enter the number of primes as an integer to return the first no_sought primes in a list [2,3,5]
    prime_list = [2,3]
    while len(prime_list) < no_sought+1:
        prime_list.append(next_prime(prime_list[-1]))
    return prime_list[0:-1]


# In[12]:

def is_prime(input):
    # Enter a number, return 1 if prime or 0 if not
    counter = 3
    if input == 2:
        return 1
    if input%2 == 0:
        return 0
    while counter < (input/2):
        if input%counter == 0:
            return 0
        counter += 2
    return 1


# In[13]:

def compute_permutations(input_list):
    # Enter indices or primes as a list to output all the permutations of those indices/primes as list of tuples [(2,3,5),(2,5,3)]
    return list(itertools.permutations(input_list, len(input_list)))


# In[14]:

def perms_by_constant_index(prime_list,index):
# The index here is constant, so we run through all the different perms of the prime list. Return a list of
# any triangulars
# Input = list of primes e.g. [2,3,5,7] and the max. index e.g. 9
# Output = list of triangular numbers
    triangular_list = []
    perms = compute_permutations(prime_list)
    for i in perms:
        index_list_no = len(index) - 1
        product = 1
        while index_list_no > 0:
            product *= i[index_list_no]**index[index_list_no]
            index_list_no -= 1
            if index_list_no == 0:
                if is_it_tri(product) == 1 and product not in triangular_list and product !=0:
                    triangular_list.append(product)
                    product = 1
    return triangular_list


# In[15]:

def indices_by_constant_primes(index_list,prime_list):
    # Input = list of primes e.g. [2,3,5,7] and a list of indices e.g. [2,2,2,2]
    # Output = list of triangular numbers
    triangular_list = []
    indices = compute_permutations(index_list)
    for i in indices:
        index_list_no = len(prime_list) - 1
        product = 1
        while index_list_no > 0:
            product *= i[index_list_no]**index[index_list_no]
            index_list_no -= 1
            if index_list_no == 0:
                if (is_it_tri(product) == 1 and product not in triangular_list and product !=0):
                    triangular_list.append(product)
                    product = 1
    return triangular_list


# In[16]:

def cycling_both(prime_list,index):
    triangular_list = []
    indices = compute_permutations(index)
    perms = perms_by_constant_index(index,prime_list)
    for j in indices:
        for i in perms:
            triangular_list.append(i)
    return min(triangular_list)


# # What do we have by this stage?#

# - The knowledge that if you take the indices of a group of primes, add one to each of them and multiply them together, then the result gives you the number of factors the product of the base primes
# - A way to find n prime numbers
# - A way to check if a number is a triangle number
# - A way to check all permutations of a list of primes raised to certain powers (eventually powers+1 equalling more than 500)
# - A way to check all permustations of a list of indices when the list of bases (primes) remain constant

# # Next Step #

# Find a way to take [2,2,2,2,2,2,2,2,2] to [2,2,2,2,2,2,2,2,3] etc.

# In[17]:

def get_indices(start_no,end_no):
    list_of_lists = [start_no]
    while start_no != end_no:
        start_no += 1
        list_of_lists.append(start_no)
    return list_of_lists
    


# In[18]:

def numbers_to_list(input_list):
    # Take regular numbers e.g. 123 and turn into [123]
    return [input_list]


# In[19]:

def comma_numbers(input_string):
    # Takes e.g. [111] as input and outputs [1,1,1]
    output_list = []
    string = str(input_string)
    for i in string:
        output_list.append(int(i))
    return output_list


# In[20]:

def list_of_numbers(start_no, end_no):
    # input a start and end no to return a list of list of numbers between those numbers.
    # Input 111,112 to ouput [[1,1,1],[1,1,2]]
    number_list = get_indices(start_no,end_no)
    all_lists = []
    bigger_list = []
    str_list = []
    for i in number_list:
        next_list = numbers_to_list(i)[0]
        all_lists.append(next_list)
    for i in all_lists:
        bigger_list.append(numbers_to_list(i)[0])
    for i in bigger_list:
        sep_no = comma_numbers(i)
        str_list.append(sep_no)
    return str_list


# In[21]:

def list_to_500(input1):
    #input a list and output the product of each member of that list multiplied together as an integer
    list_length = len(input1)
    product = 1
    i = 0
    while i < list_length:
        product *= (input1[i]+1)
        i+=1
    return product


# In[22]:

mi_list = list_of_numbers(1111111111,1111111199)


# Find a way to take [111] and turn into [1,1,1]

# In[23]:

prime_list(10)


# In[24]:

list_to_500([1,2,3])


# In[25]:

3*5**2*7**3


# In[ ]:

final_list = []
for i in mi_list:
    the_list = perms_by_constant_index(prime_list(10),i)
    if len(the_list) > 0:
        final_list.append(the_list)
    print (i,the_list)
print (min(final_list))


# Using the above code I found out 236215980 is a triangle number, is reached in this way: 2**2*3*3
# *5*7*11*13*19*23 and has 768 factors. Though it is not the answer so we have to look at less than 9 indices.

# In[ ]:

is_it_tri(4573800)


# In[ ]:

prime_factors(4573800)


# In[ ]:

no_factors(25725)


# In[ ]:



