<template>
  <div id="app">

    <div class="container-fluid my-5 pt-2" id="myLittleIMDB">
      <div class="row">
        <div class="col-lg"></div>

        <!-- Settings section  -->
        <div class="col-3">

          <div class="accordion" id="settingsWindow">
            <div class="card">
              <div class="card-header d-flex justify-content-between align-items-center" id="headingOne" data-toggle="collapse" data-target="#collapseOne">
                <h6 class="mb-0">Year</h6>
                <i class="fas fa-caret-down"></i>
              </div>

              <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#settingsWindow">
                <div class="card-body my-2">
                    <vue-slider v-model="year" ref="slider" :min="1950" :max="2018"></vue-slider>
                </div>
              </div>
            </div>


            <div class="card">
              <div class="card-header collapsed d-flex justify-content-between align-items-center" id="headingTwo" data-toggle="collapse" data-target="#collapseTwo">
                <h6 class="mb-0">Genre</h6>
                <i class="fas fa-caret-down"></i>
              </div>

              <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#settingsWindow">
                <div class="card-body">
                  <ul class="options-list">
                    <li v-for="genre in genres" class="form-group form-check">
                      <input type="checkbox"
                             :value="genre.id" class="form-check-input" :id="genre.name + ' - check'"
                             v-model="checkedGenres">
                      <label :for="genre.name + ' - check'" class="form-check-label">{{genre.name}}</label>
                    </li>
                  </ul>
                </div>
              </div>
            </div>


            <div class="card">

              <div class="card-header collapsed d-flex justify-content-between align-items-center" id="headingThree" data-toggle="collapse" data-target="#collapseThree">
                <h6 class="mb-0">Country</h6>
                <i class="fas fa-caret-down"></i>
              </div>

              <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#settingsWindow">
                <div class="card-body">

                  <ul class="options-list">
                    <li v-for="country in productionCountries" class="form-group form-check">
                      <input type="checkbox" class="form-check-input"
                             :id="country.name + ' - check'" :value="country.id" v-model="checkedCountries">
                      <label :for="country.name + ' - check'" class="form-check-label">{{country.name}}</label>
                    </li>
                  </ul>

                </div>
              </div>
            </div>

          </div>

          <button class="btn btn-block btn-outline-primary mt-2" @click="searchByGenreAndTitleAndCountry()">Filter films</button>

        </div>

        <!-- Main section -->
        <div class="col-6">
          <div class="container">

            <div class="input-group mb-3">
              <input type="text" class="form-control" placeholder="Search by title" @keypressed="searched=!searched" @change="getFilmsByTitle(searchTitle)" v-model="searchTitle">

              <div class="input-group-append">
                <button class="btn btn-secondary"> <i class="fas fa-search"></i></button>
              </div>
            </div>


            <div class="container-fluid">
              <div class="row">

                <div class="loader my-5 mx-auto" v-if="loading">
                </div>


                <div class="card-columns" v-else>
                  <div class="card w-100 bg-light" v-for="film in filmsList">
                    <ul class="badges-over-img">
                      <li class="badge badge-pill badge-success" title="Rating">{{film.vote_average}}</li>
                      <li class="badge badge-pill badge-info" title="Popularity">{{Math.round(film.popularity)}}</li>
                      <li class="badge badge-pill badge-warning" v-if="film.adult">18+</li>
                    </ul>
                    <img :src="getMediaPath(film.poster_path)" :alt="film.title + ' poster'" class="card-img-top img-fluid">

                    <div class="card-body">
                      <h5 class="card-title">{{film.title}}</h5>
                      <h6 class="card-subtitle mb-2 text-muted" v-if="film.original_title !== film.title">{{film.original_title}}</h6>
                    </div>
                </div>
                </div>
              </div>


              <div class="row mb-5" v-if="!loading && nextPageURL">
                <button @click="getNextPage(nextPageURL)" class="btn btn-block btn-outline-primary">More</button>
              </div>
            </div>


          </div>
        </div>

        <div class="col-lg"></div>
      </div>
    </div>


  </div>
</template>


<script>
import vueSlider from 'vue-slider-component';

