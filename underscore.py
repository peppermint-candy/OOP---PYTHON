class Underscore(object):
    def map(self, itrerable, fnc):
        output = []
        for i in itrerable:
            output.append(fnc(i))
        return output
        # your code here
    def reduce(self , iterable , fnc ,*memo):
        if memo:
            memo = memo[0]
            for i in iterable:
                memo = fnc(memo,i)
            return memo
            
            memo = iterable[0]
            for i in range(1,len(iterable)):
                memo = fnc (memo,iterable[i])
            return memo


        # your code here
    def find(self, iterable, fnc):
        for i in iterable:
            if fnc(i):
                return i

        # your code here
    def filter(self, itrerable, fnc):
        output = []
        for i in itrerable:
            if fnc(i):
                output.append(i)
        return output
        # your code 
    def reject(self, itrerable, fnc):
        output = []
        for i in itrerable:
            if fnc(i):
                pass
            else:
                output.append(i)
        return output
# you just created a library with 5 methods!
# # let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print evens
## should return [2, 4, 6] after you finish implementing the code above

finds = _.find([1,2,3,4,5,6] , lambda x: x % 2 == 0 )
print finds


num_map = _.map([1,2,3,4,5], lambda i: i**i)
print num_map

rejects = _.reject([1,2,3,4,5] , lambda x: x %2 == 0)
print rejects

reduces = _.reduce([1,2,3,4,5], lambda x,y: x+y)
print reduces