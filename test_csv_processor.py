import pytest
from csv_processor import CSVProcessor

# Test if the CSVProcessor can load data correctly
def test_load_data():
    processor = CSVProcessor('test_data.csv')
    assert len(processor.data) > 0, "Data loading failed"

# Test the average calculation
def test_calculate_average():
    processor = CSVProcessor('test_data.csv')
    result = processor.calculate_average()
    assert isinstance(result, list), "Result should be a list"
    assert len(result) > 0, "Average calculation failed"

# Test standard deviation calculation
def test_calculate_stddev():
    processor = CSVProcessor('test_data.csv')
    result = processor.calculate_stddev()
    assert isinstance(result, list), "Result should be a list"
    assert len(result) > 0, "Standard deviation calculation failed"
