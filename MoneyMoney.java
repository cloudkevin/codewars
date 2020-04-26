// Your task is to complete the method provided and return the number of years 'Y' as a whole in order for Mr. Scrooge to get the desired sum.
// Assumptions : Assume that Desired Principal 'D' is always greater than the initial principal, however it is best
 // to take into consideration that if the Desired Principal 'D' is equal to Principal 'P' this should return 0 Years.

public class Kata {
	public static int calculateYears(double principal, double interest,  double tax, double desired) {
		double total = principal;
		int years = 0;
		while(total<desired) {
			years +=1;
			total = ((total + (total * interest)*(1.00-tax)));
		}
		return years;		
	}
}