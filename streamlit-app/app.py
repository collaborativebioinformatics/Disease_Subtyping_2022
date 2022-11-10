import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import preprocess

def read_preprocessed_data(tsv):
    read_counts = pd.read_csv(tsv, sep='\t')
    read_counts = read_counts.set_index('Unnamed: 0')
    read_counts.index.name = None
    # st.dataframe(read_counts)

    st.write(f'Number of patients: {len(read_counts.columns)}')

    return read_counts

def over_under_expressed_genes(df):
    df_expr = df.copy()
    df_expr = df_expr.transpose()
    df_expr_copy = df_expr.copy()

    for col in df_expr.columns:
        df_expr_copy.loc[df_expr[col] > df_expr[col].mean() * 1.4, col] = 'high'
        df_expr_copy.loc[df_expr[col] < df_expr[col].mean() * 0.7, col] = 'low'
    
    df_expr_copy = df_expr_copy.transpose()

    return df_expr_copy

st.header("Disease Subtyping 2022")

## Reading data

st.header("Read counts")

cmscaller_input = preprocess.get_data_for_CMScaller(reads_path=None)
data = preprocess.read_counts_from_TCGA(reads_path=None, genes_tsv='data/canonical_genes.tsv')

# choose genes to drop
# removing DCC - it's underexpressed in every sample
to_drop = st.selectbox("Do you want to remove genes?", data.index.to_list())
data = data.drop(to_drop, axis=0)
data = data.astype(int)

st.dataframe(data)

## Run CMScaller with cmscaller_input

st.header("Sample Subtyping / CMScaller Results")

# Run script for CMScaller
subtyping_res = pd.read_csv('data/cmscaller_results.csv')
subtyping_res = subtyping_res.set_index('Unnamed: 0')
subtyping_res.index.name = None

## Plot Subtyping Summary
fig, ax = plt.subplots()
ax.hist(subtyping_res['prediction'].to_list())
st.pyplot(fig)

read_counts_with_pred = pd.read_csv('data/read_counts_per_canonical_gene_with_pred.tsv')
read_counts_with_pred = read_counts_with_pred.set_index('Unnamed: 0')
read_counts_with_pred.index.name = None

## DNAnexus:over_under_exp_genes.ipynb

data = over_under_expressed_genes(data)

st.dataframe(data)

### ABOVE IS OK ###

## DNAnexus:de_combinations.ipynb

pred = subtyping_res[['prediction']]
pred = pred.transpose()
data_with_pred = pd.concat([data, pred])

st.header('data with pred')
st.dataframe(data_with_pred)

# Choosing canonical genes
low_genes = ['KRAS', 'APC', 'DCC', 'TFGBR2', 'SMAD2', 'SMAD4', 'BAX', 'P53', 'MLH1', 'MLH2']
high_genes = ['MLH3', 'BRAF', 'PIK3CA', 'COLCA2', 'GALNT12']

selected_low_canonical_genes = st.multiselect('Choose Low Canonical Genes', low_genes)

selected_low_canonical_genes = st.multiselect('Choose High Canonical Genes', high_genes)


# Count gene combinations
st.write("Gene Combinations")

df1 = pd.DataFrame(columns=['cms', 'high', 'low', 'high_number', 'low_number', 'combined_number'])

dfm = gene_expression_with_pred

for col in dfm.columns:
    cms = dfm.loc['prediction'][col]
    gene = dfm[col].index
    high = dfm[dfm[col] == 'high'].index.to_list()
    low = dfm[dfm[col] == 'low'].index.to_list()
    df1.loc[col] = [cms, high, low, len(high), len(low), len(high)+len(low)]

d = {}
for idx,row in df1.iterrows():
    com = list(set(df1.loc[idx]['high']) & set(high_genes)) + list(set(df1.loc[idx]['low']) & set(low_genes))
    cms = df1.loc[idx]['cms']
    d[idx] = [cms, com]

df3 = pd.DataFrame.from_dict(d)
df3 = df3.transpose()
df3.columns=['cms', 'genes']

df3['genes'] = df3['genes'].apply(str)
gene_combinations = df3.groupby(['cms', 'genes']).size()

st.write(gene_combinations)