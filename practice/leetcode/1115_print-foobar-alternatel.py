from threading import Event

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_dones = [
            Event() for _ in range(n)
        ]
        self.bar_dones = [
            Event() for _ in range(n)
        ]


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            if i > 0:
                self.bar_dones[i - 1].wait()
            printFoo()
            self.foo_dones[i].set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_dones[i].wait()
            printBar()
            self.bar_dones[i].set()
