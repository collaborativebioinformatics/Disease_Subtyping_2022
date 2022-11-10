import pandas as pd
import glob

def read_counts_from_TCGA(reads_path, genes_tsv):
    
    # df = pd.DataFrame()
    
    # for tsv in glob.glob(reads_path+'*/*.tsv'):
    #     sample_name = tsv.split('/')[5].split('.')[0]
    #     tsv_df = pd.read_csv(tsv, sep='\t', skiprows=1)
    #     tsv_df = tsv_df.iloc[5:]
    #     tsv_df = tsv_df[['gene_id', 'tpm_unstranded']]

    #     tsv_df = tsv_df.set_index('gene_name')    
    #     tsv_df.index.name = None
    #     tsv_df.columns = [sample_name]

    #     tsv_df = tsv_df.transpose()

    #     df = pd.concat([df, tsv_df])
        
    # df = df.transpose()

    ## loading already preprocessed data
    df = pd.read_csv('data/read_counts_per_canonical_gene.tsv', sep='\t')
    df = df.set_index('Unnamed: 0')
    df.index.name = None

    ## loading canonical genes list
    genes_df = pd.read_csv('data/canonical_genes.tsv', sep='\t')
    genes_df = genes_df[['SYMBOL']]
    genes_df = genes_df.set_index('SYMBOL')
    dfm = pd.merge(df, genes_df, how='inner', left_index=True, right_index=True)

    return dfm


def get_data_for_CMScaller(reads_path):
    
    df = pd.DataFrame()
    
    for tsv in glob.glob(reads_path+'*/*.tsv'):
        sample_name = tsv.split('/')[5].split('.')[0]
        tsv_df = pd.read_csv(tsv, sep='\t', skiprows=1)
        tsv_df = tsv_df.iloc[5:]
        tsv_df = tsv_df[['gene_id', 'tpm_unstranded']]

        tsv_df = tsv_df.set_index('gene_id')    
        tsv_df.index.name = None
        tsv_df.columns = [sample_name]

        tsv_df = tsv_df.transpose()

        df = pd.concat([df, tsv_df])
        
    df = df.transpose()

    return df