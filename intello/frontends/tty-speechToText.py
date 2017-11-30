import random
import sys
import time

import frontend
import pyttsx
import speech_recognition as sr



# This string needs to be defined for each front end.  It should
# contain the name of the front-end class defined in this module.
frontEndClass = "FrontEndTTY"

# List the default values for the INI file.  This should be a dictionary
# with keys of the form "<fe>.<entry>", where <fe> is the name of the
# frontend (e.g. "aim", "msn"), and entry is the name of the configuration
# variable (e.g. "username", "password").  All values should be strings.
#
# Each frontend must define an "active" entry, whose possible values
# are "yes" and "no", which indicates whether that frontend should
# be activated.
configDefaults = {
    "tty.active":       "yes"
    }

class FrontEndTTY(frontend.IFrontEnd):
    """
    A butt-simple class demonstrating the bare minimum needed to
    implement a new front-end for Howie.
    """    
    def go(self):
        self._sessionID = "localhost@TTY"
        import intello.core
        intello.core.kernel.setPredicate("secure", "yes", self._sessionID)
        #Speech-To-Text
        r = sr.Recognizer()
		#Text-To-Speech 
        engine = pyttsx.init()
        rate = engine.getProperty('rate')
        engine.setProperty('rate', rate-30)
        while True:
            with sr.Microphone() as source:
                  print(">>>"),
                  audio = r.listen(source)
                  #input = raw_input(">>> ")
                  input = r.recognize_google(audio)
                  print input
            response = self.submit(input, self._sessionID)
            self.display(response, self._sessionID)
            engine.say(response)
            engine.runAndWait()
            #time.sleep(random.random() * 4)
            


    def display(self, output, user):
        print output
