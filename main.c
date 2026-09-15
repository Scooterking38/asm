#include <stdio.h>

const char* check_age(long age) {
    if (age < 19) {
        return "Not allowed to drink! arrest him!";
    }
    return "Allowed to drink! yay!";
}

int main() {
    // Test the function
    printf("%s\n", check_age(20));
    return 0;
}
