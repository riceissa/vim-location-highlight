vim -c "normal Mgm" -c "let @a=getcurpos()[1]" -c "let @b=getcurpos()[2]" -c "edit junk" -c "$ | put a | put b | normal GkJ" -c "write | quit" longlines.vim
# old version:
# vim -c "normal MgmG" -c "let @a=getcurpos()[1]" -c "let @b=getcurpos()[2]" -c "edit junk" -c "put a" -c "put b" -c "write | quit" longlines.vim
# then in vim do e.g.
# highlight highlightgroup ctermbg=darkred
# match highlightgroup /\%3c\%4l\|\%1c\%1l/
