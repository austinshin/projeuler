/*
@author: Austin Shin
projecteuler problem 4

A palindromic number reads the same both ways. The largest palindrome 
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

public class prob4 {
/*
notes:
999 is the largest 3 digit number.
The largest number is 999 * 999 = 998001
The smallest 3 digit number is 100 * 100 = 10000
The palindrome number we are looking for is between 10000 < x < 998001

We must do two checks because it ranges from a five digit number to a six digit number.
_ _ _ _ _ five-digit
a b c b a 



_ _ _ _ _ _ six-digit
a b c c b a 

One thing we could do is create a list where we only add stuff to hte list if it is
a palindrome and we would
work backwards starting from 999 then multiply each.

*/


	public static void main(String[] args) {

	}
}