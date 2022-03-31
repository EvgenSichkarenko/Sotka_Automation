import imaplib
import email
import sys
import re

class Email:
	def __init__(self, app):
		self.app = app

	def get_link_from_email(self):
		server = "imap.mail.yahoo.com"
		port = 993
		login = "evgen20@yahoo.com"
		password = "udxyliiyxemzfjww"

		mail = imaplib.IMAP4_SSL(server, port)
		mail.login(login, password)
		mail.select()
		type, data = mail.search(None, "(FROM 'sotka.io')")
		data = data[0].split()
		latest_id = data[-1]
		result, data = mail.fetch(latest_id, "(RFC822)")
		raw_email = data[0][1]
		message = email.message_from_bytes(raw_email)
		text, encoding, mime = get_message_info(message)
		link = re.search("(?P<url>https?://[^\s]+)", text).group("url")
		return link

def get_message_info(message):
	"""Получить текст сообщения в правильной кодировке.

	Параметры:
        - message: сообщение email.Message.

	Результат:
      - message (str): сообщение или строка "Нет тела сообщения";
      - encoding (str): кодировка сообщения или "-";
      - mime (str): MIME-тип или "-"."""

	# Алгоритм получения текста письма:
	# - если письмо состоит из нескольких частей
	# (message.is_multipart()) - необходимо пройти по составным
	# частям письма: "text/plain" или "text/html"
	# - если нет - текст можно получить напрямую

	message_text, encoding, mime = "Нет тела сообщения", "-", "-"
	if message.is_multipart():
		for part in message.walk():
			if part.get_content_type() in ("text/html", "text/plain"):
				message_text, encoding, mime = get_part_info(part)
				break  # Только первое вхождение
	else:
		message_text, encoding, mime = get_part_info(message)

	return message_text, encoding, mime

def get_part_info(part):

	encoding = part.get_content_charset()
	if not encoding:
		encoding = sys.stdout.encoding

	mime = part.get_content_type()
	message = part.get_payload(decode=True).decode(encoding, errors="ignore").strip()

	return message, encoding, mime



