import pandas as pd
import numpy as np


class FeatureValidator:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    # ==========================================================
    # Missing Values
    # ==========================================================

    def check_missing_values(self):

        missing = (
            self.df.isnull()
            .sum()
            .sort_values(ascending=False)
        )

        missing = missing[missing > 0]

        return missing

    # ==========================================================
    # Constant Features
    # ==========================================================

    def check_constant_features(self):

        constant = []

        for col in self.df.columns:

            if self.df[col].nunique() <= 1:
                constant.append(col)

        return constant

    # ==========================================================
    # Duplicate Features
    # ==========================================================

    def check_duplicate_features(self):

        duplicates = []

        cols = self.df.columns

        for i in range(len(cols)):

            for j in range(i + 1, len(cols)):

                if self.df[cols[i]].equals(self.df[cols[j]]):

                    duplicates.append(
                        (cols[i], cols[j])
                    )

        return duplicates

    # ==========================================================
    # Highly Correlated Features
    # ==========================================================

    def check_correlation(
        self,
        threshold=0.95
    ):

        numeric_df = self.df.select_dtypes(include=np.number)

        corr_matrix = numeric_df.corr().abs()

        correlated = []

        for i in range(len(corr_matrix.columns)):

            for j in range(i):

                corr = corr_matrix.iloc[i, j]

                if corr > threshold:

                    correlated.append(
                        (
                            corr_matrix.columns[i],
                            corr_matrix.columns[j],
                            round(corr, 4)
                        )
                    )

        return correlated

    # ==========================================================
    # Infinite Values
    # ==========================================================

    def check_infinite_values(self):

        inf = np.isinf(
            self.df.select_dtypes(include=np.number)
        ).sum()

        inf = inf[inf > 0]

        return inf

    # ==========================================================
    # Target Leakage
    # ==========================================================

    def check_target_leakage(self):

        leakage = []

        targets = [
            "Target",
            "Target_Return",
            "Target_Class"
        ]

        for col in self.df.columns:

            if col in targets:

                leakage.append(col)

        return leakage

    # ==========================================================
    # Complete Report
    # ==========================================================

    def generate_report(self):

        print("=" * 60)
        print("FEATURE VALIDATION REPORT")
        print("=" * 60)

        print(f"\nDataset Shape : {self.df.shape}")

        # Missing Values
        missing = self.check_missing_values()

        print("\nMissing Values")

        if len(missing) == 0:

            print("✔ No Missing Values")

        else:

            print(missing)

        # Constant Features
        constant = self.check_constant_features()

        print("\nConstant Features")

        if len(constant) == 0:

            print("✔ None")

        else:

            for c in constant:
                print(c)

        # Infinite Values
        inf = self.check_infinite_values()

        print("\nInfinite Values")

        if len(inf) == 0:

            print("✔ None")

        else:

            print(inf)

        # Duplicate Features
        dup = self.check_duplicate_features()

        print("\nDuplicate Features")

        if len(dup) == 0:

            print("✔ None")

        else:

            for d in dup:
                print(d)

        # Correlation
        corr = self.check_correlation()

        print("\nHighly Correlated Features (>0.95)")

        if len(corr) == 0:

            print("✔ None")

        else:

            for c in corr:

                print(
                    f"{c[0]} <--> {c[1]} : {c[2]}"
                )

        # Leakage
        leak = self.check_target_leakage()

        print("\nTarget Columns")

        for l in leak:
            print(l)

        print("\nValidation Complete")
        print("=" * 60)