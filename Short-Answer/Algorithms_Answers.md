#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

```python
    # This is going to be O(1)
    a = 0
    # This loop will run O(n) times
    while (a < n * n * n)
      # a is incremented by n**2 each loop
      # multiplying, addition and assignment is O(1)
      a = a + n * n
    # time complexity is O(1 + n + 1) = O(n)
```

b)

```python
    # This is going to be O(1)
    sum = 0
    # The outer loop runs in O(n) * the complexity of the inner loop
    for i in range(n):
      # This is O(1)
      j = 1
      # j doubles with each iteration, this loop is O(log n)
      while j < n:
        # this is O(1)
        j *= 2
        # This is O(1)
        sum += 1

    # time complexity is O(1) + O(n) * (O(log n) * O( 1 + 1))
    #                           == O(1) + O(n) * O(log n)
    #                           == O(n log n)
```

c)

```python
    def bunnyEars(bunnies):
      # This is going to be O(1)
      if bunnies == 0:
        return 0

      # 'bunnies' decreases by 1 on each recursion
      # so bunnyEars will recurse n times
      return 2 + bunnyEars(bunnies-1)

      # time complexity is O(1) + O(n)
      #                              == O(n)
```

## Exercise II

Binary search tree

The first egg drop will be at the halfway point of the building height n //2

If the egg breaks, we want to insert {f: false} to the right of the tree, f represents the floor and false means egg has not broken. Then we run again from floor f // 2

If the egg doesn't break, we insert {f: true} to the left of the tree, f being the floor and true being egg did not break. Next run from (n + f) // 2 the halfway point between middle and top

Continue this process until the BST's get_max ( on condition that the egg survived ) returns true and also the BST's contains method returns true for a value 1 higher than the max.
