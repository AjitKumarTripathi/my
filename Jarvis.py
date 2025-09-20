import tkinter as tk
import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

def calculate_expression(expression):
    try:
        result = eval(expression)
        return f"The result is {result}."
    except Exception:
        return "Sorry, I couldn't calculate that."


qa_pairs = {
    "name the planets": "The planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
    "name some body parts": "Some human body parts are eyes, nose, ears, hands, legs, and heart.",
    "name some flowers": "Some flowers are rose, lily, sunflower, tulip, and daisy.",
    "name some animals": "Some animals are lion, tiger, elephant, dog, and cat.",
    "what is the capital of india": "The capital of India is New Delhi.",
    "what is the largest mammal": "The largest mammal is the blue whale.",
    "what is the tallest mountain": "Mount Everest is the tallest mountain on Earth.",
    "name some fruits": "Some fruits are apple, banana, mango, orange, and grapes.",
    "name some vegetables": "Some vegetables are carrot, potato, tomato, spinach, and cucumber.",
    "how many continents are there": "There are seven continents: Asia, Africa, North America, South America, Antarctica, Europe, and Australia.",
    "who is the prime minister of india": "The Prime Minister of India is shi Damordas Narendra Modi.",
    "name the oceans": "There are five oceans: Pacific, Atlantic, Indian, Southern, and Arctic.",
    "how many bones in human body": "An adult human body has 206 bones.",
    "what is the national animal of india": "The national animal of India is the Bengal tiger.",
    "what is the national bird of india": "The national bird of India is the peacock.",
    "what is the national flower of india": "The national flower of India is the lotus.",
    "name some domestic animals": "Some domestic animals are cow, goat, dog, cat, and buffalo.",
    "name some wild animals": "Some wild animals are lion, tiger, elephant, giraffe, and zebra.",
    "what is the smallest planet": "The smallest planet in our solar system is Mercury.",
    "what is the hottest planet": "The hottest planet is Venus.",
    "which planet is known as red planet": "Mars is known as the Red Planet.",
    "which planet has rings": "Saturn is known for its rings.",
    "how many teeth in adult human": "An adult human has 32 teeth.",
    "how many lungs does a human have": "Humans have two lungs.",
    "how many kidneys does a human have": "Humans have two kidneys.",
    "name some insects": "Some insects are ant, bee, butterfly, mosquito, and beetle.",
    "name some reptiles": "Some reptiles are lizard, snake, crocodile, and turtle.",
    "name some birds": "Some birds are sparrow, eagle, parrot, pigeon, and owl.",
    "what is the largest bird": "The largest bird is the ostrich.",
    "what is the fastest land animal": "The fastest land animal is the cheetah.",
    "what is the longest river": "The longest river in the world is the Nile River.",
    "what is the largest desert": "The largest desert is the Antarctic Desert.",
    "how many states in india": "India has 28 states and 8 Union Territories.",
    "what is the national sport of india": "The national sport of India is hockey.",
    "name some healthy foods": "Some healthy foods are fruits, vegetables, nuts, grains, and fish.",
    "name some junk foods": "Some junk foods are chips, burgers, fries, pizza, and sugary drinks.",
    "what is the boiling point of water": "The boiling point of water is 100 degrees Celsius.",
    "what is the freezing point of water": "The freezing point of water is 0 degrees Celsius.",
    "name some shapes": "Some shapes are circle, square, triangle, rectangle, and hexagon.",
    "what are primary colors": "The primary colors are red, blue, and yellow.",
    "how many hours in a day": "There are 24 hours in a day.",
    "how many minutes in an hour": "There are 60 minutes in an hour.",
    "how many seconds in a minute": "There are 60 seconds in a minute.",
    "how many days in a year": "There are 365 days in a year, or 366 in a leap year.",
    "how many weeks in a year": "There are 52 weeks in a year.",
    "how many months in a year": "There are 12 months in a year.",
    "what is the largest country by area": "Russia is the largest country by area.",
    "what is the most populated country": "India is the most populated country.",
    "name some festivals of india": "Some festivals of India are Diwali, Holi, Eid, Christmas, and Navratri.",
    "name some means of transport": "Some means of transport are car, bus, train, bicycle, and airplane.",
    "name some professions": "Some professions are doctor, engineer, teacher, lawyer, and farmer.",
    "what is the main source of energy": "The sun is the main source of energy.",
    "how many senses do humans have": "Humans have five senses: sight, hearing, touch, taste, and smell.",
    "what is the nearest star": "The nearest star to Earth is the Sun.",
    "what is the moon": "The Moon is Earth's only natural satellite.",
    "name some water animals": "Some water animals are fish, dolphin, whale, octopus, and shark.",
    "name some amphibians": "Some amphibians are frog, toad, and salamander.",
    "what is gravity": "Gravity is a force that pulls objects towards each other.",
    "what is the speed of light": "The speed of light is approximately 299,792 kilometers per second.",
    "what is the earth made of": "Earth is made of core, mantle, and crust.",
    "what is your name": "My name is jarvis.",
    "hello": "hello master how can i help you",
    "give me your python code": "i can't give code",
    "give your all question": "name the planets,name some body parts,name some flowers,name some animals,what is the capital of india,what is the largest mammal,what is the tallest mountain,name some fruits,name some vegetables,how many continents are there,who is the prime minister of india,name the oceans,how many bones in human body,what is the national animal of india,what is the national bird of india,what is the national flower of india,name some domestic animals,name some wild animals,what is the smallest planet,what is the hottest planet,which planet is known as red planet,which planet has rings,how many teeth in adult human,how many lungs does a human have,how many kidneys does a human have,name some insects,name some reptiles,name some birds,what is the largest bird,what is the fastest land animal,what is the longest river,what is the largest desert,how many states in india,what is the national sport of india,name some healthy foods,name some junk foods,what is the boiling point of water,what is the freezing point of water,name some shapes,what are primary colors,how many hours in a day,how many minutes in an hour,how many seconds in a minute,how many days in a year,how many weeks in a year,how many months in a year,what is the largest country by area,what is the most populated country,name some festivals of india,name some means of transport,name some professions,what is the main source of energy,how many senses do humans have,what is the nearest star,what is the moon,name some water animal,name some amphibians,what is gravity,what is the speed of light,what is the earth made of,what is your name,hello,give me your python code,give your all question,calculate.",
}


