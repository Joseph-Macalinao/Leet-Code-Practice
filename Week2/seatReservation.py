class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        seats = {}
        for i in range(1, n + 1):
            seats[i] = ""
        self.seats = seats
        

    def reserve(self):
        """
        :rtype: int
        """
        lowest = self.n + 1
        for i in self.seats:
            if self.seats[i] == "":
                self.seats[i] = "reserved"
                return i
        

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        self.seats[seatNumber] = ""



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# solution works, just not for 100,000 people

