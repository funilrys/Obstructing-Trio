# Obstructing Trio - Python module/library for saving the list of contributors of a given public Github repository into a JSON file.
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

from distutils.core import setup

setup(
    name='obstructing_trio',
    version="1.0.1",
    description='Python module/library for saving the list of contributors of a given public Github project into JSON file.',
    long_description=open('README').read(),
    author='funilrys',
    author_email='contact@funilrys.com',
    license='MIT https://opensource.org/licenses/MIT',
    url='https://github.com/funilrys/Obstructing-Trio',
    platforms=['any'],
    packages=['obstructing_trio'],
    keywords=['Python', 'JSON', 'github', 'contributor', 'conributors'],
    classifiers=[
        'Environment :: Console',
        'Topic :: Internet',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
)

'''
test_suite='testsuite',
entry_points="""
[console_scripts]
cmd = package:main
""",
'''
