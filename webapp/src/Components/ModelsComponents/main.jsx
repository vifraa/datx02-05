import React, { Component } from 'react';
import ModelsContainer from './modelCardsContainer';
import UploadData from './uploadData.jsx'
import GeneratedfilesInfo from '../SimulatorComponents/generatedfilesInfo.jsx';

class main extends Component {
    render() {
        return (
            <div id="body">
                                
                <div id="ModelsContainerDiv" className="information_section">
                    <ModelsContainer />
                </div>

            </div>
        );
    }
}

export default main;