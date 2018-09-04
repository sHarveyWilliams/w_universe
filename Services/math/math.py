class MathService:

    def __init__(self, services):
        self.services = services

    @staticmethod
    def calc_params_match(sliders, supplier):
        params_match = 0
        params_count = 0
        for param_name, param_value in supplier.items():
            param_weight = sliders[param_name]
            params_match += param_weight * param_value
            params_count += 1

        return params_match / params_count

    @staticmethod
    def calc_cost_param(cost, all_costs):
        return 1 - (cost - min(all_costs)) / (max(all_costs) - min(all_costs))

    @staticmethod
    def calc_rating(rating_params):
        return rating_params["completed_orders_count"] / rating_params["all_orders_count"] * \
               rating_params["customers_rating"] / 5
