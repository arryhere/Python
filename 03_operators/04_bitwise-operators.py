'''
• Bitwise Operators

• it acts on bits and perform the bit-by-bit operations
• these are used to operate on binary numbers

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


print('-----------------------------------------------------------------------------------------------------------------------------------')


'''
• -ver numbers in binary
• -ve numbers are stored as 2's complement
• Here the bits in () represent the MSB, i.e bit that determine the sign
'''

print(bin(45))    # 0b101101
print(bin(~45))   # -0b101101 <-46>
'''
~ (0)101101 = (1)010010                             -> what we expect, but we need to convert it to its 2's complement
1's complement of 010010 = 101101                   -> invert bits of 010010 excluding the MSB (1)
2's complement of 101101 = 101110                   -> add 1 bit to 101101
~ 0b101101 = -0b101101                              -> thus ~45 = -46
'''

print('-----------------------------------------------------------------------------------------------------------------------------------')


print(bin(-13))   # -0b1101
print(bin(~-13))  # 0b1100 <12>
'''
we store -ve numbers after conversion, so to use -ve numbers we must reverse convert them first
-13 = (1)1101                                       -> binary of 13 as stored in python
1's complement of 1101 = 0010                       -> reverse 1's complement, invert the bits of 1101 excluding the MSB (1)
2's complement of 0010 = 0011                       -> everse 2's complement, add 1 bit to 0010

now do NOT operation
~ (1)0011 = (0)1100                                 -> final result of bitwise not
~ -0b1101 = 0b1100                                  -> thus ~-13 = 12
'''


print('-----------------------------------------------------------------------------------------------------------------------------------')
