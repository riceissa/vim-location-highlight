0d
%!sort | uniq
%s/\(\d\+\) \(\d\+\)/\\%\1l\\%\2c/
1,$-1s/$/\\|/
1s/^/\//
$s/$/\//
%join!
exe "normal Ohighlight highlightgroup ctermbg=darkred\<Esc>"
exe "normal GImatch highlightgroup \<Esc>"
