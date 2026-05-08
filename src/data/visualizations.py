import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
sns.set_style("darkgrid")
class Visualizations:
    @staticmethod
    def histogram(df, column, bins = 30):
        print(column)
        sns.histplot(df,x =column, kde=True,)
        plt.legend()
        plt.show()

    @staticmethod
    def countplot(df, target, ):
        
        plt.figure(figsize=(6, 4))
        codes = df[target]
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
        plt.savefig(f"Distribución de la variable {target}", dpi=600, bbox_inches="tight")
        plt.show()
    @staticmethod
    def boxplot(df, variable):
        plt.figure(figsize = ( 6, 4 ))
        sns.boxplot()
    
    @staticmethod
    def cola_larga(df, target, min_pct=0.01, top_n=30):
        
        serie = df[target].astype("string").str.split(" - ", n=1).str[0].str.strip()

        vc = serie.value_counts(dropna=False)
        pct = vc / vc.sum()
        cum = pct.cumsum()

        resumen = pd.DataFrame({
            "conteo": vc,
            "pct": pct,
            "pct_acum": cum
        })

        tail = resumen[resumen["pct"] < min_pct]
        print(f"Total clases: {len(resumen)}")
        print(f"Clases en cola larga (< {min_pct:.1%}): {len(tail)}")
        print(f"Peso total de la cola larga: {tail['pct'].sum():.2%}")

        display(resumen.head(top_n))
        display(tail.head(20))

        top = resumen.head(top_n)
        fig, ax1 = plt.subplots(figsize=(10, 5))
        ax1.bar(top.index.astype(str), top["conteo"], alpha=0.8)
        ax1.set_ylabel("Conteo")
        ax1.set_xlabel(f"{target} (código)")
        ax1.tick_params(axis="x", rotation=90)

        ax2 = ax1.twinx()
        ax2.plot(top.index.astype(str), top["pct_acum"] * 100, color="red", marker="o")
        ax2.set_ylabel("% acumulado")
        ax2.set_ylim(0, 100)

        plt.title(f"Cola larga de {target} (solo código, Top {top_n})")
        plt.tight_layout()
        plt.savefig(f"Cola larga de {target} (solo codigo) Top {top_n}", dpi=600, bbox_inches="tight")
        plt.show()

        return resumen, tail