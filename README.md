# Magic Jar

## Description
I made a completely useless app that give you an activity you can do if you're bored. You shake a jar to get a slip of paper with a random activity on it. Of course, if you're feeling lazy and don't want to do said activity, the app will also give you a fake excuse you can use to  get out of it. But then, as compensation, it offers you a fun fact instead.

I used ChatGPT until I ran out of messages and then I switched to Gemini. I made the separate parts of the project on different files: one for the background, one for the jar and its associated animations, and one for the text that includes the API calls. 

My code calls 4 APIs. The first one https://bored-api.appbrewery.com/random, gets called when the jar is shaken. It doesn't take in any arguments and outputs a long text that contains a random activity. Then, the key words from the activity is matched to a similar category name and passed into the second API call https://emojihub.yurace.pro/api/category/{category-name} which outputs a related emoji. The activity description and the emoji are displayed together on the paper. When the user asks for an excuse, the third excuse https://excuser-three.vercel.app/v1/excuse/unbelievable is called with the emoji category as a parameter which returns a text with an excuse that relates to the general theme. Ladtly, https://uselessfacts.jsph.pl/api/v2/facts/random is called with no parameter when the user asks for a fact.

## Important Prompts
- make an html file of a dark night background and lightly twinkling stars and fireflies flying around
- code an app that when you press a button there's a semi-transparent jar that shakes and then the lid comes off, a slip of paper flies out, and the paper unrolls to reveal text that says "hello" on it
- instead of making the shake the jar and the reset button separate, simply replace the text on the shake button with the reset button and then reset the app from the start
- edit this code so that instead of the paper displaying the word "hello" i want it to display whatever comes out of this API call: https://bored-api.appbrewery.com/random 
- i also want it printed with an emoji from this API call: https://emojihub.yurace.pro/api/random/category/food-and-drink except instead of it always being "food-and-drink" it's one of these categories that best fits the result from the first boredapi call *insert all possible categories*
- now on the "The excuse" paper can there be a button next to the close button that is called "get a random fact instead" that displays a call to https://uselessfacts.jsph.pl/api/v2/facts/random 
- combine these files 

## Run the Project
- On terminal 1 run: python app.py
- On terminal 2 run: python -m http.server 8000
- Copy into browser: http://127.0.0.1:8000/index.html

## Video Link
- https://drive.google.com/file/d/1dX6FyVuDwRiesjWNPR33-OcALwUvQUE0
