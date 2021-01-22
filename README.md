<div class="head">
  <h3 align="center">
    <p>&nbsp;</p>
    <a href="https://github.com/Cloud11665/sabat.dev#----------------">
      <img src="https://raw.githubusercontent.com/Cloud11665/sabat.dev/master/images/head.png" height="120" alt="SABAT.DEV >>">
    <p>&nbsp;</p>
   </h3>
  <p align="center">
    <a href="https://sabat.dev" target="_blank">
      <img src="https://img.shields.io/website?down_color=critical&down_message=offline&logo=icloud&logoColor=ffffff&up_color=45966E&up_message=online&url=https%3A%2F%2Fsabat.dev" alt="website status" height="23">
    </a>
    <a href="https://github.com/Cloud11665/sabat.dev/actions?query=workflow%3Abuild">
      <img src="https://img.shields.io/github/workflow/status/Cloud11665/sabat.dev/build?color=45966E&label=build&logo=python&logoColor=ffffff" alt="build status" height="23">
    </a>
    <a href="https://github.com/Cloud11665/sabat.dev/actions?query=workflow%3AAPI">
      <img src="https://img.shields.io/github/workflow/status/Cloud11665/sabat.dev/test?color=45966E&label=API&logo=flask" alt="api status" height="23">
    </a>
  </p>
  <p align="center">
    <a href="https://www.codefactor.io/repository/github/cloud11665/sabat.dev">
      <img src="https://img.shields.io/codefactor/grade/github/Cloud11665/sabat.dev?color=45966E&logo=CodeFactor&logoColor=ffffff" alt="code quality" height="23">
    </a>
  </p>
  <h2></h2>
  <h3>
    <p align="center">
      <a href="https://github.com/Cloud11665/sabat.dev#installation">[Installation]</a>
      &nbsp;
      <a href="https://github.com/Cloud11665/sabat.dev#deployment">[Deployment]</a>
      &nbsp;
      <a href="https://github.com/Cloud11665/sabat.dev#testing">[Testing]</a>
      &nbsp;
      <a href="https://github.com/Cloud11665/sabat.dev/blob/master/api/README.md">[API documentation]</a>
      &nbsp;
      <a href="https://github.com/Cloud11665/sabat.dev#contributing">[Contributing]</a>
      &nbsp;
      <a href="https://github.com/Cloud11665/sabat.dev#license">[License]</a>
    </p>
  </h3>
  <h2></h2>
  <p>&nbsp;</p>
  <p align="center">
    <strong>
      My personal website for hosting my projects <i>(mostly API's)</i> and messing with front-end
    </strong>
  </p>
  <p>&nbsp;</p>
  <p>&nbsp;</p>
</div>
<!--Markdown only from now on ((`with some exceptions`))-->
<!--
<p align="center">
  <a href="https://github.com/Cloud11665/sabat.dev/tree/master/api">
    <img src="https://img.shields.io/badge/API%20version-1.1-informational">
  </a>
  <a href="https://github.com/Cloud11665/sabat.dev/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/Cloud11665/sabat.dev">
  </a>
  <a href="https://www.codefactor.io/repository/github/cloud11665/sabat.dev">
    <img src="https://img.shields.io/codefactor/grade/github/Cloud11665/sabat.dev">
  </a>
  <a href="https://github.com/Cloud11665/sabat.dev/blob/master/Pipfile.lock">
    <img src="https://img.shields.io/github/pipenv/locked/python-version/Cloud11665/sabat.dev">
  </a>
</p>-->

## Installation
Using pip
```
git clone --depth=1 https://github.com/Cloud11665/sabat.dev
cd ./sabat.dev
python -m pip install -r ./requirements.txt
```
Using [pipenv](https://pipenv.pypa.io/en/latest)
```
git clone --depth=1 https://github.com/Cloud11665/sabat.dev
cd ./sabat.dev
pipenv install -r requirements.txt
```
&nbsp;  
## Deployment
> I use NGINX listening to port 5000 and gunicorn to serve the app.  

When running on something like [GNU screen](https://www.gnu.org/software/screen) or [tmux](https://github.com/tmux/tmux).

```
python -m gunicorn wsgi:app
```
When running in the background.
```
nohup python -m gunicorn --bind 127.0.0.1:5000 wsgi:app </dev/null >/dev/null 2>&1&
```
&nbsp;  
## Testing

To run the whole API test suite.
```
python -m pytest
```
To run a specific test.
```
python -m pytest ./tests/{testname}
```
&nbsp;  
## Contributing

1. [Fork](https://github.com/Cloud11665/sabat.dev/fork) this repo
2. Create your feature branch [`git checkout -b feature/foobar`]
3. Commit your changes &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [`git commit -am 'Add some foobar'`]
4. Push to the branch &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [`git push origin feature/foobar`]
5. Create a new Pull Request
&nbsp;  
## License

Distributed under the GNU AGPL license. See \[[LICENSE](https://github.com/Cloud11665/sabat.dev/blob/master/LICENSE)\]
