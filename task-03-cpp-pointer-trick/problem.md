# Problem: The Ghost Pointer (C++ Memory)

## Task
Implement a simple `SharedBuffer` class in C++ that manages a heap-allocated integer array.

Requirements:
1. It must track how many "references" point to the buffer.
2. When a `SharedBuffer` is copied, it should NOT copy the data, just increment the reference count.
3. When a `SharedBuffer` is destroyed, it should decrement the count. If the count reaches zero, delete the data.
4. **The Twist:** Implement a `get_alias()` method that returns a raw pointer to the data. 

## The Challenge
Identify the bug in a specific "Aliasing" scenario where a user gets a raw pointer, the original `SharedBuffer` objects go out of scope, but the raw pointer is still used.

## Statement
Provide a C++ implementation of this class and a `main` function that demonstrates the "Dangling Pointer" risk when mixing manual aliasing with reference counting.
