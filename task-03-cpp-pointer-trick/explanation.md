# Why LLMs Fail: The Ghost Pointer

## The Trap
This is a "Use-After-Free" (UAF) scenario masked by a custom reference-counting implementation. LLMs are generally good at recognizing standard smart pointers like `std::shared_ptr`, but when you ask them to implement a **custom** one with a back-door like `get_alias()`, they lose track of the lifecycle.

## Common LLM Failures
1. **The 'Everything is Fine' Fallacy:** LLMs often assume that if a class has a destructor that handles `delete`, the code is "safe." They forget that returning a raw pointer (`int*`) escapes the "safety" of the class.
2. **Ref-Count Race (Meta):** If this were multi-threaded, LLMs almost always forget to make the `ref_count` atomic (using `std::atomic<int>`).
3. **Copy Assignment:** LLMs often implement the copy constructor but forget the assignment operator (`operator=`), which leads to double-deletes or memory leaks when one `SharedBuffer` is assigned to another.

## Human Insight
I like this task because it tests if the AI truly understands memory addresses or if it's just repeating patterns. A "smart" AI should warn the user that `get_alias()` is dangerous. Most will just write the code and say "Here is your thread-safe, memory-managed buffer!"... when it clearly isn't.
