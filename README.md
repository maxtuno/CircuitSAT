# Circuit SAT Language 
A high-level (and low-level) language that emit CNF code.

## Installation

    pip install circuitsat
  
## Usage  
    
    csat file.csat

# low-level language

    /*
        > csat full_adder.csat
        > python3 test_tool.py 0 5 (only show the first 5 variables)
    */

    asm
        new A
        new B
        new Cin
        new Sum
        new Cout
    end

    def half_adder(i)
        asm
        xor A[i], B[i], S[i]
        and A[i], B[i], C[i]
        end
    end

    n = 2;
    for i=0 to n do
        asm
            new A[i]
            new B[i]
            new C[i]
            new S[i]
        end
        half_adder(i);
    end
    asm
        copy S[0], A[1]
        copy A[0], A
        copy B[0], B
        copy B[1], Cin
        copy S[1], Sum
        or   C[0], C[1], Cout
    end


## high-level language

    /*
        A script for testing CircuitSAT high-level language syntax.
    */
    
    // boolean expressions
    assert(true || false);
    assert(!false);
    assert(true && true);
    assert(!true || !false);
    assert(true && (true || false));
    
    // relational expressions
    assert(1 < 2);
    assert(666 >= 666);
    assert(-5 > -6);
    assert(0 >= -1);
    assert('a' < 's');
    assert('sw' <= 'sw');
    
    // add
    assert(1 + 999 == 1000);
    assert([1] + 1 == [1,1]);
    assert(2 - -2 == 4);
    assert(-1 + 1 == 0);
    assert(1 - 50 == -49);
    assert([1,2,3,4,5] - 4 == [1,2,3,5]);
    
    // multiply
    assert(3 * 50 == 150);
    assert(4 / 2 == 2);
    assert(1 / 4 == 0.25);
    assert(999999 % 3 == 0);
    assert(-5 * -5 == 25);
    assert([1,2,3] * 2 == [1,2,3,1,2,3]);
    assert("ab"*3 == "ababab");
    
    assert(2^10 == 1024);
    assert(3^3 == 27);
    assert(4^3^2 == 262144); // power is right associative
    assert((4^3)^2 == 4096);
    
    // for- and while statements
    a = 0;
    for i=0 to 10 do
      a = a + i;
    end
    assert(a == (1+2+3+4+5+6+7+8+9));

    b = -10;
    c = 0;
    while b < 0 do
      c = c + b;
      b = b + 1;
    end
    assert(c == -(1+2+3+4+5+6+7+8+9+10));
    
    // if
    a = 123;
    if a > 200 do
      assert(false);
    end
    
    if a < 100 do
      assert(false);
    else if a > 124 do
      assert(false);
    else if a < 124 do
      assert(true);
    else do
      assert(false);
    end
    
    if false do
      assert(false);
    else do
      assert(true);
    end
    
    // functions
    def twice(n)
      temp = n + n;
      return temp;
    end
    
    def squared(n)
      return n*n;
    end
    
    def squaredAndTwice(n)
      return twice(squared(n));
    end
    
    def list()
      return [7,8,9];
    end
    
    assert(squared(666) == 666^2);
    assert(twice(squared(5)) == 50);
    assert(squaredAndTwice(10) == 200);
    assert(squared(squared(squared(2))) == ((2^2)^2)^2);
    assert(list() == [7,8,9]);
    assert(size(list()) == 3);
    assert(list()[1] == 8);
    
    // naive bubble sort
    def sort(list)
      while !sorted(list) do
      end
    end
    def sorted(list)
      n = size(list);
      for i=0 to n-1 do
        for j=i + 1 to n do
            if list[i] > list[j] do
              temp = list[i];
              list[i] = list[j];
              list[j] = temp;
            end
          end
      end
      return true;
    end
    numbers = [3,5,1,4,2];
    sort(numbers);
    assert(numbers == [1,2,3,4,5]);
    
    // recursive calls
    def fun(n)
        if n <= 0 do
            return 0;
        else do
            return fun(n - 1);
        end
        return n;
    end
    
    assert(fun(10) == 0);
    
    // recursive calls
    def fib(n)
        if n < 2 do
            return n;
        end
        return fib(n - 1) + fib(n - 2);
    end
    
    assert(fib(4) == 3);
    sequence = [];
    for i = 0 to 10 do
      sequence = sequence + fib(i);
    end
    
    assert(sequence == [0,1,1,2,3,5,8,13,21,34]);
    
    def fib2(n)
      if n < 2 do
        return n;
      else do
        a = fib2(n-1);
        c = fib2(n-2);
        return a + c;
      end
    end
    assert(fib2(4) == 3);
    
    // lists and lookups, `in` operator
    n = [[1,0,0],[0,1,0],[0,0,1]];
    p = [-1, 'abc', true];
    
    assert('abc' in p);
    assert([0,1,0] in n);
    assert(n[0][2] == 0);
    assert(n[1][1] == n[2][2]);
    assert(p[2]);
    assert(p[1][2] == 'c');
    
    print('all high-level language test ok.');

## Note
Work in progress!

    > csat file.csat
    > python3 test_tool.py file.cnf from_var to_var
    
