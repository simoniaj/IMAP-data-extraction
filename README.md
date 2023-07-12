# IMAP-data-extraction
This program was developed to extract specific data from a large number of emails (7,000+). This was developed to complete a task I was assigned at work.

My task was to go through our notification inbox which consisted of almost 7,000 emails with JSON prompts and extract a specific line of data to add to our CRM. There were of course exceptions to the data extraction such as emails containing certain names, the phrase; 'no signal', and the word 'clear' should be ignored.

This program was developed in VSCode intending to use IMAP in the programming language Python to access the notification inbox and extract data meeting this criteria. The program extracted the needed data and wrote it to a .txt file that can be accessed. The data was then used for its intended purposes.

I was able to extract 1173 lines of data in this process.

Specify Data parts require the user to specify which data they want to be extracted from the email. The comments have also be changed to not include any defining data. This is a template code so make it your own with your specifications.
