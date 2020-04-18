import React, { Component } from 'react';
import ModelsContainer from './modelCardsContainer';
import UploadData from './uploadData.jsx'

class main extends Component {
    render() {
        return (
            <div id="body">
                <div id="UploadDataDiv" className="information_section">
                    <UploadData />
                </div>
                <div id="ModelsContainerDiv" className="information_section">
                    <ModelsContainer />
                </div>

            </div>
        );
    }
}

export default main;