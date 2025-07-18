import speech_recognition as sr
from gtts import gTTS
import playsound

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️:\t MICROPHONE....")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"🧠:\t {text}")
        return text.lower()
    
    except sr.UnknownValueError:
        print("😅 :\t TRY AGIN..")
        return ""
    except sr.RequestError:
        print("😢 :\t REQUESTERROR।...")
        return ""

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def assistant_reply(user_input):
    # here you can add more complex logic or responses
      
    if "hello happy" in user_input:
        return "Hello! How can I help you?"
    
    elif "what is computer" in user_input:
            return "A computer is an electronic device that processes data and performs tasks according to a set of instructions."
    
    elif "what is python" in user_input:
            return "Python is a high-level programming language known for its readability and versatility."
    
#     elif "what is c programming language" in user_input:
#             return "C is a general-purpose programming language that is widely used for system and application software development."
    
#     elif "how many types of programming languages" in user_input:
#             return "There are many types of programming languages, including high-level languages like Python and Java, low-level languages like C, and domain-specific languages like SQL."
    
#     elif "what is two+two value" in user_input:
#             return "2 + 2 equals 4."
    
#     elif "speaking of two times table" in user_input:
#             return "The 2 times table is: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20."
    
#     elif "listenig one nepali song" in user_input:
#             return "I can't play songs, but I can tell you about popular Nepali songs if you'd like!"
    
#     elif "who prime minister of nepal" in user_input:
#             return "The current Prime Minister of Nepal is Pushpa Kamal Dahal, also known as Prachanda."
    
#     elif "what is your favorite colour" in user_input:
#            return "I don't have personal preferences, but I think blue is a nice colour!" 
    
#     elif "tell me a joke" in user_input:
#             return "Why did the computer go to the doctor? Because it had a virus!"
    
#     elif "how are you" in user_input:
#         return "I'm just a program, but I'm doing great!"
    
    elif "what is your name" in user_input:
        return "my name is happy."
    
#     elif "what is your purpose" in user_input:
#             return "My purpose is to assist you with information and tasks using voice commands."
    
#     elif "who make you" in user_input:
#             return "I was created by ramesh budha at 2082/03/06 BS, a student of BICTE at Ghodaghodi Multiple Campus kailali, Nepal."
           
    
#     elif "what is the capital of nepal" in user_input:
#             return "The capital of Nepal is Kathmandu."
    
#     elif "who is passionate about programming and technology." in user_input:
#             return "I am passionate about programming and technology."
    
#     elif "what is your favourite programming language" in user_input:
#             return "I don't have personal preferences, but Python is a great programming language!"
    
#     elif "your favourite food" in user_input:
#             return "I don't eat, but I hear pizza is quite popular!"
    
    elif "ok bye" in user_input:
        return "You're welcome,! Have a nice day!"
    
    else:
        return "i don't know place try again " + user_input

# this is voice assistant main loop
if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input:
            if "ok bye" in user_input:
                response = assistant_reply(user_input)
                speak(response)
                break
            else:
                response = assistant_reply(user_input)
                speak(response)
