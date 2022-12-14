import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
	def __init__(self, dao: UserDAO):
		self.dao = dao

	def get_all(self):
		return self.dao.get_all()

	def get_one(self, pk: int):
		return self.dao.get_one(pk)

	def create(self, data: dict):
		data["password"] = self.get_hash(data["password"])
		return self.dao.create(data)

	def get_by_username(self, username: str):
		return self.dao.get_by_username(username)

	def get_hash(self, password: str):
		result = hashlib.pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),  # Convert the password to bytes
			PWD_HASH_SALT,
			PWD_HASH_ITERATIONS
			)
		return base64.b64encode(result)

	# Compare encode and decode passwords
	def compare_passwords(self, password_hash: bytes, password: str) -> bool:
		decode_password = base64.b64decode(password_hash)
		new_password = base64.b64decode(self.get_hash(password))

		return hmac.compare_digest(decode_password, new_password)



