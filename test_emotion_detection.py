import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotion(unittest.TestCase): 

    def test_emotions(self): 
        self.assertEqual(emotion_detector('I am glad this happened')['dominant_emotion'], 'joy') 


s')['dominant_emotion'], 'disgust') 

s')['dominant_emotion'], 'sadness') 

ppen')['dominant_emotion'], 'fear') 
     
