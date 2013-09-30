"""
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
import cPickle as pickle
import os


class WordDictionary(object):
    """Word dictionary utilities for pickling GRE words."""
    _PICKLE_PATH = 'data/word_dictionary.pkl'

    def __init__(self):
        self.word_dictionary = {}
        self.display_name = 'Super Dictionary'

    def Write(self):
        """Blindly writes to pickle file. Writes object as __dict__."""
        try:
            if os.path.isfile(self._PICKLE_PATH):
                pickle.dump(self.__dict__, file(self._PICKLE_PATH, 'wb'))
            else:
                print self._PICKLE_PATH
        except IOError:
            print "I could not find pickle:{0}".format(self._PICKLE_PATH)
        return self

    def Load(self):
        """Loads the pickle file and returns the object."""
        try:
            if os.path.isfile(self._PICKLE_PATH):
                self.__dict__ = pickle.load(file(self._PICKLE_PATH, 'r+b'))
        except IOError:
            print "I could not find pickle:{0}".format(self._PICKLE_PATH)
        return self

    def AddWord(self, word, definition):
        """Adds a word and definition to the word_dictionary."""
        self.word_dictionary[word] = definition
        self.Write()
        return self

    def DeleteWord(self, word):
        """Removes a word from the word_dictionary."""
        if word in self.word_dictionary:
            del self.word_dictionary[word]
            self.Write()
        return self