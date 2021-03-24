from pprint import pprint
import sys

class Order:
    def __init__(self, price, qty, side, clientId, orderId, next=None, previous=None):
        self.price = price
        self.side = side
        self.qty = qty
        self.clientId = clientId
        self.orderId = orderId
        self.next = next
        self.previous = previous


class OrderBook(object):
    def __init__(self, initOrderId=0, maxPrice=100000):
        self.orderId = initOrderId
        self.head = None
        self.tail = None
        self.bestBuy = None
        self.bestSell = None

    def newOrder(self, price, qty, side, clientId):
        """
        price = price in pence
        qty = do I need explain this one...
        side =  buy / sell
        clientId = unique client id per customer
        """
        self.orderId += 1
        
        wOrder = self.head

        



        # Deal with the order if there are no orders on the book

        if self.head == None:
            newOrder = Order(price, qty, side, clientId, self.orderId)
            print("foo1")
            self.head = newOrder

            if side == "buy":
                self.bestBuy = price
            elif side == "sell":
                self.bestSell = price
            return(self.orderId)
        else:
            if side == "buy":
                while(wOrder):
                    if wOrder.side == "buy":
                        break
                    else:
                        print("foo")
                    wOrder = wOrder.next

        # At this point we assume that there are orders on the book
        # We need to figure out where to slot this order in

        # At this point there is remaining qty on the order, so we need to add it to the book
        newOrder = Order(price, qty, side, clientId, self.orderId)

        # Loop through the orders in the book
        mOrder = self.head
        while(mOrder):

            if mOrder.next == None:
                mOrder.next = newOrder
                newOrder.previous = mOrder
                self.tail = newOrder
                return(self.orderId)
            
            if newOrder.price < mOrder.price:
                newOrder.next = mOrder
                mOrder.previous = newOrder

                #This is the first order in the book
                if self.head == mOrder:
                    self.head = newOrder

                return(self.orderId)
            
            if newOrder.price == mOrder.price:
                if mOrder.next.price != mOrder.price:
                    mOrder.next.previous = newOrder
                    newOrder.next = mOrder.next
                    mOrder.next = newOrder
                    newOrder.previous = mOrder
                    return(self.orderId)


            
            #This order is the end in the chain
            #This means that our order must be a new highest price
            #We will put our order here

            mOrder = mOrder.next

    def printOrderBook(self):
        currentOrder = self.head
        while currentOrder:
            print("OrderId:", currentOrder.orderId, "Price:", currentOrder.price, "Qty:", currentOrder.qty, "Side:", currentOrder.side)
            currentOrder = currentOrder.next


            



ob = OrderBook()


# ob.newOrder(price, qty, side, clientId)
ob.newOrder(900, 100, "buy", 101)
ob.newOrder(1000, 100, "buy", 101)
ob.newOrder(2000, 100, "sell", 101)
ob.newOrder(2100, 100, "sell", 101)

#ob.newOrder(2000, 100, "buy", 101)

#ob.newOrder(
#    price = 3000,
#    qty = 100,
#    side = "sell", 
#    clientId = 101
#)

ob.printOrderBook()


