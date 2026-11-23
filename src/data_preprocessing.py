
import pandas as pd
from pathlib import Path


def load_data():
    """
    Load the SECOM manufacturing dataset.

    Returns:
        X: DataFrame containing 590 input features.
        y: Series containing manufacturing quality outcomes.
    """

    # Locate the project root
    project_root = Path(__file__).resolve().parent.parent

    # Define dataset paths
    data_dir = project_root / "secom_data" / "raw"

    features_path = data_dir / "secom.data"
    labels_path = data_dir / "secom_labels.data"

    # Load input features
    X = pd.read_csv(
        features_path,
        sep=r"\s+",
        header=None
    )

    # Load target variable
    y_raw = pd.read_csv(
        labels_path,
        sep=r"\s+",
        header=None
    )

    y = y_raw.iloc[:, 1]

    return X, y
