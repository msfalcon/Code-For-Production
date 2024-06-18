
# Import the necessary library for splitting data into training and testing sets
from sklearn.model_selection import train_test_split

class ModelTrainer:
    def __init__(self, model, X, y):
        """
        Initialize ModelTrainer with a model, features, and target variable.
        
        Parameters:
        model: The machine learning model to be trained.
        X (pd.DataFrame or np.ndarray): Features (independent variables) for training.
        y (pd.Series or np.ndarray): Target variable (dependent variable) for training.
        """
        self.model = model  # Assign the model to an instance variable
        # Split the data into training and testing sets with 80-20 split and a fixed random state for reproducibility
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train(self):
        """
        Train the model using the training data.
        """
        self.model.fit(self.X_train, self.y_train)  # Fit the model to the training data

    def get_training_data(self):
        """
        Return the training data.
        
        Returns:
        tuple: A tuple containing the training features and target variable.
        """
        return self.X_train, self.y_train  # Return the training features and target variable

    def get_test_data(self):
        """
        Return the test data.
        
        Returns:
        tuple: A tuple containing the test features and target variable.
        """
        return self.X_test, self.y_test  # Return the test features and target variable
