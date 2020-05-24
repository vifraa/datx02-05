import React, { Component } from 'react';
import GenerateIndividuals from './generateIndividuals';
import TrainIndividuals from './trainIndividuals';
import GeneratedfilesInfo from './generatedfilesInfo';
import TransformData from './transformData';
export default class simulator_main extends Component {
    componentDidMount() {
        document.title = 'DATX02-05';
    }
    
    render() {
        
        return (
            <div>
                <div className="information_section">
                    <div id="GeneratedfilesInfo" className="rcorners">
                        <GeneratedfilesInfo />
                    </div>
                    <div id="GenerateIndividuals" className="rcorners">
                        <GenerateIndividuals />
                    </div>
                    <div id="TrainIndividuals" className="rcorners">
                        <TrainIndividuals />
                    </div>
                    <div id="TransformData" className="rcorners">
                        <TransformData />
                    </div>
                </div>
            </div>
        )
    }
}
