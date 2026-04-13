class preprocess:
    

    def CIE10_to_categorie(self, df):
        cols_diag = [c for c in df.columns if  'Diag' in c and '(cod+des)']
        for col in cols_diag:
            df[col] = (
                df[col].str.split(" - ").str[0].str[:3]
            )
    def CIE9_to_categorie(self, df):
        cols_proc = [c for c in df.columns if  'Proced' in c and '(cod+des)']
        for col in cols_proc:
            df[col] = (
                df[col].fillna('').astype(str)
                .str.split(" - ").str[0].str[:2]
            )
    

    # def encoding




