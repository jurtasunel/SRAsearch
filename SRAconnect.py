# Connect SRA

from Bio import Entrez

Entrez.email = "jmurtasun.94@gmail.com"
Entrez.api_key = "1c5b74af4f785579858076ca3d607d927008"

# handle = Entrez.esearch(db = "sra", term = "SRR390728")
# record = Entrez.read(handle)

# print(record)


handle = Entrez.efetch(db="sra", id="SRR390728", rettype="runinfo", retmode="text")
metadata = handle.read()
handle.close()

print(metadata)
