# Flashcards for Differentiated Learning Styles

A crud application for flashcard review that attempts to ingratiate itself to adherents of the [differentiated learning](https://education.cu-portland.edu/blog/classroom-resources/examples-of-differentiated-instruction/) philosophy.

## Hypothesis 
Learners will enhance review session efficacy and knowledge retention if their natural learning style is engaged.

## Approach 
Provide users with the ability to customise flashcard review to a preffered learning style. The following learning styles will be available:
1. Visual - Flashcards styled with the intention to visually engage the reviewer
2. Auditory/Aural - Users are able to hear the contents of their flashcards as they quiz themselves

*Each of the above features can be greatly expanded upon to maximise the effect of the separate styles. What has been accomplished thusfar stands as a working proof of concept.*


## Technologies
* Python
* Flask
* Postgresql
* SQLAlchemy
* jQuery
* [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)

## Known Issues
* Poor cross browser compatibility. Some important styles break outside of chrome.
* No unit testing
* Error messages aren't being communicated to the user for failed POST actions 