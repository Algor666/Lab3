import pandas as pd

# Path to the dataset
FILE_PATH = 'netflix_list.csv'

# Load data
data = pd.read_csv(FILE_PATH)

# Task 1: Iterating through main cast with more than 50 characters
class MainCastIterator:
    def __init__(self, data):
        self.data = data
        self.current_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current_idx < len(self.data):
            record = self.data.iloc[self.current_idx]
            self.current_idx += 1
            cast = record['cast']
            if len(cast) > 50:
                return cast
        raise StopIteration

# Displaying first 10 casts with length > 50
print("Top 10 main casts (longer than 50 characters):")
iterator = MainCastIterator(data)
for _ in range(10):
    print(next(iterator))

# Task 2: Calculating dataset statistics
print("\nDataset Overview:")

def get_statistics(data):
    # Handle 'isAdult' column, converting non-numeric values to NaN and replacing with 0
    data['isAdult'] = pd.to_numeric(data['isAdult'], errors='coerce').fillna(0).astype(int)
    
    # Count adult content (where isAdult == 1)
    adult_count = data['isAdult'].sum()
    
    # Average rating for items with more than 1000 votes
    popular_data = data[data['numVotes'] > 1000]
    avg_rating = popular_data['rating'].mean()
    
    return adult_count, avg_rating

adult_count, avg_rating = get_statistics(data)
print(f"Adult content count: {adult_count}")
print(f"Average rating (more than 1000 votes): {avg_rating:.2f}")

# Task 3: Generating filtered show titles based on criteria
print("\nFiltered Titles (episodes > 10 and rating above average):")

def get_high_rating_shows(data):
    # Find the overall average rating
    overall_avg_rating = data['rating'].mean()

    # Filter and return titles that meet criteria (episodes > 10, rating > overall average)
    filtered_titles = (
        record['title']
        for _, record in data.iterrows()
        if record['episodes'] > 10 and record['rating'] > overall_avg_rating
    )
    return filtered_titles

high_rating_shows = get_high_rating_shows(data)

# Show the first 10 filtered titles
for show in list(high_rating_shows)[:10]:
    print(show)

