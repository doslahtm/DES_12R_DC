#include <stdio.h>
#include <time.h>
#include <random>
#include <stdlib.h>
#include <stdint.h>
#include <algorithm>

typedef uint8_t byte;
void DES(unsigned int* key, byte* text, byte* C);
void des_key_setup(byte* key, unsigned int* ek);