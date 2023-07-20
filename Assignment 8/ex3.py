class Aggregator:
    def __init__(self, agg_type: type, ignore_errors: bool = True):
        self.agg_type = agg_type
        self.ignore_errors = ignore_errors
        self.sum = None

    def __call__(self, *args):
        if not args:
            return self.sum
            pass
        for comp in args:
            if isinstance(comp, self.agg_type) is True:
                if self.sum is None:
                    self.sum = comp
                else:
                    self.sum += comp
            if isinstance(comp, self.agg_type) is False:
                if self.ignore_errors is True:
                    continue
                else:
                    raise TypeError(f"aggregation only works on type '{self.agg_type.__name__}', not '{type(comp).__name__}'")
        return self.sum


# int_agg = Aggregator(agg_type=int)
# int_agg(1, 2, 3)
# int_agg(4, "hi", 5.1)
# print(int_agg())
# str_agg = Aggregator(agg_type=str, ignore_errors=False)
# print(str_agg("this", " ", "is a test"))
# try:
#     str_agg(1)
# except TypeError as e:
#     print(f"{type(e).__name__}: {e}")