from dao.model.user import User


class UserDAO:
	def __init__(self, session):
		self.session = session

	def create(self, data):

		user = User(**data)
		self.session.add(user)
		self.session.commit()
		return user

	def get_all(self):
		return self.session.query(User).all()

	def get_by_username(self, username):
		return self.session.query(User).filter(User.username == username).first()

	def get_one(self, pk: int):
		return self.session.query(User).get(pk)

	def delete(self, pk):
		user = self.get_one(pk)
		self.session.delete(user)
		self.session.commit()

