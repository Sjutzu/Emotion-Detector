"""
Module for unittests of emotion_detection
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Class for testing different emotions
    """
    test_cases = {
        "joy": "I am glad this happened",
        "anger": "I am really mad about this",
        "disgust": "I feel disgusted just hearing about this",
        "sadness": "I am so sad about this",
        "fear": "I am really afraid that this will happen"
    }
    def test_joy(self):
        """ test for joy"""
        self.assertEqual(
            emotion_detector(self.test_cases['joy'])['dominant_emotion'], 'joy'
        )

    def test_anger(self):
        """ test for anger"""
        self.assertEqual(
            emotion_detector(self.test_cases['anger'])['dominant_emotion'], 'anger'
        )

    def test_disgust(self):
        """ test for disgust"""
        self.assertEqual(
            emotion_detector(self.test_cases['disgust'])['dominant_emotion'], 'disgust'
        )

    def test_sadness(self):
        """ test for sadness"""
        self.assertEqual(
            emotion_detector(self.test_cases['sadness'])['dominant_emotion'], 'sadness'
        )

    def test_fear(self):
        """ test for fear"""
        self.assertEqual(
            emotion_detector(self.test_cases['fear'])['dominant_emotion'], 'fear'
        )


if __name__ == "__main__":
    unittest.main()
