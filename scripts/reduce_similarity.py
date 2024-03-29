import numpy as np
import json

def reduce_similarity(similarity_matrix, threshold):
    """
    Reduces the size of the similarity matrix by setting values below the threshold to zero.

    Args:
    - similarity_matrix (numpy.ndarray): The original similarity matrix.
    - threshold (float): The similarity threshold below which values will be set to zero.

    Returns:
    - numpy.ndarray: The reduced similarity matrix.
    """
    reduced_matrix = np.copy(similarity_matrix)
    reduced_matrix[reduced_matrix < threshold] = 0
    return reduced_matrix

def save_similarity_matrix(similarity_matrix, filename):
    """
    Saves the similarity matrix to a JSON file.

    Args:
    - similarity_matrix (numpy.ndarray): The similarity matrix to save.
    - filename (str): The name of the JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(similarity_matrix.tolist(), f)

# Example usage
if __name__ == "__main__":
    # Load the original similarity matrix from a JSON file
    with open('similarity.json', 'r') as f:
        similarity_data = json.load(f)
    similarity_matrix = np.array(similarity_data)

    # Reduce the similarity matrix
    threshold = 0.5  # Set your desired threshold here
    reduced_similarity_matrix = reduce_similarity(similarity_matrix, threshold)

    # Save the reduced similarity matrix to a JSON file
    save_similarity_matrix(reduced_similarity_matrix, 'reduced_similarity.json')
