<template>
  <v-container fluid grid-list-md>
    <v-data-iterator :items="posts" content-tag="v-layout" row wrap>
      <v-flex slot="item" slot-scope="props" sm12 sm6 md4 lg3 >
        <!-- actual data is iterating at this v-flex layer -->
        <postCard :post="props.item"/>
      </v-flex>
    </v-data-iterator>
  </v-container>
</template>


<script>
import axios from "axios";
import postCard from "@/components/post/Card";
export default {
  data() {
    return {
      posts: []
    };
  },
  mounted() {
    axios
      .get("posts/")
      .then(response => {
        // JSON responses are automatically parsed.
        console.log(response);
        this.posts = response.data;
      })
      .catch(error => {
        console.log(error);
        console.log(error.response);
      });
  },
  components: {
    postCard
  }
};
</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>