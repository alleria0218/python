#!/usr/bin/env python2

def convert(func,seq):
    'convert sequence of numbers to same type'
    return [func(eachNum) for eachNum in seq]

myseq = (123,45.67,-6.2e9, 99999999L)
print convert(int,myseq)
print convert(long,myseq)
print convert(float,myseq)

