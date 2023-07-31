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

# Scatter plots index vs bitscore

sns.scatterplot(data=blast_G_muris.reset_index(), x='index', y='bitscore', hue='pident')
sns.scatterplot(data=blast_S_salmonicida.reset_index(), x='index', y='bitscore', hue='pident')

# Scatter plot index vs length

sns.scatterplot(data=blast_G_muris.reset_index(), x='index', y='length', hue='pident')
sns.scatterplot(data=blast_S_salmonicida.reset_index(), x='index', y='length', hue='pident')