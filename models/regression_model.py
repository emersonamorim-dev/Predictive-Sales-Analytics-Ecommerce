import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

def train_model():
    data = pd.read_parquet("/data/processed/sales_data.parquet")
    X = data.drop("sales", axis=1)
    y = data["sales"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, "/models/sales_regression_model.pkl")

if __name__ == "__main__":
    train_model()
