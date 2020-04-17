import './App.css';
import Navbar from './Components/navbar.jsx'
import main from './Components/main'
import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Default from './Components/default';
import Footer from './Components/footer';


function App() {

  return (
    <div id="App">
      <link href="https://fonts.googleapis.com/css2?family=Comic+Neue:ital@1&display=swap" rel="stylesheet"></link>
      <React.Fragment>
      {/*<header className="grayTheme centerAlign">Models Admin Site</header>*/}

        <Container fluid={true} style={{ paddingLeft: 0, paddingRight: 0 }}>
          <Navbar/>
        </Container>

        {/*<Container fluid={true} style={{ paddingLeft: '4%', paddingRight: 0, marginTop: '2%' }}>*/}
        <Container fluid={true} style={{ paddingLeft: 0, paddingRight: 0}}>
            <BrowserRouter>
              <Switch>
                <Route exact path="/" component={main} />
                {/*<Route path="/" component={} />*/}
                <Route component={Default} />
              </Switch>
            </BrowserRouter>
        </Container>

        <Container fluid={true} style={{ paddingLeft: 0, paddingRight: 0}}>
          <BrowserRouter>
            <Footer />
          </BrowserRouter>
        </Container>

      </React.Fragment>
    </div>
  );
}

export default App;