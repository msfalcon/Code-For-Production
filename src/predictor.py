
class Predictor:
    def __init__(self, model, preprocessor, latest_data):
        """
        Initialize Predictor with model, preprocessor, and latest data.
        
        Parameters:
        model: The trained machine learning model used for making predictions.
        preprocessor: The preprocessor object used to scale/transform the data.
        latest_data (pd.DataFrame or np.ndarray): The latest data on which predictions are to be made.
        """
        self.model = model  # Assign the model to an instance variable
        self.preprocessor = preprocessor  # Assign the preprocessor to an instance variable
        self.latest_data = latest_data  # Assign the latest data to an instance variable

    def make_predictions(self):
        """
        Make predictions on the latest data.
        
        Returns:
        np.ndarray: The predictions made by the model on the scaled latest data.
        """
        # Ensure the latest data has the same feature names and structure
        scaled_data = self.preprocessor.transform(self.latest_data)  # Scale/transform the latest data
        predictions = self.model.predict(scaled_data)  # Use the model to make predictions on the scaled data
        return predictions  # Return the predictions
