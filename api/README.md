<div class="head">
  <h3 align="center">
    <p>&nbsp;</p>
    <a href="https://github.com/Cloud11665/sabat.dev#----------------">
      <img src="https://raw.githubusercontent.com/Cloud11665/sabat.dev/master/images/banner.png" height="120" alt="SABAT.DEV >>">
    <p>&nbsp;</p>
   </h3>
  <p align="center">
    <a href="https://sabat.dev" target="_blank">
      <img src="https://img.shields.io/website?down_color=critical&down_message=offline&logo=icloud&logoColor=ffffff&up_color=45966E&up_message=online&url=https%3A%2F%2Fsabat.dev" alt="website status" height="23">
    </a>
    <a href="https://github.com/Cloud11665/sabat.dev/actions?query=workflow%3Abuild">
      <img src="https://img.shields.io/github/workflow/status/Cloud11665/sabat.dev/build?color=45966E&label=build&logo=python&logoColor=ffffff" alt="build status" height="23">
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
        <a href="https://github.com/Cloud11665/sabat.dev/blob/master/LICENSE">[License]</a>
        &nbsp;
        <a href="https://github.com/Cloud11665/sabat.dev#contributing">[Contributing]</a>
      </p>
    </h3>
  <h2></h2>
  <p>&nbsp;</p>
  <p align="center">
    <strong>
      SABAT.DEV API documentation
    </strong>
  </p>
  <p align="center">
    <a href="https://github.com/Cloud11665/sabat.dev/tree/master/api">
      <img src="https://img.shields.io/badge/API%20version-1.3.2-EF30A1" width="150px">
    </a>
  </p>
  <p>&nbsp;</p>
  <p>&nbsp;</p>
</div>

## Overview
### [[sabat.dev/api](https://sabat.dev/api)] - main api endpoint *(as of current version)*
<p>&nbsp;</p>

This is the official [sabat.dev](https://sabat.dev) api documentation. This api will always remain open and will not require stupid auth keys.
It mostly consists of RESTful endpoints that i use for my personal / school projects.

## Timetable

##### Overview
Get the timetable of `class` for this week.

###### URL
    /api/tta

###### URL parameters
- `c` - class identifier (example of id: 3F) **(required)**
- `o` - negative offset in weeks from the current date **(optional)**
- `dbg` - debug flag **(optional, not implemented)**

###### Response
A JSON object containing the `resp` list as well as the `success` flag.

`resp` is an array of length 5, where indicies are mapped to days of the week (mon - 0; fri - 4)
`resp[n]` is an array of arrays containing `lesson` objects.
Each `lesson` has its `"classroom", "color", "date", "day_index", "duration", "subject", "teacher","group", "time_index"`

when number of elements in `resp[n][k]` is greater than one, it indicates that there are multiple lessons happening at once.
```json
{
  "success": true,
  "resp": [
    [[{...}],[{...},{...}]],
    [[{...}],[{...}]],
    [[{...}]],
    [[{...}]],
    [[{...}],[{...}],[{...}]]
  ]
}
```

## Substitutions

##### Overview
Get the timetable of `class` for this week.

###### URL
    /api/sub
###### URL parameters
- `c` - class identifier (example of id: 3F) **(required)**
- `o` - offset in days from the current date **(optional)**
- `dbg` - debug flag **(optional, not implemented)**

###### Response
A JSON object containing the `resp` list as well as the `success` flag.

`resp` is an array of arrays, where `resp[n][0]` is the time index and `resp[n][1]` is the included status / message.
###### Note
The changes are already included in the `/api/tta` endpoint and their only purpose is to be printed out in its native format e.g. `"${resp[n][0]}, ${resp[n][1]}"`.

```json
{
	"success": true,
	"resp": [
		[
			"(0)","Religia - Anulowano"
		]
	]
}
```

## Class list

##### Overview
Get a list of class identifiers.

###### URL
    /api/cla

###### Response
A JSON object containing the `resp` list as well as the `success` flag.
`resp` is an array of strings representing the individual class id.

```json
{
  "success": true,
  "resp": [
    "1A","1B","1C",...,"2BG","2CG",...,"3D","3F","3G"
  ]
}
```

## Time map

##### Overview
Get the `time_index` mapping to 24h format.

###### URL
    /api/tim

###### Response
A JSON object containing the `resp` object of objects as well as the `success` flag.
`resp` is an object of time indicies and their corresponding beggining and ending times.

```json
{
  "success":true,
  "resp": {
    "0": {"begin":"07:10","end":"07:55"},
    "1": {"begin":"08:00","end":"08:45"},
    "2": {"begin":"09:00","end":"09:45"},
    ...
    "10":{"begin":"16:30","end":"17:15"}
  }
}
```