# --- Tkinter GUI Functions ---
def process_query():
    user_input = user_entry.get().lower()
    user_entry.delete(0, tk.END)

    response = ""

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"You: {user_input}\n", 'user_text')

    if user_input == "stop":
        response = "Goodbye!"
        root.after(100, root.destroy)
    elif user_input.startswith("calculate"):
        expression = user_input.replace("calculate", "").strip()
        response = calculate_expression(expression)
    elif user_input in qa_pairs:
        response = qa_pairs[user_input]
    else:
        response = "Sorry, I don't know the answer to that."

    chat_display.insert(tk.END, f"Jarvis: {response}\n\n", 'jarvis_text')
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

    engine.say(response)
    engine.runAndWait()


# --- Tkinter GUI Setup ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Jarvis Assistant")
    root.geometry("600x500")

    chat_display = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, bg="#f0f0f0")
    chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    chat_display.tag_config('user_text', foreground='blue')
    chat_display.tag_config('jarvis_text', foreground='green')

    input_frame = tk.Frame(root)
    input_frame.pack(padx=10, pady=(0, 10), fill=tk.X)

    user_entry = tk.Entry(input_frame, font=("Arial", 12))
    user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
    user_entry.bind("<Return>", lambda event=None: process_query())

    send_button = tk.Button(input_frame, text="Send", command=process_query, font=("Arial", 12))
    send_button.pack(side=tk.RIGHT, padx=(10, 0), ipady=3)

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "Jarvis: Hello master. How can I help you?\n\n", 'jarvis_text')
    chat_display.config(state=tk.DISABLED)

    engine.say("Hello master. How can I help you?")
    engine.runAndWait()

    root.mainloop()

    import os
    import subprocess
    import tkinter as tk
    from tkinter import messagebox


    # यह फ़ंक्शन पिछले कोड से लिया गया है।
    # यह ऐप्लिकेशन खोलने का काम करता है।
    def open_basic_application(app_name):
        """
        ऑपरेटिंग सिस्टम के आधार पर विभिन्न बुनियादी ऐप्लिकेशन और टर्मिनल खोलता है।
        """
        app_name = app_name.lower()

        # ऐप्लिकेशन और उनके OS-विशिष्ट कमांड्स को परिभाषित करें
        app_commands = {
            'windows': {
                'calculator': ['calc.exe'],
                'clock': ['start', 'ms-clock:'],
                'notepad': ['notepad.exe'],
                'file explorer': ['explorer.exe'],
                'settings': ['start', 'ms-settings:'],
                'photos': ['start', 'ms-photos:'],
                'terminal': ['start', 'cmd.exe']
            },
            'macos': {
                'calculator': ['open', '-a', 'Calculator'],
                'clock': ['open', '-a', 'Clock'],
                'notepad': ['open', '-a', 'TextEdit'],
                'file explorer': ['open', '-a', 'Finder'],
                'settings': ['open', '-a', 'System Settings'],
                'photos': ['open', '-a', 'Photos'],
                'terminal': ['open', '-a', 'Terminal']
            },
            'linux': {
                'calculator': ['gnome-calculator', 'kcalc'],
                'clock': ['gnome-clocks', 'kclock'],
                'notepad': ['gedit', 'kate'],
                'file explorer': ['nautilus', 'dolphin'],
                'settings': ['gnome-control-center', 'systemsettings'],
                'photos': ['eog', 'gwenview'],
                'terminal': ['gnome-terminal', 'konsole']
            }
        }

        try:
            if os.name == 'nt':
                commands = [app_commands['windows'].get(app_name)]
            elif os.name == 'posix':
                if 'darwin' in os.uname():
                    commands = [app_commands['macos'].get(app_name)]
                else:
                    commands = app_commands['linux'].get(app_name, [])
            else:
                messagebox.showerror("त्रुटि", "आपका ऑपरेटिंग सिस्टम समर्थित नहीं है।")
                return

            if commands:
                for command in commands:
                    if command:
                        try:
                            subprocess.Popen(command, shell=(os.name == 'nt'))
                            return
                        except FileNotFoundError:
                            continue
                messagebox.showwarning("चेतावनी", f"माफ कीजिए, '{app_name}' के लिए कोई भी कमांड नहीं मिला।")
            else:
                messagebox.showwarning("चेतावनी", f"माफ कीजिए, '{app_name}' के लिए कोई कमांड नहीं मिला।")

        except Exception as e:
            messagebox.showerror("त्रुटि", f"एक त्रुटि हुई: {e}")


    # tkinter GUI बनाएं
    def create_gui():
        root = tk.Tk()
        root.title("ऐप्लिकेशन ओपनर")
        root.geometry("400x300")

        label = tk.Label(root, text="जिस ऐप्लिकेशन को खोलना चाहते हैं उस पर क्लिक करें:", font=("Helvetica", 12))
        label.pack(pady=10)

        # बटनों के लिए एक फ्रेम
        frame = tk.Frame(root)
        frame.pack(pady=10)

        # बटनों की लिस्ट
        apps = [
            ("Calculator", "कैलकुलेटर"),
            ("Clock", "क्लॉक"),
            ("Notepad", "नोटपैड"),
            ("File Explorer", "फाइल एक्सप्लोरर"),
            ("Settings", "सेटिंग्स"),
            ("Photos", "फोटोज"),
            ("Terminal", "टर्मिनल")
        ]

        for app_name, button_text in apps:
            button = tk.Button(
                frame,
                text=button_text,
                command=lambda name=app_name: open_basic_application(name),
                width=20,
                height=2
            )
            button.pack(pady=5)

        root.mainloop()


    # GUI को चलाएं
    if __name__ == "__main__":
        create_gui()

        import tkinter as tk
        from tkinter import messagebox
        from tkcalendar import Calendar
        import datetime
        import time
        import threading
        import winsound  # winsound मॉड्यूल इंपोर्ट करें


        def play_alarm_sound():
            try:
                # 1000 Hz की फ्रीक्वेंसी पर 500 मिलीसेकंड के लिए बीप बजाएं
                winsound.Beep(1000, 60000)
            except Exception as e:
                messagebox.showerror("Error", f"Error playing sound: {e}")


        def check_alarm_time(alarm_datetime):
            while True:
                now = datetime.datetime.now()
                time_difference = (alarm_datetime - now).total_seconds()

                if time_difference <= 1 and time_difference > -1:
                    messagebox.showinfo("Alarm!", "Alarm is ringing!")
                    play_alarm_sound()  # यहाँ आवाज़ बजाने वाला फ़ंक्शन कॉल किया गया है
                    break
                time.sleep(1)


        def set_alarm():
            try:
                date_obj = cal.selection_get()
                time_str = time_entry.get()
                am_pm = ampm_var.get()

                if am_pm == "PM" and int(time_str.split(":")[0]) != 12:
                    hour = int(time_str.split(":")[0]) + 12
                elif am_pm == "AM" and int(time_str.split(":")[0]) == 12:
                    hour = 0
                else:
                    hour = int(time_str.split(":")[0])

                minute = int(time_str.split(":")[1])

                alarm_datetime = datetime.datetime(date_obj.year, date_obj.month, date_obj.day, hour, minute, 0)

                if alarm_datetime <= datetime.datetime.now():
                    messagebox.showerror("Error", "Alarm time cannot be in the past.")
                    return

                messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_datetime.strftime('%Y-%m-%d %I:%M %p')}.")

                alarm_thread = threading.Thread(target=check_alarm_time, args=(alarm_datetime,))
                alarm_thread.daemon = True
                alarm_thread.start()
            except ValueError:
                messagebox.showerror("Error", "Please enter time (HH:MM) and date in correct format.")


        def set_today():
            today = datetime.date.today()
            cal.selection_set(today)
            messagebox.showinfo("Date Set", f"Date has been set to today: {today.strftime('%Y-%m-%d')}")


        root = tk.Tk()
        root.title("Python Alarm Clock")
        root.geometry("450x450")

        tk.Label(root, text="Enter Time (HH:MM):", font=("Arial", 12)).pack(pady=10)
        time_entry = tk.Entry(root, font=("Arial", 14))
        time_entry.pack(pady=5)

        ampm_var = tk.StringVar(value="AM")
        ampm_frame = tk.Frame(root)
        ampm_frame.pack(pady=5)
        tk.Radiobutton(ampm_frame, text="AM", variable=ampm_var, value="AM").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(ampm_frame, text="PM", variable=ampm_var, value="PM").pack(side=tk.LEFT, padx=10)

        cal_label = tk.Label(root, text="Select Date:", font=("Arial", 12))
        cal_label.pack(pady=10)
        cal = Calendar(root, selectmode="day", date_pattern="mm/dd/y")
        cal.pack(pady=10)

        today_button = tk.Button(root, text="Today", command=set_today)
        today_button.pack(pady=5)

        set_button = tk.Button(root, text="Set Alarm", command=set_alarm, font=("Arial", 12, "bold"))
        set_button.pack(pady=10)

        root.mainloop()

        import tkinter as tk
        from tkinter import ttk


        class BigStoryApp(tk.Tk):
            def __init__(self):
                super().__init__()
                self.title("नारुतो और बोरूटो की पूरी कहानी")
                self.geometry("1000x800")

                # A dictionary to store all story content (the big, detailed stories)
                self.story_data = {
                    "Naruto Shippuden (नारुतो शिपुडेन)": {
                        "title": "नारुतो शिपुडेन: पूरा सफर",
                        "content": """
        **भाग 1: गारा का बचाव और सासुके की तलाश**

        नारुतो शिपुडेन की कहानी ठीक वहीं से शुरू होती है जहाँ से पहली सीरीज खत्म हुई थी।
        नारुतो अब कोई बच्चा नहीं रहा।
        वह अपने गुरु जिराइया के साथ 2.5 साल की कड़ी ट्रेनिंग के बाद कोनोहा गांव लौटता है।
        वह एक मजबूत, लंबा और कहीं ज्यादा परिपक्व निंजा बन गया है।

        उसका पहला मिशन अपने पुराने दोस्त और अब पांचवें काज़ेकागे, गारा को बचाना है।
        गारा को अकात्सुकी के खतरनाक सदस्य डीडारा ने अपहरण कर लिया है।
        अकात्सुकी एक खतरनाक संगठन है जो सभी टेलड बीस्ट्स (बीजू) को पकड़कर उनके चक्र को इकट्ठा करना चाहता है।
        नारुतो अपनी टीम 7 के सदस्यों साकुरा और काकाशी के साथ गारा को बचाने के लिए निकलता है।
        रास्ते में, उनकी मुलाकात अकात्सुकी के दो सदस्यों, सासोरी और डीडारा, से होती है।
        साकुरा और लेडी चियो मिलकर कठपुतली मास्टर सासोरी का मुकाबला करते हैं और उसे हराते हैं।
        दूसरी तरफ, नारुतो डीडारा को पीछे हटाता है और गारा को बचाता है।

        गारा को बचाने के बाद, नारुतो एक बार फिर से सासुके को ढूंढने और उसे कोनोहा वापस लाने की कोशिश करता है।
        टीम 7 का पुनर्गठन होता है जिसमें साई और यामातो भी जुड़ते हैं।
        वे सासुके उचिहा को ओरोचिमारू के चंगुल से वापस लाने की कोशिश करते हैं।
        लेकिन सासुके अब और भी ज्यादा शक्तिशाली हो गया है और उसे लगता है कि वह नारुतो से कहीं ज्यादा आगे निकल गया है।

        **भाग 2: जिराइया की मौत और पेइन का हमला**

        जैसे-जैसे कहानी आगे बढ़ती है, अकात्सुकी अपने मिशन में और भी सफल होती जाती है।
        जिराइया अकेले ही अकात्सुकी के नेता पेइन का पता लगाने के लिए जाते हैं।
        पेइन और उसके छह रूप (पेइन पाथ्स) से लड़ते हुए, जिराइया एक भयंकर लड़ाई में मारे जाते हैं।
        जिराइया की मौत से नारुतो को बहुत बड़ा सदमा लगता है।
        वह दुखी होता है, लेकिन हार नहीं मानता।
        वह अपने गुरु के सपनों को पूरा करने के लिए सेज मोड की ट्रेनिंग शुरू करता है।

        जब पेइन कोनोहा पर हमला करता है, तो वह पूरे गांव को नष्ट कर देता है।
        वह अपनी शक्तिशाली "शिरा तेंसई" तकनीक का उपयोग करके गांव को तबाह कर देता है।
        नारुतो सेज मोड में लौटता है।
        वह एक-एक करके सभी पेइन पाथ्स को हराता है।
        अंत में, वह असली पेइन, नागातो से मिलता है।
        नागातो को नारुतो अपनी बातों से प्रभावित करता है।
        नागातो अपनी जान देकर उन सभी को जीवित कर देता है जिन्हें उसने मारा था।
        नारुतो कोनोहा का हीरो बन जाता है।

        **भाग 3: चौथा महान निंजा युद्ध और अंतिम लड़ाई**

        इस बीच, सासुके भी अपने भाई इताची से सच्चाई जानने के बाद कोनोहा को नष्ट करने की कसम खाता है।
        अकात्सुकी का असली नेता, ओबिटो उचिहा, सभी टेलड बीस्ट्स को इकट्ठा करने और एक अनंत भ्रम की दुनिया बनाने के लिए चौथा महान निंजा युद्ध घोषित करता है।
        सभी पांच महान निंजा गांव अकात्सुकी के खिलाफ एकजुट हो जाते हैं।
        नारुतो और सासुके मिलकर इस युद्ध को खत्म करने की कोशिश करते हैं।
        वे कई पुराने दुश्मनों और दोस्तों से मिलते हैं जिन्हें पुनर्जीवित कर दिया गया था।
        ओबिटो और मदारा उचिहा को हराने के बाद, नारुतो और सासुके मिलकर युद्ध को खत्म करने की कोशिश करते हैं।
        लेकिन कहानी का सबसे बड़ा मोड़ तब आता है जब मदारा को कोई और हराता है और असली विलेन, कागुया ओत्सुत्सुकी, प्रकट होती है।
        कागुया सभी चक्र की जड़ है और दुनिया को नष्ट करना चाहती है।
        नारुतो और सासुके अपनी नई शक्तियों का उपयोग करके कागुया का सामना करते हैं और उसे सील कर देते हैं, जिससे युद्ध का अंत होता है।
        युद्ध के बाद, नारुतो और सासुके के बीच एक अंतिम लड़ाई होती है।
        दोनों एक-दूसरे को समझते हैं और दोस्त बन जाते हैं।
        अंत में, नारुतो अपने सपनों को पूरा करता है और कोनोहा का सातवां होकागे बन जाता है, जिससे निंजा दुनिया में शांति आती है।
        """
                    },
                    "Boruto (बोरूटो)": {
                        "title": "बोरूटो: नारुतो नेक्स्ट जनरेशंस का पूरा सफर",
                        "content": """
        **भाग 1: नई पीढ़ी का उदय और ओत्सुत्सुकी का हमला**

        बोरूटो की कहानी नारुतो के सातवें होकागे बनने के कई साल बाद शुरू होती है।
        कोनोहा अब एक आधुनिक और शांतिपूर्ण गांव है।
        लेकिन बोरूटो उज़ुमाकी, नारुतो का बेटा, अपने पिता की महानता की छाया में रहता है।
        वह अपनी खुद की पहचान बनाना चाहता है।
        वह अक्सर अपने पिता से नाराज रहता है क्योंकि नारुतो होकागे होने के कारण परिवार को ज्यादा समय नहीं दे पाता।

        शुरुआती आर्क में, बोरूटो अपनी टीम मेट्स सारदा उचिहा और मित्सुकी के साथ चुनीन परीक्षा की तैयारी करता है।
        बोरूटो परीक्षा में धोखा देने के लिए एक साइंटिफिक निंजा टूल का उपयोग करता है, जिससे नारुतो निराश होता है।
        इसी दौरान, मोमोत्सुकी और किंशीकी ओत्सुत्सुकी नामक दो बाहरी लोग गांव पर हमला करते हैं।
        वे सभी टेलड बीस्ट्स को इकट्ठा करना चाहते हैं और नारुतो को अपहरण कर लेते हैं।
        बोरूटो अपनी गलती को समझता है और अपने पिता को बचाने में मदद करता है।
        इस लड़ाई के दौरान, बोरूटो के हाथ पर "कर्मा" नाम का एक रहस्यमय निशान बन जाता है।
        यह निशान ओत्सुत्सुकी द्वारा किए गए हमले का परिणाम है।

        **भाग 2: करा संगठन और कावाकी का आगमन**

        मोमोत्सुकी की हार के बाद, कहानी का मुख्य मोड़ "कारा" नामक एक खतरनाक संगठन के आगमन के साथ आता है।
        यह संगठन ओत्सुत्सुकी के अवशेषों और रहस्यों पर काम कर रहा है।
        कारा का उद्देश्य एक रहस्यमय लड़के, कावाकी को ढूंढना है, जिसके पास भी कर्मा का निशान है।
        कावाकी भागकर कोनोहा आ जाता है।
        नारुतो उसे अपने घर में रहने के लिए जगह देता है।
        बोरूटो और कावाकी की दोस्ती विकसित होती है।
        वे एक-दूसरे के कर्मा के निशान के रहस्य को समझने की कोशिश करते हैं।
        इस दौरान, वे करा संगठन के सदस्यों से लड़ते हैं और कई मुश्किलों का सामना करते हैं।
        नारुतो, सासुके, बोरूटो और कावाकी मिलकर जिशिकी ओत्सुत्सुकी का सामना करते हैं।

        **भाग 3: कर्मा का खतरा और नियति का संघर्ष**

        जिशिकी के खिलाफ लड़ाई में, नारुतो को अपनी जान जोखिम में डालकर अपनी अंतिम शक्ति, बैरॉन मोड, का उपयोग करना पड़ता है।
        बोरूटो को पता चलता है कि कर्मा का निशान उसे धीरे-धीरे मोमोत्सुकी में बदल रहा है।
        बाद में, अमदो, करा संगठन का एक वैज्ञानिक, कोनोहा में शरण लेता है।
        वह उन्हें ओत्सुत्सुकी के बारे में महत्वपूर्ण जानकारी देता है।
        बोरूटो और कावाकी को अपनी नियति का सामना करना पड़ता है।
        वे अपनी पहचान को बनाए रखने के लिए संघर्ष करते हैं।
        बोरूटो की कहानी अभी भी चल रही है।
        यह दिखाती है कि कैसे एक नई पीढ़ी अपने माता-पिता की विरासत को आगे बढ़ाती है।
        वे अपने स्वयं के रास्ते का पता लगाते हैं।
        भविष्य में बोरूटो और कावाकी के बीच होने वाली लड़ाई की शुरुआत भी इस कहानी में धीरे-धीरे होती है।
        """
                    }
                }

                # Create the main menu
                self.main_frame = tk.Frame(self)
                self.main_frame.pack(fill="both", expand=True)
                self.create_main_menu()

            def create_main_menu(self):
                # Clear the current frame
                for widget in self.main_frame.winfo_children():
                    widget.destroy()

                heading = ttk.Label(self.main_frame, text="कहानी चुनें:", font=("Helvetica", 20, "bold"))
                heading.pack(pady=40)

                for story_name in self.story_data:
                    button = ttk.Button(self.main_frame, text=story_name,
                                        command=lambda name=story_name: self.show_story_page(name))
                    button.pack(pady=10, ipadx=20, ipady=10)

            def show_story_page(self, story_name):
                # Clear the current frame
                for widget in self.main_frame.winfo_children():
                    widget.destroy()

                story_content = self.story_data[story_name]["content"]

                # Add a heading for the story
                heading = ttk.Label(self.main_frame, text=self.story_data[story_name]["title"],
                                    font=("Helvetica", 20, "bold"))
                heading.pack(pady=10)

                # Add a back button
                back_button = ttk.Button(self.main_frame, text="← मेनू पर वापस जाएँ", command=self.create_main_menu)
                back_button.pack(pady=5, padx=10, anchor="nw")

                # Create a text widget to display the story
                self.story_text = tk.Text(self.main_frame, wrap="word", font=("Helvetica", 14), padx=15, pady=15)
                self.story_text.pack(fill="both", expand=True)
                self.story_text.insert(tk.END, story_content)
                self.story_text.config(state=tk.DISABLED)


        if __name__ == "__main__":
            app = BigStoryApp()
            app.mainloop()

            import tkinter as tk
            from tkinter import messagebox


            class PuzzleGameGUI:
                def __init__(self, root):
                    self.root = root
                    self.root.title("Brain Test: Professor Gyan's Puzzles")
                    self.root.geometry("600x400")
                    self.root.config(bg="#f0f0f0")

                    self.puzzles = [
                        # --- Level 1 ---
                        [
                            {
                                'question': 'Ek aisi cheez jiske paas do aankhein hain, par wo dekh nahi sakti. Batao kya hai?',
                                'answer': 'sui',
                                'hint': 'Yeh kapde silne mein istemal hoti hai.'
                            },
                            {
                                'question': 'Main aapki awaaz ki tarah bol sakta hoon, par mere paas muh nahi hai. Main chala jata hoon jab tum bolte ho. Batao main kaun hoon?',
                                'answer': 'goonj',
                                'hint': 'Yeh ek awaaz hai jo laut kar aati hai, khaas kar pahadon mein.'
                            }
                        ],

                        # --- Level 2 ---
                        [
                            {
                                'question': 'Aisa kya hai jo tootne ke baad hi kaam aata hai?',
                                'answer': 'anda',
                                'hint': 'Ise tod kar omelette banaya ja sakta hai.'
                            },
                            {
                                'question': 'Aisa kya hai jo aap ka hai, par aap se zyada aapke dost istemal karte hain?',
                                'answer': 'aapka naam',
                                'hint': 'Yeh woh hai jo aapki pehchaan hai, par doosre iska upyog aapko bulane ke liye karte hain.'
                            }
                        ],

                        # --- Level 3 ---
                        [
                            {
                                'question': 'Aisa kya hai jo hamesha aata hai, par kabhi pahunchta nahi?',
                                'answer': 'kal',
                                'hint': 'Yeh woh samay hai jo aaj ke baad aayega.'
                            },
                            {
                                'question': 'Ek aadmi ke paas 500 ghode hain, 100 ghode mar gaye. Batao kitne ghode bache?',
                                'answer': '500',
                                'hint': 'Sawal mein chupa hai ki ghode mar gaye, gayab nahi hue.'
                            }
                        ]
                    ]

                    self.story = "Mai Professor Gyan hoon. Maine apna saara gyan in puzzles mein chupa diya hai. Inhe hal karke tum meri vidya ko anlok kar sakte ho. Shubh labh!"

                    self.current_level = 0
                    self.current_puzzle = 0
                    self.correct_answers = 0
                    self.total_puzzles = sum(len(level) for level in self.puzzles)

                    self.setup_widgets()
                    self.display_story_and_first_puzzle()

                def setup_widgets(self):
                    # Story Label
                    self.story_label = tk.Label(self.root, text="", wraplength=550, bg="#f0f0f0", font=("Arial", 12))
                    self.story_label.pack(pady=10)

                    # Level Label
                    self.level_label = tk.Label(self.root, text="", bg="#f0f0f0", font=("Arial", 14, "bold"))
                    self.level_label.pack(pady=5)

                    # Question Label
                    self.question_label = tk.Label(self.root, text="", wraplength=550, bg="#f0f0f0", font=("Arial", 14))
                    self.question_label.pack(pady=10)

                    # Answer Entry
                    self.answer_entry = tk.Entry(self.root, font=("Arial", 12))
                    self.answer_entry.pack(pady=5)
                    self.answer_entry.bind("<Return>", lambda event: self.check_answer())

                    # Buttons Frame
                    button_frame = tk.Frame(self.root, bg="#f0f0f0")
                    button_frame.pack(pady=10)

                    self.submit_button = tk.Button(button_frame, text="Jawab Do", command=self.check_answer,
                                                   font=("Arial", 12))
                    self.submit_button.pack(side=tk.LEFT, padx=10)

                    self.hint_button = tk.Button(button_frame, text="Sanket", command=self.show_hint,
                                                 font=("Arial", 12))
                    self.hint_button.pack(side=tk.LEFT, padx=10)

                    # Feedback Label
                    self.feedback_label = tk.Label(self.root, text="", bg="#f0f0f0", font=("Arial", 12, "italic"))
                    self.feedback_label.pack(pady=10)

                def display_story_and_first_puzzle(self):
                    self.story_label.config(text=self.story)
                    self.root.after(5000, self.show_next_puzzle)  # 5 seconds baad agla puzzle dikhao

                def show_next_puzzle(self):
                    self.story_label.pack_forget()  # Kahani ko chupa do
                    self.feedback_label.config(text="")
                    self.answer_entry.delete(0, tk.END)

                    if self.current_level < len(self.puzzles):
                        if self.current_puzzle < len(self.puzzles[self.current_level]):
                            # Agla puzzle dikhao
                            puzzle = self.puzzles[self.current_level][self.current_puzzle]
                            self.level_label.config(text=f"Level {self.current_level + 1}")
                            self.question_label.config(text=puzzle['question'])
                        else:
                            # Level khatam, agle level par jao
                            self.current_level += 1
                            self.current_puzzle = 0
                            self.show_next_puzzle()
                    else:
                        # Game khatam
                        self.show_final_score()

                def check_answer(self):
                    if self.current_level >= len(self.puzzles) or self.current_puzzle >= len(
                            self.puzzles[self.current_level]):
                        return

                    puzzle = self.puzzles[self.current_level][self.current_puzzle]
                    user_answer = self.answer_entry.get().strip().lower()

                    if user_answer == puzzle['answer']:
                        self.feedback_label.config(text="Bilkul sahi! Badhai ho!", fg="green")
                        self.correct_answers += 1
                        self.current_puzzle += 1
                        self.root.after(1500, self.show_next_puzzle)
                    else:
                        self.feedback_label.config(text="Galat jawab. Koshish karte rahiye.", fg="red")

                def show_hint(self):
                    if self.current_level < len(self.puzzles) and self.current_puzzle < len(
                            self.puzzles[self.current_level]):
                        hint = self.puzzles[self.current_level][self.current_puzzle]['hint']
                        self.feedback_label.config(text=f"Sanket: {hint}", fg="blue")

                def show_final_score(self):
                    self.level_label.config(text="")
                    self.question_label.config(text="")
                    self.answer_entry.pack_forget()
                    self.submit_button.pack_forget()
                    self.hint_button.pack_forget()
                    self.feedback_label.pack_forget()

                    message = f"Game khatam ho gaya! Aapne {self.total_puzzles} mein se {self.correct_answers} puzzles sahi hal kiye."
                    if self.correct_answers == self.total_puzzles:
                        message += "\nShandar! Aapne sabhi puzzles sahi hal kiye!"
                    else:
                        message += "\nAage bhi koshish karte rahiye!"

                    final_score_label = tk.Label(self.root, text=message, bg="#f0f0f0", font=("Arial", 16, "bold"))
                    final_score_label.pack(pady=50)


            if __name__ == "__main__":
                root = tk.Tk()
                game = PuzzleGameGUI(root)
                root.mainloop()

