# In Mainz, we believe that fastas are the future

## Rationale
There ain't much to do with fastas but to download them and use.
For this you could open the terminal (or powershell on windows) and type

```console
wget -O human.fasta "http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta"
```
to download human database.
Then, to get contaminants used in our group, you could simply type
```console
wget -O contaminants.fasta "https://raw.githubusercontent.com/MatteoLacki/protein_contaminants/master/contaminants.fasta"
```
Finally, you would merge the two files as simple as
```console
cat human.fasta contaminants.fasta > ready.fasta
```
and would feed `ready.fasta` into the software (on Windows you might use `type` instead of `cat`).

To do this in Python with `furious_fastas` you can simply run:
```{Python}
from furious_fastas import fastas, contaminants

fs = fastas("http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta")
fs.extend(contaminants)
fs.write('/my/favourit/location/for/fastas/human.fastas')
```

Need to add in reversed sequences?
We have you covered:
```{Python}
fs.reverse()
fs.write('/my/favourit/location/for/fastas/human_rev.fastas')
```

Do you work with proteome mixtures?
Here's how to deal with a search involving human, yeast, and ecoli:
```{Python}
from furious_fastas import Fastas, contaminants

fs = Fastas()
fs.download('http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=fasta')
fs.download('http://www.uniprot.org/uniprot/?query=organism:643680&format=fasta')
fs.download('http://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:83333&format=fasta')
fs.extend(contaminants)
fs.reverse()
fs.write('/my/favourit/location/for/fastas/hye.fastas')
```

Now, we also automate the process of managing the database with fasta folders, cause, you know, why not?
To do this, use the update_fastas script.

```{bash}
% python3 update_fastas -h

usage: update_fastas [-h] db_path species2url_path

Update fasta databases.

positional arguments:
  db_path           Path to the folder treated as database.
  species2url_path  Path to the file mapping species names to urls.

optional arguments:
  -h, --help        show this help message and exit
```
However:
* do make sure that no software is running while we update the fastas
* do make sure that python is to be found in system variable Path
* add the whole thing to `chronjobs` or `windows scheduler` to make it automatic

Finally, it's sometimes good to simply parse fasta files for Python scripting.
`biopython` is bloated, and we keep it much more free of additional dependencies.



Best Regards,
Matteo Lacki
