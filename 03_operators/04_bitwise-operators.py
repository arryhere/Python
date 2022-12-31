'''
• Bitwise Operators
• Bitwise operators act on bits and perform the bit-by-bit operations
• These are used to operate on binary numbers

  Operator	 Description	    Syntax
  &	         Bitwise AND	    x & y
  |	         Bitwise OR	      x | y
  ~	         Bitwise NOT	    ~x
  ^	         Bitwise XOR	    x ^ y
  >>         Bitwise right    shift	x>>
  <<         Bitwise left     shift	x<<
'''

x = 15
y = 20
z = 45
print(bin(x))   # 01111
print(bin(y))   # 10100
print(bin(z))   # 101101

bitwiseAND = x & y
bitwiseOR = x | y
bitwiseNOT = ~z
bitwiseXOR = x ^ y
bitwiseRightShift = z >> 2
bitwiseLefttShift = z << 2


print(bin(bitwiseAND), bitwiseAND)                  # 0b100 4
print(bin(bitwiseOR), bitwiseOR)                    # 0b11111 31
print(bin(bitwiseNOT), bitwiseNOT)                  # -0b101110 -46
print(bin(bitwiseXOR), bitwiseXOR)                  # 0b11011 27
print(bin(bitwiseRightShift), bitwiseRightShift)    # 0b1011 11
print(bin(bitwiseLefttShift), bitwiseLefttShift)    # 0b10110100 180


print('-------------------------------------------------------------------------------------------------------------------------')


'''
• -ver numbers in binary
• -ve numbers are stored as 2's complement
• Here the bits in () represent the MSB, i.e bit that determine the sign
'''

print(bin(45))    # 0b101101
print(bin(~45))   # -0b101101 <-46>
'''
NOT of (0)101101 <~45> = (1)010010
1's complement of 010010 = NOT OF 010010 = 101101
2's complement of 101101 = 101101 + 1 = 101110
NOT of 0b101101 <~45> = -0b101101 <-46>
'''

print(bin(-13))   # -0b1101
print(bin(~-13))  # 0b1100 <12>
'''
we store -ve numbers after conversion, so to use -ve numbers we must reverse convert them first
<-13> = (1)1101
reverse 2's complement
NOT of 1101 = 0010
0010 + 1 = 0011

now do NOT operation
~(1)0011 = (0)1100
NOT of -0b1101 <~13> = 0b1100 <12>
'''


print('-------------------------------------------------------------------------------------------------------------------------')
