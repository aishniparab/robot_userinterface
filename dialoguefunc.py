from gtts import gTTS
import playsound
import os

# The following classes are grouped on the basis of the nature of the dialogue.
class Introduction(object):
        print "in intro"
        @classmethod
        def hello(cls):
            print "in hello"
            hello = ("""Hello, my name is Luna. What's your name?""")
            tts = gTTS(text=hello, lang='en-us')
            path = os.path.join(os.getcwd(), "1a_hello.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def nice2meet(cls):
            nice2meet = ("""Nice to meet you! I hope I can be of some assistance today.
             As a robot, I don't need to sleep but I do need to charge!
             You, on the other hand, need to sleep quite a bit.
             My job as a sleep robot is to assess sleeping habits, and to assist in improving quality of sleep.
             As you might be aware, sleep deprivation is a big issue on college campuses.
             .
             A recent study found that over half of college students experience problems with sleep deprivation.
             I'm here to try and lower that number by giving students such as yourself some tips and tricks for developing healthy sleeping habits.
             First, I'm going to ask you a series of questions about your particular habits.

            Are you ready??""")
            tts = gTTS(text=nice2meet, lang='en-us')
            path = os.path.join(os.getcwd(), "1b_nice2meet.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

class SleepDiscussion(object):

        @classmethod
        def whatSleepTime(cls):
            whatSleepTime = ("""Let's get started!.
            What time do you usually start trying to fall asleep?""")
            tts = gTTS(text=whatSleepTime, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"2a_whatSleepTime.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def whatWakeTime(cls):
            whatWakeTime = ("""Good.
                Now, what time do you usually wake up in the morning?""")
            tts = gTTS(text=whatWakeTime, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"2b_whatWakeTime.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def howOftenSleepTrouble(cls):
            howOftenSleepTrouble = ("""Okay.
                How often do you have trouble falling asleep at night?""")
            tts = gTTS(text=howOftenSleepTrouble, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"2c_howOftenSleepTrouble.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def isRestedFeeling(cls):
            isRestedFeeling = ("""Do you usually feel well-rested when you wake up in the morning?""")
            tts = gTTS(text=isRestedFeeling, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"2d_isRestedFeeling.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def normal2wakeNight(cls):
            normal2wakeNight = ("""Thanks for sharing.
                I just have a few more questions.
                Is it normal for you to wake up throughout the night?""")
            tts = gTTS(text=normal2wakeNight, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"2e_normal2wakeNight.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def daySleepy(cls):
            daySleepy = ("""Okay.
                Do you experience any sleepiness throughout the day?""")
            tts = gTTS(text=daySleepy, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"2f_daySleepy.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def howOftenNap(cls):
            howOftenNap = ("""Good.
                How often do you nap during the week?""")
            tts = gTTS(text=howOftenNap, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"2g_howOftenNap.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def sleepDuringTask(cls):
            sleepDuringTask = ("""Great.
                Have you ever fallen asleep while attempting to complete a task, such as your homework?""")
            tts = gTTS(text=sleepDuringTask, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"2h_sleepDuringTask.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def feedbackTips(cls):
            feedbackTips = mod2c9 = ("""Thank you for sharing!
                Based on your answers from both the pre-study questionnaire and from our discussion,
                I believe that you could benefit from a few tips and tricks I've learned that enable healthy sleeping habits.
                There are flyers for a local sleep clinic to the left of the door where you entered.
                If you want, you may take one on your way out.
                I also know a few exercises that have been shown to assist getting a better night's sleep, such as colouring, listening to relaxing sounds, and reading poetry.
                I would love to show you if you are interested.
                Would you like to try one of them out?""")
            tts = gTTS(text=feedbackTips, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"2i_feedbackTips.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

class SleepExercises(object):

        @classmethod
        def mindfulBreathing(cls):
            mindfulBreathing = ("""Perfect! Today we are going to practice mindful breathing exercises.
            Many people have a hard time falling asleep, and staying asleep,
            because of overwhelming thoughts during bedtime that keep the brain anxious and busy
            instead of relaxed and calm.
            Practicing mindful breathing before going to sleep can be a great way to soothe an overactive, worried mind and to help unwind from an eventful day.
            I will now lead you in a mindful breathing exercise that you can practice before bedtime,
            or anytime you are feeling stress or anxiety.
            Are you ready to begin??""")
            tts = gTTS(text=mindfulBreathing, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3a_mindfulBreathing.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def submindfulBreathing(cls):
            submindfulBreathing = ("""Great.
            First, I would like you to close your eyes and take a moment to get comfortable.
            Try to mentally release tension from your muscles.
            Notice places in your body where you may be storing more tension, and deeply relax into those places.
            Focus your attention on your breathing.
            Try to slow down your breathing, relaxing deeper into your body with each breath.""")
            tts = gTTS(text=submindfulBreathing, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3b_submindfulBreathing.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def abdominalBreathing(cls):
            abdominalBreathing = ("""Wonderful.
            Now, keep breathing deeply and slowly while placing one hand on your stomach and one on your chest.
            See if they both rise when you breathe in or just one of them rises.
            Try to breathe in such a way that the hand on your stomach rises, and the hand on your chest only rises a little.
            This is called abdominal breathing and is what you should ideally try to do.
            You may find it tricky at first, but keep practicing and it will come in time.""")
            tts = gTTS(text=abdominalBreathing, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3c_abdominalBreathing.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def timedBreathing(cls):
            timedBreathing = ("""Perfect. Now, we are going to work with timing.
            I would like you to breath in with your nose for 5 seconds, hold the breath for 5 seconds,
            then breath out through your mouth for 5 seconds.
            You will do this for 3 minutes and I will count for you.
            We will now begin""")
            tts = gTTS(text=timedBreathing, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3d_timedBreathing.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def countBreathing(cls):
            countBreathing = ("""
                In...2...3...4...5
                Hold...2...3...4...5
                Out...2...3...4...5

                In...2...3...4...5
                Hold...2...3...4...5
                Out...2...3...4...5

                In...2...3...4...5
                Hold...2...3...4...5
                Out...2...3...4...5
            .""")
            tts = gTTS(text=countBreathing, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3e_countBreathing.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def thankParticipant(cls):
            thankParticipant = ("""You may now open your eyes.
                Thank you so much for participating.
                The session is now complete.""")
            tts = gTTS(text=thankParticipant, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3f_thankParticipant.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def colouringTask(cls):
            colouringTask = ("""Excellent! Today we are going to practice a coloring task.
                Coloring can be beneficial for adults in many ways.
                Research shows it may lower stress, aid relaxation, boost creativity,
                and even help improve sleep and attention spans.
                Coloring can be a great replacement for the use of electronics before bed,
                as electronics have been shown to disrupt circadian rhythms, reduce the sleep hormone melatonin,
                and to contribute to insomnia.""")
            tts = gTTS(text=colouringTask, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3g_colouringTask.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def colouringDirections(cls):
            colouringDirections = ("""On the table to my right we have a selection of coloring sheets to chose from,
                as well as some colored pencils.
                If you like, you can try out some coloring right now, and see if it relaxes you.
                Would you like to try some coloring today?""")
            tts = gTTS(text=colouringDirections, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3h_colouringDirections.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def beginColouringCue(cls):
            beginColouringCue = ("""Great. You may begin coloring when you are ready.""")
            tts = gTTS(text=beginColouringCue, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3i_beginColouringCue.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def stopColouringCue(cls):
            stopColouringCue = ("""You may now stop coloring.
                Thank you so much for participating.
                The session is now complete.""")
            tts = gTTS(text=stopColouringCue, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3j_stopColouringCue.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def listenMusicTip(cls):
            listenMusicTip = ("""Excellent!
                One helpful tip for getting a better night's sleep is to listen to certain relaxing sounds.
                The sound of relaxing music distracts your mind and induces a physical state of calmness.
                Relaxing music reduces the activity of the nervous system resulting in a decrease in anxiety, heart rate,
                lower breathing and lower blood pressure much like a state of meditation.
                Importantly, relaxing music has been found to reduce the stress hormone noradrenalin which is associated with insomnia.
                White noise combines all noise frequencies and can mask other sounds, and it sometimes helps treat insomnia.
                Natural noises are less likely to annoy us than some other sounds because they usually include fluctuations in amplitude and frequency.
                Ocean waves, rainforest animals, and thunderstorms can all be pleasant sounds to fall asleep to.
                Slow-paced music without lyrics such as jazz, classical and contemporary can be relaxing to many people.
                Some people even find human voices soothing to listen to, and may choose a relaxing guided meditation or spoken poetry to fall asleep to.
                Here I have a selection of songs and noises that could possibly fit in """)
            tts = gTTS(text=listenMusicTip, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3k_listenMusicTip.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)

        @classmethod
        def readingVsPhoneTip(cls):
            readingVsPhoneTip = ("""Excellent! One helpful tip for getting a better night's sleep
                is to replace stimulating activities such as playing on your phone or watching something on your laptop with reading a book.
                Sleep studies have shown that reading each night can make it easier to fall asleep,
                as well as to initiate a simple routine that tells your body it is time for bed,
                and to activate and maintain deep sleep.
                Deep sleep reduces activity in parts of the brain that control emotions, decision-making processes, and social interactions,
                allowing for optimal emotional and social functioning while you are awake.
                Deep sleep is also necessary for your nervous systems to work properly,
                allowing for a healthy and alert body and mind during the day.
                You can train yourself to associate reading with sleep and make it part of your bedtime ritual by reading for six minutes or more each night before sleep.
                Here we have some reading materials that may put you in a calm headspace.
                Would you like to take a few minutes to read and relax?""")
            tts = gTTS(text=readingVsPhoneTip, lang='en-us')
            #tts.save("/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3")
            #playsound.playsound('/Users/nicholassanter/Desktop/CODING/WizardInterface/mod2c1.mp3', True)
            path = os.path.join(os.getcwd(),"3l_readingVsPhoneTip.mp3")
            (filepath, filename) = os.path.split(path)
            tts.save(path)
            playsound.playsound(path, True)
