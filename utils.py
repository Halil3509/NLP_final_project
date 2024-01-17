from disorder_detection import DisorderDetection


def full_disorder_detection_legacy(self, audio_text):
    self.logger.info("Full Disorder Detection Legacy process is starting...")

    # Disorder Part
    disorder_class = DisorderDetection(text=audio_text)
    total_disorder_result_json = disorder_class.run_disorder_detection()

    self.logger.info("Full Disorder Detection Legacy process was finished.")

    return total_disorder_result_json
