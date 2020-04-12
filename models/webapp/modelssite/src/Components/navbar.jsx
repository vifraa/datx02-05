import React, { Component } from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';

class navbar extends Component {
    render() {
        return (
            <div>
                <Navbar bg="dark" variant="dark">
                    <Navbar.Brand href="#home">Models</Navbar.Brand>
                    <Nav className="mr-auto">
                        <Nav.Link href="#home">Rubrik1</Nav.Link>
                        <Nav.Link href="#features">Rubrik2</Nav.Link>
                        <Nav.Link href="#pricing">Rubrik3</Nav.Link>
                    </Nav>
                </Navbar> 
                
            </div>
        );
    }
}

export default navbar;