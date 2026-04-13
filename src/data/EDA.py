import pandas as  pd
import warnings
from IPython.display import display
warnings.filterwarnings('ignore')
from src.data.visualizations import Visualizations
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, ConfusionMatrixDisplay, classification_report, balanced_accuracy_score
)
class EDA:    
    def __init__(self):
        self.viz = Visualizations()
    def dataType(self,  df ):
        print( 'Tipos de datos: ' ) 
        display( df.dtypes.to_frame( 'tipo' ) )
    
    def missingValues( self, df ):
        print( '\n Valores faltantes por columna' )
        display( df.isnull().sum().to_frame( 'Valores faltantes' ) )

    def description( self, df ):
        print( '\n Estadística descriptiva' )
        display( df.describe( include = 'all' ).T )
    
    def variableDistribution(self, df, target):
        print('\nDistribución de la variable objetivo:')

        display(df[target].value_counts(dropna=False).to_frame('conteo'))
        self.viz.countplot(df, target)

    def analyze_categorical_data(self, df):
        print('\nColumnas categóricas - Top 5 valores:')
        for col in df.select_dtypes(include='object').columns:
            print(f'\n{col}:')
            print(df[col].value_counts().head())
    
    def check_cardinality(self, df, threshold=100):
        print(f'\nVariables con alta cardinalidad ( > {threshold} categorías):')
        cardinality = df.select_dtypes(include='object').nunique().sort_values(ascending=False)
        high_card = cardinality[cardinality > threshold]
        display(high_card.to_frame('Unique_Values'))
    
    def summaryEda(self, df, target):
        self.dataType( df )
        self.missingValues( df )
        self.check_cardinality( df )
        self.description( df )
        self.variableDistribution( df, target )
        self.analyze_categorical_data( df )
    
