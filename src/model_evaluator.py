# Import the necessary library for generating a classification report
from sklearn.metrics import classification_report

class ModelEvaluator:
    def __init__(self, model, X_test, y_test):
        """
        Initialize the ModelEvaluator with a model, test features, and test labels.
        
        Parameters:
        model: The trained machine learning model to be evaluated.
        X_test: Test data features (independent variables).
        y_test: True labels for the test data (dependent variable).
        """
        self.model = model  # Assign the model to an instance variable
        self.X_test = X_test  # Assign the test data features to an instance variable
        self.y_test = y_test  # Assign the true labels to an instance variable

    def evaluate(self):
        """
        Evaluate the model on the test data and return a classification report.
        
        Returns:
        A string representation of the classification report which includes 
        precision, recall, f1-score, and support for each class.
        """
        y_pred = self.model.predict(self.X_test)  # Use the model to make predictions on the test data
        return classification_report(self.y_test, y_pred)  # Generate and return the classification report
