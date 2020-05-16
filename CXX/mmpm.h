#ifndef MMPM_H
#define MMPM_H

#include "fort.h"
#include <stdio.h>
#include <string.h>

void warning_message(const char* message);
void error_message(const char* message);
void display_modules(const char*** modules, const int rows, const int columns);

#endif
