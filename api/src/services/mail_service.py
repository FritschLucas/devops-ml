from inference import SpamClassifier
from api.src.models.mail import Mail

class MailService:
    def __init__(self, mail: Mail):
        self.classifier = SpamClassifier(config_path="inference_config.yaml")
        self.mail = mail

    def classify(self):
        result = self.classifier.predict_single(self.mail.subject)
        print(f"Prediction: {result['label']}")
        print(f"Confidence: {result['confidence']:.2%}")
        print(f"Probabilities: {result['probabilities']}")
        return result
