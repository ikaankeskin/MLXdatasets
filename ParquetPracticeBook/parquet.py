import pandas as pd
import requests
import time

# Function to get the maximum item ID
def get_max_item_id():
    response = requests.get('https://hacker-news.firebaseio.com/v0/maxitem.json')
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to get max_item_id. Exiting.")
        return None

# Initialize DataFrame to hold all the items
df = pd.DataFrame()

# Initialize max_item_id with the current maximum item id from the API
max_item_id = get_max_item_id()
current_id = max_item_id
step_size = 1
post_capacity = 1000

print(f"Starting to fetch items from item ID {max_item_id} until {max_item_id-post_capacity}.")


# Loop through item IDs from max_item_id to 1
for item_id in range(current_id, (current_id-post_capacity), -1):
    
    print(f"Fetching data for item ID {item_id}...")
    
    # Fetch item data from API
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
    response = requests.get(item_url)
    
    if response.status_code == 200:
        item_data = response.json()
        if item_data is not None:      
            # Append to DataFrame
            df = pd.concat([df, pd.DataFrame([item_data])], ignore_index=True)
        else:
            print(f"No data for item ID {item_id}. Skipping.")
            current_id -= step_size
    else:
        print(f"Failed to fetch data for item ID {item_id}")
    
    
    # Add sleep to respect rate limits if any
    time.sleep(0.1)

print(f"Finished fetching items")

# Save DataFrame to Parquet format
df.to_parquet('hacker_news_Mini.parquet')
print("Saved data to hacker_news_2022.parquet.")
