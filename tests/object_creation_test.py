import unittest

import confit.store

class TestObjectCreation(unittest.TestCase):
    def test_simple_object(self):
        confit_config = {"my_simple_object": {
            "type": "confit.example.MySimpleObject",
            "param_a": 12,
            "param_b": 45,
            "param_c": "random"
        }}

        store = store = confit.store.build_store(confit_config)
        store.get("my_simple_object")

    def test_deep_object(self):
        confit_config = {"trader": {
                "type": "confit.example.Trader",
                "market": {
                    "type": "confit.example.Market",
                    "p1": 23,
                    "p2": 5
                },
                "quoter": {
                    "type": "confit.example.Quoter",
                    "q1": "jj",
                    "q2": "klf"
                }
            }}
        
        store = confit.store.build_store(confit_config)
        a = store.get("trader")
        b = store.get("trader.quoter")
        c = store.get("trader.market")
        self.assertEqual(a.market.p1, 23)
        self.assertEqual(a.market.p2, 5)
        self.assertEqual(a.quoter.q1, "jj")
        self.assertEqual(a.quoter.q2, "klf")
        self.assertEqual(id(a.quoter), id(b))
        self.assertEqual(id(a.market), id(c))

    def test_deep_with_interface(self):
        confit_config = {"trader": {
                "type": "confit.example.TraderWithInterface",
                "market": {
                    "type": "confit.example.Market",
                    "p1": 23,
                    "p2": 5
                },
                "quoter": {
                    "type": "confit.example.Quoter",
                    "q1": "jj",
                    "q2": "klf"
                }
            }}

        store = confit.store.build_store(confit_config)
        a = store.get("trader")
        b = store.get("trader.quoter")
        c = store.get("trader.market")
        self.assertEqual(a.market.p1, 23)
        self.assertEqual(a.market.p2, 5)
        self.assertEqual(a.quoter.q1, "jj")
        self.assertEqual(a.quoter.q2, "klf")
        self.assertEqual(id(a.quoter), id(b))
        self.assertEqual(id(a.market), id(c))


    def test_deep_with_interface(self):
        confit_config = {"trader": {
                "type": "confit.example.TraderWithInterface",
                "market": {
                    "type": "confit.example.Market",
                    "p1": 23,
                    "p2": 5
                },
                "quoter": {
                    "type": "confit.example.Quoter",
                    "q1": "jj",
                    "q2": "klf"
                }
            }}

        store = confit.store.build_store(confit_config)
        a = store.get("trader")
        b = store.get("trader.quoter")
        c = store.get("trader.market")
        self.assertEqual(a.market.p1, 23)
        self.assertEqual(a.market.p2, 5)
        self.assertEqual(a.quoter.q1, "jj")
        self.assertEqual(a.quoter.q2, "klf")
        self.assertEqual(id(a.quoter), id(b))
        self.assertEqual(id(a.market), id(c))


    def test_with_resuing_deep_object(self):
        confit_config = {
                "trader1": {
                    "type": "confit.example.Trader",
                    "market": {
                        "type": "confit.example.Market",
                        "p1": 11,
                        "p2": 22
                    },
                    "quoter": {
                        "type": "confit.example.Quoter",
                        "q1": "jj",
                        "q2": "klf"
                    }
                },
                "trader2": {
                    "type": "confit.example.Trader",
                    "market": {
                        "_id": "trader1.market"
                    },
                    "quoter": {
                        "type": "confit.example.Quoter",
                        "q1": "uu",
                        "q2": "ii"
                    }
                }
            }
        
        store = confit.store.build_store(confit_config)
        a = store.get("trader1")
        b = store.get("trader2")
        self.assertEqual(a.market.p1, 11)
        self.assertEqual(id(a.market), id(b.market))


    def test_with_resuing_deep_object_flatten_structure(self):
        confit_config = {
                
                "trader1": {
                    "type": "confit.example.Trader",
                    "market": {
                        "_id": "market1"
                    },
                    "quoter": {
                        "type": "confit.example.Quoter",
                        "q1": "jj",
                        "q2": "klf"
                    }
                },
                "trader2": {
                    "type": "confit.example.Trader",
                    "market": {
                        "_id": "market1"
                    },
                    "quoter": {
                        "type": "confit.example.Quoter",
                        "q1": "uu",
                        "q2": "ii"
                    }
                },
                "market1": {
                        "type": "confit.example.Market",
                        "p1": 11,
                        "p2": 22
                    }
            }
    

        store = confit.store.build_store(confit_config)
        a = store.get("trader1")
        b = store.get("trader2")
        self.assertEqual(a.market.p1, 11)
        self.assertEqual(id(a.market), id(b.market))



if __name__ == '__main__':
    unittest.main()