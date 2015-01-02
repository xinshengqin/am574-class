# rsyncs all files in _build/html to the repository used to
# display on the web, visible at https://amath574w2015.github.io/

rsync -azv _build/html/ ../../amath574w2015.github.com/
