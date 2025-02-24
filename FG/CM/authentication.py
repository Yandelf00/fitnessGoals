from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class CustomAuth(BaseBackend):
    def authenticate(self, request, username = None ,password = None, **kwargs):
        Agent = get_user_model()
        try : 
            agent = Agent.objects.get(username = username)
            if agent.check_password(password):
                return agent
        except Agent.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        Agent = get_user_model()
        try :
            return Agent.objects.get(id=user_id)
        except Agent.DoesNotExist: 
            return None
