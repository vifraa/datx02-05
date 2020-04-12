import './App.css';
import Navbar from './Components/navbar.jsx';
import main from './Components/main'
import React, { Component } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Default from './Components/default';
import Footer from './Components/footer';


function App() {
  return (
    <div className="App">
      <React.Fragment>
      <header className="grayTheme centerAlign">Models Admin Site</header>

        <Container fluid={true} style={{ paddingLeft: 0, paddingRight: 0 }}>
          <Navbar/>
        </Container>

        <Container fluid={true} style={{ paddingLeft: '4%', paddingRight: 0, marginTop: '2%' }}>
            <BrowserRouter>
              <Switch>
                <Route exact path="/" component={main} />
                {/*<Route path="/" component={} />*/}
                <Route component={Default} />
              </Switch>
            </BrowserRouter>
        </Container>


        <Container fluid={true} style={{ paddingLeft: 0, paddingRight: 0,  marginTop: '10%'}}>
          <BrowserRouter>
            <Footer />
          </BrowserRouter>
        </Container>

      </React.Fragment>
    </div>
  );
}

export default App;
