from itertools import islice

# Sample dictionary
chapters_html = {
    "Chapter 1": "<html>Content of Chapter 1</html>",
    "Chapter 2": "<html>Content of Chapter 2</html>",
    "Chapter 3": "<html>Content of Chapter 3</html>",
    "Chapter 4": "<html>Content of Chapter 4</html>",
    "Chapter 5": "<html>Content of Chapter 5</html>"
}

# Define the range you want to slice (e.g., from chapter 2 to 4 inclusive)
start = 1  # starting index (0-based)
end = 4    # ending index (0-based, exclusive)

# Create a sub-iterator for the specified range
sliced_items = islice(chapters_html.items(), start, end)

# Convert the sliced items back to a dictionary
sliced_dict = dict(sliced_items)

# Print the sliced dictionary
print(sliced_dict)
