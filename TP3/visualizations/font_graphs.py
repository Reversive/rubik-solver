
IMAGE_WIDTH = 8
IMAGE_HEIGHT = 7
INPUT_SIZE = 7*IMAGE_WIDTH
LATENT_SPACE_DIM = 2

def plot_error_and_accuracy_changing_layers():
    hidden_layers = [
        [  INPUT_SIZE, 
            IMAGE_WIDTH,
            LATENT_SPACE_DIM,
            IMAGE_WIDTH, 
            INPUT_SIZE],
    ]
