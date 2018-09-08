import math
import scipy
from scipy.optimize import linprog


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
        return (rating_params["completed_orders_count"] / rating_params["all_orders_count"] + \
               rating_params["customers_rating"] / 5) / 2


class SecondHand:

    def __init__(self, a):
        self.a = a
        self.n = len(a[0])

        self.mincol = []
        self.maxrow = []

        self.vx = []
        self.vy = []

        self.xy = []
        self.yx = []

        self.ans = None

    def dotry(self, i: int) -> bool:
        if self.vx[i]:
            return False
        self.vx[i] = True

        for j in range(self.n):
            if self.a[i][j] - self.maxrow[i] - self.mincol[j] == 0:
                self.vy[j] = True

        for j in range(self.n):
            if self.a[i][j] - self.maxrow[i] - self.mincol[j] == 0 and self.yx[j] == -1:
                self.xy[i] = j
                self.yx[j] = i

                return True

        for j in range(self.n):
            if self.a[i][j] - self.maxrow[i] - self.mincol[j] == 0 and self.dotry(self.yx[j]):
                self.xy[i] = j
                self.yx[j] = i

                return True

        return False

    def calc(self):
        self.mincol = [0] * self.n
        self.maxrow = [0] * self.n

        for i in range(self.n):
            for j in range(self.n):
                self.maxrow[i] = max(self.maxrow[i], self.a[i][j])

        self.xy = [-1] * self.n
        self.yx = [-1] * self.n

        c = 0
        while c < self.n:
            self.vx = [0] * self.n
            self.vy = [0] * self.n

            k = 0

            for i in range(self.n):
                if self.xy[i] == -1 and self.dotry(i):
                    k += 1

            c += k

            if k == 0:
                z = math.inf

                for i in range(self.n):
                    if self.vx[i]:
                        for j in range(self.n):
                            if not self.vy[j]:
                                z = min(z, self.maxrow[i]+self.mincol[j]-self.a[i][j])

                for i in range(self.n):
                    if self.vx[i]:
                        self.maxrow[i] -= z

                    if self.vy[i]:
                        self.mincol[i] += z

        self.ans = 0
        for i in range(self.n):
            self.ans += self.a[i][self.xy[i]]

        return {"ans": self.ans, "jobs": self.xy}


if __name__ == "__main__":
    name = input(">>> ")

    if name == "nazn":
        n = int(input(">>> "))
        a = []

        for _ in range(n):
            row = input(">>> ")
            a.append([int(elem) for elem in row.split(" ")])

        res = SecondHand(a)
        answer = res.calc()

        print("ans: ", answer["ans"])
        for job in answer["jobs"]:
            print(job+1, end=" ")
        print()

    elif name == "opti":
        n = int(input(">>> "))
        m = int(input(">>> "))

        a = []
        for _ in range(m):
            row = input(">>> ")
            a.append([int(elem) for elem in row.split(" ")])

        inp = input(">>> ")
        c = [-int(elem) for elem in inp.split(" ")]

        inp = input(">>> ")
        b = [int(elem) for elem in inp.split(" ")]

        d = linprog(c, a, b)

        for key, val in d.items():
            print(key, val)  # вывод решения
            if key == 'x':
                q = [sum(i) for i in a * val]  # использованные ресурсы
                print('A_ub*x', q)
                q1 = scipy.array(b) - scipy.array(q)  # остатки ресурсов
                print('b_ub-A_ub*x', q1)
