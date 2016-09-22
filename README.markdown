## Steps

- Run `get_ending_pos.py` to generate a `junk.sh` shell script. Each line of
  this shell script will open, move, exit Vim, and record the position in
  `junk`.
- Open `junk` in Vim. Now do `:source generate_hl.vim`. This will convert
  `junk` into a valid highlighting file that Vim can use. Save `junk`.
- Go to `test.txt` (can by any file). Do `:source junk`. Now all of the
  positions are highlighted.

Here is an example limiting to 2 keystrokes:

![](example.png)
