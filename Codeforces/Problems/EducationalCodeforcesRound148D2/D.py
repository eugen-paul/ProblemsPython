"""internet solution:
https://codeforces.com/blog/entry/116396


First of all, if k <= n the solution is easy, so everything I will say is for k > n.

If you perform an even number of operations on an element you are guaranteed to decrease some value from it, 
since for each number you add you subtract a bigger number right after, so if you are trying to increase a value 
(and therefore made an odd number of operations) it's really only the last number you add that is the "deciding factor".

Knowing that, you should try to have the smallest number of your array, let's call it a(0), 
be added by K and a(1) by K-1, a(2) by K-2, ..., a(n) by K-n.

If (K-n) is an even number you can do it, because for each of the operations before getting to k-n 
you can just do an even number of operations on each element you change and you are going to end with all elements being ready for an addition.

Also, performing an addition and right after a subtraction, is going to result in decreasing the element by one, 
so you just have to add each (K-i) to each a(i) and then remove (K-n)/2, in total, from the elements of the resulting array, 
distributing it the best way to get the biggest minimum value.

If (K-n) is odd you won't be able to increase every element of the array, because to do that you need an odd number of operations on each element, 
but at least one element will necessarily have an even number of operations on it, so the best you can do is make this element the biggest one, a(n), 
and not add anything to it (instead of decreasing it) then you can add each value from k-n+1 to k to each element from a(0) to a(n-1) 
and you are gonna have an even number of operations left. Then again, you will remove (K-n+1)/2 from the resulting array in the best way possible.

If you want to solve D2 you do the same thing, but with some tricks to make it all faster, I can describe them if you want.
"""
import sys


input = sys.stdin.readline

n, q = map(int, input().split())
a0 = sorted(map(int, input().split()))
ak = list(map(int, input().split()))
res = []
for k in ak:
    a = a0[:]
    if k <= n:
        inc, dec = k, 0
    else:
        inc = n - (n - k) % 2
        dec = (k - inc) // 2
    for i in range(inc):
        a[i] += k - i
    mn = min(a)
    s = sum(a) - mn * n
    res.append(mn - (max(0, dec - s) + n - 1) // n)
print(*res)
