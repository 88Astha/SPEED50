
CLS

# Speed50: The Typing Speed Calculator(in words per minute / wpm)

# Introducing the Speed50 typing speed calculator

Speed50 is a command-line typing speed calculator built with Python and various python libraries such as time, curses, requests. 
This project was developed as the final submission for Harvard University's CS50 course. 
Speed50 utilizes the Ninja Quotes API to provide users with a typing challenge, calculating their words-per-minute (wpm) score upon completion.
It allows the user to play unlimited number of times, where each time there is a new quote to type!

#VIDEO DEMO : Below is the youtube link to find out the working of my project-

https://youtu.be/EHxcn-agMsM?feature=shared

# Features of SPEED50

- Typing Challenge: Speed50 fetches a random quote from the Ninja Quotes API and presents it to the user as a typing challenge.
(with the help of requests library in python)
- Real-time Feedback: As the user types, Speed50 provides real-time feedback on accuracy, highlighting correct and incorrect keystrokes with the help of colored characters.
(You can see if you have typed the right or wrong character with the help of colored character feature provided)
(Also enables the user to backspace whenever a mistake is detected!)
- WPM Calculation: Upon completing the typing challenge, Speed50 calculates the user's words-per-minute (wpm) score.
( with the help of the time library, providing an accurate measure of their typing speed.)
- Error Detection: Speed50 detects errors in the user's input, including typos and missed words, ensuring an accurate WPM calculation.


# Usage

1. Clone the Speed50 repository to your local machine using `git clone https://github.com/me50/Astha-88.git.
2. Navigate to the project directory using cd Speed50.
3. Install the required dependencies using pip install -r requirements.txt.
4. Run the application using python (https://www.python.org/).
5. Follow the on-screen instructions to complete the typing challenge.


# Functions in SPEED50

THE UNCUT DESCRIPTION OF MY FINAL CS50 PROJECT - SPEED50:

SPEED50 pretty much sums up the working itself but in order to summarize it furthermore:
SPEED50 is my CS50 final project that helps measure the typing speed of an individual
in words per minute.
I have implemented the "SPEED50" with the help of three main functions:

#The Welcome Screen function for the welcome page!

The Welcome Screen initiates user engagement by displaying the welcome message
It also enables user to continue by pressing any key to begin the typing test..

# The Display50 function for checking in with your progress

The display50():
    print("Helps you see what you've typed so far!! with the colors - green & red )
    Display50 helps you to acutally be able to see what you are typing!
    If the text is green: it means you are doing great!
    but if you encounter red text!!, it means you have simply pressed the wrong key!! 
    You can always backspace to address this issue!

# The Speed50 function -  The absolute core of the project!

Next is the speed50 which helps you know your score in WPM(words per minute)!!
I have also integrated quote api in order to generate random quotes. 

# API USED : https://api-ninjas.com/api/quotes

Ninja quote api helps my project be more versatile ..by getting new quotes every single time!!

#__main__

Then We have our __main__ !! because every story has its own origin!!
....and the END!
main function is used in order to call our various other functions as well as to display the ending texts!!






# Technical Details

- Programming Language: Speed50 is built using Python 3.10.
- API Integration: The application utilizes the Ninja Quotes API to fetch random quotes for the typing challenge.( https://api-ninjas.com/api/quotes)
- Error Handling: Speed50 employs robust error handling mechanisms to ensure accurate WPM calculations and provide real-time feedback to the user.

# Future Development

- Multi-Quote Challenges: Implement a feature to allow users to complete multiple typing challenges in a row, with the option to track progress and calculate average WPM scores.
- Customizable Difficulty: Introduce a feature to enable users to adjust the difficulty level of the typing challenge, such as by increasing or decreasing the quote length or complexity.
- Graphical User Interface: Develop a graphical user interface (GUI) for Speed50, providing users with a more interactive and engaging experience.
- Challenge: Allowing users to challenge one another & challenge others to a duel.
- Friends: Allowing users to Add friends and talk to them at a chill local environment.

# Acknowledgments

- CS50: This project was developed as part of Harvard University's CS50 course, which provided invaluable guidance and resources and shaped me such that I am able to complete this project on my own!.
- Ninja Quotes API: The Ninja Quotes API was used to fetch random quotes for the typing challenge, adding an exciting element to the application as well as allowing me to enter another domain of learning and broadening  my knowledge on API.
- StackOverFlow: Whenever in doubt, it's always a good idea to look in there...thousands of people with the same problem as you!
- Google: Same as StackOverFlow but yes! no project is ever complete without the help from google here and there and it also helps increase my productivity by learning new stuff!

# License

Speed50 is licensed under the MIT License.

# Contact

For questions, feedback, or suggestions, please don't hesitate to reach out:

Astha Bisht

Asthabst88@gmail.com

Astha-88

Thankyou again CS50 for providing such high quality education all over the world.

END