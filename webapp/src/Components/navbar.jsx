import React, { Component } from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import { Button } from 'react-bootstrap';

class navbar extends Component {
    render() {
        return (
            <div>
                <Navbar id="navbar" variant="dark" className="justify-content-md-center">
                    <Navbar.Brand href="#home">Powerlifting strength coach AI Webapp</Navbar.Brand>
                </Navbar> 

                <Navbar id="navbar_buttons" variant="dark">
                        <div id= "nav_btn_group" className="btn-group" role="group" aria-label="Basic example">
                            <Button id="sim_button_nav" type="button" className="btn btn-info" href="simulator">Simulator</Button>
                            <Button id="mod_button_nav" type="button" className="btn btn-info" href="/">Machine Learning Regression Models</Button>
                            <Button id="rec_button_nav" type="button" className="btn btn-info" href="recengine">Recommendation Engine</Button>
                        </div>                    
                </Navbar> 
                
            </div>
        );
    }
}

export default navbar;