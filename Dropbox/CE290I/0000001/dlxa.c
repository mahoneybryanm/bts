#include <stdio.h>

int decode();
int decodeF3();

int op;
int a;
int b;
int c;

int mem[2^32];

int main(void)
{
    return 0;
}

int decode()
{
    // in linker and emulator
    // works for F1 and F2 not F3
    // assuming  <= instruction <= 2^32-1
    op = (instruction >> 26) & 63; // 0x3F: 6 lsbs
    a = (instruction >> 21) & 31; // 0x1F: 5 lsbs
    b = (instruction >> 16) & 31; // 0x1F: 5 lsbs
    c = instruction & 65535; // 0xFFFF: 16 lsbs
    if (c >= 32768)
        c = c - 65536; // 0x10000: 2^16
    printf("op = %i\na = %i\nb = %i\nc = %i\n", op, a, b, c);
    return 0;
}

int decodeF3()
{
    return 0;
}
