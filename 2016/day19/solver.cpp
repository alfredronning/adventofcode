#include <iostream>
#include <unordered_map>

int main() {
    int inp = 3014387;
    std::unordered_map<int, int> cyclic;
    for (int i = 1; i <= inp; i++) {
        cyclic[i] = i + 1;
    }
    cyclic[inp] = 1;
    int current = 1;
    while (cyclic[current] != current) {
        cyclic[current] = cyclic[cyclic[current]];
        current = cyclic[current];
    }
    std::cout << current << std::endl;
    return 0;
}

