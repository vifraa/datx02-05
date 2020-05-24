import React, { Component } from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { Button } from 'react-bootstrap';

class navbar extends Component {
    render() {
        return (
            <div>
                <Navbar id="navbar"  className="justify-content-md-center">
                    <Navbar.Brand href="#home">Powerlifting strength coach AI Webapp</Navbar.Brand>
                </Navbar> 

                <Navbar>
                        <div id= "nav_btn_group" className="btn-group" role="group">
                            <Button id="sim_button_nav" type="button" className="btn" href="simulator">Simulator</Button>
                            <Button id="mod_button_nav" type="button" className="btn" href="models">Machine Learning Regression Models</Button>
                            <Button id="rec_button_nav" type="button" className="btn" href="recengine">Recommendation Engine</Button>
                            <Button id="ttr_rec_button_nav" type="button" className="btn " href="ttrrecengine">TTR Recommendation Engine</Button>
                        </div>                    
                </Navbar> 
                
            </div>
        );
    }
}

export default navbar;