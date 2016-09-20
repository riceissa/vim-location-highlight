
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
        ("*n", 2),
        ("#", 2),
        ("^", 1),
        ("(", 1),
        (")", 1),
        ("{", 1),
        ("}", 1),
        ("%", 1),
]

vim_movements = []
vim_movements.extend(vim_atomic_movements)
for cmd in ["f", "F", "t", "T"]:
    # print(cmd)
    for c_ord in range(ord("A"), ord("z")+1):
        c = chr(c_ord)
        # print(c)
        vim_movements.append((cmd+c, 2))
for m, c in vim_atomic_movements:
    for count in range(1, 10):
        vim_movements.append((str(count)+m, c+1))
# print(vim_movements)
# print(len(vim_movements))

use = [tup for tup in vim_movements if tup[1] <= 1]
print(use)

fname = "longlines.vim"
with open('junk.sh', 'w') as f:
    for m in use:
        cmd = """vim -c 'exe "normal {}"' -c "let @a=getcurpos()[1]" -c "let @b=getcurpos()[2]" -c "edit junk" -c "$ | put a | put b | normal GkJ" -c "write | quit" {}""".format(m[0], fname)
        f.write(cmd + "\n")

