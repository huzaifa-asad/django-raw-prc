from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created



@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("-------------------------------------")
    print("Logged-in Signal... Run Intro..")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print("User Password: ", user.password)
    print(f"Kwargs: {kwargs}")
    
# use decorator or use this: 
# user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print("-------------------------------------")
    print("Logged-out Signal... Run Outro..")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print("User Password: ", user.password)
    print(f"Kwargs: {kwargs}")
    

@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwargs):
    print("-------------------------------------")
    print("Login Failed Signals...")
    print("Sender: ", sender)
    print("Request: ", request)
    print("Credentials: ", credentials)
    print(f"Kwargs: {kwargs}")
    
    
# @receiver(pre_save, sender=User)
# def log_out(sender, instance, **kwargs):
#     print("-------------------------------------")
#     print("Pre Save Signal...")
#     print("Sender: ", sender)
#     print("Instance: ", instance)
#     print(f"Kwargs: {kwargs}")


@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print("-------------------------------------")
        print("Post Save Signals...")
        print("New Record")
        print("Sender: ", sender)
        print("Instance: ", instance)
        print("Created: ", created)
        print(f"Kwargs: {kwargs}")
    else:
        print("-------------------------------------")
        print("Post Save Signals...")
        print("Update")
        print("Sender: ", sender)
        print("Instance: ", instance)
        print("Created: ", created)
        print(f"Kwargs: {kwargs}")
        
        
@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("-------------------------------------")
    print("Pre Delete Signal...")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f"Kwargs: {kwargs}")
    
@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("-------------------------------------")
    print("Post Delete Signal...")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f"Kwargs: {kwargs}")
    

@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("-------------------------------------")
    print("Pre Init Signal...")
    print("Sender: ", sender)
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
    
@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("-------------------------------------")
    print("Post Init Signal...")
    print("Sender: ", sender)
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
    

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("------------------------------------------")
    print("before_install_app....")
    print("Sender: ", sender)
    print("App Config: ", app_config)
    print("Verbosity: ", verbosity)
    print("Interactive: ", interactive)
    print("Using: ", using)
    print("Plan: ", plan)
    print("App: ", apps)
    print(f"Kwargs: {kwargs}")
    
@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("------------------------------------------")
    print("bt_end_migrate_flush....")
    print("Sender: ", sender)
    print("App Config: ", app_config)
    print("Verbosity: ", verbosity)
    print("Interactive: ", interactive)
    print("Using: ", using)
    print("Plan: ", plan)
    print("App: ", apps)
    print(f"Kwargs: {kwargs}")


@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("-------------------------------------")
    print("At Beginning Request Signal...")
    print("Sender: ", sender)
    print("Environ: ", environ)
    print(f"Kwargs: {kwargs}")

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("-------------------------------------")
    print("At Ending Request Signal...")
    print("Sender: ", sender)
    print(f"Kwargs: {kwargs}")
    
@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    print("-------------------------------------")
    print("At Request Exception...")
    print("Sender: ", sender)
    print("Request: ", request)
    print(f"Kwargs: {kwargs}")
    

@receiver(connection_created)
def connect_db(sender, connection, **kwargs):
    print("-------------------------------------")
    print("Initial connection to the database...")
    print("Sender: ", sender)
    print("Connection: ", connection)
    print(f"Kwargs: {kwargs}")