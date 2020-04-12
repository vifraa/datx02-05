import './App.css';
<<<<<<< HEAD
import Navbar from './Components/navbar.jsx'
import UploadData from './Components/uploadData.jsx'
=======
import Navbar from './Components/navbar.jsx';
import main from './Components/main'
import React, { Component } from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Default from './Components/default';
import Footer from './Components/footer';
>>>>>>> 24e2c174c34605b01afc0aa3fd1ff6749c008e3e

function App() {
  return (
    <div className="App">
<<<<<<< HEAD
    <Navbar/>
    <UploadData/>
=======
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
>>>>>>> 24e2c174c34605b01afc0aa3fd1ff6749c008e3e
    </div>
  );
}

export default App;
