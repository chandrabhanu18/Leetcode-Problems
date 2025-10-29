import math
import time

class Solution(object):
    def smallestNumber(self, n):
        """
        Finds the smallest integer X >= n whose binary representation is all ones (2^k - 1).

        :type n: int
        :rtype: int
        """
        if n <= 0:
            # The smallest all-ones number is 1 ('1').
            return 1 

        # 1. Get the minimum number of bits required to represent 'n'.
        # For an integer 'n', n.bit_length() returns the number of bits required 
        # to represent it in binary, excluding the '0b' prefix.
        num_bits = n.bit_length()
        
        # 2. Construct the all-ones number with 'num_bits': (2^num_bits) - 1.
        # This is the smallest all-ones number that is guaranteed to have enough bits.
        # (1 << num_bits) is a fast way to calculate 2^num_bits.
        all_ones_candidate = (1 << num_bits) - 1
        
        # 3. Check if this candidate is the answer.
        if all_ones_candidate >= n:
            # If the all-ones number of that bit length is >= n, it is the answer.
            return all_ones_candidate
        else:
            # If it's < n (e.g., n=16, all_ones_candidate=15), 
            # we need the next largest all-ones number, which has one more bit.
            return (1 << (num_bits + 1)) - 1

# --- Example Execution (Main Function) ---

if __name__ == "__main__":
    # Instantiate the Solution class
    solver = Solution()

    # Test Cases
    test_cases = [
        (1, "1 in binary is '1'"),
        (2, "2 in binary is '10', next all-ones is 3 ('11')"),
        (7, "7 in binary is '111'"),
        (8, "8 in binary is '1000', next all-ones is 15 ('1111')"),
        (15, "15 in binary is '1111'"),
        (16, "16 in binary is '10000', next all-ones is 31 ('11111')"),
        (0, "Edge case for zero"),
    ]

    print("--- Smallest All-Ones Number Finder ---")

    for n, description in test_cases:
        result = solver.smallestNumber(n)
        
        # Optional: Check the binary representation of the result for confirmation
        binary_check = bin(result)[2:]
        
        print(f"\nInput n: {n}")
        print(f"Goal: {description}")
        print(f"Result: {result}")
        print(f"Binary Check: '0b{binary_check}'")
        
        # Simple verification of the result
        if '0' not in binary_check:
            print("Status: ✅ Correct (Result is all ones)")
        else:
            print("Status: ❌ Error (Result is NOT all ones)")