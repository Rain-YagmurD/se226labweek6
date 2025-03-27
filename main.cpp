#include <iostream>
using namespace std;

int recursive_sum(int n) {
    if (n == 0)
        return 0;
    return n + recursive_sum(n - 1);
}

int recursive_sum_user(int n) {
    if (n == 0)
        return 0;
    return n + recursive_sum_user(n - 1);
}

int recursive_sum() {
    int n;
    cout << "Enter number n: ";
    cin >> n;
    return n + recursive_sum_user(n - 1);
}

int main() {
    int n_1;
    cout << "Enter n_1: ";
    cin >> n_1;
    cout << "Sum from 1 to " << n_1 << " = " << recursive_sum(n_1) << endl;
    cout << "\n overload" << endl;
    int total = recursive_sum();
    cout << "Sum (overloaded) = " << total << endl;

    return 0;
}
