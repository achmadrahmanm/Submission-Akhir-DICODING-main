import json

notebook_path = r'c:\laragon\www\Submission-Akhir-DICODING-main\[Clustering]_Submission_Akhir_BMLP_Achmad_Rahman_M.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code':
        source = cell['source']
        new_source = []
        for line in source:
            updated_line = line
            
            # EDA and Data Loading
            if 'df = ________' in updated_line:
                updated_line = updated_line.replace('df = ________', 'df = pd.read_csv(url)')
            elif 'df.________()' in updated_line:
                updated_line = updated_line.replace('df.________()', 'df.head()')
            elif '________.info()' in updated_line:
                updated_line = updated_line.replace('________.info()', 'df.info()')
            elif '________.describe()' in updated_line:
                updated_line = updated_line.replace('________.describe()', 'df.describe()')
            elif '________.________()' in updated_line:
                if 'info' in str(cell.get('source', [])):
                    updated_line = updated_line.replace('________.________()', 'df.info()')
                else:
                    updated_line = updated_line.replace('________.________()', 'df.describe()')
            
            # EDA Specific summary checks
            if 'df.isna().________()' in updated_line:
                 updated_line = updated_line.replace('________', 'sum')
            if 'df.duplicated().________()' in updated_line:
                 updated_line = updated_line.replace('________', 'sum')
            
            # Correlation
            if 'correlation = df[numerical_cols].________()' in updated_line:
                updated_line = updated_line.replace('________', 'corr')
            if 'sns.scatterplot(correlation,' in updated_line:
                updated_line = updated_line.replace('sns.scatterplot', 'sns.heatmap')

            # Visualization - Histplot with many params
            if "sns.scatterplot(df[column], bins=20, kde=True, color='skyblue', ________)" in updated_line:
                 updated_line = updated_line.replace('sns.scatterplot', 'sns.histplot').replace('________', "edgecolor='black'")
            if "sns.scatterplot(df[column], bins=20, kde=True, color='skyblue', edgecolor='black')" in updated_line:
                 updated_line = updated_line.replace('sns.scatterplot', 'sns.histplot')
            
            # Boxplot
            if "sns.boxplot(x=df[column], color='lightcoral', ________)" in updated_line:
                 updated_line = updated_line.replace('________', 'showfliers=True')
            
            # Specific cluster scatterplot fix (avoiding double edgecolor error)
            if "sns.scatterplot(x=________, y=________, data=df)" in updated_line:
                 updated_line = updated_line.replace("x=________", "x='CustomerOccupation'").replace("y=________", "y='TransactionAmount'")
            
            # CRITICAL FIX for corrupted line
            if "sns.scatterplot(x=edgecolor='black', y=edgecolor='black', data=df)" in updated_line:
                 updated_line = updated_line.replace("sns.scatterplot(x=edgecolor='black', y=edgecolor='black', data=df)", "sns.scatterplot(x='CustomerOccupation', y='TransactionAmount', data=df)")
            
            if 'plt.________(rotation=45)' in updated_line:
                updated_line = updated_line.replace('________', 'xticks')

            # Preprocessing
            if 'df.________.sum()' in updated_line:
                if 'isnull' in updated_line or 'isnull' in str(cell.get('source', [])):
                    updated_line = updated_line.replace('________', 'isnull()')
                else:
                    updated_line = updated_line.replace('________', 'duplicated()')
            
            if 'df.________(________=True)' in updated_line:
                if 'isnull' in str(cell.get('source', [])) or 'dropna' in updated_line:
                    updated_line = updated_line.replace('________(________=True)', 'dropna(inplace=True)')
                else:
                    updated_line = updated_line.replace('________(________=True)', 'drop_duplicates(inplace=True)')

            if 'cols_to_drop = [col for col in ________' in updated_line:
                updated_line = updated_line.replace('________', 'df.columns')
            if '________ in col.lower()' in updated_line:
                updated_line = updated_line.replace('________', "'id'")
            if 'col.________()' in updated_line:
                updated_line = updated_line.replace('________', 'lower')
            if 'df = df.________(columns=cols_to_drop)' in updated_line:
                updated_line = updated_line.replace('________', 'drop')

            if "df.________(include=['object']).________" in updated_line:
                updated_line = updated_line.replace("df.________(include=['object']).________", "df.select_dtypes(include=['object']).columns")
            
            if 'label_encoder.________(df[column])' in updated_line:
                updated_line = updated_line.replace('________', 'fit_transform')

            if '____.columns.tolist()' in updated_line:
                updated_line = updated_line.replace('____', 'df')

            if 'df[col].________(0.25)' in updated_line:
                updated_line = updated_line.replace('________', 'quantile')
            if 'df[col].________(0.75)' in updated_line:
                updated_line = updated_line.replace('________', 'quantile')
            
            # Catch corrupted outlier lines
            if "df[col].________(0.25)" in updated_line:
                updated_line = updated_line.replace('________', 'quantile')
            if 'df[col].________(0.75)' in updated_line:
                updated_line = updated_line.replace('________', 'quantile')

            if 'df = df[(df[col] >= ________) & (df[col] <= ________)]' in updated_line:
                 updated_line = updated_line.replace("df = df[(df[col] >= ________) & (df[col] <= ________)]", "df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]")
            if 'IQR = ________ - ________' in updated_line:
                 updated_line = updated_line.replace('________ - ________', 'Q3 - Q1')

            if 'df[numerical_cols] = scaler.________(df[numerical_cols])' in updated_line:
                 updated_line = updated_line.replace('________', 'fit_transform')

            # Binning
            if "col_to_bin = '________'" in updated_line:
                updated_line = updated_line.replace("col_to_bin = '________'", "col_to_bin = 'TransactionAmount'")
            if "new_col_name = '________'" in updated_line:
                updated_line = updated_line.replace("new_col_name = '________'", "new_col_name = 'Amount_Level'")
            if "bin_labels = ['________', '________', '________']" in updated_line:
                updated_line = updated_line.replace("bin_labels = ['________', '________', '________']", "bin_labels = ['Low', 'Medium', 'High']")
            if 'pd.________' in updated_line and 'labels=bin_labels' in updated_line:
                updated_line = updated_line.replace('pd.________', 'pd.qcut')
            if 'label_encoder = ________()' in updated_line:
                updated_line = updated_line.replace('________()', 'LabelEncoder()')
            if 'label_encoder.________' in updated_line and 'fit_transform' not in updated_line:
                updated_line = updated_line.replace('label_encoder.________', 'label_encoder.fit_transform')

            # Modeling
            if 'df_used = df.________()' in updated_line:
                updated_line = updated_line.replace('df.________()', 'df.copy()')
            if 'df_used.________()' in updated_line:
                updated_line = updated_line.replace('df_used.________()', 'df_used.describe()')
            
            # Modeling
            if 'model = KMeans()' in updated_line or 'model = KMeans(random_state=42)' in updated_line:
                updated_line = "model = KMeans(random_state=42)\n"
            
            if 'visualizer = ________(model,' in updated_line:
                updated_line = updated_line.replace('________', 'KElbowVisualizer')
            if '________=(2,10)' in updated_line:
                updated_line = updated_line.replace('________', 'k')
            if "________='silhouette'" in updated_line:
                updated_line = updated_line.replace('________', 'metric')
            if 'visualizer.________(df)' in updated_line:
                updated_line = updated_line.replace('________', 'fit')
            if 'visualizer.________()' in updated_line:
                updated_line = updated_line.replace('________', 'show')

            if 'KMeans(n_clusters=________' in updated_line:
                updated_line = updated_line.replace('________', '2')
            if 'model.________(df)' in updated_line:
                updated_line = updated_line.replace('________', 'fit')
            
            if '________.dump(model, "model_clustering.h5")' in updated_line:
                updated_line = updated_line.replace('________', 'joblib')
            
            if 'labels = model.________' in updated_line:
                updated_line = updated_line.replace('________', 'labels_')
            if 'score = ________(df, labels)' in updated_line:
                updated_line = updated_line.replace('________', 'silhouette_score')

            if 'pca = ________(n_components=________)' in updated_line:
                updated_line = updated_line.replace('pca = ________(n_components=________)', 'pca = PCA(n_components=2)')
            if 'df_pca = pca.________(df)' in updated_line:
                updated_line = updated_line.replace('________', 'fit_transform')
            if "df_pca['Cluster'] = ________" in updated_line:
                updated_line = updated_line.replace('________', 'labels')
            
            # PCA Cluster plot hue
            if 'sns.________(' in updated_line and 'Cluster' in updated_line:
                updated_line = updated_line.replace('sns.________', 'sns.scatterplot').replace("________='Cluster'", "hue='Cluster'")
            
            if 'centers = pca.transform(kmeans.cluster_centers_)' in updated_line:
                 updated_line = updated_line.replace('kmeans', 'model')

            # Summary and Rename
            if 'df_pca_array = pca.________(df_used)' in updated_line:
                 updated_line = updated_line.replace('________', 'fit_transform')
            if 'data_final = pd.DataFrame(data=________' in updated_line:
                 updated_line = updated_line.replace('________', 'df_pca_array')
            if 'kmeans_pca = ________(n_clusters=________' in updated_line:
                 updated_line = updated_line.replace('________(n_clusters=________', 'KMeans(n_clusters=2')
            if 'kmeans_pca.________(________)' in updated_line:
                 updated_line = updated_line.replace('________(________)', 'fit(data_final)')
            
            if '________.dump(________, "PCA_model_clustering.h5")' in updated_line:
                 updated_line = updated_line.replace('________.dump(________', 'joblib.dump(kmeans_pca')
            
            if 'df_used[\'Cluster\'] = ________' in updated_line:
                 updated_line = updated_line.replace('________', 'labels')
            if 'agg_summary = df_used.________(________)[numerical_cols].________([' in updated_line:
                 updated_line = updated_line.replace('________(________)', 'groupby(\'Cluster\')').replace('________', 'agg')
            if 'display(________)' in updated_line:
                 updated_line = updated_line.replace('display(________)', 'display(agg_summary if "agg_summary" in locals() else df_inverse)')
            
            if 'df_used.________(________={"Cluster": "Target"}, ________=True)' in updated_line:
                 updated_line = updated_line.replace('________(________={"Cluster": "Target"}, ________=True)', 'rename(columns={"Cluster": "Target"}, inplace=True)')
            
            if '________.to_csv(\'data_clustering.csv\', index=False)' in updated_line:
                 updated_line = updated_line.replace('________', 'df_used')
            
            if 'df_inverse[numerical_cols] = scaler.________(df_inverse[numerical_cols])' in updated_line:
                 updated_line = updated_line.replace('________', 'inverse_transform')
            
            if 'df_inverse.________()' in updated_line:
                 updated_line = updated_line.replace('________', 'head')
            
            if 'encoder = ________[________]' in updated_line:
                 updated_line = updated_line.replace('________[________]', 'encoders[column]')
            if 'df_inverse[column] = encoder.________(df_inverse[column].astype(int))' in updated_line:
                 updated_line = updated_line.replace('________', 'inverse_transform')

            if 'agg_summary_num = df_inverse.________(\'Target\')[numerical_cols].________([' in updated_line:
                 updated_line = updated_line.replace('________(\'Target\')', 'groupby(\'Target\')').replace('________', 'agg')
            if 'agg_summary_cat = df_inverse.________(\'Target\')[categorical_cols].________(lambda x: x.mode()[0])' in updated_line:
                  updated_line = updated_line.replace('________(\'Target\')', 'groupby(\'Target\')').replace('________', 'agg')

            if '________.to_csv(\'data_clustering_inverse.csv\', index=False)' in updated_line:
                 updated_line = updated_line.replace('________', 'df_inverse')

            new_source.append(updated_line)
        cell['source'] = new_source

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully.")
