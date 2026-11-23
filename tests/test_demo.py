from pathlib import Path
import unittest
import wave

from open_tmr.cli import demo
from open_tmr.content import validate_lesson
from open_tmr.cue import Modality, create_association, validate_association


class OfflineDemoTests(unittest.TestCase):
    def test_demo_creates_expected_synthetic_outputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = demo(temporary)
            root = Path(temporary)
            self.assertTrue((root / "lesson.json").exists())
            self.assertTrue((root / "session.json").exists())
            self.assertTrue((root / "audio_metadata.json").exists())
            self.assertTrue((root / "cue_associations.json").exists())
            self.assertTrue((root / "validation.txt").exists())

    def test_marker_wav_is_pcm(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            demo(root)
            wav_path = root / "segment-topic-memory-stages.wav"
            with wave.open(str(wav_path), "rb") as wav:
                self.assertEqual(wav.getnchannels(), 1)
                self.assertEqual(wav.getsampwidth(), 2)
                self.assertGreater(wav.getnframes(), 0)


if __name__ == "__main__":
    unittest.main()
