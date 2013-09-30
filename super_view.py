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
__copyright__   = "Copyright 2013, Superrawr"

import json
from django.views.generic.base import TemplateView
from django.http import HttpResponse


class SuperHandler(TemplateView):
    """Super class handler for non-ajax responses to the client."""

    def RenderTemplate(self, template_values):
        """Renders html interpolated with tv template values dictionary.

        Args:
          tn: String path name of the HTML template file.
          tv: Dictionary of template values to be interpolated into the
            HTML template provided in tn.
        """
        return self.render_to_response(template_values)


class SuperJaxHandler(TemplateView):
    """Super class handler for ajax responses to the client."""

    def Respond(self, template_to_json):
        """Responds to the client with a json object created from template_to_json.

        Args:
          template_to_json: Dictionary to be converted into json object.
        """
        return HttpResponse(json.dumps(template_to_json), mimetype="application/json")
