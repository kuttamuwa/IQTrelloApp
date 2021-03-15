from abc import ABC

import yagmail


class BaseYagMailSender(ABC):
    __source_mail = 'ucok.umut1190'
    __source_pass = 'figo1190'
    __host = 'smtp.gmail.com'

    _yag = yagmail.SMTP(__source_mail, __source_pass, __host, encoding='utf-8')

    @classmethod
    def send_mail(cls, to, subject, content):
        pass


class YagGmailMailSender(BaseYagMailSender):
    @classmethod
    def send_mail(cls, to, subject, content):
        res = cls._yag.send(to, subject, content)

        # do something
        return res
