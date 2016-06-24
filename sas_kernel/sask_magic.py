#
# Copyright SAS Institute
#
#  Licensed under the Apache License, Version 2.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from __future__ import print_function
from metakernel import Magic
from IPython.display import HTML

class SASKMagic(Magic):

    def __init__(self, *args, **kwargs):
        super(SASKMagic, self).__init__(*args, **kwargs)

    def line_prompt4var(self, code):
        """
        %prompt4var CODE - display code as HTML
        This line magic will send the CODE to the browser as
        HTML.
        Example:
            %html <u>This is underlined!</u>
        """
        html = HTML(code)
        self.kernel.Display(html)

    def cell_prompt4var(self):
        """
        %%prompt4var - display contents of cell as HTML
        This cell magic will send the cell to the browser as
        HTML.
        Example:
            %%html

            <script src="..."></script>
            <div>Contents of div tag</div>
        """
        html = HTML(self.code)
        self.kernel.Display(html)
        self.evaluate = False


def register_magics(kernel):
    kernel.register_magics(SASKMagic)