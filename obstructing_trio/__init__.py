# Obstructing Trio -  Python module/library for saving the list of contributors of a given public Github repository into a JSON file.
# Copyright (C) 2017  Funilrys - Nissar Chababy <contact at funilrys dot com>
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Original Version: https://github.com/funilrys/Obstructing-Trio

from .core import Core


def get(github_repository,  **args):
    """Send data and perform Core()"""

    return Core(github_repository, **args).get()
