class LogicService:

    def __init__(self, services):
        self.services = services

    def get_range_of_goods(self, ids=None):
        if ids is None:
            db_answer = self.services.db_service.exec("select id, name from rangeofgoods")
        elif ids:
            db_answer = self.services.db_service.exec("select id, name from rangeofgoods "
                                                      "where id in (" + ", ".join(ids) + ")")
        else:
            return {"goods": []}

        if db_answer["error"] is None:
            goods = [{"id": str(good[0]), "name": good[1]}
                     for good in db_answer["fetch"]]
        else:
            goods = []

        return {"goods": goods}

    def get_all_goods(self):
        goods = self.get_range_of_goods()

        for good in goods["goods"]:
            good["checked"] = False
            good["show"] = True

        return goods

    def get_needable_delivery(self, settings):
        goods_parameters = self.get_goods_parameters(settings)
        goods_parameters = sorted(goods_parameters, key=lambda k: k["count"])

        delivery = {}
        delivery_ones = []
        delivery_more = []

        for good_parameters in goods_parameters:
            if good_parameters["count"] == 1:
                if good_parameters["delivery"][0]["id"] in delivery_ones:
                    delivery[good_parameters["delivery"][0]["id"]]["ones"].append(good_parameters["id"])

                else:
                    delivery_ones.append(good_parameters["delivery"][0]["id"])
                    delivery[good_parameters["delivery"][0]["id"]] = {"ones": [good_parameters["id"]]}

            else:
                temp_delivery = good_parameters["delivery"].copy()
                supplier_added = False
                first_max_id = ""

                while temp_delivery:
                    max_match_supplier_id = max(temp_delivery, key=lambda k: k["params_match"])["id"]
                    if first_max_id == "":
                        first_max_id = max_match_supplier_id

                    if max_match_supplier_id in delivery.keys():
                        if max_match_supplier_id in delivery_more:
                            delivery[max_match_supplier_id]["mores"].append(good_parameters["id"])
                        else:
                            delivery_more.append(max_match_supplier_id)
                            delivery[max_match_supplier_id]["mores"] = [good_parameters["id"]]

                        supplier_added = True
                        break

                    temp_delivery = [i for i in temp_delivery if i["id"] != max_match_supplier_id]

                if not supplier_added:
                    if first_max_id in delivery_more:
                        delivery[first_max_id]["mores"].append(good_parameters["id"])
                    else:
                        delivery_more.append(first_max_id)
                        delivery[first_max_id] = {"mores": [good_parameters["id"]]}

        needable_delivery_ids = delivery.keys()

        needable_delivery = self.get_suppliers(needable_delivery_ids)["suppliers"]

        for supplier in needable_delivery:
            goods_ids = []
            if "ones" in delivery[supplier["id"]].keys():
                goods_ids += delivery[supplier["id"]]["ones"]
            if "mores" in delivery[supplier["id"]].keys():
                goods_ids += delivery[supplier["id"]]["mores"]

            goods_list = self.get_range_of_goods(goods_ids)

            supplier["goods"] = goods_list["goods"]

        return needable_delivery

    def get_goods_parameters(self, settings):
        db_answer = self.services.db_service.exec("select supplier_id, production_id, cost, speed from production "
                                                  "where production_id in ("+", ".join(settings["needable_goods"])+")")

        ratings = self.get_ratings([str(row[0]) for row in db_answer["fetch"]])["ratings"]

        goods_params = []

        for good_id in settings["needable_goods"]:
            good_params = {"id": good_id, "count": 0, "delivery": []}
            for row in db_answer["fetch"]:
                if str(row[1]) == good_id:
                    rating = [rate for rate in ratings if rate["id"] == str(row[0])][0]
                    rating_final = self.services.math_service.calc_rating(rating)
                    cost = self.services.math_service.calc_cost_param(row[2], [new_row[2]
                                                                               for new_row in db_answer["fetch"]])
                    supplier = {
                        "cost": cost,
                        "quality": rating["quality"],
                        "speed": row[3],
                        "rating": rating_final
                    }
                    params_match = self.services.math_service.calc_params_match(settings["sliders"], supplier)

                    good_params["count"] += 1
                    good_params["delivery"].append({
                        "id": str(row[0]),
                        "params_match": params_match
                    })
            goods_params.append(good_params)

        return goods_params

    def get_ratings(self, ids):
        if ids:
            db_answer = self.services.db_service.exec("select supplier_id, quality, completed_orders_count, "
                                                      "all_orders_count, customers_rating from ratings "
                                                      "where supplier_id in ("+", ".join(ids)+")")
        else:
            return {"ratings": []}

        ratings = [{
            "id": str(row[0]),
            "quality": row[1],
            "completed_orders_count": row[2],
            "all_orders_count": row[3],
            "customers_rating": row[4]
        } for row in db_answer["fetch"]]

        return {"ratings": ratings}

    def get_suppliers(self, ids):
        if ids:
            db_answer = self.services.db_service.exec("select id, name, phone, email, address from suppliers "
                                                      "where id in ("+", ".join(ids)+")")
        else:
            return {"suppliers": []}

        suppliers = [{"id": str(row[0]), "name": row[1], "phone": row[2], "email": row[3], "address": row[4]}
                     for row in db_answer["fetch"]]

        return {"suppliers": suppliers}
