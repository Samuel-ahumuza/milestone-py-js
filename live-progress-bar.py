import time
import sys

# This function creates and prints the progress bar
def update_progress_bar(progress, total, bar_length=40):
    """
    Displays or updates a console progress bar.
    
    Args:
        progress (int): The current progress (e.g., number of items processed).
        total (int): The total number of items.
        bar_length (int): The character length of the bar.
    """
    
    # Calculate the percentage
    percent = float(progress) / float(total)
    
    # Calculate the number of '#' characters to fill
    filled_length = int(bar_length * percent)
    
    # Create the bar string
    bar = '#' * filled_length + '-' * (bar_length - filled_length)
    
    # Create the output string
    # \r (carriage return) moves the cursor to the beginning of the line
    # end='' prevents print from adding a newline
    output_string = f'\rProgress: [{bar}] {percent * 100:.1f}%'
    
    # Print the bar
    sys.stdout.write(output_string)
    
    # Flush stdout to make sure it displays immediately
    sys.stdout.flush()

# --- How to use it ---

print("Simulating a task...")
total_items = 100

# Loop from 0 to total_items
for i in range(total_items + 1):
    # Update the progress bar for each item
    update_progress_bar(i, total_items)
    
    # Simulate work being done
    time.sleep(0.05) # Sleep for 50 milliseconds

# Print a newline at the end
print("\nTask complete!")

