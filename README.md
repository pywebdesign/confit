# Confit

Confit is a tool to bring better readability into complex object building scheme.

As a project become a bit more that an simple few script together, it generally grow in scope, adding optional feature, execution flags, conditional procedure and multiple sources of data. The code generally has a Object Oriented approach that allow multiple different implementation to be swapped depending on the configs and params used to run the software. On case would be to use local data file and be able to switch to a cloud storage source in production with a single config.

More complex system will map the complex world. For example in trading you would need interface for the protocol for communicating with markets, then you would have specific market rules, flags to add to order, differnet regulations for different country, even more complex rules for different product and so on. Those end up exploding in complexity. What you end up with is a very large proportion of code that mix object creation patterns to suits the flexibilité needed and generate all the connected peice into a working strategy or system. This is a lot of no so interesting code that, when read, do not really deal with trading per se, but just preparing and applying choice in a very large combinatory space.

Confit is a pragmatic, config approach to auto create all the resources needed. It takes idea form dependency injection and lean on the fact that, in all intended purpose, all software configs are exposed in a way or another, at worst as a hard coded string deep in a project code, and best in a very easy accessible config to enable building and creating the object and the structure.


# Getting started

# Simple Object creation and retreival

In the config file

my_simple_object:
    type: MySimpleObject:
    param_a: 12
    param_b: 45
    param_c: "random"

In code

class MySimpleObject:

    def __init__(self, param_a, param_b, param_c):
        self.param_a = param_a
        self.param_b = param_b
        self.param_c = param_c


Then you object will be available in the object store

import confit

confit.store.init()
config.store.get("my_simple_object")


this is somewhat useful, but really that's not much. Arguably there is still a bunch of stuff that was not coded that are not related to the business logic.
    
    - reading config files, maybe with reader classes
    - some refletion way to get the object from the string in the type field of the config, some emum or some if else cascade
    - actually creating the object and setting it into a variable, a context to create, maybe a builder class
    - probably some class to hold everything together or the main scrict would already be quite long
  

Let's see how we can go further with related object creation


# Related Object Creation

Up until now we create a self contained unrelated object floating in nothingness which is quite nice but not that intenrestion. Let's see how we can define an object that has other object in them as we still want to use interface and composition for our software.


class Market:

    def __init__(self, p1, p2)
        self.p1 = p1
        self.p2 = p2

class Quoter:

    def __init__(self, q1, q2)
        self.q1 = q1
        self.q2 = q2


class Trader:

    def __init__(self, market: Market, quoter: Quoter):
        self.market = market
        self.quoter = quoter



And the config is simply:

    trader:
        type: Trader
        market: 
            type: Market
            p1 = 23
            p2 = 5
        quoter:
            type: Quoter
            q1 = "jj"
            q2 = "klf"

Accessing the object is the same

confit.store.init()
config.store.get("trader")

And you can access deep object with

config.store.get("trader.quoter")

This is nice but it still do not cover composability and interface.

# Using interface

Let's assume IMarket and IQuoter are interface and MarkerA and MarketB, QuoterA, QuoterB are implementation

here's the new Trader class

class Trader:

    def __init__(self, market: IMarket, quoter: IQuoter):
        ...

And the same config would still work:

    trader:
        type: Trader
        market: 
            type: Market
            p1 = 23
            p2 = 5
        quoter:
            type: Quoter
            q1 = "jj"
            q2 = "klf"


Again pretty great and simple.


# Reusing the same object multiple times

There is a case for sharing resources in between multiple object, be it a resource with a lock or just for simplicity

You can simply add an _id field to the resource in the yaml and reusing this resource allow you to share

here's how it look


    trader1:
        type: Trader
        market: 
            type: Market
            _id: 1
            p1 = 11
            p2 = 22
        quoter:
            type: Quoter
            q1 = "jj"
            q2 = "klf"
    
    trader2:
        type: Trader
        market: 
            _id: 1


You can even flatten the structure at this point

    market1: 
        type: Market
        _it: 1
        p1 = 11
        p2 = 22


    trader1:
        type: Trader
        market: 
            _id: 1
        quoter:
            type: Quoter
            q1 = "jj"
            q2 = "klf"
    
    trader2:
        type: Trader
        market: 
            _id: 1
        quoter:
            type: Quoter
            q1 = "ee"
            q2 = "44"