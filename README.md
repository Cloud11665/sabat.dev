<div class="head">
	<h3 align="center">
		<p>&nbsp;</p>
		<a href="./README.md">
			<img src="./static/icon/banner.png" height="120" alt="SABAT.DEV >>">
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
			<a href="./README.md#installation">[Installation]</a>
			&nbsp;
			<a href="./README.md#deployment">[Deployment]</a>
			&nbsp;
			<a href="./README.md#testing">[Testing]</a>
			&nbsp;
			<a href="./api/README.md">[API documentation]</a>
			&nbsp;
			<a href="./README.md#contributing">[Contributing]</a>
			&nbsp;
			<a href="./README.md#license">[License]</a>
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
python -m gunicorn main:app
```
When running in the background.
```
nohup python -m gunicorn main:app </dev/null >/dev/null 2>&1&
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
2. Create your feature branch ( `git checkout -b feature/foobar` )
3. Commit your changes &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ( `git commit -am 'Add some foobar'` )
4. Push to the branch &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ( `git push origin feature/foobar` )
5. Create a new Pull Request
&nbsp;

## License
[![GNU AGPLv3 Image](https://www.gnu.org/graphics/agplv3-with-text-162x68.png)](https://www.gnu.org/licenses/agpl-3.0.en.html)

sabat.dev is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms and conditions of GNU General Public License