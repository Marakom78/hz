from models.active_record_entity import ActiveRecordEntity

class User(ActiveRecordEntity):
  _nickname = None
  _email = None
  _is_confirmed = None
  _role = None
  _password_hash = None
  _author_token = None
  _created_at = None

  def get_nickname(self):
    return self._nickname

  def get_email(self):
    return self._email

  def get_role(self):
    return self._role

  def get_password_hash(self):
    return self._password_hash
        
  def get_author_token(self):
    return self._author_token

  def get_created_ath(self):
    return self._created_at



  def set_nickname(self, author_id):
    self._nickname = nickname

  def set_email(self, name):
    self._email = email

  def set_role(self, text):
    self._role = role



  @staticmethod
  def get_table_name():
    return 'users'