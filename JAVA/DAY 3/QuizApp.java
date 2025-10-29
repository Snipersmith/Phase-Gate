import java.util.Scanner;

public class QuizApp {
  public static void main (String [] args) {

	Scanner input = new Scanner(System.in);

	String intro = "Welcome to the Quiz Game";

	int score = 0;	


	String [] questions = {

		"What is the capital of England?"
		"Where can i get food in Semicolon?"
		"Who is the president of Nigeria?"

				};

	String [][] options = {
 
		{"1-> London", "2 -> "Paris "3 -> Berlin" "4 -> Rome"},
		{"1-> Ask nelson, "2 -> Glass house, "3 -> Toilet", "4 ->Floor"},
		{"1-> Tinubu," "2 -> Buhari", "3 -> Obi," "4 -> Jonathan"}

	};

	int [] correctAnswers = {1,1,1};



	System.out.println(intro);
	
	for (int index =0; < questions.length; index++) {

	System.out.println("Question " + (index+1) + ":" + questions[index]);

	}

	for (String option : options[index]){
		System.out.println(options);
	}

	System.out.print("Enter yur answer (1-4):");
	int userAnswer = input.nextInt();


	if(userAnswer == correctAnswers[index]) {
	
		System.out.println("Correct!");
		score++;

	} else {
		System.out.println("Wrong!");
	}

	





}

	
}








/*
PSUEDO

- Create questions for the user 
- Create Options for the user
- Create answers for the user
- Show message if the question is right or wrong
- Keep track of how many questions they got right 
- Show final score at the end 

*/