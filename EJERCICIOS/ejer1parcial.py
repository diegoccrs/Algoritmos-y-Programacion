"""
Dada una lista de números de tamaño 2n con elementos de la forma
`[x1,x2,...,xn,y1,y2,...,yn].`
Realice una función que regrese una lista organizada de la siguiente forma.
`[x1,y1,x2,y2,...,xn,yn]`

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]
"""


def organizar(nums, n, aux):
    for e in range(0, len(nums)//2):
        aux.append(nums[e])
        aux.append(nums[e+n])
    return aux

nums = [1, 1, 2, 2]
n = 2
aux = []

print(organizar(nums, n, aux))