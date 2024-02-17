import jwt

class JWTHandler:
    @staticmethod
    def extract_user_id(jwt_token):
        try:
            decoded_token = jwt.decode(jwt_token, verify=False)
            user_id = decoded_token.get("user_id")
            return user_id
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
