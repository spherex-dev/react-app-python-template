# Starter React Template with a Python Backend

This starter template combines a react single page application with a python sanic backend. Modifications have been added to the sanic backend to allow cors from any host to interact with the single page app during the development phase.

If you wish to see animated installation, testing and running of this application. Please see [this](https://www.spherex.dev/how-to-use-react-with-a-python-backend/) post at our development blog.

## Prerequisites

To use this template, ensure that the following commands are available in your environment

- yarn or npm (if npm is used, modify `setup.sh` to use the `npm` command instead of yarn)
- virtualenv for installation of a python virtual environment

## Installation

Installation of this application can be done using the `setup.sh` script provided in the root of this project.

The required node packages will be installed will be installed using `yarn`. However if you prefer to use `npm` please modify `setup.sh` script to use `npm` instead.

the `backend` directory will contain the python code which runs a [sanic](https://sanic.dev/) server to run the backend service. Sanic is very similar to flask, however is based on async code which uses the `uvloop` which is very performant.

## Demo Code

Before running this application, ensure that the backend is running by calling `yarn start-sanic-test`. The test version of the sanic server that allows permissive `CORS` access will allow your local running instance of the react page to communicate with the backend server. The backend server will also have an `auto_reload` flag set when running in testing mode will whill allow for rapid development.

The `App.js` for this demo application is modified to perform a fetch from the backend and will perform a fetch against the `api/hello/hello` url to show that data is being fetched. You should see `Greeting from backend is world` when the fetch is successful.

## Testing

`yarn test` has been augmentedto call `yarn start-sanic-test` then run jest and then terminate the `sanic` server once tests are complete. the `react-scripts test` command has been also been updated to proxy test requests to `http://localhost:8000`

## Modifications

The following block of code has been removed from `package.json` as this causes problems when making changes to the javascript code with the following error ` "Failed to load config "react-app" to extend from."`.

```
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
```
