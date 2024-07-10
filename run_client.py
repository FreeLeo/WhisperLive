from whisper_live.client import TranscriptionClient


def run_client():
    client = TranscriptionClient(
        # "172.31.10.90",
        "54.191.115.54",
        # "127.0.0.1",
        8282,
        lang="zh",
        translate=False,
        model="large-v2",
        use_vad=False,
        # Only used for microphone input, False by Default
        save_output_recording=True,
        # Only used for microphone input
        output_recording_filename="./output_recording.wav"
    )
    client()


if __name__ == "__main__":
    run_client()
    print("Transcription end.")
