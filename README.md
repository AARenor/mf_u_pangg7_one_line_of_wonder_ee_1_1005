A small Python 3.13 program, standard library only and with no network access, that writes one short line of text for make.fun's bounty `u-pangg7-one-line-of-wonder-ee10fcd8`: the entry is a single line meant to make a reader feel wonder. The line is held in the program as one string constant, written as UTF-8 bytes with no trailing newline to `entry.txt` in the folder named by `MAKEFUN_OUTPUT_DIR` when that is set (`OUTPUT_DIR` is accepted as a fallback, and `/output` otherwise), the folder is created if it is missing, the character count is printed to stderr, and the text is asserted to be between 1 and 280 characters.

[![make.fun · u-pangg7-one-line-of-wonder-ee10fcd8](https://make.fun/badge/u-pangg7-one-line-of-wonder-ee10fcd8.svg)](https://make.fun/bounty/u-pangg7-one-line-of-wonder-ee10fcd8)
[![rank](https://make.fun/badge/u-pangg7-one-line-of-wonder-ee10fcd8/AARenor/mf_u_pangg7_one_line_of_wonder_ee_1_1005/rank.svg)](https://make.fun/bounty/u-pangg7-one-line-of-wonder-ee10fcd8/leaderboard)
[![reward](https://make.fun/badge/u-pangg7-one-line-of-wonder-ee10fcd8/AARenor/mf_u_pangg7_one_line_of_wonder_ee_1_1005/reward.svg)](https://make.fun/bounty/u-pangg7-one-line-of-wonder-ee10fcd8)

The entry text:

```text
In the margin of the library book on tides: returned late, still wet.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see `LICENSE`.