import tkinter as tk
import random
import time


class LudoGame:
    def __init__(self, master, players, is_ai_enabled):
        self.master = master
        self.players = players
        self.is_ai_enabled = is_ai_enabled
        self.current_player_index = 0
        self.current_player = self.players[0]
        self.dice_value = 0

        self.board_size = 500
        self.cell_size = self.board_size // 15
        self.piece_size = self.cell_size // 2

        self.colors = ['red', 'green', 'yellow', 'blue']
        self.player_colors = {player_name: self.colors[i] for i, player_name in enumerate(self.players)}

        # Ludo board ki positions
        self.path = [
            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (5, 6), (4, 6), (3, 6), (2, 6), (1, 6), (0, 6),
            (0, 7), (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14),
            (7, 14), (8, 14), (8, 13), (8, 12), (8, 11), (8, 10), (8, 9), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8),
            (14, 8),
            (14, 7), (14, 6), (13, 6), (12, 6), (11, 6), (10, 6), (9, 6), (8, 5), (8, 4), (8, 3), (8, 2), (8, 1),
            (8, 0),
            (7, 0)
        ]

        # Har player ke home paths
        self.home_paths = {
            'red': [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7)],
            'green': [(7, 13), (7, 12), (7, 11), (7, 10), (7, 9)],
            'yellow': [(13, 7), (12, 7), (11, 7), (10, 7), (9, 7)],
            'blue': [(7, 1), (7, 2), (7, 3), (7, 4), (7, 5)]
        }

        self.pieces = {player: [0, 0, 0, 0] for player in self.players}
        self.piece_positions = {player: ['home'] * 4 for player in self.players}

        self.canvas = tk.Canvas(master, width=self.board_size, height=self.board_size)
        self.canvas.pack()

        self.draw_board()
        self.draw_pieces()

        self.dice_button = tk.Button(master, text="Roll Dice", command=self.roll_dice, font=("Arial", 16))
        self.dice_button.pack(pady=10)

        self.turn_label = tk.Label(master, text=f"Player {self.current_player}'s Turn", font=("Arial", 14))
        self.turn_label.pack()

    def draw_board(self):
        # Board ke boxes
        self.canvas.create_rectangle(0, 0, self.board_size, self.board_size, fill='white')

        # Player ke home zones
        self.canvas.create_rectangle(0, 0, 6 * self.cell_size, 6 * self.cell_size, fill='red')
        self.canvas.create_rectangle(9 * self.cell_size, 0, 15 * self.cell_size, 6 * self.cell_size, fill='green')
        self.canvas.create_rectangle(0, 9 * self.cell_size, 6 * self.cell_size, 15 * self.cell_size, fill='blue')
        self.canvas.create_rectangle(9 * self.cell_size, 9 * self.cell_size, 15 * self.cell_size, 15 * self.cell_size,
                                     fill='yellow')

        # Stars aur safe spots
        self.canvas.create_oval(6 * self.cell_size, 2 * self.cell_size, 7 * self.cell_size, 3 * self.cell_size,
                                fill="black")  # Star
        self.canvas.create_oval(12 * self.cell_size, 6 * self.cell_size, 13 * self.cell_size, 7 * self.cell_size,
                                fill="black")
        self.canvas.create_oval(8 * self.cell_size, 12 * self.cell_size, 9 * self.cell_size, 13 * self.cell_size,
                                fill="black")
        self.canvas.create_oval(2 * self.cell_size, 8 * self.cell_size, 3 * self.cell_size, 9 * self.cell_size,
                                fill="black")

        # Home squares
        self.canvas.create_rectangle(6 * self.cell_size, 6 * self.cell_size, 9 * self.cell_size, 9 * self.cell_size,
                                     fill='pink')

        # Paths
        for r, c in self.path:
            x1, y1 = c * self.cell_size, r * self.cell_size
            x2, y2 = x1 + self.cell_size, y1 + self.cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, outline='black')

        # Home paths
        for color, path in self.home_paths.items():
            for r, c in path:
                x1, y1 = c * self.cell_size, r * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def draw_pieces(self):
        self.canvas.delete("pieces")
        for player, positions in self.piece_positions.items():
            for i, pos in enumerate(positions):
                color = self.player_colors[player]
                if pos == 'home':
                    x, y = self.get_home_coords(player, i)
                    self.canvas.create_oval(x, y, x + self.piece_size, y + self.piece_size, fill=color, tags="pieces")
                elif pos == 'final':
                    x, y = self.get_final_coords(player, i)
                    self.canvas.create_oval(x, y, x + self.piece_size, y + self.piece_size, fill='white', outline=color,
                                            tags="pieces")
                else:
                    r, c = pos
                    x, y = c * self.cell_size, r * self.cell_size
                    self.canvas.create_oval(x, y, x + self.piece_size, y + self.piece_size, fill=color, tags="pieces")

    def get_home_coords(self, player, piece_index):
        base_coords = {'red': (1, 1), 'green': (10, 1), 'yellow': (10, 10), 'blue': (1, 10)}
        row, col = base_coords[self.player_colors[player]]

        if piece_index == 0: return (col * self.cell_size, row * self.cell_size)
        if piece_index == 1: return ((col + 2) * self.cell_size, row * self.cell_size)
        if piece_index == 2: return (col * self.cell_size, (row + 2) * self.cell_size)
        if piece_index == 3: return ((col + 2) * self.cell_size, (row + 2) * self.cell_size)

    def get_final_coords(self, player, piece_index):
        base_coords = {'red': (6, 7), 'green': (7, 8), 'yellow': (8, 7), 'blue': (7, 6)}
        row, col = base_coords[self.player_colors[player]]

        if piece_index == 0: return (col * self.cell_size, row * self.cell_size)
        if piece_index == 1: return ((col) * self.cell_size, (row + 1) * self.cell_size)
        if piece_index == 2: return ((col + 1) * self.cell_size, (row) * self.cell_size)
        if piece_index == 3: return ((col + 1) * self.cell_size, (row + 1) * self.cell_size)

    def roll_dice(self):
        self.dice_value = random.randint(1, 6)
        self.turn_label.config(text=f"{self.current_player}'s turn. Dice: {self.dice_value}")

        if self.dice_value == 6:
            # Check if any pieces can move out from home
            if 'home' in self.piece_positions[self.current_player]:
                self.move_out_of_home()
            else:
                self.master.after(500, self.player_move)
        else:
            self.master.after(500, self.player_move)

    def player_move(self):
        movable_pieces = self.get_movable_pieces()
        if not movable_pieces:
            self.next_turn()
            return

        if self.is_ai_enabled and self.current_player == "AI Player":
            self.ai_move()
        else:
            self.turn_label.config(
                text=f"{self.current_player}'s turn. Dice: {self.dice_value}. Click a piece to move.")
            self.canvas.bind("<Button-1>", self.on_piece_click)

    def on_piece_click(self, event):
        clicked_piece_id = self.canvas.find_closest(event.x, event.y)
        # Check if the clicked piece is a valid one to move
        # (This part is complex, for this example we'll assume a simplified check)
        # For a full game, you'd check if the click matches a piece of the current player

        # Simplify for demo: just move the first movable piece
        movable_pieces = self.get_movable_pieces()
        if movable_pieces:
            piece_index_to_move = movable_pieces[0]
            self.move_piece(piece_index_to_move, self.dice_value)
            self.canvas.unbind("<Button-1>")
            self.next_turn()
        else:
            self.next_turn()

    def get_movable_pieces(self):
        movable_pieces = []
        for i, pos in enumerate(self.piece_positions[self.current_player]):
            if pos != 'home' and pos != 'final':
                movable_pieces.append(i)
            elif pos == 'home' and self.dice_value == 6:
                movable_pieces.append(i)
        return movable_pieces

    def move_out_of_home(self):
        piece_index = self.piece_positions[self.current_player].index('home')
        start_pos_index = self.get_start_pos_index(self.current_player)
        self.piece_positions[self.current_player][piece_index] = self.path[start_pos_index]
        self.draw_pieces()
        self.next_turn()

    def move_piece(self, piece_index, steps):
        current_pos = self.piece_positions[self.current_player][piece_index]
        if current_pos == 'home' or current_pos == 'final':
            return

        try:
            current_path_index = self.path.index(current_pos)
        except ValueError:
            # Piece is in a home path
            # This part is for a full game, simplifying for this example
            return

        new_path_index = current_path_index + steps
        if new_path_index < len(self.path):
            self.piece_positions[self.current_player][piece_index] = self.path[new_path_index]
        else:
            # Piece has completed the path
            self.piece_positions[self.current_player][piece_index] = 'final'

        self.draw_pieces()

    def ai_move(self):
        time.sleep(1)  # AI ko sochne ka time do
        movable_pieces = self.get_movable_pieces()

        if not movable_pieces:
            self.next_turn()
            return

        # AI logic: pehla movable piece chalo
        piece_index_to_move = movable_pieces[0]
        self.move_piece(piece_index_to_move, self.dice_value)
        self.next_turn()

    def get_start_pos_index(self, player):
        start_indices = {'red': 0, 'green': 13, 'yellow': 26, 'blue': 39}
        return start_indices[self.player_colors[player]]

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]
        self.turn_label.config(text=f"{self.current_player}'s turn.")

        if self.is_ai_enabled and self.current_player == "AI Player":
            self.master.after(1000, self.roll_dice)


