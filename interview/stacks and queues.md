1 -**Queue with two stacks**.

 Implement a queue with two stacks so that each queue operations takes a constant amortized number of stack operations.

**sol**: 

* enqueue : push elements onto a stack1
* dequeue : if another stack is empty, for each element in stack 1, pop them then push them in stack 2. then pop from stack 2

2 -**Stack with max** Create a data structure that efficiently supports the stack operations (push and pop) and also a return-the-maximum operation. Assume the elements are reals numbers so that you can compare them.

**sol:** Use two stacks, one to store all of the items and a second stack to store the maximums.

3 -**Java generics** Explain why Java prohibits generic array creation.

**sol:** Java arrays are covariant but Java generics are not: that is, **String[]** is a subtype of **Object[]**, but **Stack<String\>** is not a subtype of **Stack<Object\>**. So when arrays object is created, it should be provided explicitly about  type of array, including an explicit component type. However, Generic types in code are a compile-time illusion.That means it represents a type that is unknown at runtime, and thus you cannot create an array of T since you cannot provide the component type needed to create the array.