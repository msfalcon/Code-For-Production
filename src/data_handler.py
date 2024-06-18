
# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import logging  # For logging errors and other messages

class DataHandler:
    def __init__(self, historical_data_path, latest_data_path=None):
        """
        Initialize DataHandler with paths to historical and latest data.
        
        Parameters:
        historical_data_path (str): Path to the historical data CSV file.
        latest_data_path (str, optional): Path to the latest data CSV file. Default is None.
        """
        self.historical_data_path = historical_data_path  # Path to the historical data file
        self.latest_data_path = latest_data_path  # Path to the latest data file, if provided
        self.historical_data = None  # Placeholder for historical data
        self.latest_data = None  # Placeholder for latest data

    def load_data(self):
        """
        Load data from CSV files.
        
        This method reads the historical data from the specified path.
        If a latest data path is provided, it also reads the latest data.
        """
        try:
            self.historical_data = pd.read_csv(self.historical_data_path)  # Load historical data
            if self.latest_data_path:
                self.latest_data = pd.read_csv(self.latest_data_path)  # Load latest data if path is provided
        except Exception as e:
            # Log any errors encountered during loading
            logging.error(f"Error loading data: {e}")
            raise  # Re-raise the exception after logging

    def get_historical_data(self):
        """
        Return the historical data.
        
        Returns:
        pd.DataFrame: The historical data loaded from the CSV file.
        """
        return self.historical_data  # Return the historical data

    def get_latest_data(self):
        """
        Return the latest data.
        
        Returns:
        pd.DataFrame: The latest data loaded from the CSV file, if available.
        """
        return self.latest_data  # Return the latest data, if available

