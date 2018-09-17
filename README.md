# SENG2011

Using django, Vue.js, vuetifyjs

## Getting involve

### Set Your Working Branch

```bash
# create to your branch and working there
$ git checkout -b YOUR_BRANCH_NAME

# when you finshish, push the commits
$ git add && git commmit && git push
# IF you are push this branch FIRST TIME, you may use this line
$ git push --set-upstream origin YOUR_BRANCH_NAME
```

# Backend 


## One Script to Run the Backend 

Make sure you can use command line start python3, that's all we need. Then you can type:

```bash
./run.sh 
# if you meet some database conflict, you can jst type 
./run.sh -f 
```


# Frontend

## Install the System Environment

Install node.js: [Node Install Use Package Manager](https://nodejs.org/en/download/package-manager/)  

Install yarn: [Yarn Install Documents](https://yarnpkg.com/zh-Hans/docs/install#debian-stable)

## Install The Dependencies of Frontend

``` bash
# install dependencies
$ yarn install
```

## Run the Frontend

You also need another shell to keep fronend server running.

```bash
# serve with hot reload at localhost:8080
$ yarn serve
```

## Some Helpful Commands

```bash
# build for production with minification
$ yarn build

# build for production and view the bundle analyzer report
$ yarn build --report

# <!-- These two can not run, doesn't matter -->
# run unit tests
$ npm run unit

# run all tests
$ npm test
```

Also you may want to checkout
[vue](https://cn.vuejs.org/v2/guide/),
[vuex](https://vuex.vuejs.org/guide/),
[Vuetify](https://vuetifyjs.com/en/getting-started/quick-start),
[Vue-router](https://router.vuejs.org/),
[Axios](https://cn.vuejs.org/v2/cookbook/using-axios-to-consume-apis.html)
and [vue-loader](http://vuejs.github.io/vue-loader)..

## APIs Documents 

The api document is in api.http ; You need to run it via [vscode Rest Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)

You can install it via this command:

```bash
ext install humao.rest-client
```


## URLs

### Frondend

URL | Detail
:--- | :---
http://127.0.0.1:8080/ | Home Page
http://localhost:8080/post | Post Tasks Page

### Backend

URL | Detail
:--- | :---
http://127.0.0.1:8000/admin | Django admin
http://127.0.0.1:8000/api-v0/ | Index of party whip's api  
http://127.0.0.1:8000/ | Index of party whip's (Not active yet)