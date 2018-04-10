#!/usr/bin/python2
# encoding: utf-8
output=open("output", 'w')
for line in open("./tcl.dict", 'r'):
    if line.split() !=[]:
        word=line.split()[0]
        snip="""
snippet %s "Innovus command" i
%s
endsnippet
""" % (word,word)
        output.write(snip)

