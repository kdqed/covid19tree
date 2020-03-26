import requests
import os
import csv

sequence_folder = 'sequences'
seqlist_file = 'seqlist.csv'
fasta_download_link = "https://www.ncbi.nlm.nih.gov/nuccore/{}?report=fasta&log$=seqview&format=text"


def read_seqlist(filename):
  with open(filename) as f:
    reader = csv.reader(f, skipinitialspace=True)
    header = next(reader)
    a = [dict(zip(header, row)) for row in reader]
    return a    

if not os.path.exists(sequence_folder):
  os.mkdir(sequence_folder)


seqlist = read_seqlist(seqlist_file)
for seq in seqlist:
  gb_id = seq['GenBankId']
  print("Downloading: {}".format(gb_id))
  r = requests.get(fasta_download_link.format(gb_id))
  with open('{}/{}.fasta'.format(sequence_folder,gb_id),'w') as f:
    f.write(r.text)
    f.close()
  print("Downloaded: {}".format(gb_id))
    
 