const BASE_URL = '/api/';
const FILM_API_URL = BASE_URL + 'films/';
const GENRE_API_URL = BASE_URL + 'genres/';
const COUNTRIES_API_URL = BASE_URL + 'countries/';
const MAX_COUNTRIES_COUNT = 160;

const MEDIA_URL = 'http://image.tmdb.org/t/p/w185/';

export default {
  name: 'app',
  components: {
    vueSlider
  },
  data () {
    return {

      filmsList: [],
      genres: [],
      checkedGenres: [],

      productionCountries: [],
      checkedCountries: [],


      totalFilmCount: 0,

      searchTitle: '',
      searched: false,
      queryString: '',

      nextPageURL: '',
      prevPageURL: '',
      loading: true,
      year: [1950, 2018],
    }
  },
  methods: {
      getFilmsByTitle: function (searchTitle) {
        this.loading = true;
        let symbol = "?";

        if (this.queryString.length > 0){
          symbol = "&";
        }

        fetch(FILM_API_URL + this.queryString + symbol + 'search=' + searchTitle)
          .then((response) => {
            if (response.ok){
              return response.json().then((result) => {
                this.filmsList = result.results;
                this.searched = true;
                this.totalFilmCount = result.count;
                this.loading = false;
              })
            }

          }).catch((error) => {
          console.log(error)
        })
      },
      getNextPage: function (page_url) {
        this.loading = true;

        fetch(page_url)
          .then((response) => {
            if (response.ok) {
              return response.json().then((results) => {
                this.filmsList = results.results;
                this.nextPageURL = results.next;
                this.prevPageURL = results.prev;
                console.log(results);
                this.loading = false;
              });
            }
            console.log(response)
          })
          .catch((error) => {
            console.log(error)
          });
      },

      getMediaPath: function(posterPath){
        return MEDIA_URL + posterPath;
      },

      loadGenres: function () {
        fetch(GENRE_API_URL)
          .then((response) => {
            if (response.ok){
              response.json().then((result) => {
                this.genres = result.results;
                console.log(result);
                console.log(this.genres)
              })
            }
          })
      },

      searchByGenreAndTitleAndCountry: function () {
        this.searchTitle = "";
        this.loading = true;
        let queryString = convertToQueryString({'genres': this.checkedGenres,
          'release_date_after': [this.year[0] + '-01-1'],
          'release_date_before': [this.year[1] + '-12-31'],
          'production_countries': this.checkedCountries});

        fetch(FILM_API_URL + queryString)
          .then((response) => {
              if (response.ok) {
                response.json()
                  .then((json) => {
                      this.filmsList = json.results;
                      this.nextPageURL = json.next;
                      this.prevPageURL = json.prev;
                      this.queryString = queryString;

                      this.loading = false;
                  })
              }
          });
      },


      loadCountries: function (next) {
        fetch(next === "" ? COUNTRIES_API_URL : next)
          .then((response) => {
            if (response.ok){
              response.json().then((results) => {
                this.productionCountries = this.productionCountries.concat(results.results);
                if (results.next) {this.loadCountries(results.next)} // uploading all countries
              })
            }
          })
      },

    },
    created: function () {
      this.getNextPage(FILM_API_URL);
      this.loadGenres();
      this.loadCountries("");
    },
}

  function convertToQueryString(obj) {
    let queryString = "?", currentKey = "";
    for (let k in obj){
      currentKey = k.toString();
      for (let i in obj[k]){
        queryString = queryString.concat(currentKey + "=" + obj[k][i] + "&")
      }
    }
    console.log(queryString.substring(0, queryString.length - 1));
    return queryString.substring(0, queryString.length - 1);
  }
</script>


<style scoped>
  .badges-over-img {
    position: absolute;
    top: 0;
    right: 0;
    margin-top: 5px;
    margin-right: 5px;
    list-style-type: none;
    display: inline-block;
  }

  .loader {
    border: 13px solid #f3f3f3;
    border-top: 13px solid #3573db;
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .options-list {
    height: 200px;
    overflow-y: scroll;
  }

</style>
