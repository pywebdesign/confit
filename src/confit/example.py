class MySimpleObject:

    def __init__(self, param_a, param_b, param_c):
        self.param_a = param_a
        self.param_b = param_b
        self.param_c = param_c

class IMarket:
    pass

class IQuoter:
    pass

class Market(IMarket):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Quoter(IQuoter):

    def __init__(self, q1, q2):
        self.q1 = q1
        self.q2 = q2


class Trader:

    def __init__(self, market: Market, quoter: Quoter):
        self.market = market
        self.quoter = quoter


class TraderWithInterface:

    def __init__(self, market: IMarket, quoter: IQuoter):
        self.market = market
        self.quoter = quoter