
import React, { Component } from 'react'
import Navbar from 'react-bootstrap/Navbar'

export default class Footer extends Component {
    render() {
        return (
            <div>
                 <Navbar className="footer">
                    <h6>This project is part of the Bachelor's Thesis project: Powerlifting strength coach AI using machine learning methods. Chalmers University of technology 2020. </h6>
                    <br/><h6> The project is developed by: Yazan Ghafir, Daniel Berg Thomsen, Carl Östling, Viktor Franzén, Ljubo Cvijetic and Henrik Lagergren.</h6>
                </Navbar>
            </div>
        )
    }
}