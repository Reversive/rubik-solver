from onelayer_network.linear_classifier import LinearClassifier
from onelayer_network.nolinear_classifier import NoLinearClassifier, NoLinearClassifierType
from onelayer_network.step_classifier import StepClassifier
import configparser


def get_classifier(config):
    general_config = config['general_config']
    if general_config['classifier'] == 'step':
        return StepClassifier(config['step_config'])
    elif general_config['classifier'] == 'linear':
        return LinearClassifier(config['linear_classifier'])
    elif general_config['classifier'] == 'nolinear':
        return NoLinearClassifier(config['nolinear_classifier'])



if __name__ == '__main__':
    # StepClassifier()
    # LinearClassifier()
    # classifier = NoLinearClassifier(NoLinearClassifierType.TANH)
    # classifier.execute()

    config = configparser.ConfigParser()
    config.read("./config.yaml")
    classifier = get_classifier(config)
    classifier.execute()
