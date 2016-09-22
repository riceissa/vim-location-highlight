
vim_atomic_movements = [
        (r"\<Left>", 1),
        (r"\<Right>", 1),
        (r"\<Up>", 1),
        (r"\<Down>", 1),
        ("h", 1),
        ("l", 1),
        ("j", 1),
        ("k", 1),
        ("w", 1),
        ("W", 1),
        ("e", 1),
        ("E", 1),
        ("b", 1),
        ("B", 1),
        ("0", 1),
        ("$", 1),
        ("*", 1),
        ("#", 1),
        ("+", 1),
        ("-", 1),
        (r"\<CR>", 1),
        (r"\<BS>", 1),
        ("G", 1),
        ("H", 1),
        ("L", 1),
        ("M", 1),
        (r"\<C-F>", 1),
        (r"\<C-B>", 1),
        (r"\<C-U>", 1),
        (r"\<C-D>", 1),
        ("gg", 2),
        ("ge", 2),
        ("gE", 2),
        ("*n", 2),
        ("#", 2),
        ("^", 1),
        ("(", 1),
        (")", 1),
        ("{", 1),
        ("}", 1),
        ("%", 1),
]

def get_starting_pos(line=1, col=1):
    return "{}G{}|".format(line, col)

vim_movements = []
vim_movements.extend(vim_atomic_movements)
for cmd in ["f", "F", "t", "T"]:
    # print(cmd)
    # okay, \ and ' and " also work, but i don't want to deal with escaping
    # those right now
    for c in ("!@#$%^&*()-_=+[{}]|;:,<>./?`~1234567890" +
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
        vim_movements.append((cmd+c, 2))
for m, c in vim_atomic_movements:
    for count in range(1, 10):
        vim_movements.append((str(count)+m, c+1))
# print(vim_movements)
# print(len(vim_movements))

def add_with_prefix(prefix=("", 0), movements=vim_movements, max_allowed=2):
    res = []
    pm, pc = prefix
    for m, c in movements:
        if pc + c <= max_allowed:
            res.append((pm+m, pc+c))
        if pc + c < max_allowed:
            res.extend(add_with_prefix((pm+m, pc+c), movements, max_allowed))
    return res

if __name__ == "__main__":
    fname = "test.txt"
    starting_pos = get_starting_pos(line=100, col=22)
    use = add_with_prefix()
    with open('junk.sh', 'w') as f:
        for m in use:
            cmd = """vim -Nu NONE -c 'exe "normal {}{}"' -c "let @a=getcurpos()[1]" -c "let @b=getcurpos()[2]" -c "edit junk" -c "$ | put a | put b | normal GkJ" -c "write | quit" {}""".format(starting_pos, m[0], fname)
            f.write(cmd + "\n")

