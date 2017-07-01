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

from os import makedirs, path
from shutil import rmtree

from .helpers import (convert_JSON_to_dict, execute_save_cmd, format_list,
                      read_file, save_dict_to_JSON)


class Core(object):
    """Brain of the program. Get the list of contributor(s) from a Github project"""

    def __init__(self, repository,  **args):
        splited = repository.split('/')
        (self.username, self.repo) = (splited[0], splited[1])

        self.API_BASE_URL = 'https://api.github.com/repos/'
        self.REPO_URL = self.API_BASE_URL + \
            self.username + '/' + self.repo + '/contributors'

        self.OUTPUT_DESTINATION = './contributors.json'
        self.QUERY_OUTPUT_DESTINATION = './query_results/'
        self.FULL_INFO_OUTPUT = self.QUERY_OUTPUT_DESTINATION + 'details_contributors.json'

        self.COMMAND = 'curl ' + self.REPO_URL

        optional_arguments = {
            "show_dict": False,
            "show_list": False,
            "save_in_file": True,
            "excluded": ['gitter-badger']
        }

        for (arg, default) in optional_arguments.items():
            setattr(self, arg, args.get(arg, default))

        self.contributors_info = []
        self.final_list_contributors = []

    def get_api_information(self):
        """Get the list of contributor(s) informations from Github API"""

        execute_save_cmd(self.COMMAND, self.FULL_INFO_OUTPUT)

        content = read_file(self.FULL_INFO_OUTPUT)
        data = convert_JSON_to_dict(content)

        if 'message' in data:
            return data['message']
        self.contributors_info = data
        return True

    def format_result(self):
        """Return a formated list of formated dict"""
        if self.show_list and self.show_dict or self.show_dict:
            self.result = {'contributors': format_list(
                self.final_list_contributors)}
        else:
            self.result = format_list(self.final_list_contributors)

    def save_dict(self):
        """Save result into a file"""

        if self.save_in_file and isinstance(self.result, dict):
            save_dict_to_JSON(self.result, self.OUTPUT_DESTINATION)
            return True
        return False

    def get_login_of_contributors(self):
        """Get the logins from self.get_api_information results"""

        if self.contributors_info != []:
            for item in self.contributors_info:
                if item['login'] not in self.excluded:
                    self.final_list_contributors.append(item['login'])

            self.format_result()

            return True
        return False

    def get(self):
        """Get contributors_info, then get the list of contributor(s) nickname(s).
        In between, we return an error in case we can't get usable informations
        """

        if not path.exists(self.QUERY_OUTPUT_DESTINATION):
            makedirs(self.QUERY_OUTPUT_DESTINATION)

        funilrys = self.get_api_information()

        if funilrys:
            if self.get_login_of_contributors():
                rmtree(self.QUERY_OUTPUT_DESTINATION)

                if self.save_dict() and self.show_list == False and self.show_dict == False:
                    print('You can find you list of contributor(s) into %s =)' %
                          path.abspath(self.OUTPUT_DESTINATION))
                    exit()
                else:
                    return self.result
        rmtree(self.QUERY_OUTPUT_DESTINATION)

        print(funilrys)
        exit()
