import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

blast_G_muris = pd.read_csv('/media/busranur/SSD/busra/miuul/output/blastn/G_intestinalis/G_muris.blastn', sep='\t', header=None)

blast_G_muris.columns = ['qseqid', 'sseqid', 'pident',
'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart',
'send', 'evalue', 'bitscore']

blast_S_salmonicida = pd.read_csv('/media/busranur/SSD/busra/miuul/output/blastn/G_intestinalis/S_salmonicida.blastn', sep='\t',header=None)

blast_S_salmonicida.columns = ['qseqid', 'sseqid', 'pident',
'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart',
'send', 'evalue', 'bitscore']

# Pivot table

pivot_table_G_muris = pd.pivot_table(blast_G_muris, values = 'length', index = 'qseqid', columns = 'sseqid')
sns.heatmap(pivot_table_G_muris)
pivot_table_S_salmonicida = pd.pivot_table(blast_S_salmonicida, values = 'length', index = 'qseqid', columns = 'sseqid')
sns.heatmap(pivot_table_S_salmonicida)