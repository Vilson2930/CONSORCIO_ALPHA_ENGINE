# ============================================================
# CONSÓRCIO ALPHA ENGINE
# Secondary Market Engine
# Seleção Institucional de Oportunidades
# ============================================================

import pandas as pd

from engine.calculator import analyze_opportunity
from engine.validator import validate_opportunity


class SecondaryMarketEngine:

    def __init__(self):

        self.resultados = []

    # ========================================================
    # Analisa todas as oportunidades
    # ========================================================

    def analyze(self, oportunidades):

        self.resultados = []

        for dados in oportunidades:

            erros = validate_opportunity(dados)

            if erros:
                continue

            r = analyze_opportunity(dados)

            self.resultados.append(r)

        if len(self.resultados) == 0:
            return pd.DataFrame()

        return self.rank()

    # ========================================================
    # Ranking
    # ========================================================

    def rank(self):

        df = pd.DataFrame(self.resultados)

        df = df.sort_values(

            by=[

                "score",
                "roi",
                "lucro_liquido",
                "valor_economico_cota"

            ],

            ascending=False

        )

        df.reset_index(drop=True, inplace=True)

        df.insert(0, "ranking", df.index + 1)

        return df

    # ========================================================
    # Apenas oportunidades aprovadas
    # ========================================================

    def approved(self):

        if len(self.resultados) == 0:
            return pd.DataFrame()

        df = pd.DataFrame(self.resultados)

        return df[df["score"] >= 70]

    # ========================================================
    # Melhor oportunidade
    # ========================================================

    def best(self):

        df = self.rank()

        if len(df) == 0:
            return None

        return df.iloc[0]

    # ========================================================
    # Estatísticas
    # ========================================================

    def statistics(self):

        if len(self.resultados) == 0:

            return {}

        df = pd.DataFrame(self.resultados)

        return {

            "total": len(df),

            "comprar": len(df[df.score >= 80]),

            "negociar": len(df[(df.score >= 70) & (df.score < 80)]),

            "analisar": len(df[(df.score >= 60) & (df.score < 70)]),

            "evitar": len(df[df.score < 60]),

            "score_medio": round(df.score.mean(),2),

            "roi_medio": round(df.roi.mean()*100,2),

            "lucro_medio": round(df.lucro_liquido.mean(),2)

        }
