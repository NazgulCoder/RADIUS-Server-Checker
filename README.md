# RADIUS Server Checker
Originally developed for personal use in testing RADIUS connections between a MikroTik router and a Windows Server RADIUS setup, this tool simplifies the configuration testing process. While initially tailored for MikroTik and Windows Server, it may prove useful for testing connections with other RADIUS servers as well.


Supported RADIUS authentication methods:
- CHAP: **WORKING** *(tested with a MikroTik and Windows RADIUS Server)*
- PAP: **NOT TESTED**
- MSCHAPv2: **TO BE IMPLEMENTED**


Supported features:
- CHAP ID
- CHAP challenge
- Called Station ID
- NAS Port Type


Credits:
- Me
- gustaebel for his <a href="https://gist.github.com/gustaebel/b58e887ba93a4d0eba102dae871e11af" target="_blank">poll.py</a> windows implementation
- *feel free to contribute to implement more features*



## LICENSE



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

MIT License

Copyright (c) [2024] [NazgulCoder]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
