import React, { Component } from 'react';
import ModelsContainer from './modelCardsContainer';
import UploadData from './uploadData.jsx'

class main extends Component {
    render() {
        return (
            <div id="body">
                <div id="UploadDataDiv">
                    <UploadData />
                </div>
                <div id="ModelsContainerDiv">
                    <ModelsContainer />
                </div>

            </div>
        );
    }
}

export default main;