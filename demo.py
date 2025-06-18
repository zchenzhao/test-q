from main import timestamp_to_epoch, epoch_to_timestamp
import time

# Current time demonstration
current_epoch = time.time()
print(f"Current epoch time: {current_epoch}")

# Convert to timestamp
current_timestamp = epoch_to_timestamp(current_epoch)
print(f"As ISO timestamp: {current_timestamp}")

# Convert back to epoch
converted_epoch = timestamp_to_epoch(current_timestamp)
print(f"Converted back to epoch: {converted_epoch}")
print(f"Difference: {abs(current_epoch - converted_epoch)} seconds")

# Example with a specific date
specific_timestamp = "2023-01-01T12:00:00Z"
specific_epoch = timestamp_to_epoch(specific_timestamp)
print(f"\nTimestamp {specific_timestamp} as epoch: {specific_epoch}")

# Custom format example
custom_timestamp = "01/01/2023 12:00:00"
custom_format = "%m/%d/%Y %H:%M:%S"
custom_epoch = timestamp_to_epoch(custom_timestamp, custom_format)
print(f"Timestamp {custom_timestamp} as epoch: {custom_epoch}")

# Convert epoch back to different formats
iso_format = epoch_to_timestamp(custom_epoch)
custom_format_result = epoch_to_timestamp(custom_epoch, "%m/%d/%Y %H:%M:%S")
print(f"Epoch {custom_epoch} as ISO: {iso_format}")
print(f"Epoch {custom_epoch} as custom format: {custom_format_result}")