import pandas as pd
import warnings
from IPython.display import display
warnings.filterwarnings('ignore')
from src.data.visualizations import Visualizations

import pandas as pd


from pandas.api.types import is_numeric_dtype





class EDA:    
    def __init__(self):
        self.viz = Visualizations()
    def dataType(self,  df ):
        print( 'Tipos de datos: ' ) 
        display( df.dtypes.to_frame( 'tipo' ) )
        # columnas de procedimiento
        cols_proc = [c for c in df.columns if "Proced" in c]

        # cardinalidad por columna (número de categorías únicas)
        card_proc = df[cols_proc].nunique(dropna=False).sort_values(ascending=False)

        # ver ranking completo
        display(card_proc.to_frame("cardinalidad"))

        # procedimiento con mayor cardinalidad
        col_max = card_proc.index[0]
        print(f"Procedimiento con mayor cardinalidad: {col_max}")
        print(f"Cardinalidad: {card_proc.iloc[0]}")
    
    def missingValues( self, df ):
        print( '\n Valores faltantes por columna' )
        display( df.isnull().sum().to_frame( 'Valores faltantes' ) )

    def description( self, df ):
        numeric = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        categoric = df.select_dtypes(include =['object']).columns.tolist()
        print( '\n Estadística descriptiva variables numéricas' )
        display( df[numeric].describe().T)
        print( '\n Estadística descriptiva variables categóricas' )
        display( df[categoric].describe().T)
    
    def variableDistribution(self, df, target):
        print('\nDistribución de la variable objetivo:')
        print(f'Cardinalidad variable {target}: {df[ target ].nunique(dropna=False)}' )
        vc = df[target].value_counts(dropna=False)
        display(df[target].value_counts(dropna=False).to_frame('conteo').head())

        low_10 = vc[vc < 10]
        high_100 = vc[vc > 100]

        print(f'\nClases con conteo menor a 10: {len(low_10)}')
        display(low_10.to_frame('conteo'))

        print(f'\nClases con conteo mayor a 100: {len(high_100)}')
        display(high_100.to_frame('conteo'))
        if is_numeric_dtype(df[target]) and df[target].nunique(dropna=False) > 15:
            self.viz.histogram(df, target)
        else:
            self.viz.countplot(df, target)
            
            self.viz.cola_larga(df, target)

    def analyze_categorical_data(self, df):
        print('\nColumnas categóricas - Top 5 valores:')
        for col in df.select_dtypes(include='object').columns:
            tabla = df[col].value_counts(dropna=False).head(5).reset_index()
            tabla.columns = [col, 'conteo']
            display(tabla)
    def check_cardinality(self, df):
        
        cardinality = df.select_dtypes(include='object').nunique().sort_values(ascending=False)
        print(f'\nVariables con baja cardinalidad ( < {20} categorías):')
        low_card = cardinality[cardinality < 20]
        display(low_card.to_frame('Unique_Values').head(10))
        display(low_card.to_frame('Unique_Values').tail(10))
        
        print(f'\nVariables con alta cardinalidad ( > {100} categorías):')
        high_card = cardinality[cardinality > 100]
        print(len(high_card))
        display(high_card.to_frame('Unique_Values').head(10))
        display(high_card.to_frame('Unique_Values').tail(10))
    
    def summaryEda(self, df, target):
        self.dataType( df )
        self.missingValues( df )
        self.check_cardinality( df )
        self.description( df )
        self.variableDistribution( df, target )
        self.analyze_categorical_data( df )
