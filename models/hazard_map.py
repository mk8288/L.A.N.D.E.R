import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage import sobel

def load_image(image_path):
    """
    Load an image and convert it to grayscale.
    
    Parameters:
        image_path (str): Path to the image file.
        
    Returns:
        np.ndarray: Grayscale image as a 2D numpy array.
    """
    img = Image.open(image_path).convert('L')  # Convert to grayscale
    return np.array(img)

def generate_hazard_map(image_data):
    """
    Generate a hazard map from the image data.
    
    Parameters:
        image_data (np.ndarray): 2D array of grayscale pixel values.
        
    Returns:
        np.ndarray: Hazard map normalized to a [0, 1] scale.
    """
    # Invert the image for elevation (lighter = higher)
    inverted_image = 255 - image_data
    
    # Normalize the inverted image to [0, 1]
    hazard_map = inverted_image / 255.0  
    return hazard_map

def detect_edges(image_data):
    """
    Detect edges in the image using the Sobel operator.
    
    Parameters:
        image_data (np.ndarray): 2D array of grayscale pixel values.
        
    Returns:
        np.ndarray: Edge map with values indicating the presence of edges.
    """
    dx = sobel(image_data, axis=0, mode='constant')  # Sobel filter in x direction
    dy = sobel(image_data, axis=1, mode='constant')  # Sobel filter in y direction
    edge_magnitude = np.hypot(dx, dy)  # Calculate the edge magnitude
    edge_magnitude = edge_magnitude / np.max(edge_magnitude)  # Normalize to [0, 1]
    return edge_magnitude

def create_hazard_map(hazard_map, edge_map):
    """
    Create and display the hazard map with edges highlighted.
    
    Parameters:
        hazard_map (np.ndarray): 2D array of hazard levels.
        edge_map (np.ndarray): 2D array indicating edge presence.
    """
    plt.figure(figsize=(10, 8))
    
    # Create a color image based on the hazard map and edges
    color_map = np.zeros((*hazard_map.shape, 3))
    
    # Mark plains in green (low elevation)
    color_map[..., 1] = hazard_map  # Green channel for plains
    
    # Mark edges in red
    color_map[..., 0] = np.where(edge_map > 0.1, 1, 0)  # Red channel for edges

    # Set blue channel to zero (or adjust as needed)
    color_map[..., 2] = 0

    plt.imshow(color_map)
    plt.title('Elevation Hazard Map with Edges')
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.grid(False)
    plt.axis('off')  # Turn off axis
    plt.show()

def main(image_path):
    # Load the image
    image_data = load_image(image_path)
    
    # Generate the hazard map
    hazard_map = generate_hazard_map(image_data)
    
    # Detect edges
    edge_map = detect_edges(image_data)
    
    # Create the hazard map visualization with edges
    create_hazard_map(hazard_map, edge_map)

if __name__ == "__main__":
    # Replace 'path_to_your_image.tif' with the actual image path
    main('moonTest.tif')

