#include "mmpm.h"

void error_message(const char *message) {
  printf("%s\n", message);
}

void warning_message(const char *message) {
  printf("%s\n", message);
}

void display_modules(const char*** modules, const int rows, const int columns) {
  ft_table_t *table = ft_create_table();

  ft_set_border_style(table, FT_BOLD2_STYLE);
  ft_set_cell_prop(table, 0, FT_ANY_COLUMN, FT_CPROP_ROW_TYPE, FT_ROW_HEADER);

  for (int i = 0; i < columns; i++) {
    ft_set_cell_prop(table, 0, i, FT_CPROP_CONT_FG_COLOR, FT_COLOR_CYAN);
    ft_set_cell_prop(table, 0, i, FT_CPROP_CELL_TEXT_STYLE, FT_TSTYLE_BOLD);
    ft_set_cell_prop(table, 0, i, FT_CPROP_TEXT_ALIGN, FT_ALIGNED_LEFT);
  }

  //char ***modules = (char ***)malloc(rows * sizeof(char **));

  //const char *mods[5][5] = {
  //  { "Category", "Title", "Repository", "Author", "Description" },
  //  { "Health", "MMM-NightScout", "https://github.com/bureus/MMM-Nightscout", "bureus",
  //    "Keep track of blood glucose levels with ease thru your magic mirro..." },
  //  { "Health", "MMM-OneTouchReveal", "https://github.com/Canonip/MMM-OneTouchReveal", "Canonip",
  //    "Keep track of blood glucose levels measured with your LifeScan One..." },
  //  { "Health", "MMM-SugarValue", "https://github.com/balharrie", "balharrie",
  //    "Displays last reading from your Dexcom G6 via the share API" },
  //  { "Health", "MMM-COVID19", "https://github.com/bibaldo/MMM-COVID19", "bibaldo",
  //    "Keep track of the Corona Virus (COVID-19) cases via rapidapi API" }
  //};

  for (int row = 0; row < rows; row++) {
    ft_write_ln(table, modules[row][0], modules[row][1], modules[row][2], modules[row][3], modules[row][4]);
  }

  printf("%s\n", ft_to_string(table));
  ft_destroy_table(table);
}
