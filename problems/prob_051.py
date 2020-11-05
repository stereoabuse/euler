################################################################################
#                          Project Euler Problem 051                           #
#                     https://projecteuler.net/problem=051                     #
#                                                                              #
# Author:   Chris B.                                                           #
# Date:     November 05, 2020                                                  #
################################################################################

def prob_051():
    
    def prime_group(x):
        '''Returns a list of booleans.  Assumes the input number
        is a string with a ? for the digit to replace'''
        digits = '0123456789'
        return sum(1 for d in digits if is_prime(int(x.replace('?', d))))

    
    def ordering(n_digits):
        '''Returns a sorted list showing the index ordering for N digits of how to check'''
        all_combos, result = [], []
        for i in range(1, n_digits):
            all_combos += list(combinations(list(range(n_digits -1)), i))
        for t in all_combos:
            item = ''.join([str(i) if i in t else ' ' for i in range(n_digits)])
            item_2 = [i for i in range(n_digits) if i in t]
            result.append((item, item_2))
        results = sorted(result, key=lambda result: result[0])
        return_val = [r[1] for r in results]
        return_val.remove([0,1,2])
        return return_val
    ans = []
    low, high = 100001, 188001 * 100
    for n in range(low, high, 2):
        order = ordering(len(str(n)))
        for item in order:
            num_string = list(str(n))
            for index in item:
                num_string[index] = '?'
            if prime_group(''.join(num_string)) == 8 and is_prime(n):
                ans.append(n)
                if len(ans) == 2:
                    return ans[1]
                break

prob_051()