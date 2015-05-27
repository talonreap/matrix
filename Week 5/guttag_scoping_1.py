def f(x):
    
    def g():
        x='abc'
        print 'in g, x=',x

    def h():
        z=x
        print 'in h, z=',z
##        x=x+2
##        print 'in h, x=',x

    x=x+1
    print 'first time in f, x=',x
    
    h()
    g()

    print 'second time in f, x=',x
    return g

x=3
z=f(x)
print 'outside, x=', x
print 'outside, z=', z

z()
    
