from google.cloud.firestore_v1 import Client, ArrayUnion, ArrayRemove, Increment, FieldFilter
from google.oauth2 import service_account
from lib.models import UserBase, User
import os
import uuid
import traceback

CREDENTIALS_PATH = "./firebase.json"

cred = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH)

class FirestoreClient(Client):
    def __init__(self, credentials=cred):
        super().__init__(credentials=credentials)

    def add_user(self, user_base: UserBase) -> User:
        for _ in self.collection("users").\
                where(filter=FieldFilter("email", "==", user_base.email)).limit(1).stream():
            raise Exception("Tente outro email")

        while True:
            user_id = str(uuid.uuid4())

            if self.collection("users").document(user_id).get().exists:
                continue
            break

        user = User(id=user_id, **user_base.model_dump())
        
        print(user.model_dump())

        self.collection("users").document(user_id).set(user.model_dump())

        return user

    def get_user(self, user_mail, user_password):
        try:
            query = self.collection("users")\
                .where(filter=FieldFilter("email", "==", user_mail))\
                .where(filter=FieldFilter("password", "==", user_password))\
                .limit(1).stream()
            return User(**(next(query).to_dict()))
        except:
            traceback.print_exc()
            raise Exception("Verifique se seu email/senha está correto e tente novamente")
    
    def login_by_id(self, user_id :str):
        user_ref = self.collection("users").document(user_id).get()
        if user_ref.exists:
            return User(**user_ref.to_dict())
        raise Exception("Não foi possível encontrar o usuário salvo")

firestore = FirestoreClient()