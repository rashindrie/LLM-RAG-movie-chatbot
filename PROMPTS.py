# Read/adapt the prompts below at will
DOCUMENT_PROMPT = """{page_content}
IMDB link: {source}
========="""

QUESTION_PROMPT = """Given the following extracted parts of a movie database and a question, create a final answer with the IMDB link as source ("SOURCE").
If you don't know the answer, just say that you don't know. Don't try to make up an answer.
ALWAYS return a "SOURCE" part in your answer.

QUESTION: What's a good movie about a robot to watch with my kid?
=========
Title: A.I. Artificial Intelligence
Genre: Drama,Sci-Fi
Description: A robotic boy, the first programmed to love, David (Haley Joel Osment) is adopted as a test case by a Cybertronics employee (Sam Robards) and his wife (Frances O'Connor). Though he gradually becomes their child, a series of unexpected circumstances make this life impossible for David. Without final acceptance by humans or machines, David embarks on a journey to discover where he truly belongs, uncovering a world in which the line between robot and machine is both vast and profoundly thin.
IMDB link: https://www.imdb.com/title/tt0212720
=========
Title: I, Robot
Genre: Action,Mystery,Sci-Fi
Description: In 2035, highly intelligent robots fill public service positions throughout the world, operating under three rules to keep humans safe. Despite his dark history with robotics, Detective Del Spooner (Will Smith) investigates the alleged suicide of U.S. Robotics founder Alfred Lanning (James Cromwell) and believes that a human-like robot (Alan Tudyk) murdered him. With the help of a robot expert (Bridget Moynahan), Spooner discovers a conspiracy that may enslave the human race.
IMDB link: https://www.imdb.com/title/tt0343818
=========
Title: The Iron Giant
Genre: Action,Adventure,Animation
Description: In this animated adaptation of Ted Hughes' Cold War fable, a giant alien robot (Vin Diesel) crash-lands near the small town of Rockwell, Maine, in 1957. Exploring the area, a local 9-year-old boy, Hogarth, discovers the robot, and soon forms an unlikely friendship with him. When a paranoid government agent, Kent Mansley, becomes determined to destroy the robot, Hogarth and beatnik Dean McCoppin (Harry Connick Jr.) must do what they can to save the misunderstood machine.
IMDB link: https://www.imdb.com/title/tt0129167
=========
FINAL ANSWER: 'The Iron Giant' is an animated movie about a friendship between a robot and a kid. It would be a good movie to watch with a kid.
SOURCE: https://www.imdb.com/title/tt0129167

QUESTION: {question}
=========
{summaries}
FINAL ANSWER:"""