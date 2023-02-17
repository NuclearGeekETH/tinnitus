# Tinnitus Treatment with Python

## Description
This project is a tool to create a reversing phase tone to try to help with the symptoms of tinnitus. The idea here is to create an audio file that plays a reversing phase tone that attempts to cancel out the tone you hear from tinnitus symptoms. While there is no scientific proof for this method, the symptoms of tinnitus can be so intense that many people are willing to try anything to alleviate them. The thought is to utilize the same principle as destructive noise cancellation, although in reality, this does not cause destructive noise cancellation because tinnitus is not a physical noise but a sensation. However, in the creator's testing, this method has shown to provide some relief even if that is anecdotal evidence.

## How to Use
If you want to try it out, follow these steps:

1. Find a tone that matches your tinnitus on a website like this: [Tone Generator](https://www.szynalski.com/tone-generator/).
2. Edit line 5 of `tinnitus.py` with your frequency you found in step 1.
3. Run `tinnitus.py` and play the output `test_tone.wav` using high-end headphones to see if this helps, some people report uneasy feelings while listening. Experimentation is important to finding a tone that helps.

The creator found 18500 Hz as their sweet spot for symptomatic relief. For them, when their symptoms are intense, they will play this file on a loop and it seems to cause some relief. They keep it stored on their mobile and play it over earbuds. It really helps them most at night when trying to fall asleep.

## Contact
If you try this method and it helps you or if you have any questions, feel free to reach out to the creator on [Twitter](https://twitter.com/NuclearGeeketh).

**Note:** The creator of this project is not a medical professional and this tool is not intended as a replacement for professional medical advice. If you are experiencing symptoms of tinnitus or any other health concerns, please consult a medical professional.
