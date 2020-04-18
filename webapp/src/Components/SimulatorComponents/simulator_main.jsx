import React, { Component } from 'react'
import generateIndividuals from './generateIndividuals';
import trainIndividuals from './trainIndividuals';

export default class simulator_main extends Component {
    render() {
        return (
            <div>
                <div id="simulator_body">
                    <div id="GenerateIndividuals">
                        <generateIndividuals />
                    </div>
                    <div id="TrainIndividuals">
                        <trainIndividuals />
                    </div>
                </div>
            </div>
        )
    }
}
