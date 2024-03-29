import smtplib


class Request:
    def __init__(self, email, password):
        self.server = smtplib.SMTP('smtp.yandex.ru', 587)
        self.login, self.password = email, password
        self.server.ehlo()
        self.server.starttls()
        self.response = self.server.login(self.login, self.password)

    def send_email(self, subject, to_addr, body_text):
        """
        Send an email
        """

        BODY = "\r\n".join((
            "From: %s" % self.login,
            "To: %s" % to_addr,
            "Subject: %s" % subject,
            "",
            body_text
        ))

        self.server.sendmail(self.login, [to_addr], BODY)

