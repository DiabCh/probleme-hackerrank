'''You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized:

%

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains  space separated integers  and .
The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.

Constraints





Output Format

Output a single integer denoting the value .

Sample Input

3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
Sample Output

206
Explanation

Picking  from the st list,  from the nd list and  from the rd list gives the maximum  value equal to % = .'''

from itertools import product
def func(possible_com, M, outcomes=[], total = 0):
    for element in possible_com:
        total = 0
        for sub_element in element:
            total += sub_element**2

        outcomes.append(total % M)

    print(outcomes)
    print(max(outcomes))




# K,M = map(int,input().split())
# array = []
# for i in range(K):
#     to_add = input().split()
#     to_add = [int(x) for x in to_add]
#     array.append(list(to_add[1:]))


K,M = 1, 384
array = []
for i in range(K):
    to_add = input().split()
    to_add = [int(x) for x in to_add]
    array.append(list(to_add[1:]))


if K == 1:
    results = []
    for element in array:
        for sub_element in element:
            results.append((sub_element**2)%M)
    print(max(results))

else:
    possible_com = list(product(*array))
    print(possible_com)
    func(possible_com, M)
