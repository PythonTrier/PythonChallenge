#http://www.pythonchallenge.com/pc/return/good.html
import numpy
from matplotlib import pyplot
first=[
...
]
second=[
...
]
x=numpy.r_[first[0::2]]
y=numpy.r_[first[1::2]]
x2=numpy.r_[second[0::2]]
y2=numpy.r_[second[1::2]]
pyplot.plot(-x,-y)
pyplot.plot(-x2,-y2)
pyplot.show()