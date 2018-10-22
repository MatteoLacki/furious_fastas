## Here in Mainz, we believe that fastas are the future

These scripts are used to download files directly from Uniprot.

Usage:
First, always:
```{bash}
    make executable
```
to make all the scripts executable.

Then:

```{bash}
    make <what>
```
<what> can be either: human, hye, ecoli, laishmania, yeast, mouse or wheat

If you want to have something different, then:
```{bash}
    ./update <http address to Uniprot data> <name for file>
```

That's it.