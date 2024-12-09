import csv
import statistics

class CSVProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []
        self.load_data()

    def load_data(self):
        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    self.data.append(list(map(int, row)))
                except ValueError as e:
                    print(f"Error converting row {row}: {e}")
    
    def calculate_average(self):
        if not self.data:
            return None
        return [statistics.mean(col) for col in zip(*self.data)]
    
    def calculate_stddev(self):
        if not self.data:
            return None
        return [statistics.stdev(col) for col in zip(*self.data)]
    
    def summary(self):
        avg = self.calculate_average()
        stddev = self.calculate_stddev()
        return {
            'average': avg,
            'stddev': stddev,
            'total_rows': len(self.data)
        }

if __name__ == "__main__":
    processor = CSVProcessor("data.csv")
    print(processor.summary())
