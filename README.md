# PTE-reading-marker
## Features:
1. App's introduction for the user.
2. User input a paragraph to be tested 
3. The user can record what he/she say to compare with the inputed paragraph.

## Code flow:
1. Present the user with the paragraph:
   1. Get the length of the paragraph.
   2. Generate a random number from 0 to the len of paragraphs - 1.
   3. Use that random number as the index.
2. Generate text from the user's speech.
   1. Use google cloud.
3. Anaylyze correctness:
   1. Paragraph vs UserInput.
   2. Split the paragraph and the UserInput into arrays of words.
   3. Compare each word from each array to each other.
