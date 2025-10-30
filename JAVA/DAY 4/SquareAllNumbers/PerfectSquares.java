public class PerfectSquares {

	public static int isAllPerfectSquare(int numbers) {
		if (numbers < 0) return 0;
	
		int index = 0;
		while (index * index <= numbers){
			if (index * index == numbers) {

				return 1;
					}
			index ++;
			}
		return 0;
		}





	public static int areAllPerfectSquares(int[] numbers) {

		for (int index = 0; index < numbers.length; index++ ) {

		if (isAllPerfectSquare(numbers[index]) == 0) {

				return 0;

				}

			}
			return 1;
		}




	
}