class LudoLobby:
    def __init__(self, master):
        self.master = master
        self.master.title("Ludo Game - Lobby")

        self.lobby_frame = tk.Frame(master)
        self.lobby_frame.pack()

        self.label = tk.Label(self.lobby_frame, text="Select Game Mode", font=("Arial", 20))
        self.label.pack(pady=20)

        self.pvp_button = tk.Button(self.lobby_frame, text="Player vs Player", font=("Arial", 16),
                                    command=self.start_pvp)
        self.pvp_button.pack(pady=10)

        self.pva_button = tk.Button(self.lobby_frame, text="Player vs AI", font=("Arial", 16), command=self.start_pva)
        self.pva_button.pack(pady=10)

    def start_pvp(self):
        self.lobby_frame.destroy()
        LudoGame(self.master, ['Player 1', 'Player 2'], False)

    def start_pva(self):
        self.lobby_frame.destroy()
        LudoGame(self.master, ['You', 'AI Player'], True)


if __name__ == "__main__":
    root = tk.Tk()
    lobby = LudoLobby(root)
    root.mainloop()

import pygame
import sys
import time

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kids Auto Learning")

# Set fonts
font = pygame.font.SysFont("Arial", 200, bold=True)
title_font = pygame.font.SysFont("Arial", 50, bold=True)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Learning content
english_alphabets = [chr(i) for i in range(ord('A'), ord('Z')+1)]
numbers = [str(i) for i in range(1, 101)]
hindi_letters = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ']

