from itertools import islice

def slice_dict(d, start, end):
    """Slice a dictionary to include items from start index to end index (exclusive).
    
    Args:
        d (dict): The dictionary to slice.
        start (int): The starting index (inclusive).
        end (int): The ending index (exclusive).
    
    Returns:
        dict: A new dictionary with items from the specified range.
    """
    sliced_items = islice(d.items(), start, end)
    return dict(sliced_items)

def save_html(html, filename):
    """Save the given HTML content to a file.
    
    Args:
        html (str): The HTML content to save.
        filename (str): The name of the file to save the HTML content to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html)

if __name__ == "__main__":

    # Example usage
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

    # Get the sliced dictionary
    sliced_dict = slice_dict(chapters_html, start, end)

    # Print the sliced dictionary
    print(sliced_dict)
