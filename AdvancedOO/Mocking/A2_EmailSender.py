from unittest.mock import MagicMock


class EmailSender:
    def send_email(self):
        # Sendet eine E-Mail
        pass

# Test-Klasse

class TestEmailSender:
    def email_test(self):

        email_content = EmailSender()
        email_content.send_email = MagicMock(
            return_value={"recipient": "Johnny@hftm.ch", "Body": "Hello Boss"})

        # Rufe die Methode auf
        result = email_content.send_email("Johnny@hftm.ch")

        # Überprüfen, ob die Methode aufgerufen wurde
        email_content.send_email.assert_called_once_with("Johnny@hftm.ch")
        assert result == {"recipient": "Johnny@hftm.ch", "Body": "Hello Boss"}

TestEmailSender().email_test()