# Function to display text
def display_centered(text, title="Learning...", delay=2):
    screen.fill(WHITE)
    # Title
    title_surface = title_font.render(title, True, BLACK)
    title_rect = title_surface.get_rect(center=(WIDTH//2, 60))
    screen.blit(title_surface, title_rect)

    # Main Text
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(text_surface, text_rect)

    pygame.display.update()
    time.sleep(delay)

# Function to run auto learning mode
def auto_learn(content_list, title="Learning...", delay=2):
    for item in content_list:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        display_centered(item, title, delay)

# Main Menu
def main_menu():
    menu_items = ["Learn English Alphabets", "Learn Numbers", "Learn Hindi Letters", "Exit"]
    selected = 0
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        title_surface = title_font.render("Kids Learning Menu", True, BLACK)
        screen.blit(title_surface, (WIDTH//2 - 180, 50))

        for i, item in enumerate(menu_items):
            color = (0, 0, 255) if i == selected else (0, 0, 0)
            text_surface = title_font.render(item, True, color)
            screen.blit(text_surface, (WIDTH//2 - 200, 150 + i * 60))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_items)
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        auto_learn(english_alphabets, "English A-Z")
                    elif selected == 1:
                        auto_learn(numbers, "Numbers 1-100")
                    elif selected == 2:
                        auto_learn(hindi_letters, "Hindi Letters")
                    elif selected == 3:
                        pygame.quit()
                        sys.exit()

        clock.tick(30)

# Run the app
if __name__ == "__main__":
    main_menu()

