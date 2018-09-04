from Server.Server import Application
from Services.services import Services

if __name__ == "__main__":
    services = Services()
    services.db_service.init_db()

    application = Application(services)
    application.start_server()
