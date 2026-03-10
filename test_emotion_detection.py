import EmotionDetection as ed

statements = ["I am glad this happened",
    "I am really mad about this",
    "I feel disgusted just hearing about this",
    "I am so sad about this",
    "I am really afraid that this will happen"]

for s in statements:
    print (f"{s}\t{ed.emotion_detector(s)['dominant_emotion']}")