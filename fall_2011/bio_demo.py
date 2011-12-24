"""
BioPython + regular expression demo
based on http://www.pasteur.fr/recherche/unites/sis/formation/python/ch11s04.html
"""

from Bio import SwissProt
import re

fd = open('ceru_human.sp') # file descriptor (handle)
r = SwissProt.read(fd) # record from file
print r.entry_name
print r.sequence
PS00079 = 'G.[FYW].[LIVMFYW].[CST].{8,8}G[LM]...[LIVMFYW]' # pattern for regexp
p = re.compile(PS00079) # regular expression pattern object
m = p.search(r.sequence) # matching string in sequence
i =  m.start() # index of start of match
j = m.end() # index of end of match
print i
print j
print r.sequence[i:j] # print a slice of the sequence

