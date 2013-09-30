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

__author__      = "Alex Gainer (superrawr@gmail.com)"
__copyright__   = "Copyright 2013, superrawr"

import random

from super_view import SuperHandler
from super_view import SuperJaxHandler
from word_dictionary import WordDictionary


class AddView(SuperHandler):
    """View for the add page."""
    template_name = 'wordplay/add.html'

    def get(self, request, *args, **kwargs):
        template_values = {
            'page_title': 'Add a New Word',
            'add': True,
            'new_word': kwargs.get('new_word'),
            'words_definitions': WordDictionary().Load().word_dictionary
        }
        return self.RenderTemplate(template_values)

    def post(self, request):
        WordDictionary().Load().AddWord(request.POST['word'], request.POST['definition'])
        print request.POST
        return self.get(None, new_word=request.POST['word'])


class QuizView(SuperHandler):
    """View for the quiz page."""
    template_name = 'wordplay/quiz.html'

    def get(self, request, *args, **kwargs):
        words_definitions = WordDictionary().Load().word_dictionary.items()
        word_definition = random.choice(words_definitions)
        word, definition = word_definition
        template_values = {
            'page_title': 'Quiz',
            'quiz': True,
            'word': word,
            'definition': definition
        }
        return self.RenderTemplate(template_values)


class WordJaxView(SuperJaxHandler):
    """Deletes word from word dictionary."""
    def post(self, request):
        WordDictionary().Load().DeleteWord(request.POST['word'])
        return self.Respond({})