from furious_fastas import fastas, Fastas
from furious_fastas.uniprot import uniprot_url

import re

wheat = fastas('/home/matteo/SYMPHONY_VODKAS/fastas/wheat.fasta')
prots = wheat[1:100]

p = prots[0].sequence

p = 'AAAKAAKKAAKPAAAKA'
pslit = p.split('K')
i = 0
for i in range(len(pslit)-1):
    b = pslit[:i]
    x = 