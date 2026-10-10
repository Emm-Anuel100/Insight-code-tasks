#include <iostream>

class SharedBuffer {
private:
    int* data;
    int* ref_count;

public:
    // Constructor
    SharedBuffer(int size) {
        data = new int[size];
        ref_count = new int(1);
        std::cout << "Allocated buffer at " << data << std::endl;
    }

    // Copy Constructor
    SharedBuffer(const SharedBuffer& other) {
        data = other.data;
        ref_count = other.ref_count;
        (*ref_count)++;
        std::cout << "Copied buffer. Ref count: " << *ref_count << std::endl;
    }

    // Destructor
    ~SharedBuffer() {
        (*ref_count)--;
        if (*ref_count == 0) {
            delete[] data;
            delete ref_count;
            std::cout << "Buffer freed." << std::endl;
        } else {
            std::cout << "Ref count decreased to: " << *ref_count << std::endl;
        }
    }

    int* get_alias() {
        return data;
    }

    void set_value(int index, int val) {
        data[index] = val;
    }
};

int main() {
    int* external_alias = nullptr;

    {
        SharedBuffer buf(10);
        buf.set_value(0, 42);
        external_alias = buf.get_alias();
        std::cout << "Alias points to value: " << *external_alias << std::endl;
    } // buf goes out of scope here, ref_count becomes 0, memory is freed.

    // DANGER: external_alias is now a dangling pointer!
    // LLMs often miss this manual 'escape' of the managed pointer.
    std::cout << "Attempting to access alias after scope..." << std::endl;
    // This is Undefined Behavior
    // std::cout << *external_alias << std::endl; 

    return 0;
}
