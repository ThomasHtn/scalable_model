from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def preprocessing(df, numerical_cols, categorical_cols):
    num_pipeline = Pipeline(
        [("imputer", SimpleImputer(strategy="mean")), ("scaler", StandardScaler())]
    )

    cat_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False)),
        ]
    )

    preprocessor = ColumnTransformer(
        [("num", num_pipeline, numerical_cols), ("cat", cat_pipeline, categorical_cols)]
    )

    X_processed = preprocessor.fit_transform(df)

    return X_processed, None, preprocessor
