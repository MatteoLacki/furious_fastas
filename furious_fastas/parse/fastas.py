from functools import partial
import re

from ..fasta import UniprotFasta, NCBIgeneralFasta



def parse_fastas(raw_fastas, pattern, FASTA):
    for f in re.finditer(pattern, raw_fastas):
        sequence = "".join(f[0].split('\n')[1:])
        header = f[1]
        yield FASTA(sequence, header)


uniprot_fastas_pattern = re.compile(r"(>.+\|.+\|.*)\n(\w+\n)+")
parse_uniprot_fastas = partial(	parse_fastas,
								pattern=uniprot_fastas_pattern,
					     	   	FASTA=UniprotFasta )

ncbi_general_fastas_pattern = re.compile(r"(>.*\|.*\|\w+\s.*)\n(\w+\n)+")
parse_ncbi_general_fastas = partial( parse_fastas,
    pattern=ncbi_general_fastas_pattern,
    FASTA=NCBIgeneralFasta)

def test_parse():
    fasta = ">sp|P61513|RL37A_HUMAN 60S ribosomal protein L37a OS=Homo sapiens OX=9606 GN=RPL37A PE=1 SV=2\nMAKRTKKVGIVGKYGTRYGASLRKMVKKIEISQHAKYTCSFCGKTKMKRRAVGIWHCGSC\nMKTVAGGAWTYNTTSAVTVKSAIRRLKELKDQ\n>sp|P61513|RL37A_HUMAN 60S ribosomal protein L37a OS=Homo sapiens OX=9606 GN=RPL37A PE=1 SV=2\nMAKRTKKVGIVGKYGTRYGASLRKMVKKIEISQHAKYTCSFCGKTKMKRRAVGIWHCGSC\nMKTVAGGAWTYNTTSAVTVKSAIRRLKELKDQ\n"
    r = list(parse(fasta))
    assert len(r) == 2
    assert str(r[0]) == "MAKRTKKVGIVGKYGTRYGASLRKMVKKIEISQHAKYTCSFCGKTKMKRRAVGIWHCGSCMKTVAGGAWTYNTTSAVTVKSAIRRLKELKDQ"
    assert str(r[1]) == "MAKRTKKVGIVGKYGTRYGASLRKMVKKIEISQHAKYTCSFCGKTKMKRRAVGIWHCGSCMKTVAGGAWTYNTTSAVTVKSAIRRLKELKDQ"
