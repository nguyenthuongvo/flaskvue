<template>
  <b-container>
    <div id="app">
      <div id="nav">
        <div class="row">
          <div class="col-md-4"></div>
          <div class="col-md-4"><h1>Vo Nguyen</h1></div>
          <div class="col-md-4"></div>
        </div>
        <hr>
        <b-nav align="center">
          <b-nav-item active>Active</b-nav-item>
          <b-nav-item>Link</b-nav-item>
          <b-nav-item>Another Link</b-nav-item>
          <b-nav-item disabled>Disabled</b-nav-item>
        </b-nav>
        <div>
          <b-jumbotron>
            <template #header>
              <div class="text-left">BootstrapVue</div>
              <div class="text-left">Descriptions</div>
            </template>
            <template #lead>
              This is a simple hero unit, a simple jumbotron-style component
              for calling extra attention to
              featured content or information.
            </template>
            <hr class="my-4">
            <p>
              It uses utility classes for typography and spacing
              to space content out within the larger
              container.
            </p>
          </b-jumbotron>
        </div>
        <div class="row">
          <div class="col-md-6">
            <b-card no-body class="overflow-hidden">
              <b-row no-gutters>
                <b-col md="6">
                  <b-card-img src="https://picsum.photos/400/400/?image=20"
                  alt="Image" class="rounded-0"></b-card-img>
                </b-col>
                <b-col md="6">
                  <b-card-body title="Horizontal Card">
                    <b-card-text>
                      This is a wider card with supporting
                      text as a natural lead-in to additional content.
                      This content is a little bit longer.
                    </b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </div>
          <div class="col-md-6">
            <b-card no-body class="overflow-hidden">
              <b-row no-gutters>
                <b-col md="6">
                  <b-card-img src="https://picsum.photos/400/400/?image=20"
                  alt="Image" class="rounded-0"></b-card-img>
                </b-col>
                <b-col md="6">
                  <b-card-body title="Horizontal Card">
                    <b-card-text>
                      This is a wider card with supporting text
                      as a natural lead-in to additional content.
                      This content is a little bit longer.
                    </b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </div>
        </div>
      </div>
      <b-row>
        <b-col cols="8">
          <div><h3>From the Firehose</h3></div>
          <hr>
        </b-col>
        <b-col cols="4">
          <b-card bg-variant="light" header="About" class="text-center">
            <b-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</b-card-text>
          </b-card>
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
