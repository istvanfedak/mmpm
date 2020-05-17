#include "mmpm.h"

void error_message(const char *message) {
  printf("%s\n", message);
}

void warning_message(const char *message) {
  printf("%s\n", message);
}

void test_single_string(const char *string) {
  printf("C Function (test_single_string):\n\n%s\n", string);
}

void test_array_of_char_ptrs(const char **array, const int num_strings) {
  printf("C Function (test_array_of_strings):\n\n");
  for (int i = 0; i < num_strings; i++) { printf("%s\n", array[i]); }
}

void display_modules(const char ***modules, const int rows, const int width) {
  ft_table_t *table = ft_create_table();

  ft_set_border_style(table, FT_BOLD2_STYLE);
  ft_set_cell_prop(table, 0, FT_ANY_COLUMN, FT_CPROP_ROW_TYPE, FT_ROW_HEADER);

  for (int i = 0; i < width; i++) {
    ft_set_cell_prop(table, 0, i, FT_CPROP_CONT_FG_COLOR, FT_COLOR_CYAN);
    ft_set_cell_prop(table, 0, i, FT_CPROP_CELL_TEXT_STYLE, FT_TSTYLE_BOLD);
    ft_set_cell_prop(table, 0, i, FT_CPROP_TEXT_ALIGN, FT_ALIGNED_LEFT);
  }

  for (int row = 0; row < rows; row++) {
    ft_row_write_ln(table, width, modules[row]);
  }

  printf("%s\n", ft_to_string(table));
  ft_destroy_table(table);
}
