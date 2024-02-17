import jwt

class JWTHandler:
    @staticmethod
    def extract_user_id(jwt_token):
        # Extract user identifier from JWT payload
        # Ensure proper error handling and validation
        try:
            decoded_token = jwt.decode(jwt_token, verify=False)
            user_id = decoded_token.get("user_id")
            return user_id
        except jwt.ExpiredSignatureError:
            # Handle token expiration
            return None
        except jwt.InvalidTokenError:
            # Handle invalid tokens
            return None
