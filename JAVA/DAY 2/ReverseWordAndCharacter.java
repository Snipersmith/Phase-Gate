public class ReverseWordsAndCharacter {

  public static void main (String[] args){

	String words = "abcd";
        String words2 = "efd";

        String result = addSecondWord(words, words2);
        System.out.println(result); 
        }

  public static String reverseWord(String word) {
	String  reversed = "";
	for (int index = 0; index < word.lenght(); index++) {

		reversed = word.charAt(letters) + reversed;
	}
	return reversed;
    }
	public static String addSecondWord(String first, String second) {

	return reverseWord(first) + second;		
	}

}









