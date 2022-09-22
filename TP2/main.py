from onelayer_network.linear_classifier import LinearClassifier
from onelayer_network.nolinear_classifier import NoLinearClassifier, NoLinearClassifierType
from onelayer_network.step_classifier import StepClassifier
import numpy as np


if __name__ == '__main__':
    # StepClassifier()
    # LinearClassifier()
    np.random.seed(12345)
    classifier = NoLinearClassifier(NoLinearClassifierType.TANH, BETA=0.5, epochs = 10000)
    classifier.execute()
    np.random.seed(12345)
    classifier = NoLinearClassifier(NoLinearClassifierType.EXP, BETA=0.5, epochs = 10000)
    classifier.execute()
