
import React, { Component } from 'react'
import Navbar from 'react-bootstrap/Navbar'

export default class Footer extends Component {
    render() {
        return (
            <div>
                 <Navbar id="footernav"variant="dark" fixed="bottom" className="justify-content-md-center footer">
                    This is a part of the Bachelor's Thesis project: Powerlifting strength coach AI using machine learning methods. Chalmers University of technology 2020
                </Navbar>
            </div>
        )
    }
}