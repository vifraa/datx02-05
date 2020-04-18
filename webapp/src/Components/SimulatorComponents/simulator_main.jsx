import React, { Component } from 'react';
import GenerateIndividuals from './generateIndividuals';
import TrainIndividuals from './trainIndividuals';
import GeneratedfilesInfo from './generatedfilesInfo';

export default class simulator_main extends Component {
    render() {
        return (
            <div>
                <div id="simulator_body">
                    <div id="GeneratedfilesInfo">
                        <GeneratedfilesInfo />
                    </div>
                    <div id="GenerateIndividuals">
                        <GenerateIndividuals />
                    </div>
                    <div id="TrainIndividuals">
                        <TrainIndividuals />
                    </div>
                </div>
            </div>
        )
    }
}
