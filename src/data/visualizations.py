import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")
class Visualizations:
    @staticmethod
    def histogram(df, column, bins = 30):
        sns.histplot(df,)
        sns.histplot(df,x ="Valor", kde=True,)
        plt.legend()
        plt.show()

    @staticmethod
    def countplot(df, target, ):
        plt.figure(figsize=(6, 4))
        codes = df[target].str.split(' - ').str[0]
        top = codes.value_counts().head( 10 ).index
        sns.countplot(
            # data=df, 
            y=codes[codes.isin( top )], 
            order=top
            )
        plt.title(f"Distribución de la variable {target}")
        plt.xlabel("Cantidad")
        plt.ylabel("Código")
        plt.tight_layout()
        plt.show()
