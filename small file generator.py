from elevenlabslib import *
from elevenlabslib.helpers import *
def display_models(models):
    print("\nAvailable Models:")
    for i, model in enumerate(models, start=1):
        print(f"Press {i} for {model['name']}")

def get_user_choice(models):
    choice = None
    while choice is None or choice < 1 or choice > len(models) + 1:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > len(models) + 1:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return choice

def display_voices(voices):
    print("\nAvailable Voices:")
    for i, voice in enumerate(voices, start=1):
        print(f"Press {i} for {voice.initialName}")

def get_user_voice_choice(voices):
    choice = None
    while choice is None or choice < 1 or choice > len(voices):
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > len(voices):
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return choice


def read_and_generate_audio(input_file):
    # Open and read the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Iterate through the lines
    for line in lines:
        # Split line into filename and text
        filename, text = [x.strip() for x in line.split('=')]
        print(f"starting synthesis of file {filename} with text {text} .\n")
        # Generate audio from text
        audio_bytes = chosen_voice.generate_audio(text)

        # Save the audio bytes with filename and .mp3 extension
        save_audio_bytes(audio_bytes, f'{filename}.mp3', "mp3")

user = ElevenLabsUser(open("elevenlabs.txt", "r").read())
models = user.get_available_models()  # get the models that can be used.
display_models(models)
user_model_choice = get_user_choice(models)
chosen_model = models[user_model_choice - 1]
print(f"\nYou have chosen the {chosen_model['name']} model.")
voices = user.get_available_voices()  # get the voices that can be used.
display_voices(voices)
user_voice_choice = get_user_voice_choice(voices)
chosen_voice = voices[user_voice_choice - 1]
print(f"\nYou have chosen the {chosen_voice.initialName} voice.")
read_and_generate_audio('input.txt')
