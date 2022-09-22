from onelayer_network.linear_classifier import LinearClassifier
from onelayer_network.nolinear_classifier import NoLinearClassifier, NoLinearClassifierType
from onelayer_network.step_classifier import StepClassifier


if __name__ == '__main__':
    #StepClassifier()
    #LinearClassifier()
    classifier = NoLinearClassifier(NoLinearClassifierType.TANH)
    classifier.execute()
