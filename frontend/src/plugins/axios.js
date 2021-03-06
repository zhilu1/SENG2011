"use strict";

import Vue from "vue";
import axios from "axios";
import { getToken } from "../utils/auth";

// Full config:  https://github.com/axios/axios#request-config
// axios.defaults.baseURL = process.env.baseURL || process.env.apiUrl || '';
axios.defaults.baseURL = "http://localhost:8000/api-v0/";
// axios.defaults.headers.common['Authorization'] = AUTH_TOKEN;
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

axios.defaults.headers.common["Authorization"] = getToken();
axios.defaults.headers.post["Content-Type"] = "application/json";

let config = {
  // The base url is the url of the api address
  // baseURL : "http://localhost:8000/api-v0/"
  // baseURL: process.env.baseURL || process.env.apiUrl || ""
  // timeout: 60 * 1000, // Timeout
  // withCredentials: true, // Check cross-site Access-Control
};

const _axios = axios.create(config);

_axios.interceptors.request.use(
  function(config) {
    // Do something before request is sent
    return config;
  },
  function(error) {
    // Do something with request error
    return Promise.reject(error);
  }
);

// Add a response interceptor
_axios.interceptors.response.use(
  function(response) {
    console.log("imhere");
    // Do something with response data
    return response;
  },
  function(error) {
    // Do something with response error
    console.log("imhere");
    return Promise.reject(error);
  }
);

// remove the compile error
// Plugin.install = function(Vue, options) {
Plugin.install = function(Vue) {
  Vue.axios = _axios;
  window.axios = _axios;
  Object.defineProperties(Vue.prototype, {
    axios: {
      get() {
        return _axios;
      }
    },
    $axios: {
      get() {
        return _axios;
      }
    }
  });
};

Vue.use(Plugin);

export default Plugin;
