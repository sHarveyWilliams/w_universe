import sqlite3
import os
import json
from flask import Flask, request, Response, render_template


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%', block_end_string='%)',
        variable_start_string='((', variable_end_string='))',
        comment_start_string='(#', comment_end_string='#)',
    ))


class Application:

    def __init__(self, services):
        self.self_dir = os.path.dirname(os.path.abspath(__file__))

        self.app = CustomFlask(__name__)
        self.app.env = "development"

        self.services = services

        @self.app.before_request
        def before_request():
            self.services.db_service.connect_db()

        @self.app.teardown_request
        def teardown_request(exception):
            self.services.db_service.disconnect_db()

        @self.app.route("/")
        def index():
            goods = self.services.logic_service.get_all_goods()

            return render_template("mainpage.html", goods_l=goods)

        @self.app.route("/dbWorkspace")
        def db_workspace():
            return render_template("db_workspace.html")

        @self.app.route("/getDelivery", methods=["POST"])
        def get_delivery():
            data = request.json
            delivery = self.services.logic_service.get_needable_delivery(data["settings"])
            return Response(json.dumps({"delivery": delivery}), mimetype=u'application/json')

    def start_server(self):
        self.app.run(host="127.0.0.1", port="8080", debug=True)

        # When server is down
        self.services.db_service.dump_db()
        self.services.db_service.remove_db()


if __name__ == "__main__":
    application = Application()
    application.start_server()
