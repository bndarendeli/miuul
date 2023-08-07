import pandas as pd
import seaborn as sns

blast_G_muris = pd.read_csv('/media/busra/SSD/busra/miuul/output/blastn/G_intestinalis/G_muris.blastn', sep='\t', header=None)

blast_G_muris.columns = ['qseqid', 'sseqid', 'pident',
'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart',
'send', 'evalue', 'bitscore']

blast_S_salmonicida = pd.read_csv('/media/busra/SSD/busra/miuul/output/blastn/G_intestinalis/S_salmonicida.blastn', sep='\t',header=None)

blast_S_salmonicida.columns = ['qseqid', 'sseqid', 'pident',
'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart',
'send', 'evalue', 'bitscore']

# Histogram plots for G.muris and S.salmonicida
sns.histplot(data=blast_S_salmonicida , x='pident')
plt.title("S.salmonicida")
plt.savefig("/media/busra/SSD/busra/miuul/output/plot/S.salmonicida_histogram.svg", format= "svg", bbox_inches= 'tight', dpi= 300)

sns.histplot(data=blast_G_muris, x='pident')
plt.title("G.muris")
plt.savefig("/media/busra/SSD/busra/miuul/output/plot/G_muris_histogram.svg", format= "svg", bbox_inches= 'tight', dpi= 300)