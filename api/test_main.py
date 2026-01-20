import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from api.main import app


class TestMailClassification:
    
    @pytest.fixture
    def client(self):
        return TestClient(app)
    
    @pytest.fixture
    def sample_mail(self):
        return {
            "to_address": "user@example.com",
            "subject": "Meeting next week",
            "body": "Please confirm attendance"
        }
    
    @pytest.fixture
    def spam_mail(self):
        return {
            "to_address": "victim@example.com",
            "subject": "WIN FREE MONEY NOW!!!",
            "body": "Click here to claim"
        }
    
    @patch('api.src.services.mail_service.MailService')
    def test_classify_ham(self, mock_service, client, sample_mail):
        mock_instance = Mock()
        mock_instance.classify.return_value = {
            "label": "HAM",
            "confidence": 0.95,
            "probabilities": {"HAM": 0.95, "SPAM": 0.05}
        }
        mock_service.return_value = mock_instance
        
        response = client.post("/api/classify", json=sample_mail)
        
        assert response.status_code == 200
        assert response.json()["label"] == "HAM"
        assert response.json()["confidence"] >= 0.95
    
    @patch('api.src.services.mail_service.MailService')
    def test_classify_spam(self, mock_service, client, spam_mail):
        mock_instance = Mock()
        mock_instance.classify.return_value = {
            "label": "SPAM",
            "confidence": 0.98,
            "probabilities": {"HAM": 0.02, "SPAM": 0.98}
        }
        mock_service.return_value = mock_instance
        
        response = client.post("/api/classify", json=spam_mail)
        
        assert response.status_code == 200
        assert response.json()["label"] == "SPAM"
    
    def test_missing_field(self, client):
        incomplete_mail = {
            "to_address": "user@example.com",
            "subject": "Test"
        }
        
        response = client.post("/api/classify", json=incomplete_mail)
        assert response.status_code == 422