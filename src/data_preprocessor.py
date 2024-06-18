
# Import the necessary library for data scaling
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self, data):
        """
        Initialize DataPreprocessor with data to be processed.
        
        Parameters:
        data (pd.DataFrame or np.ndarray): The data to be preprocessed.
        """
        self.data = data  # Original data to be processed
        self.scaled_data = None  # Placeholder for the scaled data
        self.scaler = StandardScaler()  # Initialize the StandardScaler

    def preprocess(self):
        """
        Preprocess the data (e.g., scaling).
        
        Returns:
        np.ndarray: The scaled version of the original data.
        
        Raises:
        ValueError: If the data is empty.
        """
        if self.data.empty:
            raise ValueError("Data is empty")  # Raise an error if the data is empty
        self.scaled_data = self.scaler.fit_transform(self.data)  # Fit and transform the data using the scaler
        return self.scaled_data  # Return the scaled data

    def transform(self, data):
        """
        Transform the data using the same scaler.
        
        Parameters:
        data (pd.DataFrame or np.ndarray): The new data to be transformed using the already fitted scaler.
        
        Returns:
        np.ndarray: The transformed version of the new data.
        
        Raises:
        ValueError: If the new data is empty.
        """
        if data.empty:
            raise ValueError("Data is empty")  # Raise an error if the new data is empty
        transformed_data = self.scaler.transform(data)  # Transform the new data using the fitted scaler
        return transformed_data  # Return the transformed data
