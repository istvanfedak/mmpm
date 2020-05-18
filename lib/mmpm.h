#ifndef MMPM_H
#define MMPM_H

#include "fort.h"
#include <stdarg.h>
#include <stdio.h>
#include <string.h>

struct magic_mirror_module {
  char* title;
  char* author;
  char* description;
  char* repository;
} module;

void display_modules(const char **modules[], const int rows, const int columns);

void test_single_string(const char *string);
void test_array_of_char_ptrs(const char **array, const int num_strings);

#endif
